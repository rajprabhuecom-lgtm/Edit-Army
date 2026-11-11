"""EDL for Jayachitra, Lakshmi Rising Ad 1 "Second Innings".
src.mkv = clips 1..11 upscaled to 1080x1920 and joined. Times are authored per clip as (clip, t) and converted
to joined SOURCE time, then to OUTPUT (pre-speed) time. Final = output / 1.2.
Run: W=/path/to/work python3 plan.py"""
import json, bisect, csv, os
W = os.environ.get('W', '/home/user/w').rstrip('/') + '/'
OFF = {1: 0.0, 2: 10.9, 3: 20.1, 4: 29.7333, 5: 35.3333, 6: 41.6667, 7: 50.6667, 8: 59.3333, 9: 66.1667, 10: 72.9, 11: 76.8667}
J = lambda c, t: round(OFF[c] + t, 4)

# keep ranges (clip, start, end) - pauses > 0.35 s cut, from the silence map
KEEP = [(1, .44, 2.12), (1, 2.97, 5.34), (1, 5.72, 9.53), (2, .42, 4.50), (2, 5.04, 8.69), (3, .30, 9.06), (4, .56, 4.83),
        (5, .56, 2.01), (5, 2.30, 3.96), (6, .85, 2.46), (6, 2.84, 3.61), (6, 3.87, 8.76), (7, .34, 3.93), (7, 4.22, 8.18),
        (8, .51, 1.82), (8, 2.30, 3.54), (8, 3.75, 6.28), (9, .54, 5.94), (10, .40, 2.78), (11, .46, 9.17),
        (11, 9.17, 9.63), (10, 2.78, 3.96)]          # silent tail under the end card
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

# B-roll: (id, (clip,t0), (clip,t1), scene, layout, extra, keyword)   cue lists are (clip, t)
BROLL = [
 ('B01', (1, 5.72), (1, 9.53), 'vid', 'split', dict(file='B01.mkv', ss=0.0, cy=760, chip='EVERY DAY ✦'), '"running for everyone, forgot to live for you"'),
 ('B02', (2, .42), (2, 4.50), 'vid', 'split', dict(file='B02.mkv', ss=1.5, cy=700, chip='YOUR DREAM ✦'), '"do you dream of your own income?"'),
 ('B05', (3, 3.25), (3, 5.62), 'vid', 'split', dict(file='B05.mkv', ss=0.6, cy=760, chip='RIGHT CAREER ✦'), '"which career is right for you"'),
 ('B06', (3, 5.62), (3, 9.06), 'vid', 'split', dict(file='B06.mkv', ss=1.4, cy=820, chip='RESTART ✦'), '"how to restart after a career break"'),
 ('B07', (4, .56), (4, 3.05), 'vid', 'split', dict(file='B07.mkv', ss=2.0, cy=760, chip='YOUR INCOME ✦'), '"how to grow your income"'),
 ('B07b', (4, 3.05), (4, 4.83), 'outcomes', 'split', dict(cues=[(4, 3.1), (4, 3.35), (4, 3.6), (4, 3.95)]), '"total clarity"'),
 ('B09', (6, .85), (6, 4.62), 'dreams', 'split', dict(cues=[(6, .95), (6, 1.7), (6, 2.95), (6, 4.0)]), '"money, car, career, own home"'),
 ('B10', (6, 4.62), (6, 8.76), 'vid', 'split', dict(file='B10.mkv', ss=1.6, cy=900, chip='DREAMS → REAL ✦'), '"start the journey of making your dreams real"'),
 ('B13', (8, .51), (8, 6.28), 'vid', 'split', dict(file='B13.mkv', ss=0.1, cy=820, chip='INDEPENDENT ✦'), '"every woman: emotionally & financially independent"'),
 ('B15', (10, .40), (10, 2.78), 'vid', 'split', dict(file='B15.mkv', ss=2.4, cy=1150, chip='RISE TOGETHER ✦'), '"ready to join my community?"'),
 ('C1', (11, .46), (11, 3.90), 'poster', 'split', {}, '"register for Lakshmi Rising now" (CTA - face kept in bottom panel)'),
]
# on-face graphics (type, (clip,t0), (clip,t1), extra)
GFX = [
 ('slam', (2, 5.04), (2, 6.95), dict(html='✦ Manifestation ✦', y=930)),
 ('sparkle', (5, .56), (5, 3.96), dict(y=1300)),
 ('badge', (7, .40), (7, 3.93), dict(html='7 YRS COACHING <i>·</i> 5 YRS MANIFESTATION', y=1010)),
 ('stamp', (7, 4.30), (7, 8.18), dict(top='MY COMMUNITY', main='ONE STRICT RULE', y=860)),
 ('tslam', (9, 2.70), (9, 5.94), dict(html='யாரையும் <b>DEPEND</b><br>பண்ணக்கூடாது', y=900)),
 ('cta', (11, .46), (11, 3.90), dict(label='REGISTER NOW', y=1380)),
 ('cta', (11, 3.90), (11, 9.17), dict(label='REGISTER NOW', y=985)),
]
# captions: ((clip,t0), (clip,t1), lead-in, keyword)
CAP = [
 ((1, .44), (1, 2.12), 'ARE YOU A', 'Working Woman?'),
 ((1, 2.97), (1, 5.34), 'OR AT HOME ON A', 'Career Break?'),
 ((1, 5.72), (1, 7.55), 'RUNNING FOR', 'Everyone,'),
 ((1, 7.55), (1, 9.53), 'FORGOT TO LIVE', 'For You?'),
 ((2, .42), (2, 4.50), 'DO YOU DREAM OF', 'Your Own Income?'),
 ((2, 5.04), (2, 8.69), 'THROUGH MANIFESTATION, YOU CAN', 'Get There Too'),
 ((3, .30), (3, 3.25), 'USING LAW OF ATTRACTION', 'Techniques'),
 ((3, 3.25), (3, 5.62), 'WHICH CAREER IS', 'Right For You'),
 ((3, 5.62), (3, 9.06), 'HOW TO RESTART', 'After a Break'),
 ((4, .56), (4, 3.05), 'HOW TO GROW', 'Your Income'),
 ((4, 3.05), (4, 4.83), 'YOU GET', 'Total Clarity'),
 ((5, .56), (5, 3.96), "YOU'LL DISCOVER YOUR", 'True Potential'),
 ((6, .85), (6, 4.62), 'MONEY · CAR · CAREER', 'Your Own Home'),
 ((6, 4.62), (6, 8.76), 'START THE JOURNEY TO MAKE', 'Dreams Real'),
 ((7, .34), (7, 3.93), "I'VE WALKED THIS ROAD TOO", 'As a Woman'),
 ((7, 4.22), (7, 8.18), 'IN MY COMMUNITY, I HAVE', 'One Strict Rule'),
 ((8, .51), (8, 3.54), 'EVERY WOMAN MUST BE', 'Emotionally'),
 ((8, 3.75), (8, 6.28), '&', 'Financially Independent'),
 ((9, .54), (9, 2.70), 'FOR MONEY OR', 'Emotional Support'),
 ((9, 2.70), (9, 5.94), 'DEPEND ON', 'No One'),
 ((10, .40), (10, 2.78), 'READY TO JOIN MY', 'Community?'),
 ((11, .46), (11, 3.90), 'REGISTER NOW FOR', 'Lakshmi Rising'),
 ((11, 3.90), (11, 6.30), "COME, LET'S MANIFEST YOUR", 'Career & Money'),
 ((11, 6.30), (11, 9.17), '', 'Together ✦'),
]
PUSH = [((7, .34), (7, 3.93), 1.0, 1.12)]                     # slow push-in on her story
PUNCH = [((1, .44), (1, 2.12), 1.0), ((1, 2.97), (1, 5.34), 1.10), ((5, .56), (5, 3.96), 1.12), ((7, 4.22), (7, 8.18), 1.08),
         ((9, .54), (9, 2.70), 1.06), ((9, 2.70), (9, 5.94), 1.16), ((11, 3.90), (11, 6.30), 1.04), ((11, 6.30), (11, 9.17), 1.10)]
# music sections (start clip,t) -> carnatic-fusion mood
MUSIC = [((1, 0), 'intro'), ((2, 5.04), 'lift'), ((3, .30), 'groove'), ((7, .20), 'break'), ((7, 4.22), 'rise'), ((11, .30), 'finale')]
SFX = [((2, 5.04), 'shimmer'), ((5, .56), 'shimmer'), ((7, 4.30), 'thud'), ((9, 2.70), 'hit'), ((11, .30), 'riser'), ((11, .46), 'bell')]

def build():
    items = []; captions = []; sfx = []
    for bid, p0, p1, sc, lay, ex, _ in BROLL:
        o0, o1 = C(*p0), C(*p1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        if 'cues' in ex:
            d['cues'] = [round(C(*c) - o0, 3) for c in ex.pop('cues')]
            sfx += [(o0 + c, 'tick' if sc in ('outcomes', 'rush') else 'pop') for c in d['cues']]
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
    json.dump(dict(items=items, captions=captions, total=TOTAL), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
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
                if it['type'] == 'vid': V = [it['file'], round(it.get('ss', 0) + to - it['t0'], 4), round((to - it['t0']) / (it['t1'] - it['t0']), 4), it.get('cy', 960)]
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
