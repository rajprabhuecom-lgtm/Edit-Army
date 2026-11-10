"""EDL for 10112026-theni-insta (GOPI PHOTOGRAPHY Instagram trial ad, Theni). Single source = src.mkv (480x854 upscaled to 1080x1920).
Authored in SOURCE time; converted to OUTPUT (pre-speed) time. Final = output / 1.2. BGM is mixed AFTER the speed-up (see mix.py)."""
import json, bisect, csv
W = '/home/user/w/'
SIL = [(0.0, 0.20), (7.80, 7.95), (9.40, 9.53), (12.29, 12.51), (13.53, 13.64), (14.91, 15.10), (16.55, 16.85), (21.81, 21.92),
       (24.34, 24.47), (32.18, 32.28), (37.02, 37.12), (44.57, 44.68), (47.10, 47.35), (49.44, 49.58), (53.80, 54.10), (56.85, 56.98),
       (59.09, 59.24), (60.57, 60.67), (60.99, 61.22), (63.10, 63.40), (65.07, 65.30), (72.12, 72.28), (73.21, 73.40), (74.86, 75.09),
       (78.71, 78.91), (80.24, 80.40), (84.07, 84.27), (87.24, 87.36), (90.49, 90.60), (95.14, 95.24), (95.62, 95.84), (100.62, 100.95)]
END = 100.62
HOLD = 3.4                      # end card hold after the last word (source has no tail; last frame is frozen under the opaque card)
segs = []; t = 0.0
for a, b in SIL:
    if a > t: segs.append([t, a])
    t = b
PRE, POST = 0.04, 0.06
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), min(END, e + POST)
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep.append([END, END + HOLD])
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

G, Y, BLK = '#00C896', '#FFD60A', '#04110c'
# B-roll: (id, s0, s1, scene, layout, extra, keyword)   cue times inside extras are SOURCE times
BROLL = [
 ('B01', 1.54, 4.78, 'vid', 'full', dict(file='B01.mkv', ss=0.6), '"running a business in Theni?"'),
 ('B02', 4.78, 7.60, 'vid', 'full', dict(file='B11.mkv', ss=6.9, big='🌍 <span class="y">WORLD</span>', bcue=6.14, by=250, bsz=150), '"take your business to the world"'),
 ('B03', 7.60, 12.10, 'vid', 'split', dict(file='B03.mkv', ss=0.0, cy=40, csz=42,
      chips=[['📲 INSTAGRAM CHALLENGE'], ['📍 உங்க AREA-லயே'], ['🎥 WE COME & SHOOT', G, BLK, G]], ccues=[7.70, 9.98, 11.10]), '"Instagram challenge - we come to your area in Theni"'),
 ('B04', 12.10, 16.60, 'vid', 'split', dict(file='B04.mkv', ss=0.0, cy=40, csz=46,
      chips=[['✂️ PROPER EDIT'], ['📲 POST', G, BLK, G]], ccues=[13.40, 15.30]), '"we take the video, edit properly, post"'),
 ('B05', 23.16, 28.94, 'platforms', 'split', dict(pcues=[24.84, 26.06, 26.34], mcue=28.10), '"Instagram, Facebook, YouTube - all managed"'),
 ('B06', 29.28, 34.00, 'steps', 'split', dict(pcues=[30.62, 31.74, 32.62], fcue=33.30), '"script, edit, post"'),
 ('B07', 35.20, 43.30, 'docs', 'split', dict(pcues=[35.98, 37.60, 40.62], ecue=42.18), '"documents, target audience, value for your clients - we craft it"'),
 ('B08', 44.36, 49.60, 'slots', 'split', dict(fcue=46.88, tcue=49.16), '"only first 5 business owners in Theni - trial pack"'),
 ('B09', 57.70, 62.90, 'vid', 'split', dict(file='B09.mkv', ss=0.0, cy=40, csz=44,
      chips=[['🎬 7 VIDEOS • 1 WEEK'], ['📍 உங்க AREA-லயே SHOOT', G, BLK, G]], ccues=[57.80, 59.50]), '"7 videos in one week, shot in your area"'),
 ('B10', 63.70, 70.50, 'reach7', 'split', dict(rcue=63.88, gcue=65.76, mcue=68.76), '"in these 7 videos your business gets reach - then monthly"'),
 ('B11', 80.00, 86.10, 'vid', 'split', dict(file='B11.mkv', ss=2.8, cy=40, csz=46,
      chips=[['💰 AFFORDABLE RATE'], ['🌍 ALL OVER THE WORLD', G, BLK, G]], ccues=[80.48, 81.52]), '"affordable rate, all over the world"'),
]
GFX = [
 ('badge', 0.10, 1.54, {'html': '📍 தேனி BUSINESS OWNERS', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 58}),
 ('badge', 20.26, 23.16, {'html': '📦 PACKAGE-ல என்ன?', 'y': 230, 'size': 66}),
 ('stamp', 51.60, 54.55, {'big': 'NO RISK', 'small': 'TRIAL PACK', 'col': 'var(--em)', 'y': 200, 'bsz': 140}),
 ('price', 54.55, 57.65, {'val': 10000, 'per': '1 WEEK • 7 VIDEOS', 'y': 180}),
 ('badge', 70.50, 74.10, {'html': '🔥 ONLY 5 BUSINESS OWNERS', 'y': 230, 'size': 58}),
 ('strike', 74.10, 80.00, {'old': '₹50K – ₹1 LAKH', 'lbl': 'MARKET-ல', 'y': 190, 'lc': 3.6, 'no': '❌ செலவு தேவையில்ல'}),
 ('badge', 86.16, 91.40, {'html': '📍 தேனி • ONLY 5', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 64}),
 ('flash', 91.48, 91.63, {}),
 ('cta', 91.48, END, {'label': '👇 BOOK APPOINTMENT', 'badge': '📍 WE COME TO YOUR SHOP', 'y': 1060}),
 ('endcard', END, END + HOLD, {}),
]
CAP = [
 (0.00, 1.54, [['தேனியில்', '*BUSINESS']]),
 (1.54, 2.68, [['RUN', 'பண்றீங்களா?']]),
 (2.68, 4.75, [['இந்த', '^OPPORTUNITY-ய'], ['!MISS', 'பண்ணவே', 'கூடாது']]),
 (4.80, 7.55, [['உங்க', 'BUSINESS-ஐ'], ['*உலகத்துக்கு', 'கொண்டு', 'போக']]),
 (7.62, 9.26, [['^INSTAGRAM', '^CHALLENGE']]),
 (9.26, 12.10, [['நம்ம', '*தேனியில'], ['உங்க', 'AREA-லயே', 'வந்து']]),
 (12.10, 14.68, [['VIDEO', 'எடுத்து'], ['^PROPER-ஆ', 'EDIT', 'பண்ணி']]),
 (14.68, 17.66, [['உங்க', '*INSTAGRAM'], ['ACCOUNT-ல', 'POST']]),
 (17.66, 20.26, [['எடுத்துட்டு', 'வர்றது'], ['*எங்களோட', 'வேலை']]),
 (20.26, 23.16, [['இந்த', '*PACKAGE-ல'], ['என்ன', 'INCLUDE?']]),
 (23.16, 26.30, [['உங்க', '*INSTAGRAM'], ['*FACEBOOK']]),
 (26.30, 29.28, [['*YOUTUBE'], ['எல்லாமே', '^MANAGE', 'பண்றோம்']]),
 (29.28, 31.70, [['அது', 'மட்டும்', 'இல்ல'], ['^SCRIPT', 'CREATE']]),
 (31.70, 34.00, [['^EDIT', 'பண்றது'], ['^POST', 'பண்றது']]),
 (34.00, 37.50, [['அந்த', 'VIDEO-க்கு', 'தேவையான'], ['*DOCUMENTS']]),
 (37.50, 40.80, [['*TARGET', '*AUDIENCE'], ['CLIENTS-க்கு', '^VALUE']]),
 (40.80, 43.80, [['எல்லாத்தையுமே'], ['*நாங்களே', 'CRAFT', 'பண்ணுவோம்']]),
 (43.80, 46.80, [['^ONLY', 'நம்ம', 'தேனியில']]),
 (46.80, 48.66, [['*FIRST 5', 'BUSINESS', 'OWNERS-க்கு']]),
 (48.66, 51.10, [['மட்டுமே', '^TRIAL', '^PACK']]),
 (51.10, 53.70, [['உங்களுக்கு', 'எந்த'], ['*RISK-உம்', 'இல்ல']]),
 (53.70, 57.60, [['JUST', '*₹10,000'], ['^ONE', '^WEEK-க்கு']]),
 (57.70, 60.90, [['*7', '*VIDEOS'], ['உங்க', 'AREA-லயே', '^SHOOT']]),
 (60.90, 63.70, [['எல்லாமே', '^SET', 'பண்ணி', 'தருவோம்']]),
 (63.70, 66.60, [['இந்த', '*7 VIDEOS-ல'], ['உங்க', 'BUSINESS', '^REACH']]),
 (66.60, 70.50, [['^CONFIDENCE', 'வந்த', 'பிறகு'], ['^MONTHLY', 'PACKAGE']]),
 (70.50, 74.10, [['இந்த', 'OPPORTUNITY'], ['!ONLY', '!5', 'BUSINESS', 'OWNERS']]),
 (74.10, 77.70, [['MARKET-ல', '!₹50,000'], ['!₹1 LAKH']]),
 (77.70, 80.00, [['செலவு', 'பண்ணாம']]),
 (80.00, 82.80, [['*AFFORDABLE', 'RATE-ல'], ['^ALL OVER', '^THE WORLD']]),
 (82.80, 86.10, [['எடுத்துட்டு', 'போக'], ['*BEST', 'WAY', 'இது']]),
 (86.16, 88.60, [['நம்ம', '*தேனியில', 'இருக்கிற']]),
 (88.60, 91.40, [['!5', 'BUSINESS', 'OWNERS'], ['மட்டும்', 'தான்']]),
 (91.48, 92.40, [['^INVITE', 'பண்றோம்']]),
 (92.42, 94.20, [['இப்பவே', 'கீழே', '*LINK-ஐ'], ['^CLICK', 'பண்ணுங்க']]),
 (94.20, 95.50, [['*APPOINTMENT', 'BOOK']]),
 (95.50, 97.90, [['உங்க', 'AREA-லயே'], ['^MEET', 'பண்றோம்']]),
 (97.90, END, [['இந்த', 'OPPORTUNITY'], ['*START', 'பண்றோம்']]),
]
PUNCH = [(0.0, 1.54, 1.10), (17.66, 20.26, 1.12), (20.26, 23.16, 1.06), (51.6, 54.55, 1.10), (70.5, 74.1, 1.14), (74.1, 80.0, 1.06),
         (86.1, 88.6, 1.08), (88.6, 91.45, 1.16), (91.48, 95.5, 1.04), (95.5, END, 1.10)]
DESAT = []
SFX = [(0.0, 'hit'), (51.60, 'thud'), (54.60, 'cash'), (70.50, 'pop'), (77.55, 'thud'), (91.08, 'riser'), (91.48, 'hit'), (END, 'hit')]

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
        if 'dcues' in ex: d['cues'] = rel(ex['dcues']); sfx += [(x, 'pop') for x in ex.pop('dcues')]
        if 'ftc' in ex: d['ftc'] = rel([ex.pop('ftc')])[0]
        if 'pcues' in ex: p = ex.pop('pcues'); d['cues'] = rel(p); sfx += [(x, 'pop') for x in p]
        if 'mcue' in ex and sc == 'platforms': m = ex.pop('mcue'); d['mc'] = rel([m])[0]; sfx += [(m + .05 + i * .12, 'tick') for i in range(3)]
        if 'fcue' in ex and sc == 'steps': d['fc'] = rel([ex.pop('fcue')])[0]; sfx += [(x + .45, 'tick') for x in d['cues'] and [o2s(o0 + c) for c in d['cues']]]
        if 'ecue' in ex: e = ex.pop('ecue'); d['ce'] = rel([e])[0]; sfx += [(e, 'thud')] + [(o2s(o0 + c) + .5, 'tick') for c in d['cues']]
        if sc == 'slots': f = ex.pop('fcue'); tc = ex.pop('tcue'); d['fc'] = rel([f])[0]; d['ftc'] = rel([tc])[0]; sfx += [(f + i * .22, 'pop') for i in range(5)] + [(tc, 'ding')]
        if sc == 'reach7': r, g_, m = ex.pop('rcue'), ex.pop('gcue'), ex.pop('mcue'); d['cue'] = rel([r])[0]; d['rc'] = rel([g_])[0]; d['mc'] = rel([m])[0]; sfx += [(r + i * .12, 'pop') for i in range(7)] + [(g_, 'riser_s'), (m, 'ding')]
        ex.pop('_q', None); d.update(ex); items.append(d)
        sfx.append((o0 - 0.12, 'whoosh', 1))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
        if ty in ('text', 'badge', 'strike'): sfx.append((s0, 'pop'))
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
                if it['type'] == 'endcard': c['pos'] = 'none'
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
        if to >= s2o(END): L = 'hold'
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=V, des=any(a <= ts <= b for a, b in DESAT)))
    json.dump(frames, open(W + 'frames.json', 'w'))
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    gaps = [[round(s2o(a), 3), round(s2o(b), 3)] for a, b in SIL if s2o(b) - s2o(a) > 0.05]
    json.dump(dict(keep=keep, sfx=sfxo, total=TOTAL, end=s2o(END), gaps=gaps), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s, joined)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            src = f'clip {ex["file"]} (supplied by Prabhuraj)' if sc == 'vid' else f'animated "{sc}" scene'
            lic = 'AI-generated (Google Flow) - disclose in Meta' if sc == 'vid' and bid != 'B01' else ('supplied footage - confirm rights' if sc == 'vid' else 'original - no licence needed')
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, ('P2 real' if bid == 'B01' else 'P3 AI') if sc == 'vid' else 'P5 motion graphics',
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/1.2:.1f}s) | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
