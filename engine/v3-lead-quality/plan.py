"""EDL for sun_ads: jump cuts, B-roll map, graphics, captions, zooms, music + SFX. Source time -> output (pre-speed) time."""
import json, bisect, csv
segs = json.load(open('/home/claude/w/segs.json'))
PRE, POST = 0.06, 0.09
keep = []
for s, e in segs:
    if e - s < 0.1: continue
    a, b = max(0, s - PRE), e + POST
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
keep[-1][1] = 111.0   # hold tail under the end card
keep = [k for k in keep if k[0] < 111]
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

BROLL = [
 ('B01', 4.62, 8.70, 'clientmsg', 'split', '"an important client told me this"'),
 ('B02', 11.28, 16.47, 'leadrain', 'full', '"run ads -> quality AND junk enquiries come"'),
 ('B03', 25.30, 28.83, 'methods', 'full', '"many say use VSL, use this, use that"'),
 ('B04', 29.11, 32.56, 'cpl', 'split', '"but cost per enquiry must not increase"'),
 ('B05', 40.08, 46.52, 'pipeline', 'split', '"ads -> enquiries -> WhatsApp -> chat flows"'),
 ('B06', 46.90, 51.06, 'chatq', 'split', '"ask questions, send testimonials + brochures"'),
 ('B07', 51.35, 56.42, 'filter', 'full', '"filter out the interested candidates"'),
 ('B08', 58.78, 62.70, 'crm', 'split', '"no matter how many enquiries, only those who answer properly"'),
 ('B09', 64.88, 68.99, 'booking', 'split', '"system automatically books the appointment"'),
 ('B10', 69.28, 73.48, 'revenue', 'full', '"easily talk to the right client and generate revenue"'),
 ('B11', 87.12, 91.38, 'livedemo', 'split', '"I will show you a live demo of the chat flow"'),
 ('B12', 95.30, 98.62, 'implement', 'split', '"we can implement it for you"'),
 ('B13', 102.37, 107.34, 'time', 'full', '"save your time"'),
]
GFX = [
 ('flash', 1.05, 1.25, {}),
 ('text', 1.11, 2.60, {'html': 'NO <span class="r">JUNK</span><br>LEADS ❌', 'y': 150, 'size': 140}),
 ('text', 2.72, 4.55, {'html': 'ONLY <span class="g">QUALITY</span><br>LEADS ✅', 'y': 150, 'size': 130}),
 ('badge', 9.07, 10.96, {'html': '⚠️ BIG PROBLEM', 'y': 200, 'size': 72}),
 ('text', 16.84, 20.55, {'html': 'TALK ONLY TO<br><span class="g">QUALITY</span> LEADS?', 'y': 150, 'size': 108}),
 ('badge', 21.71, 25.10, {'html': '💡 I USED THIS METHOD', 'y': 200, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('text', 32.85, 36.56, {'html': 'PROBLEM<br><span class="g">SOLVED ✓</span>', 'y': 150, 'size': 130}),
 ('cta', 36.88, 39.90, {'label': '➕ FOLLOW ME', 'badge': '✓ PROVEN METHODS', 'y': 1070}),
 ('badge', 56.60, 58.60, {'html': '💬 MY CLIENT SAID…', 'y': 200, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 64}),
 ('text', 62.80, 64.60, {'html': 'MONITOR<br><span class="g">ONLY THEM</span>', 'y': 150, 'size': 124}),
 ('badge', 73.75, 77.80, {'html': '🎥 OPEN CLIENT TESTIMONIAL', 'y': 200, 'bg': 'var(--yl)', 'fg': '#000', 'size': 56}),
 ('text', 77.99, 81.90, {'html': 'RUNNING <span class="y">ADS</span><br>FOR YOUR BUSINESS?', 'y': 150, 'size': 96}),
 ('flash', 82.10, 82.30, {}),
 ('cta', 82.21, 87.00, {'label': '💬 DM ME', 'badge': 'GET ONLY QUALITY ENQUIRIES', 'y': 1070}),
 ('text', 91.67, 95.00, {'html': 'YOU TOO<br><span class="g">CAN DO THIS 🚀</span>', 'y': 150, 'size': 110}),
 ('cta', 98.97, 102.10, {'label': '💬 DM ME NOW', 'badge': '⚙️ WE IMPLEMENT IT', 'y': 1070}),
 ('text', 107.55, 109.25, {'html': 'YOUR <span class="y">BIGGEST</span><br><span class="y">ASSET</span> ⏰', 'y': 150, 'size': 124}),
 ('endcard', 109.25, 111.0, {'html': 'DM ME NOW<br><span class="g">QUALITY ENQUIRIES</span><br><span class="y">NOT JUNK LEADS ↓</span>'}),
]
CAP = [
 (1.11, 2.54, [['I', "DON'T", 'WANT', '!JUNK', '!LEADS']]),
 (2.77, 4.42, [['GIVE ME', 'ONLY', '*QUALITY', '*LEADS']]),
 (4.62, 8.70, [['AN', '^IMPORTANT', 'CLIENT'], ['TOLD ME', 'THIS']]),
 (9.07, 10.96, [['YES', 'THIS IS A'], ['!BIG', '!PROBLEM']]),
 (11.28, 12.89, [['WHEN YOU', 'RUN', '^ADS']]),
 (13.27, 16.47, [['*QUALITY', 'AND'], ['!JUNK', 'ENQUIRIES', 'BOTH COME']]),
 (16.84, 20.50, [['HOW DO WE', 'TALK'], ['ONLY TO', '*QUALITY', '*ENQUIRIES?']]),
 (20.84, 22.83, [['WHEN THAT', 'QUESTION', 'CAME']]),
 (23.13, 25.04, [['I USED', '^THIS METHOD']]),
 (25.30, 26.08, [['MANY', 'PEOPLE', 'SAY']]),
 (26.30, 28.83, [['USE', '^VSL'], ['USE THIS', 'USE THAT']]),
 (29.11, 32.56, [['BUT', '^COST PER', '^ENQUIRY'], ['MUST', '!NOT', '!INCREASE']]),
 (32.85, 36.56, [['WE', '*SOLVED IT'], ['WITH', 'THIS METHOD']]),
 (36.88, 39.81, [['WANT', '*PROVEN', '*METHODS?'], ['^FOLLOW ME', 'NOW']]),
 (40.08, 41.80, [['WE RUN', '^ADS'], ['WE GET', 'ENQUIRIES']]),
 (42.09, 44.90, [['ENQUIRIES', 'GO TO'], ['*WHATSAPP']]),
 (45.27, 46.52, [['INTO', '*CHAT FLOWS']]),
 (46.90, 47.90, [['WE', '^ASK QUESTIONS']]),
 (48.13, 51.06, [['SEND', '*TESTIMONIALS'], ['AND', '*BROCHURES']]),
 (51.35, 54.07, [['!FILTER', 'OUT'], ['*INTERESTED', 'LEADS']]),
 (54.29, 56.42, [['WE BUILT', 'THIS'], ['FOR OUR', '^CLIENT']]),
 (56.60, 58.56, [['WHAT', 'HE SAID']]),
 (58.78, 62.61, [['NO MATTER', 'HOW MANY'], ['ENQUIRIES', 'COME'], ['ONLY WHO', '*ANSWERS RIGHT']]),
 (62.89, 64.60, [['I', '*MONITOR', 'ONLY THEM']]),
 (64.88, 68.99, [['THE SYSTEM', '*AUTO-BOOKS'], ['THE', '*APPOINTMENT']]),
 (69.28, 73.48, [['I TALK TO', 'THE', '*RIGHT CLIENT'], ['AND MAKE', '^REVENUE', '^EASILY']]),
 (73.75, 77.74, [['THE CLIENT', 'GAVE'], ['AN', '^OPEN', '^TESTIMONIAL']]),
 (77.99, 81.88, [['YOUR', 'BUSINESS', 'TOO'], ['IS', 'RUNNING', '^ADS']]),
 (82.21, 85.45, [['WANT ONLY', 'THE'], ['*RIGHT', '*ENQUIRIES?']]),
 (85.69, 86.87, [['^DM ME', 'ONCE']]),
 (87.12, 91.38, [["I'LL SHOW", 'A'], ['^LIVE DEMO'], ['OF THE', '*CHAT FLOW']]),
 (91.67, 94.96, [['YOU TOO', 'CAN GET'], ['*BUSINESS', 'LIKE THIS']]),
 (95.30, 98.62, [['WANT', '*QUALITY', 'ENQUIRIES?'], ['WE', '*IMPLEMENT IT']]),
 (98.97, 102.05, [['^DM ME', '^NOW'], ['FOR', 'IMPLEMENTATION']]),
 (102.37, 107.34, [['TALK TO', '*QUALITY', 'ENQUIRIES'], ['AND', '^SAVE', '^YOUR TIME']]),
 (107.64, 109.23, [["THAT'S YOUR", '^BIGGEST', '^ASSET']]),
]
PUNCH = [(1.0, 2.6, 1.14), (2.7, 4.5, 1.06), (9.0, 11.0, 1.16), (16.8, 18.6, 1.10), (18.6, 20.6, 1.18), (32.8, 36.6, 1.10),
         (36.8, 40.0, 1.16), (56.5, 58.7, 1.12), (62.8, 64.7, 1.15), (73.7, 77.9, 1.08), (77.9, 82.0, 1.12), (82.1, 87.1, 1.18),
         (91.6, 95.1, 1.10), (98.9, 102.2, 1.18), (107.5, 109.3, 1.16)]
DESAT = [(9.0, 11.0)]
MUSIC = [(0.0, 20.75, 'pulse'), (20.75, 82.15, 'tech'), (82.15, 111.0, 'uplift')]
SFX = [(1.11, 'hit'), (2.72, 'pop'), (16.84, 'thud'), (36.88, 'hit'), (81.0, 'riser'), (82.21, 'hit'), (98.97, 'hit'), (109.25, 'hit')]
SCENE_SFX = {
 'clientmsg': [(.45, 'pop'), (1.25, 'pop'), (2.3, 'tick')],
 'leadrain': [(.0, 'thud')] + [(.5 + i * .13 + .45, 'tick') for i in range(16)],
 'methods': [(.25, 'swipe'), (.65, 'swipe'), (1.05, 'swipe'), (1.7, 'thud'), (1.92, 'thud'), (2.14, 'thud'), (2.4, 'pop')],
 'cpl': [(.4, 'riser_s'), (1.1, 'thud'), (1.3, 'pop')],
 'pipeline': [(.2, 'pop'), (1.1, 'pop'), (2.0, 'pop'), (2.6, 'ding')],
 'chatq': [(.4, 'pop'), (1.15, 'pop'), (1.9, 'pop')],
 'filter': [(.6 + i * .22 + .5, 'tick') for i in range(14)] + [(2.6, 'ding')],
 'crm': [(.3 + i * .18, 'tick') for i in range(5)] + [(2.0, 'click')],
 'booking': [(.7 + i * .42, 'ding') for i in range(5)],
 'revenue': [(.4, 'riser_s'), (1.0, 'cash'), (1.8, 'cash')],
 'livedemo': [(.4 + i * .22, 'pop') for i in range(6)] + [(3.0, 'click'), (3.05, 'ding')],
 'implement': [(.65 + i * .45, 'tick') for i in range(4)] + [(2.3, 'ding')],
 'time': [(.0, 'thud')] + [(.3 + i * .12, 'tick') for i in range(14)] + [(1.3, 'pop')],
}

def build():
    items = []; captions = []; sfx = list(SFX)
    for bid, s0, s1, sc, lay, _ in BROLL:
        o0 = s2o(s0)
        items.append(dict(type=sc, t0=o0, t1=s2o(s1), layout=lay, id=bid))
        sfx.append((o0 - 0.12, 'whoosh', 1)); sfx.append((s2o(s1) - 0.12, 'swipe', 1))
        for dt, n in SCENE_SFX.get(sc, []):
            if o0 + dt < s2o(s1): sfx.append((o0 + dt, n, 1))
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
    json.dump(dict(items=items, captions=captions, total=TOTAL), open('/home/claude/w/gfx/timeline.json', 'w'), ensure_ascii=False)
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.09
        for a, b, zz in PUNCH:
            if a <= ts <= b: z = zz
        L = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']: L = it['layout']
        frames.append(dict(ts=round(ts, 4), z=z, L=L, des=any(a <= ts <= b for a, b in DESAT)))
    json.dump(frames, open('/home/claude/w/frames.json', 'w'))
    # sfx: entries with 3rd elem are already in output time
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b), m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL), open('/home/claude/w/audio/cues.json', 'w'))
    with open('/home/claude/w/broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s)', 'Final time (s, after 1.2x)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen length (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, kw in BROLL:
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, f'animated "{sc}" motion-graphic scene', 'P5 motion graphics (original)', 'split screen' if lay == 'split' else 'full cutaway',
                        f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', 'original - no licence needed'])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% | captions {len(captions)} | sfx {len(sfxo)}')
if __name__ == '__main__': build()
