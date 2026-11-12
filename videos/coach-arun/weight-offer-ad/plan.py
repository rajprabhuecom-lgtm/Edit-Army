"""EDL for Coach Arun - Sree Nutrition Club weight-management offer ad.
Source = clips 1-6, Kumar testimonial cut (VID-20261111-WA0005 31.30-38.05 s), clips 7-12, joined in that order
(src.mkv, 1080x1920 30 fps) + 2.8 s frozen tail for the end card.
Everything is authored in CLIP-LOCAL time with T(clip, t) (clip 'tm' = Kumar) and converted to the joined timeline,
then jump cuts remove silences. Final = output / 1.2 (speed.sh).
Engine: engine/v6-weight-coach (scenes pain, photos, plan, beforeafter, offer, endcard2 + v5 vid)."""
import json, bisect, csv
W = '/home/user/w/'
ORDER = [1, 2, 3, 4, 5, 6, 'tm', 7, 8, 9, 10, 11, 12]
DUR = dict(zip(ORDER, [5.0, 10.0, 10.6, 8.3, 6.8, 11.5, 6.8, 4.1, 4.9, 7.8, 4.9, 6.9, 3.5]))
OFF = {c: sum(DUR[x] for x in ORDER[:i]) for i, c in enumerate(ORDER)}
def T(c, t): return round(OFF[c] + t, 3)
END = sum(DUR.values()) + 2.8
# silences per clip (silencedetect -32 dB, 0.25 s), clip-local
SILC = {1: [(0, .33), (1.0, 1.45)], 2: [(0, .57), (.85, 1.16), (4.04, 4.62), (5.65, 6.21), (9.63, 10.0)],
        3: [(0, .05), (3.14, 3.51)], 4: [(0, 1.37), (4.72, 5.11), (7.13, 7.47)], 5: [(0, 1.64), (5.19, 5.68), (6.40, 6.71)],
        6: [(0, 1.24), (4.51, 5.03), (6.40, 7.38), (9.27, 10.30), (10.97, 11.5)], 7: [(0, .74), (3.74, 4.1)],
        8: [(0, .90)], 'tm': [(4.33, 4.49), (6.68, 6.8)], 9: [(0, 1.06)], 10: [(0, 1.32)], 11: [(0, 1.07), (6.58, 6.9)], 12: [(0, 1.59)]}
SIL = sorted((T(c, a), T(c, b)) for c, v in SILC.items() for a, b in v)
segs = []; t = 0.0
for a, b in SIL:
    if a > t: segs.append([t, a])
    t = max(t, b)
segs.append([t, T(12, 3.44)])
PRE, POST = 0.06, 0.10
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), e + POST
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep[-1][1] = END            # hold the tail (frozen frame) under the end card
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

# B-roll: (id, s0, s1, scene, layout, extra, keyword, source)   every *cues list is SOURCE time (converted below)
BROLL = [
 ('B01', T(2, 1.16), T(2, 9.70), 'pain', 'split', dict(cues=[T(2, 1.9), T(2, 4.62), T(2, 6.25), T(2, 8.6)]),
  '"busy lifestyle, irregular food timings -> weight increase, diet no result, confidence low"', 'P5'),
 ('B02', T(3, 3.51), T(3, 9.20), 'photos', 'split', dict(title='<span class="y">2 YEARS</span> • REAL MEMBERS',
      imgs=['img/img3.jpg', 'img/img1.jpg', 'img/img2.jpg'], cues=[T(3, 3.6), T(3, 4.2), T(3, 4.8)],
      chips=[['👥 150–200 MEMBERS'], ['✅ PERSONALISED GUIDANCE', 'var(--yl)', '#000']], ccues=[T(3, 5.3), T(3, 8.0)]),
  '"last 2 years, 150-200 members, personalised weight management guidance"', 'P2'),
 ('B03', T(4, 2.55), T(4, 7.13), 'plan', 'split', dict(cues=[T(4, 2.6), T(4, 3.3), T(4, 5.15)], ftc=T(4, 6.2), chip='🤝 WE SUPPORT YOUR JOURNEY'),
  '"personalised nutrition system for your lifestyle -> healthy weight management journey"', 'P5'),
 ('B04', T(5, 1.64), T(5, 5.25), 'vid', 'split', dict(file='B05_centre_session.mkv', ss=1.0, cy=40, csz=46,
      chips=[['💼 BUSY WORKING PEOPLE'], ['🎯 SUITABLE APPROACH', 'var(--em)', '#04110c', 'var(--em)']], ccues=[T(5, 2.0), T(5, 4.4)]),
  '"especially for busy working people - a suitable approach"', 'P2'),
 ('B05', T('tm', 0.0), T('tm', 6.70), 'beforeafter', 'split', dict(title='REAL CLIENT <span class="y">TESTIMONIAL</span>', img='img/IMG-20261112-WA0002.jpg',
      name='KUMAR', nc=T('tm', 0.3), res=['−14 KG', 'IN 6 MONTHS'], rc=[T('tm', 5.0), T('tm', 5.35)]),
  '"Kumar (real client, own words): followed the nutrition, 3 kg in 22 days, 14 kg in 6 months"', 'P2'),
 ('B06', T(9, 1.06), T(9, 7.75), 'offer', 'split', dict(brand='SREE NUTRITION CLUB', title='<span class="y">SPECIAL OFFER</span>', cues=[T(9, 3.5), T(9, 5.0)]),
  '"Sree Nutrition Club special offer: 3 days healthy breakfast + 3 days fitness trial"', 'P5'),
]
GFX = [
 ('badge', T(1, 0.33), T(1, 1.0), {'html': '🙏 வணக்கம்!', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 66}),
 ('badge', T(1, 1.45), T(1, 5.0), {'html': '📍 KGF BUSY WORKING PEOPLE', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 56}),
 ('badge', T(3, 0.05), T(3, 3.14), {'html': '🥗 WELLNESS COACH ARUN', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('badge', T(6, 1.24), T(6, 6.40), {'html': '👤 கோபால் ஐயா', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 62}),
 ('text', T(6, 7.38), T(6, 11.0), {'html': '<span class="y">12 KG</span><br>IN 5 MONTHS', 'y': 190, 'size': 120}),
 ('text', T(7, 0.74), T(7, 3.74), {'html': 'நீங்களும்<br><span class="g">START ✓</span>', 'y': 200, 'size': 110}),
 ('badge', T(8, 0.9), T(8, 4.9), {'html': '❓ PROPER START வேணுமா?', 'y': 230, 'size': 62}),
 ('badge', T(10, 1.32), T(10, 4.9), {'html': '⚠️ LIMITED APPOINTMENTS ONLY', 'y': 230, 'bg': 'var(--rd)', 'size': 56}),
 ('flash', T(11, 1.07), T(11, 1.20), {}),
 ('cta', T(11, 1.07), T(11, 6.58), {'label': '👇 BOOK FREE CONSULTATION', 'fs': 54, 'badge': '📅 APPOINTMENT • இப்போவே', 'y': 1060}),
 ('badge', T(12, 1.59), T(12, 3.44), {'html': '🚀 இன்னைக்கே FIRST STEP', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('endcard2', T(12, 3.44), END, {'icon': '🥗', 'l1': 'SREE NUTRITION CLUB', 's1': 104, 'l2': 'FREE CONSULTATION', 's2': 96,
   'l3': '3 DAYS BREAKFAST • 3 DAYS FITNESS TRIAL', 'btn': '👇 BOOK APPOINTMENT', 'urg': 'LIMITED APPOINTMENTS', 'loc': '🥗 WELLNESS COACH ARUN • KGF'}),
]
CAP = [
 (T(1, 0.33), T(1, 1.0), [['^வணக்கம்!']]),
 (T(1, 1.45), T(1, 5.0), [['*KGF-ல', 'WORK', 'பண்ற'], ['BUSY', 'WORKING', 'PEOPLE-க்கு'], ['ஒரு', '^COMMON PROBLEM', 'தெரியுமா?']]),
 (T(2, 0.57), T(2, 4.04), [['^BUSY LIFESTYLE'], ['!IRREGULAR', 'FOOD TIMINGS']]),
 (T(2, 4.62), T(2, 5.65), [['!WEIGHT', '!INCREASE', 'ஆகி']]),
 (T(2, 6.21), T(2, 9.63), [['DIET', 'TRY', 'பண்ணியும்'], ['!RESULT', 'கிடைக்கலையா?'], ['!CONFIDENCE-உம்', 'கம்மி?']]),
 (T(3, 0.05), T(3, 3.14), [['நான்', '*WELLNESS COACH'], ['*அருண்']]),
 (T(3, 3.51), T(3, 10.55), [['LAST', '^2 YEARS'], ['*150–200', 'MEMBERS-க்கு'], ['^PERSONALISED', 'WEIGHT MANAGEMENT'], ['GUIDANCE', 'குடுத்துட்டு', 'வரேன்']]),
 (T(4, 1.37), T(4, 4.72), [['உங்க', '^LIFESTYLE-க்கு', 'SUITABLE'], ['*PERSONALISED', '*NUTRITION', 'SYSTEM']]),
 (T(4, 5.11), T(4, 8.26), [['^HEALTHY', 'WEIGHT MANAGEMENT'], ['JOURNEY-ல', '*SUPPORT', 'பண்றோம்']]),
 (T(5, 1.64), T(5, 6.75), [['ESPECIALLY'], ['^BUSY WORKING', 'PEOPLE-க்கு'], ['*SUITABLE', 'APPROACH-ல', 'FOCUS']]),
 (T(6, 1.24), T(6, 6.40), [['*கோபால்', 'ஐயா'], ['DIET', 'TRY', 'பண்ணியும்'], ['!RESULT', 'வராம', 'STRUGGLE']]),
 (T(6, 7.38), T(6, 11.0), [['PERSONALISED', 'GUIDANCE-ல'], ['^5 மாசத்துல', '*12 KG'], ['ACHIEVE', 'பண்ணாங்க']]),
 (T('tm', 0.0), T('tm', 2.4), [['அவர்', 'சொன்ன', 'மாதிரி'], ['^NUTRITION-ஐ', 'FOLLOW', 'பண்ணேன்']]),
 (T('tm', 2.4), T('tm', 4.33), [['*22 நாள்ல', '*3 KG']]),
 (T('tm', 4.49), T('tm', 6.68), [['^6 மாசத்துல', '*14 KG'], ['குறைச்சிருக்கேன்']]),
 (T(7, 0.74), T(7, 3.74), [['அவங்க', 'மாதிரி', 'நீங்களும்'], ['*PROPER', 'GUIDANCE-ஓட', 'START']]),
 (T(8, 0.90), T(8, 4.85), [['உங்க', 'WEIGHT MANAGEMENT', 'JOURNEY-க்கு'], ['ஒரு', '^PROPER START', 'வேணுமா?']]),
 (T(9, 1.06), T(9, 7.75), [['*SREE NUTRITION', 'CLUB-ஓட'], ['^SPECIAL OFFER'], ['*3 DAYS', 'HEALTHY BREAKFAST'], ['*3 DAYS', 'FITNESS TRIAL']]),
 (T(10, 1.32), T(10, 4.85), [['இந்த', 'SPECIAL OFFER'], ['!LIMITED', '!APPOINTMENTS-க்கு', 'மட்டும்']]),
 (T(11, 1.07), T(11, 6.58), [['கீழே', 'இருக்கிற', '^BUTTON-ஐ'], ['CLICK', 'பண்ணி', '*FREE CONSULTATION'], ['^இப்போவே', 'BOOK', 'பண்ணுங்க']]),
 (T(12, 1.59), T(12, 3.44), [['இன்னைக்கே', 'உங்க'], ['*FIRST STEP', 'எடுங்க!']]),
]
PUNCH = [(T(6, 7.3), T(6, 11.0), 1.12), (T(1, 0.3), T(1, 1.0), 1.10), (T(1, 1.45), T(1, 5.0), 1.14), (T(3, 0.0), T(3, 3.2), 1.10), (T(7, 0.7), T(7, 3.8), 1.12),
         (T(8, 0.9), T(8, 2.9), 1.06), (T(8, 2.9), T(8, 4.9), 1.16), (T(10, 1.3), T(10, 4.9), 1.14), (T(11, 1.0), T(11, 6.6), 1.06), (T(12, 1.5), T(12, 3.5), 1.16)]
DESAT = []
MUSIC = [(0.0, T(3, 0.0), 'dark'), (T(3, 0.0), T(9, 0.0), 'warm'), (T(9, 0.0), END, 'uplift')]
SFX = [(T(1, 0.33), 'pop'), (T(1, 1.45), 'hit'), (T(3, 0.05), 'hit'), (T(6, 7.6), 'thud'), (T(7, 0.74), 'hit'), (T(8, 0.9), 'thud'), (T(10, 1.32), 'thud'),
       (T(11, 0.8), 'riser'), (T(11, 1.07), 'hit'), (T(12, 3.44), 'hit')]

def build():
    items = []; captions = []; sfx = list(SFX)
    for bid, s0, s1, sc, lay, ex, _, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        rel = lambda ts: [round(s2o(x) - o0, 3) for x in ts]
        if 'cues' in ex: c = ex.pop('cues'); d['cues'] = rel(c); sfx += [(x, 'pop') for x in c]
        if 'ccues' in ex:
            c = ex.pop('ccues'); r = rel(c); sfx += [(x, 'pop') for x in c]
            d['ct' if sc == 'vid' else 'ccues'] = r
        for k in ('ftc', 'nc'):
            if k in ex: d[k] = rel([ex.pop(k)])[0]; sfx.append((s2o(s0) and o2s(o0 + d[k]), 'pop'))
        if 'rc' in ex: c = ex.pop('rc'); d['rc'] = rel(c); sfx += [(c[0], 'thud'), (c[1], 'ding')]
        d.update(ex); items.append(d)
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
                if it['type'].startswith('endcard'): c['pos'] = 'none'
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
        frames.append(dict(ts=round(min(ts, END - 0.04), 4), z=z, L=L, V=V, des=any(a <= ts <= b for a, b in DESAT)))
    json.dump(frames, open(W + 'frames.json', 'w'))
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL), open(W + 'audio/cues.json', 'w'))
    SRC = {'P2': 'P2 real client footage/photos', 'P5': 'P5 motion graphics'}
    VIS = {'pain': 'animated "pain" scene (4 problem cards)', 'photos': 'REAL centre/event photos img3, img1, img2 (Arun folder)',
           'plan': 'animated "plan" scene (lifestyle -> nutrition -> journey)', 'vid': 'REAL centre session video (Arun folder: "center video")',
           'beforeafter': 'REAL testimonial clip of Kumar (VID-20261111-WA0005 31.3-38.05 s) + his REAL before/after photo (IMG-20261112-WA0002.jpg)', 'offer': 'animated "offer" scene (3 days breakfast + 3 days fitness trial)'}
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s, joined)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw, src in BROLL:
            lic = 'client-supplied real footage - confirm consent on file' if src == 'P2' else 'original - no licence needed'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, VIS[sc], SRC[src],
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
