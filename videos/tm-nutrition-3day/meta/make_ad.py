"""Build one 9:16 Meta ad: cut the voice-trimmed coach takes, jump-cut pauses, plan scenes/captions, write render inputs.
usage: python3 make_ad.py ad1_kirthika_anand|ad2_joseph_raj|ad3_jones_92_67
then (engine v7): node render.js <wd> k 3 ; python3 mix.py <wd> ; WD=<wd>/ python3 comp.py ; speed.sh <wd> <out.mp4>
Inputs: selects_meta.py (lines), trims_meta.json (voice-ID cut points), /home/user/w/tm/mezz/C000xP.mp4 (portrait working copies)."""
import sys, os, json, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from selects_meta import ADS
AD = sys.argv[1]; LINES = ADS[AD]; TR = json.load(open(os.path.join(HERE, 'trims_meta.json')))
W = f'/home/user/w/meta/{AD}/'; M = '/home/user/w/tm/mezz/'; TST = '/home/user/Edit-Army/videos/tm-nutrition-3day/source/testimonials/'
FPS = 30; os.makedirs(W + 'parts', exist_ok=True); os.makedirs(W + 'broll', exist_ok=True)
run = lambda c: subprocess.run(c, check=True)
for f in os.listdir(TST):
    if f.endswith('.mp4') and not os.path.exists(W + 'broll/' + f): os.symlink(TST + f, W + 'broll/' + f)
# ---------- 1. cut ----------
takes = []; off = 0.0; lst = []
for sid, f, a0, b0, txt, mean in LINES:
    a, b = TR[sid]['a'], TR[sid]['b']; n = round((b - a) * FPS); d = n / FPS; p = W + f'parts/{sid}.mkv'
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a}', '-i', M + f + 'P.mp4', '-vf', 'fps=30', '-frames:v', str(n), '-c:v', 'libx264', '-crf', '12',
         '-preset', 'fast', '-af', f'atrim=end={d},apad=whole_dur={d}', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '1', p])
    takes.append(dict(id=sid, file=f, a=a, b=b, off=round(off, 3), dur=d, text=txt)); off += d; lst.append(p)
open(W + 'parts/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in lst))
run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', W + 'parts/list.txt', '-c', 'copy', W + 'src.mkv'])
run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', W + 'src.mkv', '-vn', '-ac', '1', '-ar', '48000', W + 'src48.wav'])
json.dump(takes, open(W + 'takes.json', 'w'), ensure_ascii=False, indent=1); TK = {t['id']: t for t in takes}
# ---------- 2. jump cuts inside takes (pauses > 0.22 s) ----------
def islands(a, b):
    log = subprocess.run(['ffmpeg', '-nostdin', '-ss', f'{a}', '-t', f'{b - a}', '-i', W + 'src48.wav', '-af', 'silencedetect=noise=-34dB:d=0.22', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ss = [float(x) + a for x in re.findall(r'silence_start: (-?[\d.]+)', log)]; se = [float(x) + a for x in re.findall(r'silence_end: ([\d.]+)', log)]
    se += [b] * (len(ss) - len(se)); out = []; t = a
    for s, e in zip(ss, se):
        if s - t > 0.06: out.append([t, s])
        t = e
    if b - t > 0.06: out.append([t, b])
    return out
# ---------- 1b. opening: real client transformation bites (own audio; mute=True plays the clip silent under the music) ----------
INTRO = {'ad1_kirthika_anand': [
    ('I01', 'T_vid_0608', 21.92, 27.80, False, 'SIVAKARTHIK • 32 • ERODE', '<span class="g">−26 KG</span><br>6 MONTHS',
     'ஆறு மாசத்துல 26 kg குறைச்சு, இப்போ ideal weight-ல fit-ஆ, happy-ஆ இருக்கேன்.'),
    ('I02', 'T_vid_0613', 37.80, 40.00, True, 'JONES • 92 → 67 KG', '<span class="g">−25 KG</span>', ''),
    ('I03', 'T_vid_0610', 39.10, 40.45, False, 'KRISHNA PRIYA • 48', None, 'Healthy-ஆ, happy-ஆ இருக்கேன்.')]}
intro = []
for bid, f, a, b, mute, nm, res, txt in INTRO.get(AD, []):
    n = round((b - a) * FPS); d = n / FPS; clip = f'{bid}.mkv'
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a}', '-i', TST + f + '.mp4', '-vf', 'fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2', '-frames:v', str(n),
         '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-af', f'atrim=end={d},apad=whole_dur={d}' + (',volume=0' if mute else ''),
         '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '1', W + 'broll/' + clip])
    intro.append(dict(k='bite', id=bid, dur=d, clip=clip, name=nm, res=res, text=txt))
pieces = [dict(p) for p in intro]
for t in takes:
    a, b = t['off'], t['off'] + t['dur']; segs = []
    for s, e in islands(a, b):
        s, e = max(a, s - .06), min(b, e + .12)
        if segs and s - segs[-1][1] < .14: segs[-1][1] = e
        else: segs.append([s, e])
    for s, e in (segs or [[a, b]]): pieces.append(dict(k='seg', id=t['id'], s0=s, s1=e))
o = 0.0
for p in pieces: p['o0'] = o; o += (p['s1'] - p['s0']) if p['k'] == 'seg' else p['dur']; p['o1'] = o
TAIL_S = 3.0; TOTAL = o + TAIL_S
def span(a_id, b_id=None):
    b_id = b_id or a_id
    return min(p['o0'] for p in pieces if p['id'] == a_id), max(p['o1'] for p in pieces if p['id'] == b_id)
def O(tid, rel=0.0):
    ts = TK[tid]['off'] + rel
    for p in pieces:
        if p['k'] != 'seg': continue
        if ts < p['s0']: return p['o0']
        if ts <= p['s1']: return p['o0'] + ts - p['s0']
    return o
# ---------- 3. scenes ----------
BROLL, GFX = [], []   # BROLL: (id, o0, o1, scene, layout, extra, line, source) ; layout 'full' (cutaway) | 'clip' (real client video, coach voice continues)
def B(bid, a, b, sc, ex, line, src='P5 motion graphics'): BROLL.append((bid, a, b, sc, 'full', ex, line, src))
def CLIP(bid, a, b, clip, ss, ex, line): BROLL.append((bid, a, b, 'testi', 'full', dict(ex, clip=(clip, ss)), line, 'P2 real client video (client-supplied)'))
def G(ty, a, b, **ex): GFX.append((ty, a, b, ex))
TOP = dict(x=0, w=1080)
def tail():
    a, b = span('A15'); B('S15', a + .2, b, 'agenda', dict(title='3 DAYS <span class="y">COUPLE</span><br>TRANSFORMATION CHALLENGE', cues=[.1, .2, .3, .4]), 'that\'s why this 3-day couple transformation challenge')
    a, b = span('A16'); G('badge', a + .1, b, html='🤔 3 நாள்ல மாற்றம் வருமா?', y=330, size=50, **TOP)
    a, b = span('A17'); B('S17', a, b, 'q3days', dict(cues=[0, .15, .35]), 'yes, it is possible')
    a, _ = span('A18'); _, b = span('A20'); B('S18', a, b, 'habits', dict(cues=[0.05, O('A19') - a, O('A20') - a]), 'Day 1: mobile -> habit pattern')
    a, b = span('A21'); B('S21', a, b, 'famhealth', dict(cues=[0.3, 1.6]), 'Day 2: whole family healthy')
    a, b = span('A22'); B('S22', a, b, 'happy', dict(cues=[0.4, 1.8]), 'Day 3: routine that brings happiness')
    a, b = span('A23'); B('S23', a, b, 'money', dict(cues=[0.5, 1.8]), 'plus financial independence roadmap')
    a, b = span('A24'); G('price', O('A24', 0.9), b + .3, value=555, pre='JUST', sub='3 DAYS LIVE + ROADMAP', x=230, y=150)
    a, b = span('A25', 'A27'); G('stamp', O('A26'), b, x=260, y=170, sub='3 DAYS LIVE • VALUE இல்லைன்னா', badge='🛡️ RISK முழுசா என் பக்கம்', bt=O('A27') - O('A26'))
    a, b = span('A28', 'A29'); G('badge', a + .1, b, html='🔥 ONLY 5 COUPLES • TRICHY', y=260, size=56, **TOP)
    a, b = span('A29'); G('text', a + .1, b, html='நானே <span class="y">PERSONAL-ஆ</span><br>TRAIN', y=400, size=80, nocap=True, **TOP)
    a, b = span('A30'); G('badge', a + .1, b, html='🍀 LUCKY COUPLES நீங்களா?', y=300, size=54, bg='var(--em)', fg='#04110c', **TOP)
    a, b = span('A31'); G('flash', a - .05, a + .1); G('cta', a + .1, b + .2, label='👇 REGISTER NOW', badge='₹555 • 100% MONEY BACK', y=260, **TOP)
    G('endcard', o, TOTAL, title='3 DAYS COUPLE<br>TRANSFORMATION CHALLENGE', price=555, btn='REGISTER NOW', seats='ONLY 5 COUPLES • TRICHY', loc='TM NUTRITION • COACH PRADHEESH MUTHARASU • TRICHY')
def trio(first, last):
    a, _ = span(first); _, b = span(last)
    B('S11', a, b, 'stack', dict(title='உண்மையான <span class="y">PROBLEM</span>', items=[['📱', 'DAILY HABITS'], ['👨‍👩‍👧', 'FAMILY ROUTINE'], ['🏡', 'HAPPINESS AT HOME']],
                                cues=[O('A11') - a, O('A12') - a, O('A13') - a]), 'daily habits / family routine / happiness at home')
if AD == 'ad1_kirthika_anand':
    a, b = span('A01', 'A02'); G('badge', a + .2, b, html='👫 KIRTHIKA & ANAND • VEDARANYAM', y=260, size=46, bg='var(--em)', fg='#04110c', **TOP)
    a, b = span('A02'); G('text', O('A02', 1.4), b, html='தனித்தனியா இல்ல<br><span class="y">சேர்ந்தே</span> மாறினாங்க', y=360, size=74, nocap=True, **TOP)
    a, b = span('A04'); G('text', a + .1, b, html='<span class="r">3</span> PROBLEMS', y=330, size=120, nocap=True, **TOP)
    a, b = span('A05'); B('S05', a, b, 'pain', dict(v='diet', cues=[1.0]), 'cannot follow a diet consistently')
    a, b = span('A06'); B('S06', a, b, 'pain', dict(v='gym', cues=[0.8]), 'no time for the gym')
    a, b = span('A07'); B('S07', a, b, 'pain', dict(v='tomorrow', cues=[1.2]), '"let\'s start tomorrow"')
    a, b = span('A09'); G('badge', a + .1, b, html='❌ DIET இல்ல', y=320, size=60, **TOP)
    a, b = span('A10'); G('badge', a + .1, b, html='✅ DAILY HABITS', y=320, size=60, bg='var(--em)', fg='#04110c', **TOP)
    trio('A11', 'A13')
    a, b = span('A14'); G('text', a + .1, b, html='🔗 ALL 3<br><span class="g">CONNECTED</span>', y=330, size=96, nocap=True, **TOP)
elif AD == 'ad2_joseph_raj':
    a, b = span('B01'); G('badge', O('B01', 2.0), b, html='❌ காரணம் DIET இல்ல', y=320, size=58, **TOP)
    a, _ = span('B02'); _, b = span('B03'); B('S02', a, b, 'pain', dict(v='diet', cues=[O('B03') - a]), '3 days diet... then biryani')
    a, b = span('B04'); B('S04', a, b, 'pain', dict(v='gym', cues=[1.2]), 'gym, never even two weeks')
    a, _ = span('B05'); _, b = span('B06'); B('S05', a, b, 'pain', dict(v='tomorrow', cues=[O('B06') - a]), '"you start first, I will come later"')
    a, _ = span('B07'); _, b = span('B10'); CLIP('C07', a, b, 'T_vid_0615.mp4', 1.3, dict(name='JOSEPH RAJ • 62', x=40, y=200, rx=60, ry=1150, rt=O('B10') - a,
                                                                             res='<span class="g">IDEAL WEIGHT ✓</span><br>HEALTHY & FIT'), 'Joseph Raj, 62 -> ideal weight')
    a, b = span('B11'); G('text', a + .1, b, html='<span class="y">62</span> வயசுல<br>முடியும்னா?', y=330, size=100, nocap=True, **TOP)
    a, b = span('B12'); G('badge', a + .1, b, html='⚖️ WEIGHT மட்டும் PROBLEM இல்ல', y=320, size=46, **TOP)
    trio('A11', 'A13')
    a, b = span('B14'); G('text', a + .1, b, html='3 சேர்ந்தா<br><span class="g">COUPLES WIN 🏆</span>', y=330, size=84, nocap=True, **TOP)
elif AD == 'ad3_jones_92_67':
    a, b = span('C02'); G('text', O('C02', 1.0), b, html='<span class="y">25 KG</span><br>குறைக்கிறது?', y=330, size=110, nocap=False, **TOP)
    a, b = span('C03'); CLIP('C03', a, b, 'T_vid_0613.mp4', 0.4, dict(name='JONES • 30 • TRICHY', x=40, y=200), 'this is Jones')
    a, b = span('C04'); m = O('C04', 2.4)
    CLIP('C04a', a, m, 'T_vid_0613.mp4', 11.2, dict(name='JONES • BEFORE', x=40, y=200), '92 kg ...')
    CLIP('C04b', m, min(b, m + 2.2), 'T_vid_0613.mp4', 37.8,   # the before/after card lasts ~2.2 s, then the reel's own outro starts
          dict(name='JONES • 92 → 67 KG', x=40, y=200, res='<span class="g">−25 KG</span>', rx=60, ry=1150, rt=0.6), '... to 67 kg, not by diet alone')
    a, b = span('C05'); G('badge', a + .1, b, html='✅ HABITS மாறினதனால', y=320, size=58, bg='var(--em)', fg='#04110c', **TOP)
    a, _ = span('C06'); _, b = span('C10')
    B('S06', a, b, 'stack', dict(title='நம்ம வீட்டு <span class="r">PROBLEM</span>', bad=True, items=[['📱', 'கையில எப்பவும் MOBILE'], ['🍽️', 'LATE NIGHT DINNER'], ['😴', 'சரியா தூக்கம் இல்ல'], ['🚶', 'WALKING இல்ல']],
                              cues=[O('C07') - a, O('C08') - a, O('C09') - a, O('C10') - a]), 'phone, late dinner, no sleep, no walking')
    a, b = span('C11'); B('S11', a, b, 'pattern', dict(cues=[0.3, 1.2]), 'both stuck in the same pattern')
for p in pieces:
    if p['k'] == 'bite':
        BROLL.append((p['id'], p['o0'], p['o1'], 'testi', 'full', dict(name=p['name'], res=p['res'], x=40, y=200, rx=60, ry=1150, rt=.5, note='Individual results vary'),
                      'opening: real client transformation', 'P2 real client video (client-supplied)'))
tail()
# ---------- 4. captions (from the cleaned line text) ----------
KEY = re.compile(r'(\d|₹|DIET|GYM|MOBILE|HABIT|FAMILY|HAPPINESS|CHALLENGE|POSSIBLE|MONEY|RISK|COUPLES?|LINK|REGISTER|KILO|KG|IDEAL|HEALTHY|FIT|PATTERN|ROADMAP|FINANCIAL|BIRYANI|LIVE|VALUE|LUCKY|PERSONAL|DAY|ROUTINE|TRICHY)', re.I)
def chunks(txt, n=3):
    w = txt.replace('"', '').split(); out = []
    for i in range(0, len(w), n): out.append(w[i:i + n])
    if len(out) > 1 and len(out[-1]) == 1: last = out.pop(); out[-1] += last
    return out
captions = []
def full_at(t): return any(a <= t < b and lay == 'full' for _, a, b, sc, lay, *_ in BROLL)
nocap = [(a, b) for ty, a, b, ex in GFX if ex.get('nocap')]
for t in [dict(id=p['id'], text=p['text']) for p in pieces if p['k'] == 'bite' and p['text']] + takes:
    ps = [p for p in pieces if p['id'] == t['id']]; a0, b0 = ps[0]['o0'], ps[-1]['o1']; cs = chunks(t['text']); wts = [sum(len(x) for x in c) + 3 for c in cs]; tt = a0
    for c, wt in zip(cs, wts):
        d = (b0 - a0) * wt / sum(wts); hl = [i for i, x in enumerate(c) if KEY.search(x)]
        cap = dict(t0=round(tt, 3), t1=round(tt + d, 3), words=[x.upper() if re.match(r'^[A-Za-z]', x) else x for x in c], hl=hl,
                   col='#FFD60A' if any(re.search(r'\d|₹', x) for x in c) else '#00C896')
        if full_at(tt + d / 2): cap['pos'] = 'side'          # over a cutaway: captions move to the lower band (y 1600)
        captions.append(cap); tt += d
# ---------- 5. outputs ----------
items, sfx = [], []
for bid, a, b, sc, lay, ex, line, src in BROLL:
    d = dict(type=sc, t0=round(a, 3), t1=round(b, 3), layout='full', id=bid); e = dict(ex); e.pop('clip', None); d.update(e); items.append(d); sfx.append((a - .1, 'whoosh'))
for ty, a, b, ex in GFX:
    d = dict(type=ty, t0=round(a, 3), t1=round(b, 3)); d.update(ex); items.append(d)
    sfx.append((a, {'text': 'hit', 'badge': 'pop', 'price': 'cash', 'stamp': 'thud', 'cta': 'ding', 'lower': 'swipe', 'flash': 'whoosh', 'endcard': 'hit'}[ty]))
sfx.append((span('A31')[0] - 1.4, 'riser')); sfx = sorted((max(0, round(t, 3)), n) for t, n in sfx)
os.makedirs(W + 'gfx', exist_ok=True); os.makedirs(W + 'audio', exist_ok=True)
json.dump(dict(total=round(TOTAL, 3), items=items, captions=captions), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
segz = {}; k = 0
for p in pieces: k += 1; segz[id(p)] = 1.0 if k % 2 else 1.12
frames = []; last = 0
for i in range(int(round(TOTAL * FPS))):
    t = i / FPS; p = next((q for q in pieces if q['o0'] <= t < q['o1']), None); fr = dict(L='face', z=1.0)
    if p and p['k'] == 'seg': last = p['s0'] + t - p['o0']; fr['z'] = round(segz[id(p)] * (1 + .02 * (t - p['o0']) / max(.01, p['o1'] - p['o0'])), 4)
    if p and p['k'] == 'bite': last = pieces[len(intro)]['s0'] if len(pieces) > len(intro) else 0
    fr['ts'] = round(last, 4)
    for bid, a, b, sc, lay, ex, line, src in BROLL:
        if a <= t < b:
            fr['L'] = 'full'
            if 'clip' in ex: fr['V'] = [ex['clip'][0], round(ex['clip'][1] + t - a, 4), round((t - a) / (b - a), 3)]
    if p and p['k'] == 'bite': fr['L'] = 'full'; fr['V'] = [p['clip'], round(t - p['o0'], 4), round((t - p['o0']) / p['dur'], 3)]
    if t >= o: fr = dict(L='face', z=1.0, ts=round(last, 4))
    frames.append(fr)
json.dump(frames, open(W + 'frames.json', 'w'))
end = span(LINES[-1][0])[0]
MUSIC = [(0.0, span('A15')[0], 'warm' if intro else 'dark'), (span('A15')[0], span('A24')[0], 'tech'), (span('A24')[0], TOTAL, 'uplift')]
json.dump(dict(total=TOTAL, pieces=pieces, sfx=sfx, music=MUSIC), open(W + 'audio/cues.json', 'w'))
json.dump(dict(size=[1080, 1920], face=[600, 985]), open(W + 'comp_cfg.json', 'w'))
with open(os.path.join(HERE, f'broll_{AD}.csv'), 'w') as f:
    f.write('ID,Final time (s),Line,Visual,Source\n')
    for bid, a, b, sc, lay, ex, line, src in sorted(BROLL, key=lambda r: r[1]):
        f.write(f'{bid},{a / 1.2:.1f}-{b / 1.2:.1f},"{line}","{ex["clip"][0] if "clip" in ex else sc}",{src}\n')
cov = sum(b - a for _, a, b, *_ in BROLL)
print(f'{AD}: {len(takes)} takes, {len(pieces)} shots, {TOTAL / 1.2:.1f}s final, cutaways {cov / TOTAL * 100:.0f}%')
