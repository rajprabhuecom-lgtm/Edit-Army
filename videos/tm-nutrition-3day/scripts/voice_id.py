"""Coach vs prompter by VOICE (speaker embeddings), 50 ms resolution. Run after selects_v2.py is roughly right.
ECAPA (speechbrain/spkrec-ecapa-voxceleb) embeddings on 0.8 s windows, 50 ms hop; each window is scored against a coach
centroid and a prompter centroid built from known lines. Then each selected take gets trimmed so that it starts after the
prompter's last syllable and ends before the prompter's next one, with the cut snapped to the quietest 10 ms in the gap.
usage: python3 voice_id.py  -> /home/user/w/tm/voice/report.txt + trims.json"""
import sys, os, json, numpy as np, soundfile as sf, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'vsl')); from selects_v2 import SEL
from speechbrain.inference.speaker import EncoderClassifier
B = '/home/user/w/tm/'; os.makedirs(B + 'voice', exist_ok=True)
enc = EncoderClassifier.from_hparams(source='speechbrain/spkrec-ecapa-voxceleb', savedir='/root/models/ecapa', run_opts={'device': 'cpu'})
AU = {f: sf.read(B + f'mezz/{f}.16k.wav', dtype='float32')[0] for f in ('C0007', 'C0008')}; SR = 16000
def emb(f, t0, t1):
    x = torch.tensor(AU[f][int(t0 * SR):int(t1 * SR)])[None]
    with torch.no_grad(): e = enc.encode_batch(x)[0, 0].numpy()
    return e / np.linalg.norm(e)
def centroid(spans, win=1.0):
    es = []
    for f, a, b in spans:
        t = a
        while t + win <= b: es.append(emb(f, t, t + win)); t += 0.5
    c = np.mean(es, 0); return c / np.linalg.norm(c)
# reference voices: lines confirmed by face tracking (prompter = voice with the coach's mouth still)
COACH = [('C0007', 46.6, 50.5), ('C0007', 55.6, 59.4), ('C0007', 101.5, 105.1), ('C0007', 146.2, 149.4), ('C0007', 162.9, 167.3),
         ('C0007', 202.3, 205.4), ('C0008', 247.7, 253.6), ('C0008', 360.2, 365.5), ('C0008', 437.8, 441.0), ('C0008', 483.2, 488.9), ('C0008', 499.4, 503.4)]
PROMPT = [('C0007', 197.7, 201.8), ('C0007', 111.9, 114.3), ('C0007', 136.8, 139.2), ('C0007', 83.7, 92.0), ('C0008', 159.7, 166.6)]
cC, cP = centroid(COACH), centroid(PROMPT)
print('coach/prompter centroid similarity', round(float(cC @ cP), 3))
def rms_db(f, t, w=0.01):
    x = AU[f][int(t * SR):int((t + w) * SR)]; return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
WIN, HOP = 0.8, 0.05
rep = []; trims = {}
for sid, f, a, b, txt, mean in SEL:
    if not f.startswith('C'): continue
    lo, hi = max(0, a - 1.2), b + 1.2; ts = np.arange(lo, hi - WIN, HOP)
    sc = []
    for t in ts:
        e = emb(f, t, t + WIN); sc.append(float(e @ cC - e @ cP))           # >0 coach, <0 prompter
    sc = np.array(sc); ctr = ts + WIN / 2
    lv = np.array([rms_db(f, c - .02, .04) for c in ctr]); floor = np.percentile([rms_db(f, t) for t in np.arange(lo, hi, .01)], 10)
    voiced = lv > floor + 12
    lab = np.where(~voiced, '.', np.where(sc > 0.05, 'C', np.where(sc < -0.05, 'P', '?')))
    # coach span: from the first to the last coach window inside [a,b] (+/- the window half-width), clipped by prompter windows
    inside = (ctr >= a - .3) & (ctr <= b + .3)
    cidx = np.where(inside & (lab == 'C'))[0]
    if not len(cidx): rep.append(f'{sid}: NO COACH VOICE FOUND'); continue
    s_c, e_c = ctr[cidx[0]], ctr[cidx[-1]]
    # last prompter window before the coach starts / first one after the coach ends
    pb = [c for c, l in zip(ctr, lab) if l == 'P' and c < s_c]; pa = [c for c, l in zip(ctr, lab) if l == 'P' and c > e_c]
    def quietest(t0, t1):
        ts_ = np.arange(t0, t1, .01)
        return float(ts_[np.argmin([rms_db(f, t) for t in ts_])]) if len(ts_) else t0
    # start: quietest point between (prompter end) and the coach's first voiced onset; never earlier than the selected a minus 0.3
    st_lo = max(a - .3, (pb[-1] + .25) if pb else a - .3); st_hi = max(st_lo + .02, s_c - .25)
    new_a = quietest(st_lo, st_hi)
    en_hi = min(b + .3, (pa[0] - .25) if pa else b + .3); en_lo = min(en_hi - .02, e_c + .25)
    new_b = quietest(en_lo, en_hi) + .01
    # prompter windows INSIDE the kept span (overlap / interruptions) -> report for manual cut
    inner = [round(float(c), 2) for c, l in zip(ctr, lab) if l == 'P' and new_a + .3 < c < new_b - .3]
    trims[sid] = dict(file=f, a=round(new_a, 2), b=round(new_b, 2), old=[a, b], prompter_inside=inner)
    strip = ''.join(lab[(ctr >= new_a - .6) & (ctr <= new_b + .6)])
    rep.append(f'{sid} {f} {a:.2f}-{b:.2f} -> {new_a:.2f}-{new_b:.2f}  prompter-before@{pb[-1] if pb else None}  inner-P:{inner[:6]}  |{strip}|')
open(B + 'voice/report.txt', 'w').write('\n'.join(rep)); json.dump(trims, open(B + 'voice/trims.json', 'w'), indent=1)
print('\n'.join(rep))
