"""Shared EDL builder for the 'my videos' batch. A plan module defines BROLL, GFX, CAP, PUNCH, MUSIC, SFX, CFG.
Source time -> output (pre-speed) time via jump cuts from silencedetect. Final = output / 1.2."""
import json, bisect, csv, os, re, subprocess
def silences(src, db=-33, d=0.32):
    r = subprocess.run(['ffmpeg', '-i', src, '-af', f'silencedetect=noise={db}dB:d={d}', '-f', 'null', '-'], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: (-?[\d.]+)', r)]; en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
    if len(en) < len(st): en.append(dur)
    return list(zip([max(0, s) for s in st], en)), dur
def make_keep(src, end_hold=1.8, PRE=0.08, POST=0.12):
    sil, dur = silences(src); segs = []; t = 0.0
    for a, b in sil:
        if a > t: segs.append([t, a])
        t = b
    if t < dur: segs.append([t, dur])
    keep = []
    for s, e in segs:
        if e - s < 0.12: continue
        a, b = max(0, s - PRE), min(dur, e + POST)
        if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
        else: keep.append([a, b])
    keep[-1][1] = keep[-1][1] + end_hold   # hold under end card (frames clamp to last source frame)
    return keep, dur
class EDL:
    def __init__(s, keep):
        s.keep = keep; s.ost = []; acc = 0
        for a, b in keep: s.ost.append(acc); acc += b - a
        s.total = acc
    def s2o(s, t):
        for (a, b), o in zip(s.keep, s.ost):
            if t < a: return o
            if t <= b: return o + (t - a)
        return s.total
    def o2s(s, t):
        i = max(0, bisect.bisect_right(s.ost, t) - 1); return s.keep[i][0] + (t - s.ost[i])
SCENE_SFX = {}
def build(P, W):
    keep, dur = make_keep(W + 'src.mp4', getattr(P, 'END_HOLD', 1.8)); E = EDL(keep); s2o = E.s2o; TOTAL = E.total
    items = []; captions = []; sfx = list(P.SFX)
    for row in P.BROLL:
        bid, s0, s1, sc, lay, ex, _ = row
        o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); d.update(ex)
        for k in list(d):   # keys ending in _s are source times -> relative scene time
            if k.endswith('_s'):
                v = d.pop(k); d[k[:-2]] = [s2o(x) - o0 for x in v] if isinstance(v, list) else s2o(v) - o0
        items.append(d)
        sfx.append((o0 - 0.12, 'whoosh', 1)); sfx.append((o1 - 0.12, 'swipe', 1))
        for dt, n in P.SCENE_SFX.get(sc, [(.35, 'pop'), (1.1, 'pop'), (1.9, 'ding')]):
            if o0 + dt < o1: sfx.append((o0 + dt, n, 1))
    for ty, s0, s1, ex in P.GFX:
        d = dict(type=ty, t0=s2o(s0), t1=s2o(s1) if s1 < 900 else TOTAL); d.update(ex); items.append(d)
        if ty in ('text', 'badge', 'stamp'): sfx.append((s0, 'pop'))
        if ty == 'cta': sfx.append((s0 + 0.35, 'tick'))
        if ty in ('endcard', 'endps'): sfx.append((s0, 'hit'))
    for s0, s1, chunks in P.CAP:
        o0, o1 = s2o(s0), s2o(s1); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts); t = o0
        for c, wt in zip(chunks, wts):
            d = (o1 - o0) * wt / tot
            words = [w.lstrip('*!^') for w in c]; hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
            col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
            captions.append(dict(t0=t, t1=t + d, words=words, hl=hl, col=col)); t += d
    for a, b in zip(captions, captions[1:]):
        if 0 < b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
    for c in captions:
        mid = (c['t0'] + c['t1']) / 2
        if any(s2o(a) <= mid < s2o(b) for a, b in getattr(P, 'CAPMID', [])): c['pos'] = 'mid'
        for it in items:
            if it['t0'] <= mid < it['t1']:
                if it.get('layout') == 'split': c['pos'] = 'split'
                if it['type'] == 'cta': c['pos'] = 'hi'
                if it['type'] in ('endcard', 'endps') or (it.get('layout') == 'full' and it.get('nocap')): c['pos'] = 'none'
    C = P.CFG
    json.dump(dict(items=items, captions=captions, total=TOTAL, capTop=C.get('capTop', 1175), capH=C.get('capH', 300), midTop=C.get('midTop', 290)), open(W + 'timeline.json', 'w'), ensure_ascii=False)
    fps = 30; frames = []
    for i in range(int(round(TOTAL * fps))):
        to = i / fps; ts = E.o2s(to); k = max(0, bisect.bisect_right(E.ost, to) - 1)
        z = 1.0 if k % 2 == 0 else 1.08
        for a, b, zz in P.PUNCH:
            if a <= ts <= b: z = zz
        L = None
        for it in items:
            if it.get('layout') and it['t0'] <= to < it['t1']: L = it['layout']
        frames.append(dict(ts=round(min(ts, dur - 0.05), 4), z=z, L=L, des=any(a <= ts <= b for a, b in getattr(P, 'DESAT', []))))
    json.dump(dict(frames=frames, blur=C.get('blur', []), cy=C.get('cy', 760), cropY=C.get('cropY', 230)), open(W + 'frames.json', 'w'))
    sfxo = sorted([(x[0], x[1]) if len(x) == 3 else (s2o(x[0]), x[1]) for x in sfx])
    json.dump(dict(keep=keep, music=[(s2o(a), s2o(b) if b < 900 else TOTAL, m) for a, b, m in P.MUSIC], sfx=sfxo, total=TOTAL), open(W + 'cues.json', 'w'))
    with open(W + 'broll_plan.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['ID', 'Source time (s)', 'Final time (s, after 1.2x)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen length (s, final)', 'Status', 'Licence'])
        for bid, s0, s1, sc, lay, ex, kw in P.BROLL:
            w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/1.2:.1f}-{s2o(s1)/1.2:.1f}', kw, f'animated "{sc}" motion-graphic scene', 'P5 motion graphics (original)',
                        'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/1.2:.1f}', ex.get('status', 'rendered'), 'original - no licence needed'])
    cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
    print(f'{W}: src {dur:.1f}s -> {TOTAL:.2f}s -> final {TOTAL/1.2:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% | captions {len(captions)} | sfx {len(sfxo)}')
