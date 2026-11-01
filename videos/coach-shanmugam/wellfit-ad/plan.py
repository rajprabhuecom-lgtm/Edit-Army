"""EDL for Coach Shanmugam - SK WellFit Club ad (Namakkal).
Alignment follows the client's script (approved by Prabhuraj 1 Nov 2026):
  question (6.30.01) -> coach intro (6.30.00_2) -> support (6.30.00_1) -> CTA (6.30.02, 0-6.75 s)
  -> offer / "appointment details" (6.30.01_1) -> close (6.30.02, 6.75 s-end)
src.mkv = those 6 pieces joined, each scaled to 1080 wide and cropped to 1080x1920 from the top.
Cues below are written on the ORIGINAL recording timeline (clips joined 6.30.00_1, 6.30.00_2, 6.30.01, 6.30.01_1, 6.30.02 -
see the transcript in notes.md) and mapped onto src.mkv with M(). Final time = output / 1.2."""
import json, bisect, csv
W = '/home/user/w/'
SIL = [(0.0, 1.50), (8.86, 11.91), (18.57, 18.78), (22.24, 25.07), (33.30, 35.42), (40.53, 43.30), (46.55, 46.79),
       (48.28, 48.75), (51.92, 53.21), (56.97, 58.13)]   # src.mkv time
def M(t):
    """original-recording time -> src.mkv time"""
    if t < 23.913: return t + 10.21          # 6.30.00_2 intro, 6.30.00_1 support
    if t < 34.124: return t - 23.913         # 6.30.01 question (opening)
    if t < 46.149: return t + 6.749          # 6.30.01_1 offer
    if t < 52.899: return t - 12.026         # 6.30.02 first half: CTA
    return t                                 # 6.30.02 second half: close
END = 59.80   # hold under the end card (frames past the source end repeat the last frame; the end card covers them)
segs = []; t = 0.0
for a, b in SIL:
    if a > t: segs.append([t, a])
    t = b
PRE, POST = 0.06, 0.10
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), e + POST
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep.append([56.97, END])   # hold the tail under the end card
ostarts = []; acc = 0
for a, b in keep: ostarts.append(acc); acc += b - a
TOTAL = acc
def s2o(t):
    for (a, b), o in zip(keep, ostarts):
        if t < a: return o
        if t <= b: return o + (t - a)
    return TOTAL
def o2s(t):
    i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])

# B-roll: (id, s0, s1, scene, layout, extra, keyword)   cue times inside extras are SOURCE times
BROLL = [
 ('B01', 3.62, 6.25, 'vid', 'split', dict(file='B01_studio.mkv', ss=0.0, cy=26, csz=44,
      chips=[['🏋️ SK WELLFIT CLUB'], ['WELLNESS & FITNESS CENTRE', '#00C896', '#04110c', '#00C896']], ccues=[3.70, 4.92]), '"SK WellFit Club, Wellness & Fitness Centre" - real session footage'),
 ('B02', 7.98, 12.03, 'beforeafter', 'split', dict(title='<span class="y" data-cnt="1000">1000</span><span class="y">+</span> PEOPLE ✓', ph=[3, 5, 4], pcues=[8.10, 9.40, 10.70]),
      '"1000+ people, their transformation" - real client photos'),
 ('B03', 15.80, 19.71, 'pillars', 'split', dict(pcues=[15.85, 17.27, 18.63], peq=19.30), '"correct care, regular follow-up, consistent guidance"'),
 ('B04', 19.71, 23.10, 'beforeafter', 'split', dict(title='SUPER <span class="y">TRANSFORMATION</span>', tsz=66, ph=[1, 2], nolab=[1], pcues=[19.75, 21.45]),
      '"this super transformation" - real client photos with kg labels'),
 ('B05', 27.25, 29.75, 'fitdress', 'split', dict(pcues=[27.25, 27.87, 28.49]), '"look fit, wear modern dress"'),
 ('B06', 37.80, 42.20, 'offerstack', 'split', dict(pcues=[37.82, 39.46]), '"one-to-one consultation, full body analysis"'),
 ('B07', 42.20, 44.70, 'vid', 'split', dict(file='B07_trial.mkv', ss=0.2, cy=26, csz=48,
      chips=[['🏋️ FITNESS TRIAL PROGRAM ✓', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[42.35]), '"fitness trial program" - real session footage'),
]
GFX = [
 ('badge', 1.80, 3.62, {'html': '💪 COACH சண்முகம்', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('text', 6.32, 7.95, {'html': '<span class="y">6 YEARS</span><br>EXPERIENCE', 'y': 200, 'size': 110}),
 ('text', 25.45, 27.22, {'html': 'WEIGHT<br><span class="y">REDUCE?</span> ⚖️', 'y': 200, 'size': 120}),
 ('badge', 29.79, 32.75, {'html': '💪 JOIN SK WELLFIT CLUB', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 62}),
 ('badge', 36.52, 37.80, {'html': '🔥 EXCLUSIVE OFFER', 'y': 230, 'size': 72}),
 ('text', 47.45, 48.45, {'html': 'இன்னும் ஏன்<br><span class="y">யோசிக்கிறீங்க?</span> 🤔', 'y': 200, 'size': 92}),
 ('flash', 48.45, 48.60, {}),
 ('cta', 48.49, 52.58, {'label': '📅 BOOK APPOINTMENT', 'badge': '👇 CLICK THE LINK BELOW', 'y': 1060}),
 ('text', 53.21, 56.97, {'html': 'START<br><span class="g">TODAY 🚀</span>', 'y': 200, 'size': 140}),
 ('clubend', 56.97, END, {'loc': 'COACH SHANMUGAM • NAMAKKAL'}),
]
CAP = [
 (1.70, 3.62, [['HI,', 'நான்', 'உங்க'], ['COACH', '^சண்முகம்']]),
 (3.62, 6.25, [['*SK WELLFIT', '*CLUB'], ['WELLNESS &', 'FITNESS', 'CENTRE']]),
 (6.32, 7.95, [['^6 YEAR', 'EXPERIENCE-ஓட']]),
 (7.98, 9.80, [['*1000+', 'PEOPLE-க்கு']]),
 (9.80, 12.03, [['அவங்க', '^TRANSFORMATION-க்கு'], ['HEALTHY-ஆ', 'SUPPORT'], ['பண்ணிருக்கேன்']]),
 (14.86, 15.80, [['இந்த', 'COMBINATION-ல']]),
 (15.85, 17.20, [['*CORRECT-ஆன', '*CARE']]),
 (17.27, 18.58, [['*REGULAR', '*FOLLOW-UP']]),
 (18.63, 19.71, [['*CONSISTENT', '*GUIDANCE']]),
 (19.71, 23.10, [['இந்த', '^SUPER', '^TRANSFORMATION-க்கு'], ['முக்கியமான', 'காரணம்']]),
 (25.45, 27.22, [['உங்களுக்கு', '^WEIGHT', '^REDUCE'], ['பண்ணணும்னு', 'ஆசையா?']]),
 (27.25, 29.72, [['பார்க்க', '*FIT-ஆ'], ['*MODERN', '*DRESS', 'போடணும்னு'], ['தோணுதா?']]),
 (29.79, 32.75, [['அப்படின்னா', 'இப்பவே'], ['*SK WELLFIT', '*CLUB-ல'], ['^JOIN', 'பண்ணுங்க']]),
 (36.52, 37.80, [['இப்ப', '^EXCLUSIVE', '^OFFER-ஆ']]),
 (37.82, 39.40, [['*ONE-TO-ONE'], ['*CONSULTATION']]),
 (39.46, 41.05, [['*FULL BODY', '*ANALYSIS']]),
 (41.18, 42.25, [['இதோட']]),
 (42.30, 45.16, [['*FITNESS', '*TRIAL', '*PROGRAM'], ['உங்களுக்கு', 'குடுத்துட்டு', 'இருக்கோம்']]),
 (47.45, 48.45, [['இன்னும்', '!ஏன்', '!யோசிக்கிறீங்க?']]),
 (48.49, 50.40, [['கீழ', 'இருக்கிற', '^LINK-ஐ'], ['^CLICK', 'பண்ணி']]),
 (50.40, 52.58, [['உங்க', '*APPOINTMENT-ஐ'], ['இப்பவே', '^BOOK', 'பண்ணுங்க']]),
 (53.21, 56.97, [['உங்களோட', '*HEALTHY'], ['*TRANSFORMATION', 'JOURNEY-ஐ'], ['^இன்னைக்கே', '^START', 'பண்ணுங்க']]),
]
PUNCH = [(1.6, 3.62, 1.10), (6.3, 7.96, 1.16), (25.4, 27.23, 1.12), (29.78, 32.8, 1.08), (36.5, 37.81, 1.15),
         (47.4, 48.46, 1.18), (48.46, 52.6, 1.06), (53.2, 55.0, 1.10), (55.0, 57.0, 1.16)]
DESAT = []
MUSIC = [(0.0, 22.24, 'pulse'), (22.24, 43.30, 'tech'), (43.30, END, 'uplift')]   # src.mkv time
SFX = [(25.45, 'hit'), (1.75, 'thud'), (36.52, 'hit'), (48.05, 'riser'), (48.49, 'hit'), (56.97, 'hit')]
SCENE_SFX = {}
# map everything authored on the original timeline onto src.mkv
_CUE = ('ccues', 'pcues')
BROLL = [(i, M(a), M(b), sc, l, {k: ([M(x) for x in v] if k in _CUE else (M(v) if k in ('peq', 'bcue') else v)) for k, v in ex.items()}, kw) for i, a, b, sc, l, ex, kw in BROLL]
GFX = [(ty, M(a), (b if b == END else M(b)), ex) for ty, a, b, ex in GFX]
CAP = [(M(a), M(b), c) for a, b, c in CAP]
PUNCH = [(M(a), M(b), z) for a, b, z in PUNCH]
SFX = [(M(t), n) for t, n in SFX]

def build():
    items = []; captions = []; sfx = list(SFX)
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid)
        ex = dict(ex)
        rel = lambda ts: [round(s2o(x) - o0, 3) for x in ts]
        if 'ccues' in ex: d['ct'] = rel(ex.pop('ccues')); sfx += [(s2o(x), 'pop') for x in [o2s(o0 + c) for c in d['ct']]]
        if 'bcue' in ex: b = ex.pop('bcue'); d['bt'] = rel([b])[0]; sfx.append((b, 'thud'))
        if 'qcues' in ex: ex['_q'] = ex['qcues'] + [ex['qend']]; d['cues'] = rel(ex.pop('qcues')); d['endq'] = rel([ex.pop('qend')])[0]; sfx += [(x, 'pop') for x in ex.get('_q', [])]
        if 'kcues' in ex: d['cues'] = rel(ex['kcues']); sfx += [(x + .45, 'tick') for x in ex.pop('kcues')] + [(s0 + 0.5, 'swipe')]
        if 'mcues' in ex: d['cues'] = rel(ex['mcues']); m = ex.pop('mcues'); sfx += [(m[1], 'swipe'), (m[2] + .3, 'thud'), (m[3], 'pop')]
        if 'pcues' in ex: d['cues'] = rel(ex['pcues']); sfx += [(x, 'pop') for x in ex.pop('pcues')]
        if 'peq' in ex: d['eqt'] = rel([ex.pop('peq')])[0]; sfx.append((o2s(o0 + d['eqt']), 'ding'))
        if 'dcues' in ex: d['cues'] = rel(ex['dcues']); sfx += [(x, 'pop') for x in ex.pop('dcues')]
        if 'ftc' in ex: d['ftc'] = rel([ex.pop('ftc')])[0]
        ex.pop('_q', None); d.update(ex); items.append(d)
        sfx.append((o0 - 0.12, 'whoosh', 1))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
        if ty in ('text', 'badge'): sfx.append((s0, 'pop'))
        if ty == 'cta': sfx.append((s0 + 0.35, 'click'))
    for s0, s1, chunks in CAP:
        o0, o1 = s2o(s0), s2o(s1); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts); t = o0
        for c, wt in zip(chunks, wts):
            d = (o1 - o0) * wt / tot
            words = [w.lstrip('*!^') for w in c]; hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
            col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
            captions.append(dict(t0=t, t1=t + d, words=words, hl=hl, col=col)); t += d
    for a, b in zip(captions, captions[1:]):
        if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        for it in items:
            if it['t0'] <= mid < it['t1']:
                if it.get('layout') == 'split': c['pos'] = 'split'
                if it['type'] == 'cta': c['pos'] = 'hi'
                if it['type'] in ('endcard', 'clubend'): c['pos'] = 'none'
    json.dump(dict(items=items, captions=captions, total=TOTAL), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.08
        for a, b, zz in PUNCH:
            if a <= ts <= b: z = zz
        L = None; V = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']:
                L = it['layout']
                if it['type'] == 'vid': V = [it['file'], round(it.get('ss', 0) + to - it['t0'], 4), round((to - it['t0']) / (it['t1'] - it['t0']), 4)]
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=V, des=any(a <= ts <= b for a, b in DESAT)))
    json.dump(frames, open(W + 'frames.json', 'w'))
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s, joined)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            src = f'client session footage {ex["file"]}' if sc == 'vid' else (f'real client before/after photos {ex["ph"]} in animated cards' if sc == 'beforeafter' else f'animated "{sc}" scene')
            lic = 'client footage - consent on file with coach' if sc in ('vid', 'beforeafter') else 'original - no licence needed'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, 'P2 real' if sc in ('vid', 'beforeafter') else 'P5 motion graphics',
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/1.2:.1f}s) | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
