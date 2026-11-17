"""QA: scan a finished voice track for the prompter's voice (ECAPA speaker embeddings, 0.6 s windows, 50 ms hop).
usage: python3 voice_check.py <workdir>   (reads audio/voice_cut.wav + audio/cues.json; prints every suspicious window and its take)"""
import sys, json, numpy as np, soundfile as sf, torch, scipy.signal as ss
from speechbrain.inference.speaker import EncoderClassifier
W = sys.argv[1].rstrip('/') + '/'; B = '/home/user/w/tm/'; SR = 16000
enc = EncoderClassifier.from_hparams(source='speechbrain/spkrec-ecapa-voxceleb', savedir='/root/models/ecapa', run_opts={'device': 'cpu'})
AU = {f: sf.read(B + f'mezz/{f}.16k.wav', dtype='float32')[0] for f in ('C0007', 'C0008')}
def e_of(x):
    with torch.no_grad(): e = enc.encode_batch(torch.tensor(x)[None])[0, 0].numpy()
    return e / np.linalg.norm(e)
def cent(spans):
    es = [e_of(AU[f][int(t * SR):int((t + .6) * SR)]) for f, a, b in spans for t in np.arange(a, b - .6, .3)]
    c = np.mean(es, 0); return c / np.linalg.norm(c)
COACH = [('C0007', 46.6, 50.5), ('C0007', 55.6, 59.4), ('C0007', 101.5, 105.1), ('C0007', 146.2, 149.4), ('C0007', 162.9, 167.3),
         ('C0007', 202.3, 205.4), ('C0008', 247.7, 253.6), ('C0008', 360.2, 365.5), ('C0008', 437.8, 441.0), ('C0008', 483.2, 488.9), ('C0008', 499.4, 503.4)]
PROMPT = [('C0007', 197.7, 201.8), ('C0007', 111.9, 114.3), ('C0007', 136.8, 139.2), ('C0007', 83.7, 92.0), ('C0008', 159.7, 166.6)]
cC, cP = cent(COACH), cent(PROMPT)
v, sr = sf.read(W + 'audio/voice_cut.wav', dtype='float32'); v = ss.resample_poly(v, 1, sr // SR).astype(np.float32)
cues = json.load(open(W + 'audio/cues.json')); pieces = cues['pieces']
def where(t):
    p = next((p for p in pieces if p['o0'] <= t < p['o1']), None)
    if not p: return 'tail'
    return f"{p['id']}+{t - p['o0']:.2f}s" if p['k'] == 'seg' else f"{p['id']} (client bite)"
WIN, HOP = 0.6, float(sys.argv[2]) if len(sys.argv) > 2 else 0.05; bad = []; n = 0
for t in np.arange(0, len(v) / SR - WIN, HOP):
    x = v[int(t * SR):int((t + WIN) * SR)]
    if 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9) < -38: continue                   # silence
    c = t + WIN / 2; p = next((p for p in pieces if p['o0'] <= c < p['o1']), None)
    if p and p['k'] == 'bite': continue                                                  # client testimonial audio is meant to be there
    e = e_of(x); s = float(e @ cC - e @ cP); n += 1
    if s < 0: bad.append((round(c, 2), round(s, 3), where(c)))
print(f'checked {n} voiced windows; prompter-like: {len(bad)}')
for b in bad: print('  ', b)
