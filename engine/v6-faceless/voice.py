"""Studio voice for faceless ads: jump-cut pauses from Whisper word timings, denoise, studio EQ/compression, de-ess, speed.
python3 voice.py <raw48.wav> <whisper.json> <out.wav> [--speed 1.2] [--drop "word,word"] [--gap 0.30]"""
import json, sys, argparse, subprocess, numpy as np, soundfile as sf, noisereduce as nr
ap = argparse.ArgumentParser(); ap.add_argument('raw'); ap.add_argument('js'); ap.add_argument('out')
ap.add_argument('--speed', type=float, default=1.2); ap.add_argument('--drop', default=''); ap.add_argument('--gap', type=float, default=0.30)
ap.add_argument('--spans-out', default=''); ap.add_argument('--pre', type=float, default=0.07); ap.add_argument('--post', type=float, default=0.14)
a = ap.parse_args()
x, SR = sf.read(a.raw, dtype='float32')
words = [w for s in json.load(open(a.js)) for w in s['words']]
drop = [d.strip().lower() for d in a.drop.split(',') if d.strip()]
words = [w for w in words if w[0].strip().strip('.,!?').lower() not in drop]
# keep spans: merge words whose gap < a.gap
spans = []
for w, s, e in words:
    s, e = max(0, s - a.pre), e + a.post
    if spans and s - spans[-1][1] < a.gap: spans[-1][1] = max(spans[-1][1], e)
    else: spans.append([s, e])
if a.spans_out: json.dump(spans, open(a.spans_out, 'w'))
# leave a natural 0.12 s breath between kept phrases
xf = int(0.008 * SR); brk = np.zeros(int(0.12 * SR), np.float32); parts = []
for s, e in spans:
    seg = x[int(s * SR):int(e * SR)].copy(); seg[:xf] *= np.linspace(0, 1, xf); seg[-xf:] *= np.linspace(1, 0, xf); parts += [seg, brk]
y = np.concatenate(parts)
# denoise using the quietest 0.5 s of the raw file as the noise profile
win = int(0.5 * SR); rms = [np.sqrt(np.mean(x[i:i + win] ** 2)) for i in range(0, len(x) - win, win // 2)]
i0 = int(np.argmin(rms)) * (win // 2); noise = x[i0:i0 + win]
y = nr.reduce_noise(y=y, sr=SR, y_noise=noise, stationary=True, prop_decrease=0.75, n_fft=2048)
tmp = a.out + '.pre.wav'; sf.write(tmp, y, SR)
chain = ','.join([
  'highpass=f=80:p=2', 'equalizer=f=220:t=q:w=1.0:g=-3',          # cut mud / room boom
  'equalizer=f=120:t=q:w=0.8:g=1.5',                               # warmth / chest
  'equalizer=f=3200:t=q:w=1.3:g=3', 'treble=g=2.5:f=9000',          # presence + air
  'deesser=i=0.5:m=0.5:f=0.5',
  'acompressor=threshold=0.08:ratio=3.5:attack=6:release=90:makeup=2.5:knee=4',   # broadcast compression
  'acompressor=threshold=0.25:ratio=2:attack=20:release=250:makeup=1',             # leveller
  f'atempo={a.speed}', 'alimiter=limit=0.9:level=false'])
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af', chain, '-ar', '48000', a.out], check=True)
d = sf.info(a.out).duration
print(f'raw {len(x)/SR:.1f}s -> cut {len(y)/SR:.1f}s -> x{a.speed} {d:.1f}s, {len(spans)} phrases')
