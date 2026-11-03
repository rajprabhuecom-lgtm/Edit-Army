"""EDL for Coach Shanmugam - SK WellFit Club transformation ad (Namakkal). Fresh edit, 1 Nov 2026.
src.mkv = the 8 talking-head clips in Prabhuraj's Drive order (folder "coach shanmugam": 1st v ... 8th v), joined,
each scaled to 1080 wide and cropped to 1080x1920 from the top:
  1st  0.000  "Vanakkam Namakkal makkale... same person? ...46 kg"      (new)
  2nd 14.957  "no starving, no hard workout, 3 healthy meals... 46 kg"  (new)
  3rd 33.104  "service: personalized program, 1-to-1 coaching..."       (new)
  4th 43.816  "this combination: correct care, follow-up, guidance"      (= 6.30.00_1)
  5th 54.379  "Hi, I'm Coach Shanmugam, SK WellFit Club, 6 yrs, 1000+"  (= 6.30.00_2)
  6th 67.729  "want to reduce weight? look fit? join SK WellFit Club"   (= 6.30.01)
  7th 77.940  "exclusive offer: consultation, body analysis, trial"     (= 6.30.01_1)
  8th 89.965  "why wait? click the link, book... start today"           (= 6.30.02)
NEW_* lists are in src.mkv time. OLD_* lists are reused from wellfit-ad (authored on that edit's timeline: intro 0-13.35,
support 13.35-23.913, then question/offer/CTA) and mapped with M(). Final time = output / 1.2."""
import json, bisect, csv
W = '/home/user/w/'
SIL = [(0.0, 1.58), (2.99, 3.70), (7.82, 8.27), (9.25, 9.66), (13.37, 15.80), (19.48, 19.78), (20.38, 20.60),
       (23.62, 24.07), (26.72, 27.16), (32.10, 34.90), (37.20, 37.50), (40.48, 40.96), (42.74, 45.30), (53.51, 56.10),
       (62.71, 62.93), (66.38, 69.27), (76.59, 80.33), (83.57, 83.82), (85.29, 85.78), (88.94, 91.26), (96.36, 97.00),
       (100.75, 101.94)]   # src.mkv time (silencedetect -32 dB)
def M(t):
    """wellfit-ad timeline -> src.mkv time"""
    if t < 13.35: return t + 54.379          # coach intro (5th)
    if t < 23.913: return t + 30.466         # combination / support (4th)
    return t + 43.816                        # question, offer, CTA + close (6th-8th)
END = 103.60   # hold under the end card (frames past the source end repeat the last frame; the end card covers them)
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
keep.append([100.75, END])   # hold the tail under the end card
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
OLD_BROLL = [
 ('B01', 3.62, 4.90, 'vid', 'split', dict(file='B01_studio.mkv', ss=0.0, cy=26, csz=48,
      chips=[['🏋️ SK WELLFIT CLUB']], ccues=[3.70]), '"SK WellFit Club" - real Zumba session'),
 ('B01b', 4.90, 6.25, 'vid', 'split', dict(file='B11_yoga.mkv', ss=0.0, cy=26, csz=44,
      chips=[['🧘 WELLNESS & FITNESS CENTRE', '#00C896', '#04110c', '#00C896']], ccues=[4.95]), '"Wellness & Fitness Centre" - real yoga session'),
 ('B02', 7.98, 12.03, 'beforeafter', 'split', dict(title='<span class="y" data-cnt="1000">1000</span><span class="y">+</span> PEOPLE ✓', ph=[5, 4], pcues=[8.10, 9.90]),
      '"1000+ people, their transformation" - real client photos'),
 ('B03', 15.80, 19.71, 'pillars', 'split', dict(pcues=[15.85, 17.27, 18.63], peq=19.30), '"correct care, regular follow-up, consistent guidance"'),
 ('B04', 19.71, 23.10, 'beforeafter', 'split', dict(title='SUPER <span class="y">TRANSFORMATION</span>', tsz=66, ph=[1, 2], nolab=[1], pcues=[19.75, 21.45]),
      '"this super transformation" - real client photos with kg labels'),
 ('B06', 37.80, 42.20, 'offerstack', 'split', dict(pcues=[37.82, 39.46]), '"one-to-one consultation, full body analysis"'),
 ('B07', 42.20, 44.70, 'vid', 'split', dict(file='B07_trial.mkv', ss=0.2, cy=26, csz=48,
      chips=[['🏋️ FITNESS TRIAL PROGRAM ✓', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[42.35]), '"fitness trial program" - real session footage'),
]
OLD_GFX = [
 ('badge', 1.80, 3.62, {'html': '💪 COACH சண்முகம்', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('text', 6.32, 7.95, {'html': '<span class="y">6 YEARS</span><br>EXPERIENCE', 'y': 200, 'size': 110}),
 ('text', 25.45, 27.22, {'html': 'WEIGHT<br><span class="y">REDUCE?</span> ⚖️', 'y': 200, 'size': 120}),
 ('badge', 29.79, 32.75, {'html': '💪 JOIN SK WELLFIT CLUB', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 62}),
 ('badge', 36.52, 37.80, {'html': '🔥 EXCLUSIVE OFFER', 'y': 230, 'size': 72}),
 ('text', 47.45, 48.45, {'html': 'இன்னும் ஏன்<br><span class="y">யோசிக்கிறீங்க?</span> 🤔', 'y': 200, 'size': 92}),
 ('flash', 48.45, 48.60, {}),
 ('cta', 48.49, 52.58, {'label': '📅 BOOK APPOINTMENT', 'badge': '👇 CLICK THE LINK BELOW', 'y': 1060}),
 ('text', 53.21, 56.97, {'html': 'START<br><span class="g">TODAY 🚀</span>', 'y': 200, 'size': 140}),
 ('clubend', 56.97, END, {'loc': 'COACH SHANMUGAM • NAMAKKAL', 'logo': 'sk_logo.png'}),
]
OLD_CAP = [
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
OLD_PUNCH = [(1.6, 3.62, 1.10), (6.3, 7.96, 1.16), (25.4, 27.23, 1.12), (29.78, 32.8, 1.08), (36.5, 37.81, 1.15),
         (47.4, 48.46, 1.18), (48.46, 52.6, 1.06), (53.2, 55.0, 1.10), (55.0, 57.0, 1.16)]
DESAT = []
MUSIC = [(0.0, 33.10, 'pulse'), (33.10, 77.94, 'tech'), (77.94, END, 'uplift')]   # src.mkv time
OLD_SFX = [(25.45, 'hit'), (1.75, 'thud'), (36.52, 'hit'), (48.05, 'riser'), (48.49, 'hit'), (56.97, 'hit')]
SCENE_SFX = {}
# ---------- NEW: clips 1st-3rd (src.mkv time) ----------
NEW_BROLL = [
 ('N01', 3.70, 7.82, 'beforeafter', 'split', dict(title='ஒரே <span class="y">PERSON?</span> 🤔', ph=['sk46'], card=[245, 95, 590, 560], afx=398, pcues=[3.72], left='⬅️<br>BEFORE', right='AFTER<br>➡️'),
      '"would you believe the two people in these photos are the same person?" - real client photo (46 kg client, 3-stage collage sk46)'),
 ('N02', 9.66, 13.37, 'beforeafter', 'split', dict(title='நாங்க சொன்னதை <span class="g">FOLLOW</span> பண்ணி', tsz=56, ph=['sk46b'], card=[260, 100, 560, 560], afx=294, pcues=[9.68], stamp='-46 KG', stc=11.18),
      '"followed what we said and lost 46 kg" - real client before/after photo (sk46b, client-supplied, v3) + 46 KG stamp'),
 ('N03', 15.80, 19.40, 'nostarve', 'split', dict(pcues=[16.80, 17.62]), '"no starving, no hard workout"'),
 ('N04', 19.40, 22.60, 'meals', 'split', dict(pcues=[19.42, 20.26, 21.06]), '"morning, afternoon, night - healthy food"'),
 ('N04b', 36.94, 38.45, 'vid', 'split', dict(file='B08_personal.mkv', ss=0.2, cy=26, csz=46,
      chips=[['🎯 PERSONALIZED PROGRAM', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[37.0]), '"personalized program" - real session (coach in yoga)'),
 ('N05', 38.45, 40.40, 'vid', 'split', dict(file='B09_coaching.mkv', ss=0.0, cy=26, csz=44,
      chips=[['👤 ONE-TO-ONE COACHING'], ['👀 MONITORING', '#00C896', '#04110c', '#00C896']], ccues=[38.55, 39.80]), '"one to one coaching and monitoring" - real session (coach guiding a member)'),
 ('N06', 40.40, 42.74, 'vid', 'split', dict(file='B10_guidance.mkv', ss=0.0, cy=26, csz=46,
      chips=[['🏋️ PROPER WORKOUT GUIDANCE', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[40.45]), '"proper workout guidance" - real Zumba session'),
]
NEW_GFX = [
 ('text', 1.58, 2.99, {'html': 'வணக்கம்<br><span class="y">நாமக்கல்</span> மக்களே! 👋', 'y': 200, 'size': 100}),
 ('text', 8.27, 9.25, {'html': 'நம்பித்தான்<br><span class="g">ஆகணும்!</span>', 'y': 200, 'size': 120}),
 ('text', 23.72, 26.72, {'html': '❤️ FAVOURITE FOOD<br><span class="g">AVOID பண்ணல</span>', 'y': 200, 'size': 84}),
 ('text', 27.16, 30.28, {'html': '🥦 VEG ✓ 🍗 NON-VEG ✓<br><span class="y">😋 வயிறு நிறைய ✓</span>', 'y': 200, 'size': 78}),
 ('text', 30.28, 32.10, {'html': '<span class="y">46 KG</span> ↓<br>WEIGHT LOSS', 'y': 200, 'size': 120}),
 ('badge', 34.90, 36.94, {'html': '🎁 OUR SERVICE', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
]
NEW_CAP = [
 (1.58, 2.99, [['வணக்கம்'], ['^நாமக்கல்', 'மக்களே!']]),
 (3.70, 5.36, [['இந்த', '*PHOTOS-ல'], ['இருக்கிற', 'ரெண்டு', 'பேரும்']]),
 (5.36, 7.82, [['^ஒரே', '^PERSON-னு'], ['சொன்னா', 'நம்புவீங்களா?']]),
 (8.27, 9.25, [['நம்பித்தான்', '*ஆகணும்']]),
 (9.66, 11.18, [['நாங்க', 'சொன்னதை'], ['கேட்டு', '*FOLLOW', 'பண்ணி']]),
 (11.18, 13.37, [['^46 KG', 'WEIGHT'], ['குறைச்சிருக்கார்']]),
 (15.80, 17.55, [['இதுக்காக', 'அவர்'], ['!பட்டினியும்', 'கிடக்கல']]),
 (17.62, 19.40, [['!கடுமையான', '!WORKOUT-உம்'], ['பண்ணல']]),
 (19.40, 21.40, [['^MORNING', '^AFTERNOON'], ['^NIGHT']]),
 (21.44, 23.62, [['மூணு', 'வேளையும்'], ['*HEALTHY-ஆன', '*FOOD']]),
 (24.07, 26.72, [['அவருக்கு', '^FAVOURITE', '^FOOD'], ['எதையும்', 'AVOID', 'பண்ணாம']]),
 (27.16, 30.28, [['*VEGETARIAN'], ['*NON-VEGETARIAN'], ['வயிறு', 'நிறைய', 'சாப்பிட்டுதான்']]),
 (30.28, 32.10, [['இந்த', '^46 KG'], ['குறைச்சிருக்கார்']]),
 (34.90, 36.80, [['இதுக்காக', 'அவருக்கு'], ['நாங்க', 'குடுத்த', '^SERVICE']]),
 (36.94, 38.30, [['*PERSONALIZED', '*PROGRAM']]),
 (38.52, 40.40, [['*ONE-TO-ONE', '*COACHING'], ['AND', '*MONITORING']]),
 (40.40, 42.74, [['^PROPER', '^WORKOUT'], ['^GUIDANCE']]),
]
NEW_PUNCH = [(1.5, 3.0, 1.12), (8.2, 9.3, 1.18), (24.0, 26.75, 1.08), (27.1, 30.3, 1.12), (30.25, 32.1, 1.18), (34.9, 38.5, 1.10)]
NEW_SFX = [(1.58, 'hit'), (8.27, 'thud'), (11.18, 'thud'), (30.28, 'hit')]

# ---------- map OLD (wellfit-ad timeline) onto src.mkv and merge ----------
_CUE = ('ccues', 'pcues')
BROLL = NEW_BROLL + [(i, M(a), M(b), sc, l, {k: ([M(x) for x in v] if k in _CUE else (M(v) if k in ('peq', 'bcue') else v)) for k, v in ex.items()}, kw) for i, a, b, sc, l, ex, kw in OLD_BROLL]
GFX = NEW_GFX + [(ty, M(a), (b if b == END else M(b)), ex) for ty, a, b, ex in OLD_GFX]
CAP = NEW_CAP + [(M(a), M(b), c) for a, b, c in OLD_CAP]
PUNCH = NEW_PUNCH + [(M(a), M(b), z) for a, b, z in OLD_PUNCH]
SFX = NEW_SFX + [(M(t), n) for t, n in OLD_SFX]

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
        if 'stc' in ex: d['st'] = rel([ex.pop('stc')])[0]
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
