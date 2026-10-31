"""Edit decision list for comm4: jump cuts, B-roll map, graphics, captions, zooms, music + SFX cues.
All authored in SOURCE time, converted to OUTPUT (pre-speed) time."""
import json, bisect

segs = json.load(open('segs.json'))
PRE, POST = 0.06, 0.09
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), e + POST
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep[-1][1] = 53.6 # hold the tail under the end card
# output start of each kept range
ostarts = []; acc = 0
for a, b in keep: ostarts.append(acc); acc += b - a
TOTAL = acc

def s2o(t):
    for (a, b), o in zip(keep, ostarts):
        if t < a: return o
        if t <= b: return o + (t - a)
    return TOTAL
def o2s(t):
    i = bisect.bisect_right(ostarts, t) - 1; i = max(0, i)
    return keep[i][0] + (t - ostarts[i])

# ---------------- B-roll map (animated motion-graphic B-roll, P5) ----------------
BROLL = [
 ('B01', 7.35, 10.7, 'walkin', 'split', {}, '"convert your knowledge into walk-ins"'),
 ('B02', 10.95, 13.8, 'days', 'full', {'nocap': False}, '"we created a 3-Day Challenge system"'),
 ('B03', 14.1, 17.2, 'centres', 'full', {}, '"every wellness centre that implemented it"'),
 ('B04', 17.55, 20.65,'testis', 'split', {}, '"amazing results, testimonial videos"'),
 ('B05', 27.3, 30.3, 'transform','split', {}, '"how to turn your experience into a 3-day event"'),
 ('B06', 30.6, 36.15, 'chart', 'split', {}, '"how to increase walk-ins to your centre"'),
 ('B07', 36.5, 41.8, 'pin', 'split', {}, '"reach your next pin as fast as possible"'),
]
GFX = [
 ('text', 0.85, 3.3, {'html': 'WELLNESS<br><span class="g">COACH?</span>', 'y': 240, 'size': 130}),
 ('badge', 3.3, 6.95, {'html': '🌿 WELLNESS KNOWLEDGE?', 'y': 250, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 58, 'rot': -3}),
 ('text', 20.97, 23.0, {'html': 'WATCH.<br><span class="y">THEN DECIDE.</span>', 'y': 240, 'size': 110}),
 ('cta', 23.19, 27.05, {'label': 'BOOK AN APPOINTMENT', 'badge': '📞 FREE STRATEGY CALL', 'y': 1150}),
 ('text', 41.85, 44.05, {'html': 'AS FAST AS<br><span class="y">POSSIBLE 🚀</span>', 'y': 240, 'size': 110}),
 ('badge', 44.22, 45.65, {'html': '✓ BACKED BY PROOF', 'y': 250, 'bg': 'var(--yl)', 'fg': '#000', 'size': 64}),
 ('cta', 45.86, 52.0, {'label': 'BOOK YOUR CALL NOW', 'badge': '👇 LINK IN DESCRIPTION', 'y': 1150}),
 ('endcard', 52.0, 53.6, {'html': 'WELLNESS CENTRE<br><span class="g">WALK-IN ENGINE</span><br><span class="y">BOOK A CALL ↓</span>'}),
]
CAP = [
 (0.81, 6.91, [['WELLNESS', '*COACH?'], ['LOTS OF', 'MEETINGS?'], ['LOTS OF', '*WELLNESS', '*KNOWLEDGE?']]),
 (7.28, 10.67, [['TURN IT INTO'], ['YOUR CENTRE', '*WALK-INS']]),
 (10.92, 13.75, [['WE BUILT A'], ['*3-DAY', '*CHALLENGE', 'SYSTEM']]),
 (14.04, 17.16, [['EVERY', 'WELLNESS CENTRE'], ['THAT', '*IMPLEMENTED IT']]),
 (17.49, 20.63, [['*AMAZING', '*RESULTS'], ['*TESTIMONIAL', 'VIDEOS']]),
 (20.97, 22.95, [['WATCH CAREFULLY'], ['THEN', 'DECIDE']]),
 (23.19, 26.96, [['CLICK THE', '^LINK BELOW'], ['*BOOK AN', '*APPOINTMENT']]),
 (27.21, 30.26, [['YOUR', '*EXPERIENCE'], ['INTO A', '*3-DAY EVENT']]),
 (30.52, 36.13, [['HOW TO', 'INCREASE'], ['*WALK-INS'], ['WE DISCUSS'], ['YOU', 'DECIDE']]),
 (36.40, 43.98, [['IMPLEMENT', 'THIS EVENT'], ['IN YOUR', 'CENTRE'], ['HIT YOUR', '^NEXT PIN'], ['*AS FAST', '*AS POSSIBLE']]),
 (44.22, 45.59, [['WITH', '*PROOF']]),
 (45.86, 47.12, [['^LINK IN', '^DESCRIPTION']]),
 (47.56, 48.02, [['CLICK IT']]),
 (48.30, 50.12, [['*BOOK YOUR', '*APPOINTMENT']]),
 (50.36, 51.90, [['SEE YOU', 'ON THE CALL']]),
]
PUNCH = [(0.8, 2.2, 1.0), (2.2, 4.4, 1.12), (4.4, 6.95, 1.04), (20.9, 23.0, 1.12), (23.1, 25.0, 1.15), (25.0, 27.1, 1.08), (41.8, 44.1, 1.12), (44.1, 45.7, 1.16), (45.8, 48.1, 1.14), (48.2, 50.2, 1.18), (50.3, 52.0, 1.08)]
DESAT = []
MUSIC = [(0.0, 10.9, 'pulse'), (10.9, 17.4, 'tech'), (17.4, 23.05, 'warm'), (23.05, 27.1, 'uplift'), (27.1, 44.1, 'tech'),
    (44.1, 53.9, 'uplift')]
SFX = [(0.81, 'hit'), (23.19, 'hit'), (45.4, 'riser'), (45.86, 'hit'), (52.0, 'hit')]

def build():
    items = []; captions = []
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        d = dict(type=sc, t0=s2o(s0), t1=s2o(s1), layout=lay, id=bid); d.update(ex); items.append(d)
        SFX.append((s0, 'whoosh')); SFX.append((s1 - 0.05, 'swipe'))
        if sc == 'days': SFX.extend((s0 + .15 + i * .35, 'pop') for i in range(3))
        if sc == 'centres': SFX.extend((s0 + .2 + i * .22, 'tick') for i in range(9))
        if sc == 'pin': SFX.extend((s0 + .1 + i * .3, 'pop') for i in range(3))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
        if ty in ('text', 'badge'): SFX.append((s0, 'pop'))
    for s0, s1, chunks in CAP:
        o0, o1 = s2o(s0), s2o(s1); n = len(chunks); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts)
        t = o0
        for c, wt in zip(chunks, wts):
            d = (o1 - o0) * wt / tot
            words = [w.lstrip('*!^') for w in c]
            hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
            col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
            captions.append(dict(t0=t, t1=t + d, words=words, hl=hl, col=col)); t += d
# extend each caption to the next one (no flicker in tiny gaps < 0.45 s)
    for a, b in zip(captions, captions[1:]):
        if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
# caption placement per layout
    def lay_at(t):
        for it in items:
            if it['t0'] <= t < it['t1'] and it.get('layout'): return it['layout']
        return None
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2; L = lay_at(mid)
        if L == 'split': c['pos'] = 'split'
        for it in items:
            if it['type'] == 'cta' and it['t0'] <= mid < it['t1']: c['pos'] = 'hi'
            if it['type'] == 'endcard' and it['t0'] <= mid < it['t1']: c['pos'] = 'none'
    tl = dict(items=items, captions=captions, total=TOTAL)
    json.dump(tl, open('gfx/timeline.json', 'w'), ensure_ascii=False, indent=0)
# per-output-frame render plan for the compositor
    fps = 30; frames = []
    nfr = int(round(TOTAL * fps)); phrase_idx = {}
    for i in range(nfr):
        to = i / fps; ts = o2s(to)
        k = bisect.bisect_right(ostarts, to) - 1
        z = 1.0 if k % 2 == 0 else 1.10
        for a, b, zz in PUNCH:
            if a <= ts <= b: z = zz
        L = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']: L = it['layout']
        des = any(a <= ts <= b for a, b in DESAT)
        frames.append(dict(ts=round(ts, 4), z=z, L=L, des=des))
    json.dump(frames, open('frames.json', 'w'))
    mus = [(s2o(a), s2o(b), m) for a, b, m in MUSIC]
    sfx = sorted((s2o(t), n) for t, n in SFX)
    json.dump(dict(keep=keep, music=mus, sfx=sfx, total=TOTAL), open('audio/cues.json', 'w'))
# B-roll map CSV for the record
    import csv
    with open('broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['ID', 'Source time', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'Use length (s, pre-speed)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', kw, f'animated {sc} scene', 'P5 motion graphics (original)', lay, f'{s2o(s1)-s2o(s0):.1f}', 'rendered', 'original - no licence needed'])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total out {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s at 1.2x | {len(keep)} cuts | B-roll {cov:.1f}s ({cov/TOTAL*100:.0f}%), full cutaway {full:.1f}s | captions {len(captions)}')

if __name__ == '__main__': build()
