"""VSL audio: voice from timeline pieces (jump-cut speaker segments + testimonial bites), voice chain, SFX, original BGM ducked by voice.
python3 mix.py <workdir>   (reads audio/cues.json from plan.py, src48.wav, broll/<bite clips>)"""
import json, subprocess, re, sys, numpy as np, soundfile as sf
sys.path.insert(0, '/home/user/Edit-Army/engine/base/audio')
from synth import build_bgm, sfx, SR, add
W = sys.argv[1].rstrip('/') + '/'; D = W + 'audio/'
cues = json.load(open(D + 'cues.json')); total = cues['total']
run = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)
a, _ = sf.read(W + 'src48.wav', dtype='float32')
xf = int(0.006 * SR); out = np.zeros(int((total + 1) * SR), np.float32)
for p in cues['pieces']:
    if p['k'] == 'seg': seg = a[int(round(p['s0'] * SR)):int(round(p['s1'] * SR))].copy()
    else:
        run(f'ffmpeg -nostdin -v error -y -i {W}broll/{p["clip"]} -vn -ac 1 -ar {SR} {D}bite.wav'); seg, _ = sf.read(D + 'bite.wav', dtype='float32')
        seg = seg[:int(p['dur'] * SR)] * 1.0
        f = int(0.04 * SR); seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
    seg[:xf] *= np.linspace(0, 1, xf); seg[-xf:] *= np.linspace(1, 0, xf)
    i0 = int(round(p['o0'] * SR)); out[i0:i0 + len(seg)] += seg[:len(out) - i0]
sf.write(D + 'voice_cut.wav', out[:int(total * SR)], SR)
chain = 'highpass=f=80,acompressor=threshold=0.1:ratio=3:attack=10:release=120:makeup=2,deesser=i=0.4,equalizer=f=4000:t=q:w=1.2:g=2.5'
r = subprocess.run(f'ffmpeg -y -i {D}voice_cut.wav -af "{chain},loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null -', shell=True, capture_output=True, text=True).stderr
m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
ln = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
run(f'ffmpeg -v error -y -i {D}voice_cut.wav -af "{chain},{ln}" -ar {SR} {D}voice.wav')
fx = np.zeros(int((total + 2) * SR))
lvl = {'hit': 0.5, 'cash': 0.5, 'thud': 0.55, 'riser': 0.4, 'whoosh': 0.3, 'swipe': 0.25, 'pop': 0.3, 'ding': 0.3, 'tick': 0.3}
for t, n in cues['sfx']: add(fx, sfx(n) * lvl[n], max(0, t - (1.55 if n == 'riser' else 0)))
sf.write(D + 'sfx.wav', fx[:int(total * SR)].astype(np.float32), SR)
bpm = {'pulse': 104 / 1.2, 'tech': 118 / 1.2, 'warm': 92 / 1.2, 'dark': 80 / 1.2, 'uplift': 124 / 1.2}
bg = build_bgm([tuple(c) for c in cues['music']], total, bpm); bg = bg / (np.max(np.abs(bg)) + 1e-9) * 0.7
sf.write(D + 'bgm_raw.wav', bg.astype(np.float32), SR)
r = subprocess.run(f'ffmpeg -i {D}bgm_raw.wav -af ebur128 -f null -', shell=True, capture_output=True, text=True).stderr
g = -33 - float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1])
fc = (f'[1:a]highpass=f=60,equalizer=f=2800:t=q:w=1.5:g=-4,volume={g:.2f}dB[m];'
      f'[0:a]asplit=2[v][vk];[m][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[md];'
      f'[2:a]volume=-3dB[fx];[v][md][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.84:level=false[o]')
run(f'ffmpeg -v error -y -i {D}voice.wav -i {D}bgm_raw.wav -i {D}sfx.wav -filter_complex "{fc}" -map "[o]" -ar {SR} -ac 2 {D}mix.wav')
print('mix ok, BGM gain', round(g, 1))
