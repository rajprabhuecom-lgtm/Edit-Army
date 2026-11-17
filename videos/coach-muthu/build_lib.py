"""Shared EDL builder for the Coach Muthu ads that were shot with an off-camera prompter.

Only the coach's own takes (TAKES, source seconds) are kept. Inside each take, any stretch quieter
than GATE_DB for longer than GATE_MIN s is cut, which removes pauses and any prompter bleed
(prompter sits ~-33 dB on the coach's lav, coach ~-17 dB). Everything else follows dog-ad/plan.py.
"""
import json, bisect, csv, wave, numpy as np

GATE_DB, GATE_MIN, PRE, POST = -30.0, 0.30, 0.06, 0.10


def gated_keep(wav, takes, tail=None):
    w = wave.open(wav); sr = w.getframerate()
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    hop = sr // 50  # 20 ms
    n = len(a) // hop
    db = 20 * np.log10(np.sqrt(np.mean(a[:n * hop].reshape(n, hop) ** 2, axis=1)) + 1e-9)
    sm = np.convolve(db, np.ones(5) / 5, 'same')
    keep = []
    for tk in takes:
        s, e = tk[0], tk[1]
        if len(tk) > 2 and tk[2] == 'raw':   # verified on camera: keep whole take, no gate
            if keep and s <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], e)
            else: keep.append([s, e])
            continue
        i0, i1 = int(s * 50), int(e * 50)
        loud = sm[i0:i1] > GATE_DB
        runs = []; j = 0
        while j < len(loud):
            if loud[j]:
                k = j
                while k < len(loud):
                    if not loud[k]:
                        q = k
                        while q < len(loud) and not loud[q]: q += 1
                        if (q - k) / 50 >= GATE_MIN or q == len(loud): break
                        k = q
                    else: k += 1
                runs.append([s + j / 50, s + k / 50]); j = k
            else: j += 1
        for r0, r1 in runs:
            if r1 - r0 < 0.12: continue
            r0, r1 = max(s, r0 - PRE), min(e, r1 + POST)
            if keep and r0 <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], r1)
            else: keep.append([r0, r1])
    if tail: keep.append(list(tail))
    return keep


class EDL:
    def __init__(self, keep):
        self.keep = keep; self.ostarts = []; acc = 0
        for a, b in keep: self.ostarts.append(acc); acc += b - a
        self.total = acc

    def s2o(self, t):
        for (a, b), o in zip(self.keep, self.ostarts):
            if t < a: return o
            if t <= b: return o + (t - a)
        return self.total

    def o2s(self, t):
        i = max(0, bisect.bisect_right(self.ostarts, t) - 1); return self.keep[i][0] + (t - self.ostarts[i])


def build(W, wav, takes, tail, BROLL, GFX, CAP, PUNCH, DESAT, MUSIC, SFX, csv_name):
    ed = EDL(gated_keep(wav, takes, tail)); s2o, o2s, TOTAL = ed.s2o, ed.o2s, ed.total
    END = tail[1] if tail else takes[-1][1]
    items = []; captions = []; sfx = list(SFX)
    for bid, s0, s1, sc, lay, ex, _ in BROLL:
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
        rel = lambda ts: [round(s2o(x) - o0, 3) for x in ts]
        if 'ccues' in ex: d['ct'] = rel(ex['ccues']); sfx += [(x, 'pop') for x in ex.pop('ccues')]
        if 'bcue' in ex: b = ex.pop('bcue'); d['bt'] = rel([b])[0]; sfx.append((b, 'thud'))
        if 'kcues' in ex: d['cues'] = rel(ex['kcues']); sfx += [(x + .45, 'tick') for x in ex.pop('kcues')] + [(s0 + 0.5, 'swipe')]
        if 'mcues' in ex: d['cues'] = rel(ex['mcues']); m = ex.pop('mcues'); sfx += [(m[1], 'swipe'), (m[2] + .3, 'thud'), (m[3], 'pop')]
        if 'dcues' in ex: d['cues'] = rel(ex['dcues']); sfx += [(x, 'pop') for x in ex.pop('dcues')]
        if 'ftc' in ex: d['ftc'] = rel([ex.pop('ftc')])[0]
        d.update(ex); items.append(d)
        sfx.append((o0 - 0.12, 'whoosh', 1))
    for ty, s0, s1, ex in GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1) if s1 < END else TOTAL); d.update(ex); items.append(d)
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
        to = i / fps; ts = o2s(to); k = max(0, bisect.bisect_right(ed.ostarts, to) - 1)
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
    json.dump(dict(keep=ed.keep, music=[(s2o(a), s2o(b) if b < END else TOTAL, m) for a, b, m in MUSIC], sfx=sfxo, total=TOTAL), open(W + 'audio/cues.json', 'w'))
    with open(csv_name, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in BROLL:
            src = f'Google Flow AI clip {ex["file"]}' if sc == 'vid' else f'animated "{sc}" scene'
            lic = 'AI-generated (Google Flow) - disclose in Meta' if sc == 'vid' else 'original - no licence needed'
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, src, 'P3 AI' if sc == 'vid' else 'P5 motion graphics',
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', 'rendered', lic])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
    print(f'total {TOTAL:.2f}s -> {TOTAL/1.2:.2f}s | {len(ed.keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/1.2:.1f}s) | captions {len(captions)} | sfx {len(sfxo)}')
    return ed
