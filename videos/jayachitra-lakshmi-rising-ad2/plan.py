"""EDL for Jayachitra, Lakshmi Rising Ad 2 "Rise Again" (Format B).
src.mkv = clips 1..10 upscaled to 1080x1920 and joined. Times are authored per clip as (clip, t) and converted
to joined SOURCE time, then to OUTPUT (pre-speed) time. Final = output / 1.2.
Run: W=/path/to/work python3 plan.py"""
import json, bisect, csv, os
W = os.environ.get('W', '/home/user/w').rstrip('/') + '/'
OFF = {1: 0.0, 2: 5.0, 3: 14.6, 4: 18.6667, 5: 23.6667, 6: 29.3667, 7: 39.0667, 8: 52.2667, 9: 56.2334, 10: 61.2001}
J = lambda c, t: round(OFF[c] + t, 4)

# keep ranges (clip, start, end) - pauses > 0.35 s cut, from the silence map
KEEP = [(1, .46, 4.60), (2, .38, 8.68), (3, 0.0, 2.52), (4, .30, 4.13), (5, .30, 5.12), (6, .89, 2.62), (6, 2.83, 9.27),
        (7, 0.0, 1.57), (7, 1.78, 5.85), (7, 6.25, 8.46), (7, 8.69, 12.38), (8, 0.0, 3.13), (9, .33, 4.87), (10, .45, 3.19),
        (10, 3.19, 4.18), (8, 3.13, 3.95)]          # silent tail under the end card
keep = [[J(c, a), J(c, b)] for c, a, b in KEEP]
ostarts = []; acc = 0
for a, b in keep: ostarts.append(acc); acc += b - a
TOTAL = acc
END_O = ostarts[-2]                                   # end card starts where the silent tail starts
def s2o(t):
    for (a, b), o in zip(keep, ostarts):
        if a <= t <= b: return o + (t - a)
    best = min(range(len(keep)), key=lambda i: min(abs(t - keep[i][0]), abs(t - keep[i][1])))
    a, b = keep[best]; return ostarts[best] + (0 if abs(t - a) < abs(t - b) else b - a)
def o2s(t):
    i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])
C = lambda c, t: s2o(J(c, t))                         # (clip, t) -> output time

# B-roll: (id, (clip,t0), (clip,t1), scene, layout, extra, keyword)   cue lists are (clip, t). All AI clips reused from Ad 1.
BROLL = [
 ('B01', (1, 2.00), (1, 4.60), 'vid', 'split', dict(file='B01.mkv', ss=0.0, cy=760, des=True, chip='CHALLENGES'), '"facing many challenges in life?"'),
 ('B07', (2, .38), (2, 2.80), 'vid', 'split', dict(file='B07.mkv', ss=0.0, cy=780, chip='TALENT ✦'), '"even though you have the talent"'),
 ('P01', (2, 2.80), (2, 6.10), 'pressure', 'split', dict(cues=[(2, 2.95), (2, 4.05), (2, 4.85)]), '"family situation, EMI, money pressure"'),
 ('B07s', (2, 6.10), (2, 8.68), 'vid', 'split', dict(file='B07.mkv', ss=3.4, cy=720, des=True, chip='STUCK?'), '"unable to move forward?" (B&W)'),
 ('A01', (4, .30), (4, 4.13), 'aura', 'split', {}, '"women naturally have the power to manifest"'),
 ('B02', (5, 2.20), (5, 5.12), 'vid', 'split', dict(file='B02.mkv', ss=1.6, cy=700, chip='DESIGN YOUR LIFE ✦'), '"you can design your own life"'),
 ('AU1', (6, .89), (6, 5.20), 'authority', 'split', dict(img='headshot.jpg'), '"I am Jayachitra" (authority card; face stays in bottom panel)'),
 ('B06', (7, 0.0), (7, 1.78), 'vid', 'split', dict(file='B06.mkv', ss=1.6, cy=820, chip='PROMOTION ✦'), '"promotion, salary hike"'),
 ('B10', (7, 1.78), (7, 5.85), 'vid', 'split', dict(file='B10.mkv', ss=1.2, cy=900, chip='OWN CAR · OWN HOME ✦'), '"own car, own house"'),
 ('B05', (7, 6.25), (7, 8.46), 'vid', 'split', dict(file='B05.mkv', ss=0.6, cy=760, chip='MANIFESTATION ✦'), '"all of this through manifestation"'),
 ('B13', (7, 8.69), (7, 12.38), 'vid', 'split', dict(file='B13.mkv', ss=0.2, cy=820, chip='YOUR LIFE ✦'), '"through your career, into your life"'),
 ('C1', (9, .33), (9, 4.87), 'poster', 'split', {}, '"register for Lakshmi Rising now" (CTA - face kept in bottom panel)'),
 ('B15', (10, .45), (10, 3.19), 'vid', 'split', dict(file='B15.mkv', ss=2.2, cy=1150, chip='YOUR RISE ✦'), '"your rise begins now"'),
]
GFX = [
 ('slam', (3, .10), (3, 2.52), dict(html='✦ This Is For You ✦', y=330)),
 ('badge', (6, 5.20), (6, 9.27), dict(html='7 YRS COACHING <i>·</i> 5 YRS MANIFESTATION', y=1010)),
 ('cta', (8, 0.0), (8, 3.13), dict(label='CLICK THE LINK', arrow='⬇', y=1250)),
 ('cta', (9, .33), (9, 4.87), dict(label='REGISTER NOW', y=1545)),
]
CAPSTYLE = 'B'   # Format B: CAPS gold keyword on top, small subline below.  Tuples: (t0, t1, subline, KEYWORD)
CAP = [
 ((1, .46), (1, 4.60), 'facing many challenges in life?', 'As a Woman,'),
 ((2, .38), (2, 2.80), 'have the talent,', 'Even Though You'),
 ((2, 2.80), (2, 6.10), 'family, EMI & money pressure,', 'Due To'),
 ((2, 6.10), (2, 8.68), 'move forward?', 'Unable To'),
 ((3, 0.0), (3, 2.52), 'for you.', 'Then This Video Is'),
 ((4, .30), (4, 4.13), 'have the power to manifest.', 'Women Naturally'),
 ((5, .30), (5, 2.20), 'manifestation power,', 'By Using That'),
 ((5, 2.20), (5, 5.12), 'own life.', 'Design Your'),
 ((6, .89), (6, 2.62), '', "I'm Jayachitra"),
 ((6, 2.83), (6, 5.20), 'crossed many struggles,', 'As a Woman, I Too'),
 ((6, 5.20), (6, 9.27), 'and won in business & life.', 'I Fought Through It'),
 ((7, 0.0), (7, 1.78), 'salary hike,', 'Promotion,'),
 ((7, 1.78), (7, 5.85), '', 'Own Car, Own Home'),
 ((7, 6.25), (7, 8.46), 'through manifestation,', 'All of This'),
 ((7, 8.69), (7, 12.38), 'through your career.', 'Into Your Life'),
 ((9, .33), (9, 4.87), 'for Lakshmi Rising.', 'Register Now'),
 ((10, .45), (10, 3.19), 'begins now.', 'Your Rise ✦'),
]
PUSH = [((6, 5.20), (6, 9.27), 1.0, 1.12)]
PUNCH = [((1, .46), (1, 2.00), 1.0), ((3, 0.0), (3, 2.52), 1.12), ((5, .30), (5, 2.20), 1.06), ((8, 0.0), (8, 3.13), 1.04)]
MUSIC = [((1, 0), 'struggle'), ((3, 0.0), 'lift'), ((4, .30), 'groove'), ((6, .70), 'break'), ((7, 0.0), 'rise'), ((8, 0.0), 'finale')]
SFX = [((3, .10), 'shimmer'), ((4, .30), 'shimmer'), ((6, .89), 'bell'), ((9, .20), 'riser'), ((9, .33), 'bell')]

def build():
    items = []; captions = []; sfx = []
    for bid, p0, p1, sc, lay, ex, _ in BROLL:
        o0, o1 = C(*p0), C(*p1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        if 'cues' in ex:
            d['cues'] = [round(C(*c) - o0, 3) for c in ex.pop('cues')]
            sfx += [(o0 + c, 'thud' if sc == 'pressure' else ('tick' if sc in ('outcomes', 'rush') else 'pop')) for c in d['cues']]
        d.update(ex); items.append(d); sfx.append((o0 - 0.12, 'whoosh'))
    for ty, p0, p1, ex in GFX:
        d = dict(type=ty, t0=C(*p0), t1=C(*p1)); d.update(ex); items.append(d)
        if ty in ('badge', 'tslam'): sfx.append((d['t0'], 'pop'))
        if ty == 'cta': sfx.append((d['t0'] + 0.35, 'tick'))
    items.append(dict(type='endcard', t0=END_O, t1=TOTAL)); sfx.append((END_O, 'bell'))
    items.append(dict(type='brand', t0=0, t1=END_O))
    for p0, p1, lead, kw in CAP:
        captions.append(dict(t0=C(*p0), t1=C(*p1), lead=lead, kw=kw))
    for a, b in zip(captions, captions[1:]):
        if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        c['pos'] = 'split' if any(it.get('layout') == 'split' and it['t0'] <= mid < it['t1'] for it in items) else 'face'
    json.dump(dict(items=items, captions=captions, total=TOTAL, capStyle=globals().get('CAPSTYLE', 'A')), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.07
        for p0, p1, zz in PUNCH:
            if J(*p0) <= ts <= J(*p1): z = zz
        for p0, p1, z0, z1 in PUSH:
            if J(*p0) <= ts <= J(*p1): z = z0 + (z1 - z0) * (ts - J(*p0)) / (J(*p1) - J(*p0))
        L = None; V = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']:
                L = it['layout']
                if it['type'] == 'vid': V = [it['file'], round(it.get('ss', 0) + to - it['t0'], 4), round((to - it['t0']) / (it['t1'] - it['t0']), 4), it.get('cy', 960), bool(it.get('des'))]
        frames.append(dict(ts=round(ts, 4), z=round(z, 4), L=L, V=V))
    json.dump(frames, open(W + 'frames.json', 'w'))
    mus = [(C(*p), m) for p, m in MUSIC]
    mus = [(a, (mus[i + 1][0] if i + 1 < len(mus) else TOTAL), m) for i, (a, m) in enumerate(mus)]
    sfxo = sorted([(round(t, 3), n) for t, n in sfx] + [(round(C(*p), 3), n) for p, n in SFX])
    json.dump(dict(keep=keep, music=mus, sfx=sfxo, total=TOTAL, end=END_O), open(W + 'audio/cues.json', 'w'))
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'broll_log.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source (clip s)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, p0, p1, sc, lay, ex, kw in BROLL:
            o0, o1 = C(*p0), C(*p1)
            src = f'Google Flow AI clip {ex["file"]}' if sc == 'vid' else f'animated "{sc}" scene (engine v6)'
            lic = 'AI-generated (Google Flow/Veo) - disclose in Meta' if sc == 'vid' else 'original - no licence needed'
            w.writerow([bid, f'clip{p0[0]} {p0[1]:.2f}-{p1[1]:.2f}', f'{o0/1.2:.1f}-{o1/1.2:.1f}', kw, src, 'P3 AI' if sc == 'vid' else 'P5 motion graphics',
                        'split screen', f'{(o1-o0)/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout') and it['type'] != 'poster')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | end card at {END_O/1.2:.2f}s | B-roll {cov/TOTAL*100:.0f}% (excl. CTA poster) | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
