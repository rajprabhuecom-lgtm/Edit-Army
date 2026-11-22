"""Shared EDL builder for the 202603 batch (copied from 202605; captions optional, progress bar drawn in comp).  python3 build.py <video-id>
Each videos/202603/<video-id>/plan.py defines SRC, BROLL, GFX, CAP, PUNCH, MUSIC, SFX (+ optional CAPY, CAPH, BLUR, DESAT, HOLD, ENDCARD).
All plan times are SOURCE seconds; this converts them to OUTPUT (pre-speed) time.  Final = output / SPEED."""
import json, bisect, csv, sys, os, re, subprocess, importlib.util
VID = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('plan', f'{ROOT}/{VID}/plan.py'); P = importlib.util.module_from_spec(spec); spec.loader.exec_module(P)
W = f'/home/user/w/{VID}/'
for d in ('gfx', 'audio', 'ov', 'prev'): os.makedirs(W + d, exist_ok=True)
SRC = f'{ROOT}/source/{P.SRC}'
SPEED = getattr(P, 'SPEED', 1.2)
dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', SRC], capture_output=True, text=True).stdout)
# ---- jump cuts: drop pauses > 0.3 s (keep 0.06 s before / 0.10 s after speech) ----
r = subprocess.run(f'ffmpeg -i {SRC} -af silencedetect=n=-36dB:d=0.30 -f null -', shell=True, capture_output=True, text=True).stderr
ss = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; se = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
SIL = list(zip(ss, se + [dur] * (len(ss) - len(se))))
END = getattr(P, 'END', dur)
segs, t = [], 0.0
for a, b in SIL:
    if a > t: segs.append([t, min(a, END)])
    t = b
if t < END: segs.append([t, END])
PRE, POST = 0.06, 0.10
keep = []
for s, e in segs:
    if e - s < 0.08: continue
    a, b = max(0, s - PRE), min(END, e + POST)
    if keep and a <= keep[-1][1] + 0.02: keep[-1][1] = max(keep[-1][1], b)
    else: keep.append([a, b])
if not getattr(P, 'JUMPCUT', True): keep = [[0.0, END]]          # keep natural pauses (comedy / kids clips)
HOLD = getattr(P, 'HOLD', 0.0)          # seconds of frozen last frame for the end card
ostarts, acc = [], 0
for a, b in keep: ostarts.append(acc); acc += b - a
TOTAL = acc + HOLD
def s2o(t):
    if t >= END: return acc + (t - END)
    for (a, b), o in zip(keep, ostarts):
        if t < a: return o
        if t <= b: return o + (t - a)
    return acc
def o2s(t):
    if t >= acc: return END - 0.04
    i = max(0, bisect.bisect_right(ostarts, t) - 1); return keep[i][0] + (t - ostarts[i])

items, captions, sfx = [], [], list(P.SFX)
for bid, s0, s1, sc, lay, ex, _ in P.BROLL:
    o0, o1 = s2o(s0), s2o(s1); d = dict(type=sc, t0=o0, t1=o1, layout=lay, id=bid); ex = dict(ex)
    for k in ('cues', 'ca', 'cb', 'ccues'):      # cue lists given in source time -> relative output time
        if k in ex: d[k] = [round(s2o(x) - o0, 3) for x in ex.pop(k)]; sfx += [(x, 'pop') for x in [o2s(o0 + c) for c in d[k]]]
    for k in ('xc', 'bc', 'hit', 'ta', 'tb', 'tv', 'mc', 'wc', 'cc', 'lc'):
        if k in ex: d[k] = round(s2o(ex.pop(k)) - o0, 3)
    if 'xc' in d: sfx.append((o2s(o0 + d['xc']), 'thud'))
    if 'hit' in d: sfx.append((o2s(o0 + d['hit']), 'thud'))
    d.update(ex); items.append(d); sfx.append((o2s(o0) - 0.12, 'whoosh'))
for ty, s0, s1, ex in P.GFX:
    d = dict(type=ty, t0=s2o(s0), t1=s2o(s1)); d.update(ex); items.append(d)
    if ty in ('text', 'badge'): sfx.append((s0, 'pop'))
    if ty == 'price': sfx.append((s0 + 0.45, 'cash'))
    if ty == 'stat': sfx.append((s0, 'hit')); sfx.append((s0 + 0.8, 'ding'))
    if ty == 'confetti': sfx.append((s0, 'pop'))
    if ty == 'stamp': sfx.append((s0, 'thud'))
    if ty == 'cta': sfx.append((s0 + 0.35, 'click'))
    if ty in ('endcard', 'endcard2'): sfx.append((s0, 'hit'))
for s0, s1, chunks in getattr(P, 'CAP', []):
    o0, o1 = s2o(s0), s2o(s1); wts = [sum(len(w) for w in c) + 4 for c in chunks]; tot = sum(wts); t = o0
    for c, wt in zip(chunks, wts):
        dd = (o1 - o0) * wt / tot
        words = [w.lstrip('*!^') for w in c]; hl = [i for i, w in enumerate(c) if w[:1] in '*!^']
        col = '#FF3B30' if any(w.startswith('!') for w in c) else ('#FFD60A' if any(w.startswith('^') for w in c) else '#00C896')
        captions.append(dict(t0=t, t1=t + dd, words=words, hl=hl, col=col)); t += dd
for a, b in zip(captions, captions[1:]):
    if b['t0'] - a['t1'] < 0.45: a['t1'] = b['t0']
for c in captions:
    mid = (c['t0'] + c['t1']) / 2
    for it in items:
        if it['t0'] <= mid < it['t1']:
            if it.get('layout') == 'split': c['pos'] = 'split'
            if it['type'] == 'cta' and getattr(P, 'CTA_CAP_HI', True): c['pos'] = 'hi'
            if it['type'] in ('endcard', 'endcard2'): c['pos'] = 'none'
tl = dict(items=items, captions=captions, total=TOTAL)
if hasattr(P, 'CAPY'): tl.update(capy=P.CAPY, caph=getattr(P, 'CAPH', 190))
json.dump(tl, open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
FPS = 30; frames = []
for i in range(int(round(TOTAL * FPS))):
    to = i / FPS; ts = o2s(to); k = max(0, bisect.bisect_right(ostarts, to) - 1)
    z = 1.0 if k % 2 == 0 else getattr(P, 'ALTZ', 1.07)          # alternate punch-in on every jump cut
    for a, b, zz in P.PUNCH:
        if a <= ts <= b: z = zz
    if any(a <= ts <= b for a, b in getattr(P, 'NOZOOM', [])): z = 1.0   # keep burned-in banners / real proof fully in frame
    L = None
    for it in items:
        if it.get('layout') and it['t0'] <= to < it['t1']: L = it['layout']
    frames.append(dict(ts=round(ts, 4), z=z, L=L, des=any(a <= ts <= b for a, b in getattr(P, 'DESAT', []))))
json.dump(frames, open(W + 'frames.json', 'w'))
json.dump(dict(src=SRC, progress=getattr(P, 'PROGRESS', True), nprog=int(round((TOTAL - HOLD) * 30)), blur=getattr(P, 'BLUR', None), crop_y0=getattr(P, 'CROP_Y0', 230), cx=getattr(P, 'CX', 540), cy=getattr(P, 'CY', 700)), open(W + 'comp.json', 'w'))
sfxo = sorted((s2o(t), n) for t, n in sfx)
json.dump(dict(src=SRC, keep=keep, hold=HOLD, music=[(s2o(a), s2o(b), m) for a, b, m in P.MUSIC], sfx=sfxo, total=TOTAL, speed=SPEED), open(W + 'audio/cues.json', 'w'))
with open(f'{ROOT}/{VID}/broll_plan.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID', 'Source time (s)', 'Final time (s)', 'Keyword spoken (meaning)', 'Visual', 'Source', 'Layout', 'On-screen (s, final)', 'Status', 'Licence'])
    for bid, s0, s1, sc, lay, ex, kw in P.BROLL:
        w.writerow([bid, f'{s0:.2f}-{s1:.2f}', f'{s2o(s0)/SPEED:.1f}-{s2o(s1)/SPEED:.1f}', kw, f'animated "{sc}" scene (engine v6)', 'P5 motion graphics',
                    'split screen' if lay == 'split' else 'full cutaway', f'{(s2o(s1)-s2o(s0))/SPEED:.1f}', 'rendered', 'original - no licence needed'])
cov = sum(it['t1'] - it['t0'] for it in items if it.get('layout'))
full = sum(it['t1'] - it['t0'] for it in items if it.get('layout') == 'full')
print(f'{VID}: src {dur:.2f}s -> {TOTAL:.2f}s -> final {TOTAL/SPEED:.2f}s | {len(keep)} cuts | B-roll {cov/TOTAL*100:.0f}% (full {full/SPEED:.1f}s) | captions {len(captions)} | sfx {len(sfxo)}')
