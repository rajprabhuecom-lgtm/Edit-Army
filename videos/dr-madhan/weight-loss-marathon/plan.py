"""EDL: Dr. Madhan weight loss marathon ad. src.mkv = IMG_9158.MOV conformed to 1080x1920 @30.
Authored in SOURCE time, converted to OUTPUT (pre-speed) time. Final = output / 1.2. Engine: engine/v7-marathon."""
import json, bisect, csv
W = '/home/user/w/'
# pauses found from audio energy (no clean silences in this take)
SIL = [(0.0, 0.50), (13.32, 14.10), (19.92, 20.84), (22.88, 23.32), (28.04, 28.32), (33.25, 33.60), (39.39, 39.64),
       (42.86, 43.18), (46.68, 46.90)]
TAIL = (51.46, 52.60)               # hold under the end card
PRE, POST = 0.04, 0.08
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

NO = '#2a1010', '#FF3B30', '#FF3B30'
GO = '#0f2a20', '#00C896', '#00C896'
# (id, s0, s1, scene, layout, extra, keyword)   cue values are SOURCE times
BROLL = [
 ('B01', 2.00, 5.10, 'counter', 'split', dict(to=1597, unit='KG', title='⏱ LAST 10 DAYS', sub='WEIGHT LOST 🔥', c0=2.05, cd=1.3), '"1,597 kg in the last 10 days" (spoken figure - confirm)'),
 ('B02', 8.10, 11.10, 'counter', 'split', dict(to=1682, unit='', title='🏃 LAST MARATHON', sub='MEMBERS PARTICIPATED', dots=60, c0=8.20, cd=1.6), '"1,682 members in the last marathon" (spoken figure - confirm)'),
 ('B03', 15.90, 19.92, 'vid', 'full', dict(file='B03_alone.mkv', ss=0.3, big='<span class="r">ALONE?</span> 😔', bt=16.6, by=250, bsz=150), '"can you do it alone? it is not possible"'),
 ('B05', 26.10, 29.60, 'vid', 'split', dict(file='B05_measure.mkv', ss=0.2, cy=40, csz=46,
      ct=[26.32, 28.32], chips=[['🧍 BODY TYPE ✓', *GO], ['📏 BODY PARAMETERS ✓', *GO]]), '"your body type, body parameters"'),
 ('B06', 29.60, 33.25, 'vid', 'full', dict(file='B06_food.mkv', ss=0.2, cy=250, csz=56,
      ct=[30.46, 32.36], chips=[['🍲 YOUR FOOD'], ['📋 CORRECT PLAN', '#080A0D', '#FFD60A', '#FFD60A']]), '"exactly what food you need, planned correctly"'),
 ('B07', 34.60, 37.54, 'vid', 'split', dict(file='B07_coach_call.mkv', ss=0.2, cy=40, csz=50,
      ct=[34.98, 36.36], chips=[['👤 EVERY PERSON'], ['🤝 1 PERSONAL COACH', *GO]]), '"one coach appointed for every person"'),
 ('B08', 38.10, 42.86, 'struggle', 'split', dict(good=True, title='COMPLETE <span class="g">SUPPORT</span>',
      cards=[['🥗', 'FOOD PLANNER'], ['🌿', 'LIFESTYLE'], ['📅', 'WEEKLY CLASS']],
      cues=[38.24, 40.06, 41.50], xcues=[38.80, 40.80, 41.80], nrc=42.20, stamp='✓ LIFESTYLE CORRECTION'), '"complete food planner + lifestyle correction + weekly class"'),
]
GFX = [
 ('badge', 0.50, 2.00, {'html': '🔥 LAST MARATHON RESULTS', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('badge', 5.84, 8.10, {'html': '👥 TOTAL PARTICIPANTS?', 'y': 230, 'size': 62}),
 ('badge', 14.10, 15.90, {'html': '🤔 WEIGHT LOSS தனியா?', 'y': 230, 'size': 60}),
 ('text', 20.84, 22.88, {'html': 'NOT POSSIBLE<br><span class="r">BY YOURSELF ❌</span>', 'y': 210, 'size': 92}),
 ('badge', 23.32, 26.10, {'html': '👥 OUR COMMUNITY • OUR SYSTEM', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 52}),
 ('badge', 33.60, 34.60, {'html': '👤 ஒவ்வொருவருக்கும்', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 58}),
 ('badge', 43.18, 44.46, {'html': "⏰ MISS பண்ணாதீங்க!", 'y': 230, 'size': 64}),
 ('badge', 44.46, 46.68, {'html': '👋 DR. MADHAN', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 70}),
 ('flash', 46.90, 47.05, {}),
 ('cta', 46.90, 50.74, {'label': '👇 CLICK THE LINK', 'badge': '🏃 START WITH DR. MADHAN', 'y': 1040}),
 ('mdend', 50.74, END, {}),
]
CAP = [
 (0.50, 2.00, [['*1,597 KGS']]),
 (2.00, 5.84, [['LAST', '^10 DAYS-ல'], ['நம்ம', '*WEIGHT LOSS'], ['பண்ணி', 'கொடுத்திருக்கோம்']]),
 (5.84, 8.10, [['TOTAL', '^PARTICIPANTS'], ['எவ்வளவுன்னு', 'கேட்டீங்கன்னா']]),
 (8.10, 11.00, [['*1,682', 'MEMBERS'], ['PARTICIPATE', 'பண்ணாங்க']]),
 (11.00, 13.32, [['நம்ம', 'LAST'], ['*WEIGHT LOSS', '*MARATHON-ல']]),
 (14.10, 15.90, [['IF', 'YOU', 'DECIDE', 'TO'], ['DO', '*WEIGHT LOSS']]),
 (15.90, 18.60, [['CAN', 'YOU', 'DO', 'IT', '!ALONE?']]),
 (18.60, 19.92, [['IT', 'IS', '!NOT']]),
 (20.84, 22.88, [['!POSSIBLE'], ['BY YOURSELF']]),
 (23.32, 25.40, [['SO,', 'IN', 'OUR', '*COMMUNITY'], ['IN', 'OUR', '*SYSTEM']]),
 (25.40, 28.04, [['EXACTLY', 'உங்க', '^BODY TYPE', 'என்ன']]),
 (28.32, 29.60, [['^BODY PARAMETERS'], ['எப்படி', 'இருக்கு']]),
 (29.60, 31.30, [['உங்களுக்கு', 'என்ன', '*FOOD', 'வேணும்']]),
 (31.30, 33.25, [['CORRECT-ஆ', 'பார்த்து'], ['^PLAN', 'பண்ணி']]),
 (33.60, 36.00, [['ஒவ்வொரு', '*PERSON-க்கும்'], ['INDIVIDUAL-ஆ']]),
 (36.00, 37.54, [['ஒரு', '^COACH', 'APPOINT', 'பண்ணி']]),
 (37.54, 39.39, [['COMPLETE', '*FOOD PLANNER']]),
 (39.64, 41.50, [['PLUS', '^LIFESTYLE', '^CORRECTION']]),
 (41.50, 42.86, [['*WEEKLY CLASS']]),
 (43.18, 44.46, [['இந்த', 'வாய்ப்பை', '!MISS', 'பண்ணாதீங்க']]),
 (44.46, 46.68, [['I AM', '*DR. MADHAN'], ['I AM HERE', 'TO', '^HELP YOU']]),
 (46.90, 48.10, [['கீழ', 'இருக்கிற', '^LINK-ஐ'], ['^CLICK', 'பண்ணி']]),
 (48.10, 49.60, [['இப்போவே', 'உங்க'], ['*WEIGHT LOSS', 'PROGRAM']]),
 (49.60, 50.74, [['என்னுடன்', '^START', 'பண்ணுங்க']]),
]
PUNCH = [(0.5, 2.0, 1.14), (5.8, 8.1, 1.10), (14.1, 15.9, 1.12), (20.8, 22.9, 1.16), (23.3, 26.1, 1.10), (33.6, 34.6, 1.14),
         (43.1, 44.5, 1.16), (44.5, 46.7, 1.08), (46.9, 48.1, 1.06), (48.1, 50.8, 1.12)]
DESAT = [(20.84, 22.88)]
MUSIC = [(0.0, 13.4, 'tech'), (13.4, 23.3, 'dark'), (23.3, 42.9, 'tech'), (42.9, END, 'uplift')]
SFX = [(0.50, 'hit'), (5.84, 'pop'), (15.90, 'thud'), (20.84, 'thud'), (43.18, 'hit'), (46.60, 'riser'), (46.90, 'hit'), (50.74, 'hit')]
CROP, ZC = 330, 744     # split: source y where the bottom (face) panel starts; zoom centre y (face)

def build():
    items, captions, sfx = [], [], [(s2o(t), n) for t, n in SFX]
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        rel = lambda x: round(s2o(x) - o0, 3)
        for k in ('cues', 'xcues', 'ct'):
            if k in ex: ex[k] = [rel(x) for x in ex[k]]
        for k in ('c0', 'nrc', 'bt'):
            if k in ex: ex[k] = rel(ex[k])
        d.update(ex); items.append(d)
        sfx.append((o0 - 0.12, 'whoosh'))
        for x in ex.get('ct', []) + ex.get('cues', []): sfx.append((o0 + x, 'pop'))
        for x in ex.get('xcues', []): sfx.append((o0 + x, 'ding'))
        if sc == 'struggle': sfx.append((o0 + ex['nrc'], 'hit'))
        if sc == 'counter': sfx += [(o0 + ex['c0'] + k * 0.12, 'tick') for k in range(int(ex['cd'] / 0.12))] + [(o0 + ex['c0'] + ex['cd'], 'cash')]
        if 'bt' in ex: sfx.append((o0 + ex['bt'], 'thud'))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
        if ty in ('text', 'badge'): sfx.append((s2o(s0), 'pop'))
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
                if it['type'] == 'cta': c['pos'] = 'hi'
                if it['type'] == 'mdend': c['pos'] = 'none'
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
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=V, des=any(a <= ts <= b for a, b in DESAT), cy0=CROP, zc=ZC))
    json.dump(frames, open(W + 'frames.json', 'w'))
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), mm) for a, b, mm in MUSIC], sfx=sorted(sfx), total=TOTAL), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            if sc == 'vid': src, P, lic = f'Google Flow AI clip {ex["file"]}', 'P3 AI', 'AI-generated (Google Flow) - disclose in Meta'
            else: src, P, lic = f'animated "{sc}" scene', 'P5 motion graphics', 'original - no licence needed'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, P, 'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full cutaway {full/TOTAL*100:.0f}%) | captions {len(captions)} | sfx {len(sfx)}')
if __name__ == '__main__': build()
