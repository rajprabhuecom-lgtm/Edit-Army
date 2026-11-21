"""EDL for Dr. Mathan Muthu - Weight Loss before 2027 (Avadi & Ambattur). Source: 1121.mp4 (45.3 s, 1080x1920, 30 fps).
The source already carries the client's AI B-roll cutaways and a few title effects; this edit adds jump cuts, captions,
animated scenes (real client before/after proof, offer stack, name plate, calendar flip...), signature effects
(spotlight hook, glitch, whip pans, grid-dive, light leaks, shake), SFX, emotion-matched BGM, 1.2x speed, end card.
Authored in SOURCE time, converted to OUTPUT (pre-speed) time. Final = output / 1.2."""
import json, bisect, csv
W = '/home/user/w/'
SIL = [(7.52, 7.75), (12.37, 12.60), (15.08, 15.42), (17.52, 17.80), (18.56, 18.77), (20.21, 20.56), (25.32, 25.69),
       (27.21, 27.51), (28.34, 28.53), (31.17, 31.86), (35.29, 35.48), (40.81, 41.01)]
END, TAIL = 45.30, 2.7          # TAIL: end card held after the last source frame
segs = []; t = 0.0
for a, b in SIL:
    if a > t: segs.append([t, a])
    t = b
segs.append([t, END])
PRE, POST = 0.06, 0.09
keep = []
for s, e in segs:
    a, b = max(0, s - PRE), min(END, e + POST)
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
ostarts = []; acc = 0
for a, b in keep: ostarts.append(acc); acc += b - a
VTOTAL = acc; TOTAL = acc + TAIL
def s2o(t):
    if t >= END: return VTOTAL + (t - END)
    for (a, b), o in zip(keep, ostarts):
        if t < a: return o
        if t <= b: return o + (t - a)
    return VTOTAL
def o2s(t):
    if t >= VTOTAL: return END - 0.04
    i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])

R, G, Y = ('#2a1010', '#fff', '#FF3B30'), ('#0f2a20', '#fff', '#00C896'), ('#080A0D', '#FFD60A', '#FFD60A')
# Scenes: (id, s0, s1, type, layout, extra, spoken line)   cue times inside extras are SOURCE times
BROLL = [
 ('B01', 10.03, 12.37, 'vid', None, dict(cy=230, csz=50, chips=[['❌ DIET STRUGGLE', *R], ['❌ WORKOUT STRUGGLE', *R]], ccues=[10.2, 11.0]),
  'diet, workout-னு கஷ்டப்படுறதுக்கு பதிலா (instead of struggling with diet & workout) - over client AI B-roll (diet / workout chart)'),
 ('B02', 12.60, 15.08, 'vid', None, dict(cy=230, csz=54, chips=[['✅ FOOD HABITS', *G], ['✅ LIFESTYLE', *G], ['🎯 PROPER CHANGES', *Y]], ccues=[12.8, 13.5, 14.2]),
  'food habits, lifestyle-ல proper changes - over client AI B-roll (vegetables, park)'),
 ('B03', 15.42, 17.52, 'journey', 'full', dict(y=420), 'healthy weight loss journey start பண்ணலாம்'),
 ('B04', 18.67, 27.21, 'beforeafter', 'full', dict(title='MY <span class="y">CLIENTS</span> 💪', bcues=[18.85, 22.55], scue=25.69, stamp='✓ GOOD RESULTS',
      people=[dict(img='ba_thangamani.jpg', w=565, h=900, b=78, a=64), dict(img='ba_muthalagan.jpg', w=900, h=900, b=77.8, a=73)]),
  'my clients struggled like this; with proper guidance they changed lifestyle & food habits and got good results - REAL client before/after photos supplied by the client'),
 ('B05', 31.17, 35.38, 'offer', 'full', dict(title='YOU <span class="g">GET</span>', ocues=[31.95, 33.0, 34.35], scue=34.95, stamp='🎁 FREE TRIAL',
      rows=[['🩺', 'FULL BODY EVALUATION'], ['💬', 'FREE WEIGHT LOSS<br>CONSULTATION', 52], ['📅', '3 DAYS FREE TRIAL']]),
  'full body evaluation, free weight loss consultation, 3 days free trial'),
 ('B06', 38.77, 40.81, 'vid', None, dict(cy=150, csz=50, chips=[['📍 AVADI • AMBATTUR', '#080A0D', '#fff', '#00C896']], ccues=[38.9]),
  'ஆவடி & அம்பத்தூர் - over client AI B-roll (map)'),
]
GFX = [
 ('flash', 0.0, 0.12, {}),
 ('stuck', 4.30, 7.52, {'x': 640, 'y': 640, 'w': 440, 'sc': .85, 'html': 'WEIGHT ✕ குறையல', 'kg': ''}),
 ('calflip', 7.75, 10.03, {'x': 640, 'y': 330, 'sc': .85, 'tag': '2027-க்குள்', 'fc': 8.35 - 7.75}),
 ('leak', 9.90, 10.45, {}), ('leak', 18.45, 19.05, {}), ('leak', 30.95, 31.55, {}), ('leak', 38.55, 39.10, {}),
 ('flash', 27.51, 27.62, {}),
 ('nameplate', 27.51, 31.17, {'name': 'DR. MATHAN MUTHU C M', 'quals': 'B.Tech., M.Tech., PhD.', 'years': 7, 'xp': ' YEARS EXPERIENCE', 'xc': 28.6 - 27.51, 'y': 1150}),
 ('badge', 35.48, 38.77, {'html': '📍 ஆவடி & அம்பத்தூர்', 'y': 110, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 56}),
 ('flash', 38.77, 38.90, {}),
 ('cta', 38.77, END, {'label': '👇 CLICK & REGISTER', 'badge': '🎁 3 DAYS FREE TRIAL', 'y': 1330}),
 ('endcard', END, END + TAIL, {'name': 'DR. MATHAN MUTHU C M', 'loc': 'AVADI & AMBATTUR'}),
]
CAP = [
 (0.20, 3.50, [['வணக்கம்'], ['^ஆவடி', '^அம்பத்தூர்'], ['மக்களே!']], 'lo'),
 (3.60, 7.52, [['இந்த', 'வருஷம்', '*WEIGHT LOSS'], ['^TRY', 'பண்ணியும்'], ['இன்னும்', 'WEIGHT'], ['!குறையலையா?']], 'lo'),
 (7.75, 10.03, [['*2027', 'வரத்துக்குள்'], ['கொஞ்சம்', 'கொஞ்சம்'], ['*WEIGHT LOSS', 'பண்ணிடலாம்']], None),
 (10.03, 12.37, [['!DIET,', '!WORKOUT-னு'], ['கஷ்டப்படுறதுக்கு', 'பதிலா']], None),
 (12.60, 15.08, [['உங்க', '*FOOD HABITS'], ['*LIFESTYLE-ல'], ['^PROPER', 'CHANGES', 'பண்ணி']], None),
 (17.80, 20.21, [['என்', '*CLIENTS-ம்'], ['இந்த', 'மாதிரி'], ['!STRUGGLE', 'பண்ணவங்கதான்']], 'lo'),
 (20.56, 22.42, [['இந்த', '*PROPER', '*GUIDANCE'], ['^FOLLOW', 'பண்ணி']], 'lo'),
 (22.54, 25.32, [['அவங்க', '*LIFESTYLE'], ['*FOOD HABITS-ல'], ['^CHANGES', 'கொண்டு வந்து']], 'lo'),
 (25.69, 27.21, [['நல்ல', '*RESULTS'], ['^ACHIEVE', 'பண்ணிருக்காங்க']], 'lo'),
 (28.53, 31.17, [['உங்க', '*WEIGHT LOSS', '*JOURNEY-க்கு'], ['^GUIDE', 'பண்ணிட்டு', 'இருக்கேன்']], 'lo'),
 (35.48, 38.77, [['^ஆவடி', '&', '^அம்பத்தூர்-ல'], ['இருக்குற', 'நீங்களும்']], None),
 (38.77, 40.81, [['*2027-ல'], ['*WEIGHT LOSS', '^START', 'பண்ண']], None),
 (41.01, 45.25, [['கீழ', 'இருக்குற', '^BUTTON-ஐ'], ['^CLICK', 'பண்ணி'], ['*REGISTRATION'], ['COMPLETE', 'பண்ணுங்க']], None),
]
PUNCH = [(0.0, 1.9, 1.0), (1.9, 3.6, 1.10), (6.3, 7.6, 1.16), (7.75, 10.03, 1.08), (17.8, 18.67, 1.12), (28.53, 31.2, 1.10),
         (35.48, 37.0, 1.06), (37.0, 38.77, 1.14)]
DESAT = [(4.30, 7.52)]
FX = dict(spot=(0.0, 1.25), shake=[(1.9, 2.25), (6.55, 7.0)], glitch=[(6.55, 6.95)],
          whip=[12.0, 13.97, 40.77], grid=(35.48, 36.25))
MUSIC = [(0.0, 7.6, 'pulse'), (7.6, 18.6, 'tech'), (18.6, 31.1, 'warm'), (31.1, END + TAIL, 'uplift')]
SFX = [(0.0, 'hit'), (1.9, 'thud'), (6.55, 'thud'), (8.35, 'swipe'), (27.51, 'hit'), (28.6, 'ding'), (35.48, 'whoosh'),
       (38.77, 'hit'), (38.77, 'riser'), (39.12, 'click'), (END, 'hit'), (12.0, 'swipe'), (13.97, 'swipe'), (40.77, 'swipe')]

def build():
    items = []; captions = []; sfx = list(SFX)
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, id=bid); ex = dict(ex)
        if lay: d['layout'] = lay
        rel = lambda ts: [round(s2o(x) - o0, 3) for x in ts]
        if 'ccues' in ex: c = ex.pop('ccues'); d['ct'] = rel(c); sfx += [(x, 'pop') for x in c]
        if 'bcues' in ex: c = ex.pop('bcues'); d['cues'] = rel(c); sfx += [(x, 'whoosh') for x in c] + [(x + 2.1 * 1.0, 'thud') for x in c]
        if 'ocues' in ex: c = ex.pop('ocues'); d['cues'] = rel(c); sfx += [(x, 'swipe') for x in c] + [(x + .4, 'tick') for x in c]
        if 'scue' in ex: c = ex.pop('scue'); d['sc'] = rel([c])[0]; sfx.append((c, 'hit'))
        if sc == 'journey': sfx.append((s0 + .4, 'riser'))
        d.update(ex); items.append(d)
        if lay: sfx.append((s0, 'whoosh'))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex)
        for k in ('fc', 'xc'):
            if k in d: d[k] = round(s2o(s0 + d[k]) - s2o(s0), 3)
        items.append(d)
        if ty in ('badge', 'stuck', 'calflip'): sfx.append((s0, 'pop'))
        if ty == 'leak': sfx.append((s0, 'whoosh'))
    for s0, s1, chunks, pos in CAP:
        o0, o1 = s2o(s0), s2o(s1); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts); t = o0
        for c, wt in zip(chunks, wts):
            d = (o1 - o0) * wt / tot
            words = [w.lstrip('*!^') for w in c]; hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
            col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
            cap = dict(t0=t, t1=t + d, words=words, hl=hl, col=col)
            if pos: cap['pos'] = pos
            captions.append(cap); t += d
    for a, b in zip(captions, captions[1:]):
        if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        for it in items:
            if it['t0'] <= mid < it['t1']:
                if it['type'] == 'cta': c['pos'] = 'hi'
                if it['type'] in ('endcard', 'offer', 'journey', 'nameplate') and c.get('pos') != 'lo': c['pos'] = 'none'
    json.dump(dict(items=items, captions=captions, total=TOTAL), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.06
        for a, b, zz in PUNCH:
            if a <= ts <= b: z = zz
        L = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']: L = it['layout']
        fx = {}
        a, b = FX['spot']
        if a <= ts < b: fx['spot'] = round((ts - a) / (b - a), 3)
        for a, b in FX['shake']:
            if a <= ts < b: fx['shake'] = round((ts - a) / (b - a), 3)
        for a, b in FX['glitch']:
            if a <= ts < b: fx['glitch'] = i
        for c in FX['whip']:
            d = to - s2o(c)
            if -0.1 <= d < 0.1: fx['whip'] = round(d / 0.1, 3)
        a, b = FX['grid']; ga, gb = s2o(a), s2o(b)
        if ga <= to < gb: fx['grid'] = round((to - ga) / (gb - ga), 3)
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=None, des=any(a <= ts <= b for a, b in DESAT), fx=fx))
    json.dump(frames, open(W + 'frames.json', 'w'))
    sfxo = sorted([(s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL, vtotal=VTOTAL), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s)', 'Final time (s)', 'Line (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            src = {'vid': 'client AI B-roll (in source) + animated chips', 'beforeafter': 'REAL client before/after photos (Drive: mathan muthu/brolls)'}.get(sc, f'animated "{sc}" scene')
            lic = 'client-supplied, client consent assumed - confirm' if sc == 'beforeafter' else ('client-supplied AI footage' if sc == 'vid' else 'original - no licence needed')
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, sc, src, lay or 'overlay on source B-roll',
                        f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | new full cutaways {full/1.2:.1f}s | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
