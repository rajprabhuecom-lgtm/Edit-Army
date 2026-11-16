"""TM Nutrition VSL: EDL + timeline for the v6 16:9 engine.
Inputs : /home/user/w/vsl/{takes.json, src48.wav, broll/}   (from build_src.py)
Outputs: /home/user/w/vsl/{gfx/timeline.json, frames.json, audio/cues.json, comp_cfg.json} + broll_plan.csv next to this file.
Authoring times: (take id, seconds after the take's start in its source file). B-roll that runs across several takes uses span().
"""
import json, re, subprocess, os, csv, bisect
HERE = os.path.dirname(os.path.abspath(__file__)); W = '/home/user/w/vsl/'
FPS = 30
TK = {t['id']: t for t in json.load(open(W + 'takes.json'))}
ORDER = [t['id'] for t in json.load(open(W + 'takes.json'))]

# ---------- 1. jump cuts: speech islands inside each take ----------
def islands(a, b, noise=-34, d=0.22):
    log = subprocess.run(['ffmpeg', '-nostdin', '-ss', f'{a}', '-t', f'{b - a}', '-i', W + 'src48.wav', '-af', f'silencedetect=noise={noise}dB:d={d}', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ss = [float(x) + a for x in re.findall(r'silence_start: (-?[\d.]+)', log)]; se = [float(x) + a for x in re.findall(r'silence_end: ([\d.]+)', log)]
    se += [b] * (len(ss) - len(se)); out = []; t = a
    for s, e in zip(ss, se):
        if s - t > 0.06: out.append([t, s])
        t = e
    if b - t > 0.06: out.append([t, b])
    return out
PRE, POST, MERGE = 0.07, 0.13, 0.16
pieces = []          # {'k':'seg','s0','s1','id'} in src time | {'k':'bite','id','dur','clip'}
for tid in ORDER:
    t = TK[tid]
    if t['kind'] == 'bite':
        pieces.append(dict(k='bite', id=tid, dur=t['dur'], clip=t['clip'])); continue
    a, b = t['off'], t['off'] + t['dur']; segs = []
    for s, e in islands(a, b):
        s, e = max(a, s - PRE), min(b, e + POST)
        if segs and s - segs[-1][1] < MERGE: segs[-1][1] = e
        else: segs.append([s, e])
    if not segs: segs = [[a, b]]
    for s, e in segs: pieces.append(dict(k='seg', id=tid, s0=s, s1=e))
o = 0.0
for p in pieces:
    p['o0'] = o; o += (p['s1'] - p['s0']) if p['k'] == 'seg' else p['dur']; p['o1'] = o
TAIL = 3.2                                   # end card hold (output seconds, pre-speed)
TOTAL = o + TAIL

def s2o(ts):                                 # src time -> output time
    for p in pieces:
        if p['k'] != 'seg': continue
        if ts < p['s0']: return p['o0']
        if ts <= p['s1']: return p['o0'] + ts - p['s0']
    return o
def O(tid, rel=0.0):                         # (take, seconds after take start) -> output time
    t = TK[tid]
    if t['kind'] == 'bite': return [p for p in pieces if p['id'] == tid][0]['o0'] + rel
    return s2o(t['off'] + rel)
def span(a_id, b_id=None):                   # output span covering takes a..b
    b_id = b_id or a_id; ps = [p for p in pieces if p['id'] in (a_id, b_id)]
    return min(p['o0'] for p in ps if p['id'] == a_id), max(p['o1'] for p in ps if p['id'] == b_id)

# ---------- 2. B-roll / scenes (layout, visual) ----------
# muted testimonial clips shown while the coach names each client (clip, start second in the clip)
TCLIP = {'L11': ('T_vid_0606.mp4', 0.3), 'L12': ('T_vid_0608.mp4', 11.5), 'L13': ('T_vid_0610.mp4', 0.0)}
BROLL = []   # (id, o0, o1, scene, layout, extra, keyword, source)
def B(bid, o0, o1, scene, layout, extra, kw, src): BROLL.append((bid, o0, o1, scene, layout, extra, kw, src))
h0, h1 = span('L01')
B('B01', h0 + 1.5, h1, 'tally', 'side', {}, 'how many times have you both decided to lose weight?', 'P5 motion graphics')
a, b = span('L06'); B('B02', a, b, 'pain', 'side', dict(v='diet', cues=[O('L06', 1.55) - a]), '3 days diet... then biryani', 'P5 motion graphics')
a, b = span('L07'); B('B03', a, b, 'pain', 'side', dict(v='gym', cues=[1.4]), 'gym membership, not even 2 weeks', 'P5 motion graphics')
a, b = span('L08'); B('B04', a, b, 'pain', 'side', dict(v='midnight', cues=[1.3]), 'mobile in hand till midnight', 'P5 motion graphics')
a, b = span('L09'); B('B05', a, b, 'pain', 'side', dict(v='tomorrow', cues=[1.6]), '"let\'s start tomorrow"', 'P5 motion graphics')
a, b = span('L10'); B('B06', a, b, 'pattern', 'full', dict(cues=[O('L10', 1.2) - a, O('L10', 2.4) - a]), 'problem is not willpower, it is the home pattern', 'P5 motion graphics')
for tid, nm, res in [('L11', 'RAVEENDRAN • 58', None), ('L12', 'SIVAKARTHIK • 32 • ERODE', '<span class="y">26 KG</span><br>EXCESS WEIGHT'), ('L13', 'KRISHNA PRIYA • 48', None)]:
    a, b = span(tid); B('T' + tid[1:], a, b, 'testi', 'tside', dict(clip=TCLIP[tid], name=nm, res=res, x=40, y=40, rx=60, ry=760, rt=1.4), f'client named on camera ({tid})', 'P2 real testimonial (client-supplied)')
a, b = span('L14'); B('T14', a, b, 'vid', 'tside', dict(clip=('T_vid_0613.mp4', 34.0), chips=[['🤔 "இது எனக்கு WORK ஆகாது"', 'var(--ob)', '#fff', 'var(--rd)']], ct=[0.3], cy=60), 'everyone thought it would not work', 'P2 real testimonial (client-supplied)')
for bid, nm in [('B01', 'SIVAKARTHIK • ERODE'), ('B02', 'KRISHNA PRIYA • 48')]:
    a, b = span(bid); B('P' + bid[1:], a, b, 'testi', 'full', dict(clip=(TK[bid]['clip'], 0.0), name=nm, x=60, y=60, note='Individual results vary'), 'client proof bite (own audio)', 'P2 real testimonial (client-supplied)')
a, b = span('L18'); B('B07', a, b, 'q3days', 'full', dict(cues=[0.0, 0.25, 0.55]), 'Yes - change can start in 3 days', 'P5 motion graphics')
a, _ = span('L19'); B('B08', a, a + 2.0, 'agenda', 'full', dict(focus=0, cues=[0, .12, .24, .36]), 'Day 1: Habits (agenda)', 'P5 motion graphics')
_, b = span('L23'); B('B09', a + 2.0, b, 'habits', 'side', dict(cues=[0.1, O('L21', 0.2) - a - 2.0, O('L22', 0.2) - a - 2.0]), 'Day 1: mobile -> habit pattern tuned, hand-hold', 'P5 motion graphics')
a, _ = span('L24'); _, b = span('L25'); B('B10', a, b, 'famhealth', 'side', dict(cues=[0.3, O('L25', 3.5) - a]), 'Day 2: not just you - whole family healthy', 'P5 motion graphics')
a, _ = span('L26'); _, b = span('L30'); B('B11', a, b, 'happy', 'side', dict(cues=[O('L28', 3.0) - a, O('L30', 0.2) - a]), 'Day 3: routines -> happiness at home', 'P5 motion graphics')
a, b = span('L31'); B('B12', a, b, 'money', 'side', dict(cues=[0.8, 2.6]), 'first step to financial independence', 'P5 motion graphics')

# on-face graphics (speaker stays on screen): (type, o0, o1, extra)
GFX = []
def G(ty, o0, o1, **ex): GFX.append((ty, o0, o1, ex))
a, b = span('L02'); G('badge', a + .2, b, html='▶ முழுசா பாருங்க', x=60, w=760, y=140, bg='var(--yl)', fg='#000', size=56)
a, b = span('L03'); G('lower', a + .3, b + 1.0, name='COACH PRADHEESH MUTHARASU', title='TM NUTRITION CENTRE • TRICHY', x=80, y=700)
a, b = span('L04'); G('text', a + .2, b, html='<span class="y">18 YEARS</span><br>100s OF FAMILIES', x=40, w=800, y=170, size=96)
a, b = span('L05'); G('badge', a + .2, b, html='👫 NEW BATCH • COUPLES ONLY', x=40, w=820, y=180, bg='var(--em)', fg='#04110c', size=52)
a, b = span('L15'); G('text', O('L15', 2.4), b, html='வெறும்<br><span class="g">3 நாள்ல</span>', x=40, w=800, y=170, size=120, nocap=True)
a, b = span('L16', 'L17'); G('badge', a + .1, b, html='🤔 3 நாள்ல CHANGE? அது எப்படி?', x=40, w=840, y=180, size=50, bg='var(--rd)')
a, b = span('L33'); G('price', O('L33', 1.9), b + .3, value=555, pre='JUST', sub='3 SECRETS + BONUS', x=90, y=170)
a, b = span('L34', 'L35'); G('stamp', a + .3, b, x=110, y=170, sub='3 நாள் LIVE • VALUE இல்லைன்னா', badge='🛡️ RISK முழுசா என் பக்கம்', bt=O('L35') - a - .3)
a, b = span('L36'); G('badge', a + .2, b, html='🔥 ONLY 5 COUPLES • TRICHY', x=40, w=840, y=150, size=56)
G('text', O('L36', 3.6), b, html='நானே <span class="y">PERSONAL-ஆ</span><br>TRAIN', x=40, w=840, y=300, size=78, nocap=True)
a, b = span('L37'); G('flash', a - .05, a + .1); G('cta', a + .15, b + .2, label='👇 START YOUR FAMILY JOURNEY', badge='₹555 • 100% MONEY BACK', x=0, w=1000, y=520)
G('endcard', o, TOTAL, price=555, btn='BOOK NOW', seats='ONLY 5 COUPLES • THIS BATCH', loc='TM NUTRITION CENTRE • COACH PRADHEESH MUTHARASU • TRICHY')

# ---------- 3. captions (clean text; * green, ^ yellow, ! red) ----------
CAP = {
 'L01': [['உங்க', 'வீட்டுல', '^ரெண்டு பேரும்'], ['*WEIGHT', 'குறைக்கணும்னு'], ['!எத்தனை தடவை', 'முடிவு', 'பண்ணியிருப்பீங்க?']],
 'L02': [['இந்த', 'VIDEO-வ', '^முழுசா', 'பாருங்க'], ['உங்க', '*FAMILY-க்கான', '*ANSWER'], ['இந்த', 'VIDEO-ல', 'இருக்கு']],
 'L03': [['HI,', 'நான்', '*COACH PRADHEESH'], ['^TM NUTRITION', 'CENTRE,', 'TRICHY']],
 'L04': [['^18 வருஷமா'], ['நூற்றுக்கணக்கான', '*FAMILIES'], ['*HEALTHY-ஆ', 'மாத்தியிருக்கோம்']],
 'L05': [['இப்போ', 'ஒரு', '^புது BATCH'], ['*COUPLES-க்கு', 'மட்டும்']],
 'L06': [['மூணு நாள்', '*DIET...'], ['அப்புறம்', '!BIRYANI']],
 'L07': [['GYM', 'MEMBERSHIP', 'கட்டி'], ['முழுசா', '!ரெண்டு வாரம்', 'கூட', 'போறது இல்ல']],
 'L08': [['ராத்திரி', '^12 மணி', 'வரைக்கும்'], ['கையில', '!MOBILE']],
 'L09': [['^"நாளைக்கு', 'ஆரம்பிச்சுக்கலாம்"'], ['ரெண்டு பேரும்', 'ஒருவருக்கொருவர்'], ['சமாதானப்படுத்திப்பீங்க']],
 'L10': [['PROBLEM', 'உங்க', '!WILL POWER-ல', 'இல்ல'], ['உங்க', '*வீட்டோட PATTERN-ல', 'இருக்கு']],
 'L11': [['இவரு', '^58 வயசு']],
 'L12': [['இவரு', 'ERODE-லருந்து', '^32 வயசு'], ['!26 KG', 'EXCESS WEIGHT']],
 'L13': [['இவங்க', '^48 வயசு']],
 'L14': [['எல்லாருமே'], ['!"இது எனக்கு', '!WORK ஆகாது"'], ['னு நினைச்சாங்க']],
 'L15': [['ஆனா', 'அந்த', '*மாற்றம்', 'ஆரம்பிச்சது'], ['வெறும்', '*3 நாள்ல']],
 'B01': [['இங்க', '*DAY 1', 'வந்து'], ['எனக்கு', 'நெஞ்செரிச்சல்'], ['^குறைய', 'ஆரம்பிச்சது']],
 'B02': [['ரொம்ப', '*ACTIVE-ஆ,', '*FRESH-ஆ'], ['FEEL', 'பண்ண', 'ஆரம்பிச்சேன்']],
 'L16': [['^3 நாள்ல', 'எல்லாம்'], ['CHANGE', 'ஆயிடுமா?']],
 'L17': [['!அது எப்படி?']],
 'L18': [['*YES.', 'CHANGE', 'START', 'ஆகுறது'], ['*POSSIBLE']],
 'L19': [['^DAY 1:', '*HABITS']],
 'L20': [['DAY 1-ல', 'நீங்க', 'உங்க', '!MOBILE-ஐ'], ['CONTINUOUS-ஆ', 'பாத்துக்கிட்டு', 'இல்லாம']],
 'L21': [['உங்களோட', '*HABIT PATTERN-ஐ'], ['எப்படி', '^TUNE', 'பண்றதுன்னு']],
 'L22': [['*HAND-HOLD', '*GUIDANCE-ல'], ['சொல்லித்தர', 'மாதிரி']],
 'L23': [['^DAY 1', 'இருக்கப்போகுது']],
 'L24': [['^DAY 2:', '*FAMILY HEALTH']],
 'L25': [['உங்க', 'HEALTH', '^உங்களுக்கு மட்டும்', 'இல்லாம'], ['உங்க', '*மொத்த FAMILY-யும்'], ['எப்படி', '*HEALTHY-ஆ', 'இருக்கப்போறீங்கன்னு'], ['நாங்க', 'சொல்லித்தரப்போறோம்']],
 'L26': [['^DAY 3:', '*FAMILY HAPPINESS']],
 'L28': [['அந்த', '*HAPPINESS', 'உங்க', 'வீட்டுக்குள்ள', 'வரணும்னா'], ['நீங்களும்', 'உங்க', 'FAMILY-யும்'], ['என்ன', '^ROUTINE', 'FOLLOW', 'பண்ணணும்'], ['எப்படி', 'அந்த', '*HAPPINESS']],
 'L30': [['வீட்டுக்குள்ள', 'கொண்டு', 'வரணும்ங்கிறதையும்'], ['சொல்லப்போறோம்']],
 'L31': [['இதோட', '*FINANCIAL', '*INDEPENDENCE-க்கான'], ['^FIRST STEP', 'நீங்க', 'எடுக்கப்போறீங்க']],
 'L33': [['இத்தனை', '*SECRETS-உம்'], ['நாங்க', '^JUST ₹555-க்கு'], ['கொடுக்கப்போறோம்']],
 'L34': [['3 நாள்', 'LIVE-ஆ', 'ATTEND', 'பண்ணிட்டு'], ['உங்களுக்கு', 'VALUE-வே', 'கிடைக்கலைன்னு', 'நினைச்சீங்கன்னா'], ['*100%', '*MONEY BACK']],
 'L35': [['RISK', 'முழுசா', '^என் பக்கம்']],
 'L36': [['ஆனா', 'இந்த', 'BATCH-க்கு'], ['TRICHY-லருந்து', 'வெறும்', '!5 COUPLES-தான்'], ['நானே', '^PERSONAL-ஆ', 'TRAIN', 'பண்ணப்போறேன்']],
 'L37': [['கீழே', 'இருக்கும்', '^BUTTON-ஐ', 'CLICK', 'பண்ணி'], ['FAMILY-ஓட', 'இந்த', '*JOURNEY-ஐ', 'START', 'பண்ணுங்க']],
}
# caption position follows the layout under it: side/tside -> over the speaker panel; full scenes keep the bottom band
def layout_at(t):
    for bid, o0, o1, sc, lay, ex, kw, src in BROLL:
        if o0 <= t < o1: return lay
    return 'face'
PUNCH = []   # (o0, o1, zoom) face-only punch-ins on emphasis lines
for tid, z in [('L01', 1.10), ('L04', 1.12), ('L05', 1.08), ('L15', 1.14), ('L16', 1.12), ('L17', 1.18), ('L33', 1.10), ('L34', 1.06), ('L35', 1.14), ('L36', 1.10), ('L37', 1.06)]:
    a, b = span(tid); PUNCH.append((a, b, z))
DESAT = [span('L09'), span('L14')]
MUSIC = [(0.0, span('L10')[1], 'dark'), (span('L10')[1], span('L18')[0], 'warm'), (span('L18')[0], span('L33')[0], 'tech'), (span('L33')[0], TOTAL, 'uplift')]

def build():
    items, captions, sfx = [], [], []
    for bid, o0, o1, sc, lay, ex, kw, src in BROLL:
        d = dict(type=sc, t0=round(o0, 3), t1=round(o1, 3), layout='side' if lay == 'tside' else lay, id=bid); ex = dict(ex); ex.pop('clip', None); d.update(ex)
        items.append(d); sfx += [(o0 - 0.1, 'whoosh')]
        for c in (ex.get('cues') or [])[:3]: sfx.append((o0 + c, 'pop'))
    for ty, o0, o1, ex in GFX:
        d = dict(type=ty, t0=round(o0, 3), t1=round(o1, 3)); d.update(ex); items.append(d)
        sfx.append((o0, {'text': 'hit', 'badge': 'pop', 'price': 'cash', 'stamp': 'thud', 'cta': 'ding', 'lower': 'swipe', 'flash': 'whoosh', 'endcard': 'hit'}[ty]))
    for tid, chunks in CAP.items():
        ps = [p for p in pieces if p['id'] == tid]; o0, o1 = ps[0]['o0'], ps[-1]['o1']
        wts = [sum(len(w.lstrip('*^!')) for w in c) + 3 for c in chunks]; tot = sum(wts); t = o0
        for c, wt in zip(chunks, wts):
            d = (o1 - o0) * wt / tot; words = [w.lstrip('*^!') for w in c]
            hl = [i for i, w in enumerate(c) if w[0] in '*^!']; col = {'*': '#00C896', '^': '#FFD60A', '!': '#FF3B30'}
            cc = next((col[w[0]] for w in c if w[0] in col), None); lay = layout_at(t + d / 2)
            pos = 'side' if lay in ('side', 'tside') else None
            cap = dict(t0=round(t, 3), t1=round(t + d, 3), words=words, hl=hl)
            if cc: cap['col'] = cc
            if pos: cap['pos'] = pos
            captions.append(cap); t += d
    # face-only lines with a big on-face text graphic at the same spot: move captions out of its way (they sit at the bottom band; fine)
    for s, e in DESAT: sfx.append((s, 'thud'))
    sfx.append((span('L37')[0] - 1.4, 'riser'))
    sfx = sorted([(max(0, round(t, 3)), n) for t, n in sfx])
    tl = dict(total=round(TOTAL, 3), items=items, captions=captions)
    os.makedirs(W + 'gfx', exist_ok=True); os.makedirs(W + 'audio', exist_ok=True)
    json.dump(tl, open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    # per-frame comp instructions
    frames = []; n = int(round(TOTAL * FPS)); last_ts = 0
    for i in range(n):
        t = i / FPS; p = next((q for q in pieces if q['o0'] <= t < q['o1']), None); fr = dict(L='face', z=1.0)
        if p and p['k'] == 'seg': last_ts = p['s0'] + (t - p['o0'])
        fr['ts'] = round(last_ts, 4)
        if p and p['k'] == 'bite':
            fr['L'] = 'full'; fr['V'] = [p['clip'], round(t - p['o0'], 4), round((t - p['o0']) / p['dur'], 3)]
        for bid, o0, o1, sc, lay, ex, kw, src in BROLL:
            if o0 <= t < o1 and not (p and p['k'] == 'bite'):
                fr['L'] = lay
                if 'clip' in ex: fr['V'] = [ex['clip'][0], round(ex['clip'][1] + t - o0, 4), round((t - o0) / (o1 - o0), 3)]
        if fr['L'] == 'face':
            for a, b, z in PUNCH:
                if a <= t < b: fr['z'] = z
        if any(a <= t < b for a, b in DESAT): fr['des'] = True
        if t >= o: fr['L'] = 'face'
        frames.append(fr)
    json.dump(frames, open(W + 'frames.json', 'w'))
    keep = [[p['s0'], p['s1']] for p in pieces if p['k'] == 'seg']
    json.dump(dict(total=TOTAL, pieces=pieces, sfx=sfx, music=MUSIC, bites={p['id']: p['clip'] for p in pieces if p['k'] == 'bite'}), open(W + 'audio/cues.json', 'w'))
    json.dump(dict(face=[910, 330]), open(W + 'comp_cfg.json', 'w'))
    with open(os.path.join(HERE, 'broll_plan.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['ID', 'Final time (s, after 1.2x)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, o0, o1, sc, lay, ex, kw, src in sorted(BROLL, key=lambda r: r[1]):
            vis = f'clip {ex["clip"][0]}' + (f' + "{sc}" labels' if sc in ('testi', 'vid') else '') if 'clip' in ex else f'animated "{sc}" scene' + (f' ({ex["v"]})' if 'v' in ex else '')
            lic = 'client-supplied testimonial - confirm written consent' if 'P2' in src else 'original - no licence needed'
            w.writerow([bid, f'{o0 / 1.2:.1f}-{o1 / 1.2:.1f}', kw, vis, src, {'tside': 'side (clip card + speaker)', 'side': 'side (animation + speaker)', 'full': 'full cutaway'}[lay], f'{(o1 - o0) / 1.2:.1f}', 'rendered', lic])
    cov = sum(o1 - o0 for _, o0, o1, *_ in BROLL); full = sum(o1 - o0 for _, o0, o1, sc, lay, *_ in BROLL if lay == 'full')
    print(f'output {TOTAL:.1f}s pre-speed = {TOTAL / 1.2:.1f}s final | B-roll {cov / TOTAL * 100:.0f}% (full cutaway {full / 1.2:.1f}s) | {len(captions)} captions | {len(items)} items')

if __name__ == '__main__':
    build()
