"""EDL: New Life Nutritions weight-loss ad (Coach Tamil Elakkiya) + client testimonial.
src.mkv = main_video[0:23.2667] + Testimonial[0:33.4333] + main_video[23.2667:]   (JOINED time)
Author times with m() (coach clip time) and T() (testimonial clip time). Final = output / 1.2."""
import json, bisect, csv
W = '/home/user/w/'
CUT, TLEN = 23.2667, 33.4333
m = lambda t: t if t < CUT else t + TLEN          # main-video time -> joined
T = lambda t: CUT + t                              # testimonial time -> joined
SIL = [(0, 0.62), (4.46, 4.80), (6.52, 6.86), (9.72, 10.16), (15.54, 16.28), (19.74, 20.08), (23.02, T(0))]
SIL += [(T(a), T(b)) for a, b in [(1.54, 1.96), (5.22, 5.52), (8.32, 8.68), (11.28, 11.54), (12.46, 12.72), (17.84, 18.12),
                                    (19.16, 19.44), (23.04, 23.34), (27.62, 27.92), (31.46, 31.76)]]
SIL += [(T(32.82), m(23.52))]
SIL += [(m(a), m(b)) for a, b in [(28.00, 28.70), (32.50, 32.82), (36.56, 37.24), (39.94, 40.64), (44.46, 45.88), (49.80, 50.88),
        (52.20, 52.60), (55.24, 55.62), (57.14, 57.68), (59.30, 59.54), (61.30, 61.60), (62.24, 63.82), (65.64, 66.06),
        (66.72, 67.12), (68.16, 68.58), (70.16, 70.82)]]
TAIL = (m(72.26), m(73.60))          # hold under the end card
PRE, POST = 0.06, 0.10
segs, t = [], 0.0
for a, b in SIL:
    if a > t: segs.append([t, a])
    t = b
segs.append([t, TAIL[0]])
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), e + POST
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep[-1][1] = TAIL[1]
END = TAIL[1]
ostarts, acc = [], 0
for a, b in keep: ostarts.append(acc); acc += b - a
TOTAL = acc
def s2o(t):
    for (a, b), o in zip(keep, ostarts):
        if t < a: return o
        if t <= b: return o + (t - a)
    return TOTAL
def o2s(t):
    i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])
def src_of(ts): return 't' if T(0) <= ts < T(TLEN) else 'c'

I = 'img/'
NO = '#2a1010', '#FF3B30', '#FF3B30'
# (id, s0, s1, scene, layout, extra, keyword)   all cue values are JOINED source times (converted to relative output time in build)
BROLL = [
 ('B01', m(4.78), m(6.86), 'vid', 'full', dict(file='B1_scale.mkv', ss=0.0), '"trying to lose weight?" - Flow clip: woman on scale'),
 ('B02', m(6.86), m(10.16), 'vid', 'split', dict(file='B1_scale.mkv', ss=3.2, cy=40, csz=50,
      chips=[['✅ இது WORK ஆகுமா?'], ['❌ அது WORK ஆகலையா?', *NO]], ct=[m(7.0), m(8.4)]), '"what works, what doesn\'t?" - Flow clip: scrolling diet videos'),
 ('B03', m(10.16), m(12.78), 'struggle', 'split', dict(cues=[m(10.20), m(10.85), m(11.55)], xcues=[m(11.95), m(12.15), m(12.35)], nrc=m(99),
      cards=[['🥗', 'DIET'], ['🏋️', 'WORKOUT'], ['📱', 'பல விஷயங்கள்']]), '"diet, workout, many things tried"'),
 ('B04', m(12.78), m(15.60), 'vid', 'full', dict(file='B2_yoga.mkv', ss=0.4, big='<span class="r">NO RESULT?</span> 😩', bt=m(13.3), by=250, bsz=120), '"no expected result" - Flow clip: tired on yoga mat'),
 ('B05', m(16.28), m(19.74), 'vid', 'split', dict(file='B3_rush.mkv', ss=0.2, cy=40, csz=50,
      chips=[['⏰ BUSY LIFESTYLE'], ['❌ NO CONSISTENCY', *NO]], ct=[m(16.80), m(18.05)]), '"busy lifestyle, no consistency" - Flow clip: mother rushing'),
 ('B06', T(3.24), T(11.28), 'ba', 'split', dict(before=I + 'client_before.jpg', after=I + 'client_after.jpg', lbl=False, title='HER <span class="g">TRANSFORMATION</span>',
      c1=T(4.30), c2=T(6.60), stamp='REAL CLIENT ✓'), 'testimonial: her own before/after photo'),
 ('B07', T(18.12), T(27.62), 'ba', 'split', dict(before=I + 'extra_before.jpg', after=I + 'extra_after.jpg', lbl=False, title='ONE MORE <span class="g">CLIENT</span>',
      kg=[86, 66], c1=T(19.0), c2=T(21.4), stamp='-20 KG 🔥'), 'testimonial: extra client 86 kg -> 66 kg (numbers from the photo)'),
 ('B08', m(23.52), m(28.00), 'struggle', 'split', dict(good=True, title='PROPER <span class="g">GUIDANCE</span>', cards=[['🥗', 'NUTRITION'], ['🏃‍♀️', 'FITNESS'], ['💚', 'HEALTHY']],
      cues=[m(23.60), m(24.30), m(25.0)], xcues=[m(24.32), m(24.96), m(26.52)], nrc=m(27.15), stamp='✓ CHANGES ACHIEVED'), '"proper nutrition & fitness guidance -> healthy changes"'),
 ('B09', m(29.95), m(36.56), 'ba', 'split', dict(before=I + 'coach_before.jpg', after=I + 'coach_after.jpg', title="COACH'S OWN <span class=\"g\">JOURNEY</span>",
      c1=m(30.40), c2=m(31.30), stamp='5 YEARS EXPERIENCE'), '"I\'m Tamil Elakkiya, 5 years at New Life Nutritions" - coach before/after'),
 ('B10', m(37.24), m(44.46), 'steps', 'split', dict(nodes=[['🏠', 'LIFESTYLE'], ['🎯', 'YOUR GOALS'], ['📋', 'PERSONAL PLAN'], ['🤝', 'STEP-BY-STEP']],
      cues=[m(37.80), m(39.12), m(41.02), m(42.92)]), '"lifestyle & goals -> personalized, step-by-step support"'),
]
GFX = [
 ('badge', 0.62, m(4.46), {'html': '📍 சென்னை மக்களே!', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('badge', m(20.08), m(23.02), {'html': 'நம்ம CLIENTS-உம் 👇', 'y': 230, 'size': 66}),
 ('badge', T(0.0), T(3.24), {'html': '⭐ REAL CLIENT STORY', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 62}),
 ('badge', T(11.54), T(17.84), {'html': '💬 அவங்க வார்த்தையில', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 58}),
 ('badge', T(27.92), T(32.82), {'html': '💚 WEIGHT LOSS SUCCESS', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 58}),
 ('badge', m(28.70), m(29.95), {'html': '👋 COACH தமிழ் இலக்கியா', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('ticket', m(45.88), m(49.80), {'y': 170}),
 ('badge', m(50.88), m(55.24), {'html': '📍 CHENNAI', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('badge', m(55.62), m(57.14), {'html': "⏰ MISS பண்ணாதீங்க!", 'y': 230, 'size': 64}),
 ('flash', m(57.68), m(57.83), {}),
 ('cta', m(57.68), m(62.24), {'label': '👇 CLICK & REGISTER', 'badge': '🎁 3 DAYS FREE TRIAL', 'y': 1040}),
 ('cta', m(63.82), m(72.26), {'label': '📅 BOOK APPOINTMENT', 'badge': '🌿 NEW LIFE NUTRITIONS', 'y': 1040}),
 ('nlend', m(72.26), END, {'loc': 'CHENNAI'}),
]
CAP = [
 (0.62, m(4.46), [['சென்னையில்', '*WEIGHT LOSS'], ['!STRUGGLE', 'பண்ற', 'மக்களுக்கு'], ['ஒரு', '^IMPORTANT', '^UPDATE!']]),
 (m(4.80), m(6.52), [['*WEIGHT LOSS', 'பண்ண'], ['TRY', 'பண்றீங்களா?']]),
 (m(6.86), m(9.72), [['எது', '^WORK', 'ஆகுது?'], ['எது', '!WORK', 'ஆகல?'], ['புரியலையா?']]),
 (m(10.16), m(12.78), [['*DIET,', '*WORKOUT'], ['பல', 'விஷயங்கள்'], ['TRY', 'பண்ணியும்']]),
 (m(12.78), m(15.54), [['EXPECTED', '!RESULT'], ['கிடைக்காம'], ['!STRUGGLE', 'பண்றீங்களா?']]),
 (m(16.28), m(19.74), [['^BUSY', '^LIFESTYLE', 'நால'], ['!CONSISTENCY'], ['MAINTAIN', 'பண்ண', 'முடியலையா?']]),
 (m(20.08), m(23.02), [['நம்ம', '*CLIENTS-உம்'], ['இதே', 'மாதிரிதான்'], ['!STRUGGLE', 'பண்ணியிருக்காங்க']]),
 (T(27.92), T(31.46), [['*WEIGHT LOSS', 'பண்ணதுக்கு'], ['மிகவும்', '^மகிழ்ச்சியாக'], ['இருக்கிறேன்']]),
 (T(31.76), T(32.82), [['மிகவும்', '*நன்றி', 'மேடம் 🙏']]),
 (m(23.52), m(28.00), [['ஆனா', '*PROPER', '*NUTRITION'], ['*FITNESS', 'GUIDANCE'], ['FOLLOW', 'பண்ணி'], ['^HEALTHY', '^CHANGES'], ['ACHIEVE', 'பண்ணியிருக்காங்க']]),
 (m(28.70), m(29.95), [['நான்', '^தமிழ்', '^இலக்கியா']]),
 (m(29.95), m(32.50), [['*NEW LIFE', '*NUTRITIONS-ல'], ['^5 YEARS', 'EXPERIENCE-ஓட']]),
 (m(32.82), m(36.56), [['உங்க', 'FITNESS', '&', 'WEIGHT'], ['MANAGEMENT', 'JOURNEY-க்கு'], ['^GUIDE', 'பண்ணிட்டு', 'இருக்கேன்']]),
 (m(37.24), m(39.94), [['உங்க', '^LIFESTYLE'], ['&', '*FITNESS GOALS-க்கு', 'ஏத்த']]),
 (m(40.64), m(44.46), [['*PERSONALIZED', 'GUIDANCE', 'மூலமா'], ['^STEP-BY-STEP-ஆ', 'SUPPORT', 'பண்றோம்']]),
 (m(45.88), m(49.80), [['இப்போ', '*NEW LIFE NUTRITIONS-ல'], ['^3 DAYS', '^FREE TRIAL'], ['OFFER', 'AVAILABLE!']]),
 (m(50.88), m(52.20), [['^சென்னையில', 'இருக்கிற', 'நீங்களும்']]),
 (m(52.60), m(57.14), [['உங்க', '*FITNESS JOURNEY'], ['START', 'பண்ண', 'READY-ஆ', 'இருந்தா'], ['இந்த', 'OFFER-ஐ', '!MISS', 'பண்ணாதீங்க!']]),
 (m(57.68), m(62.24), [['கீழே', '^BUTTON-ஐ', '^CLICK', 'பண்ணி'], ['*ONLINE', '*REGISTRATION-ஐ'], ['இப்பவே', 'COMPLETE', 'பண்ணுங்க']]),
 (m(63.82), m(68.16), [['உங்க', '*APPOINTMENT-ஐ'], ['^BOOK', 'பண்ணி'], ['உங்க', 'FITNESS', 'JOURNEY-யை']]),
 (m(68.58), m(70.16), [['*NEW LIFE', '*NUTRITIONS-ஓட']]),
 (m(70.82), m(72.26), [['^இன்னைக்கே', 'START', 'பண்ணுங்க!']]),
]
PUNCH = [(0.6, 2.4, 1.10), (2.4, m(4.5), 1.17), (m(20.0), m(21.6), 1.08), (m(21.6), m(23.1), 1.16), (T(0), T(3.2), 1.06),
         (T(11.5), T(14.6), 1.08), (T(14.6), T(17.9), 1.14), (T(27.9), T(31.5), 1.10), (T(31.5), T(33.4), 1.18),
         (m(28.6), m(30.0), 1.14), (m(45.8), m(49.9), 1.08), (m(50.8), m(55.3), 1.12), (m(55.5), m(57.2), 1.18),
         (m(57.6), m(62.3), 1.06), (m(63.8), m(68.2), 1.10), (m(68.5), m(72.3), 1.15)]
DESAT = []
MUSIC = [(0.0, m(23.1), 'dark'), (T(0), m(23.4), 'warm'), (m(23.4), m(45.5), 'tech'), (m(45.5), END, 'uplift')]
SFX = [(0.62, 'hit'), (m(20.08), 'thud'), (T(0), 'hit'), (m(28.70), 'pop'), (m(45.88), 'cash'), (m(57.30), 'riser'), (m(57.68), 'hit'), (m(72.26), 'hit')]
CROP = {'c': 230, 't': 110}     # split-screen: source y where the bottom panel starts
ZC = {'c': 620, 't': 470}       # zoom centre y (face)

def build():
    items, captions, sfx = [], [], [(s2o(t), n) for t, n in SFX]
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        rel = lambda x: round(s2o(x) - o0, 3)
        for k in ('cues', 'xcues', 'ct'):
            if k in ex: ex[k] = [rel(x) for x in ex[k]]
        for k in ('c1', 'c2', 'nrc', 'bt'):
            if k in ex: ex[k] = rel(ex[k]) if ex[k] < 900 else 99
        d.update(ex); items.append(d)
        sfx.append((o0 - 0.12, 'whoosh'))
        for x in ex.get('ct', []) + ex.get('cues', []): sfx.append((o0 + x, 'pop'))
        for x in ex.get('xcues', []): sfx.append((o0 + x, 'ding' if ex.get('good') else 'thud'))
        if sc == 'ba': sfx += [(o0 + ex['c1'], 'swipe'), (o0 + ex['c2'] + .55, 'hit')]
        if sc == 'struggle' and ex.get('nrc', 99) < 90: sfx.append((o0 + ex['nrc'], 'hit'))
        if 'bt' in ex: sfx.append((o0 + ex['bt'], 'thud'))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
        if ty in ('text', 'badge', 'ticket'): sfx.append((s2o(s0), 'pop'))
        if ty == 'cta': sfx.append((s2o(s0) + 0.35, 'click'))
    for s0, s1, chunks in CAP:
        o0, o1 = s2o(s0), s2o(s1); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts); t = o0
        for c, wt in zip(chunks, wts):
            dd = (o1 - o0) * wt / tot
            words = [w.lstrip('*!^') for w in c]; hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
            col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
            captions.append(dict(t0=t, t1=t + dd, words=words, hl=hl, col=col)); t += dd
    captions.sort(key=lambda c: c['t0'])
    for a, b in zip(captions, captions[1:]):
        if 0 < b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        for it in items:
            if it['t0'] <= mid < it['t1']:
                if it.get('layout') == 'split': c['pos'] = 'split'
                if it['type'] in ('cta', 'ticket'): c['pos'] = 'hi' if it['type'] == 'cta' else c.get('pos')
                if it['type'] == 'nlend': c['pos'] = 'none'
    json.dump(dict(items=items, captions=captions, total=TOTAL), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    frames = []
    for i in range(int(round(TOTAL * 30))):
        to = i / 30; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.08
        for a, b, zz in PUNCH:
            if a <= ts <= b: z = zz
        L = V = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']:
                L = it['layout']
                if it['type'] == 'vid': V = [it['file'], round(it.get('ss', 0) + to - it['t0'], 4), round((to - it['t0']) / (it['t1'] - it['t0']), 4)]
        s = src_of(ts)
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=V, des=False, cy0=CROP[s], zc=ZC[s]))
    json.dump(frames, open(W + 'frames.json', 'w'))
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), mm) for a, b, mm in MUSIC], sfx=sorted(sfx), total=TOTAL), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s, joined)', 'Final time (s)', 'Line / beat', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            if sc == 'vid': src, P, lic = f'Google Flow AI clip {ex["file"]}', 'P3 AI', 'AI-generated (Google Flow)'
            elif sc == 'ba': src, P, lic = f'real before/after photos {ex["before"]} + {ex["after"]} in "ba" reveal scene', 'P2 real proof', 'client-supplied photos - keep written consent on file'
            else: src, P, lic = f'animated "{sc}" scene', 'P5 motion graphics', 'original'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, P, 'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
        w.writerow(['TESTI', f'{T(0):.2f}-{T(TLEN):.2f}', f'{s2o(T(0))/1.2:.1f}-{s2o(T(32.82))/1.2:.1f}', 'client testimonial video (own audio)', 'real testimonial clip', 'P2 real', 'full + split under B06/B07', f'{(s2o(T(32.82))-s2o(T(0)))/1.2:.1f}', 'rendered', 'client-supplied - keep consent'])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/1.2:.1f}s) | captions {len(captions)} | sfx {len(sfx)}')
if __name__ == '__main__': build()
