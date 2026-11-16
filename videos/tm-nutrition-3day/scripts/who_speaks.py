"""Who is speaking? Combine face tracking (mouth movement) with voice activity.
usage: python3 who_speaks.py C0008L   (reads face/<name>_*.json, mezz/<name minus L>.16k.wav; writes speak/<name>.json)
Per 40 ms frame:
  voice  = audio RMS above the noise floor
  mouth  = lip opening varies (rolling std) or is open beyond the resting level
  client = voice & mouth    -> the coach is speaking: usable
  prompt = voice & !mouth   -> someone off camera (the prompter) is speaking: never usable
  idle   = !voice           -> silence (the coach may be sitting idle)
Writes intervals of client speech (merged, min length) and the per-frame labels for inspection."""
import sys, json, glob, numpy as np, soundfile as sf
B = '/home/user/w/tm/'; name = sys.argv[1]
F = sorted(sum((json.load(open(p)) for p in sorted(glob.glob(B + f'face/{name}_*.json'))), []), key=lambda r: r[0])
t = np.array([r[0] for r in F]); pres = np.array([r[1] for r in F]); gap = np.array([r[2] for r in F])
a, sr = sf.read(B + f'mezz/{name[:-1]}.16k.wav', dtype='float32')
hop = int(0.04 * sr)
rms = np.array([np.sqrt(np.mean(a[max(0, int(x * sr) - hop):int(x * sr) + hop] ** 2) + 1e-10) for x in t])
db = 20 * np.log10(rms)
floor = np.percentile(db, 10); voice = db > floor + 14                         # ~14 dB above the room tone
# mouth activity: rolling std of lip gap over ~0.36 s + open beyond resting
def roll(x, k, f):
    pad = np.pad(x, (k // 2, k // 2), mode='edge'); return np.array([f(pad[i:i + k]) for i in range(len(x))])
g = np.where(pres > 0, gap, np.nan); g = np.where(np.isnan(g), np.nanmedian(g), g)
rest = np.percentile(g, 20)
sd = roll(g, 9, np.std); op = roll(g, 7, np.max) - rest
mouth = (sd > 0.006) | (op > 0.035)
mouth = roll(mouth.astype(float), 9, np.max) > 0                                # bridge short closures between syllables
client = voice & mouth & (pres > 0); prompt = voice & ~mouth
def intervals(m, mingap=0.30, minlen=0.35):
    out = []; s = None
    for i, v in enumerate(m):
        if v and s is None: s = t[i]
        if not v and s is not None: out.append([s, t[i]]); s = None
    if s is not None: out.append([s, t[-1]])
    mg = []
    for x in out:
        if mg and x[0] - mg[-1][1] < mingap: mg[-1][1] = x[1]
        else: mg.append(x)
    return [[round(p, 2), round(q, 2)] for p, q in mg if q - p >= minlen]
res = dict(client=intervals(client), prompt=intervals(prompt, 0.2, 0.25), floor=round(float(floor), 1),
           frames=[[round(float(x), 2), int(v), int(m), round(float(d), 1), round(float(gg), 3)] for x, v, m, d, gg in zip(t, voice, mouth, db, g)])
import os; os.makedirs(B + 'speak', exist_ok=True); json.dump(res, open(B + f'speak/{name}.json', 'w'))
print(name, 'client', round(sum(q - p for p, q in res['client']), 1), 's in', len(res['client']), 'pieces | prompter/off-camera voice',
      round(sum(q - p for p, q in res['prompt']), 1), 's | face found', round(pres.mean() * 100), '%')
