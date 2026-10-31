"""EDL for coach-muthu dog ad (IMG_2533 + IMG_2538 + IMG_2540 joined = src.mkv).
Authored in SOURCE time (joined timeline); converted to OUTPUT (pre-speed) time. Final = output / 1.2."""
import json, bisect, csv
W = '/home/user/w/'
SIL = [(0.0, 1.25), (3.19, 3.52), (10.82, 11.12), (13.16, 13.54), (23.40, 23.62), (26.52, 26.79), (29.02, 31.88),
       (48.62, 49.40), (52.17, 52.39), (59.14, 61.47), (68.04, 68.57), (74.37, 75.25), (77.55, 77.77), (78.79, 79.55),
       (86.41, 86.69), (88.46, 90.02)]
END = 90.0
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
keep.append([88.46, END])   # hold the tail under the end card
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

# B-roll: (id, s0, s1, scene, layout, extra, keyword)   cue times inside extras are SOURCE times (converted below)
BROLL = [
 ('B01', 2.94, 6.10, 'vid', 'full', dict(file='B01_dog_scale.mkv', ss=0.3, big='<span class="y">18 KG</span> 🐕', bcue=4.42, by=250), '"his weight is 18 kg"'),
 ('B02', 6.10, 9.80, 'vid', 'split', dict(file='B02_food_card.mkv', ss=0.0, cy=60, csz=44,
      chips=[['💉 VACCINATION ✓'], ['🍲 FOOD CHART ✓'], ['🚶 WALK TIME ✓']], ccues=[6.14, 7.42, 8.34]), '"vaccination date, food chart, walking time"'),
 ('B03', 13.95, 21.40, 'questions', 'split', dict(qcues=[14.06, 16.76, 19.62], qend=20.90), '"your BMI? mother\'s BMR? wife\'s body fat?"'),
 ('B04', 23.62, 28.60, 'vid', 'split', dict(file='B04_brushing.mkv', ss=0.0, cy=50, csz=48,
      chips=[['🐕 DOG ✓', '#0f2a20', '#00C896', '#00C896'], ['👨👩👧 FAMILY ?', '#2a1010', '#FF3B30', '#FF3B30']], ccues=[24.0, 27.0]), '"we care for our dog - but our family?"'),
 ('B05a', 32.42, 35.90, 'days', 'split', dict(dcues=[32.80, 33.35, 33.90], ftc=34.60), '"Family Health Reset 3 Day Challenge, first 2 days"'),
 ('B05', 35.90, 39.30, 'vid', 'split', dict(file='B05_zoom_family.mkv', ss=0.5, cy=60, csz=44,
      chips=[['💻 ZOOM • MORNING 1 HOUR'], ['🏠 FROM HOME', '#00C896', '#04110c', '#00C896']], ccues=[36.1, 38.1]), '"morning 1 hour on Zoom, from home"'),
 ('B06', 39.30, 42.90, 'vid', 'split', dict(file='B06_park_walk.mkv', ss=0.3, cy=60, csz=46,
      chips=[['👨👩👧👦 HEALTHY FAMILY'], ['🏥 LESS HOSPITAL VISITS', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[39.5, 41.3]), '"keep your family away from hospital visits"'),
 ('B07', 50.90, 57.30, 'checkup', 'split', dict(kcues=[52.88, 53.68, 54.44]), '"Day 3 - come here, BMI, BMR, fat % check"'),
 ('B08', 78.10, 83.90, 'mappin', 'split', dict(mcues=[78.31, 80.03, 81.03, 82.25]), '"centre: Guduvanchery, Nellikuppam Rd, Periyar Nagar, opp. SRM School"'),
]
GFX = [
 ('badge', 1.25, 2.94, {'html': '✋ ஒரு நிமிஷம்!', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
 ('badge', 10.70, 12.86, {'html': '❓ ஒரு கேள்வி', 'y': 230, 'size': 72}),
 ('text', 43.40, 48.38, {'html': '<span class="y">8+ YEARS</span><br>WELLNESS EXPERIENCE', 'y': 200, 'size': 84}),
 ('text', 57.30, 58.70, {'html': 'COMPLETELY<br><span class="g">FREE ✓</span>', 'y': 200, 'size': 140}),
 ('flash', 61.47, 61.62, {}),
 ('cta', 61.50, 67.90, {'label': '👇 CLICK & REGISTER', 'badge': '💬 PREMIUM WHATSAPP GROUP', 'y': 1060}),
 ('badge', 68.38, 74.20, {'html': 'ONLY FIRST 10 FAMILIES 🔥', 'y': 200, 'size': 64}),
 ('text', 70.97, 74.20, {'html': 'AFTER THAT<br><span class="y">₹2,000</span>', 'y': 330, 'size': 110}),
 ('badge', 84.39, 86.61, {'html': '📍 LOCATION உங்களுக்கு வரும்', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 50}),
 ('badge', 86.61, 88.46, {'html': '🤝 SEE YOU AT THE CENTRE', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('endcard', 88.46, END, {'loc': 'COACH MUTHU • GUDUVANCHERY'}),
]
CAP = [
 (1.25, 2.94, [['குடுவாஞ்சேரி', 'மக்களே,'], ['ஒரு', '^நிமிஷம்!']]),
 (2.94, 5.28, [['இவரோட', 'WEIGHT', '*18 KG']]),
 (5.38, 8.00, [['^VACCINATION', 'DATE'], ['^FOOD CHART']]),
 (8.34, 10.70, [['^WALKING TIME'], ['எல்லாமே', 'நமக்கு', 'தெரியும்']]),
 (10.70, 12.84, [['ஆனா', 'உங்ககிட்ட'], ['ஒரு', '^கேள்வி']]),
 (12.90, 15.48, [['உங்களோட', '*BMI', 'எவ்வளவு?']]),
 (15.60, 18.22, [['உங்க', 'அம்மாவோட', '*BMR?']]),
 (18.22, 21.60, [['உங்க', 'WIFE-ஓட'], ['*BODY FAT %?']]),
 (21.68, 22.86, [['!தெரியாது', 'இல்ல?']]),
 (22.86, 26.30, [['நம்ம', 'வீட்டு', '*DOG-ஐ'], ['ரொம்ப', 'நல்லா', 'பாத்துக்கிறோம்']]),
 (26.30, 28.58, [['ஆனா', '!நம்மள?'], ['நம்ம', '!FAMILY-ய?']]),
 (31.88, 34.88, [['அதுக்குதான்'], ['*FAMILY HEALTH', '*RESET'], ['^3 DAY', '^CHALLENGE']]),
 (35.14, 37.26, [['முதல்', '2 நாள்'], ['^MORNING', '^1 HOUR']]),
 (37.38, 39.30, [['*ZOOM-ல'], ['உங்க', 'வீட்டில', 'இருந்தே']]),
 (39.30, 43.38, [['உங்க', 'FAMILY'], ['!HOSPITAL', 'போகாம'], ['இருக்க']]),
 (43.38, 48.38, [['என்னோட', '*8+ YEARS'], ['WELLNESS', 'EXPERIENCE'], ['நான்', '^TRAIN', 'பண்றேன்']]),
 (49.40, 51.76, [['^3RD DAY'], ['வாங்க', 'இங்க']]),
 (51.76, 57.34, [['உங்க', '*BMI', '*BMR'], ['*FAT %'], ['எல்லாமே', '^CHECK', 'பண்ணலாம்']]),
 (57.34, 58.70, [['இது', '*COMPLETELY', '*FREE']]),
 (61.50, 64.17, [['கீழே', '^BUTTON-ஐ'], ['CLICK', 'பண்ணி', '^REGISTER']]),
 (64.27, 67.85, [['உடனே', '*PREMIUM'], ['*WHATSAPP', 'GROUP-ல', 'JOIN']]),
 (68.57, 70.83, [['முதல்', '!10 FAMILY-க்கு', 'மட்டும்']]),
 (70.97, 74.13, [['அதுக்கப்புறம்'], ['MINIMUM', '!₹2000']]),
 (75.25, 77.51, [['வாங்க', 'நம்ம', '*CENTRE-ல'], ['MEET', 'பண்ணலாம்']]),
 (77.77, 81.03, [['^குடுவாஞ்சேரி'], ['நெல்லிக்குப்பம்', 'ROAD']]),
 (81.03, 84.31, [['^பெரியார் நகர்'], ['*SRM SCHOOL', 'OPPOSITE']]),
 (84.39, 86.41, [['இந்த', '*LOCATION'], ['உங்களுக்கு', 'வந்துரும்']]),
 (86.69, 88.46, [['நேர்ல', '*CENTRE-ல'], ['MEET', 'பண்ணலாம்']]),
]
PUNCH = [(1.2, 2.95, 1.12), (10.7, 12.9, 1.15), (43.4, 46.0, 1.10), (46.0, 48.4, 1.16), (57.3, 58.8, 1.18),
         (61.4, 64.2, 1.06), (64.2, 68.0, 1.12), (68.3, 70.9, 1.16), (70.9, 74.3, 1.10), (74.6, 77.6, 1.08), (84.3, 86.6, 1.12), (86.6, 88.5, 1.16)]
DESAT = [(21.68, 22.86)]
MUSIC = [(0.0, 31.4, 'pulse'), (31.4, 59.2, 'tech'), (59.2, END, 'uplift')]
SFX = [(1.25, 'hit'), (10.70, 'thud'), (21.68, 'thud'), (57.30, 'hit'), (61.10, 'riser'), (61.50, 'hit'), (88.46, 'hit')]
SCENE_SFX = {'questions': [], 'checkup': [], 'mappin': [], 'days': [], 'vid': []}

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
        frames.append(dict(ts=round(ts, 4), z=z, L=L, V=V, des=any(a <= ts <= b for a, b in DESAT)))
    json.dump(frames, open(W + 'frames.json', 'w'))
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL), open(W + 'audio/cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s, joined)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            src = f'Google Flow AI clip {ex["file"]}' if sc == 'vid' else f'animated "{sc}" scene'
            lic = 'AI-generated (Google Flow) - disclose in Meta' if sc == 'vid' else 'original - no licence needed'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, 'P3 AI' if sc == 'vid' else 'P5 motion graphics',
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/1.2:.1f}s) | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
