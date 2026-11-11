import json, subprocess, numpy as np, soundfile as sf, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carnatic import build_bgm, sfx, SR, add
WD = os.environ.get('W', '/home/user/w').rstrip('/')
D = WD + '/audio/'
cues = json.load(open(D + 'cues.json')); total = cues['total']
run = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)
# 1. voice: jump cuts with 6 ms crossfades
run(f'ffmpeg -v error -y -i {WD}/src.mkv -vn -ac 1 -ar {SR} {D}src48.wav')
a, _ = sf.read(D + 'src48.wav', dtype='float32')
xf = int(0.006 * SR); out = np.zeros(int((total + 1) * SR), np.float32); pos = 0
for s, e in cues['keep']:
    seg = a[int(s * SR):int(e * SR)].copy()
    seg[:xf] *= np.linspace(0, 1, xf); seg[-xf:] *= np.linspace(1, 0, xf)
    out[pos:pos + len(seg)] += seg; pos += len(seg)
sf.write(D + 'voice_cut.wav', out[:int(total * SR)], SR)
# 2. voice chain + two-pass loudnorm
chain = 'afftdn=nr=10:nf=-40,highpass=f=80,acompressor=threshold=0.1:ratio=3:attack=10:release=120:makeup=2,deesser=i=0.4,equalizer=f=4000:t=q:w=1.2:g=2.5'
r = subprocess.run(f'ffmpeg -y -i {D}voice_cut.wav -af "{chain},loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json" -f null -', shell=True, capture_output=True, text=True).stderr
m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
ln = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
run(f'ffmpeg -v error -y -i {D}voice_cut.wav -af "{chain},{ln}" -ar {SR} {D}voice.wav')
# 3. SFX bus
fx = np.zeros(int((total + 2) * SR))
lvl = {'hit': 0.45, 'thud': 0.5, 'riser': 0.35, 'whoosh': 0.28, 'pop': 0.28, 'tick': 0.25, 'shimmer': 0.6, 'bell': 0.45}
for t, n in cues['sfx']: add(fx, sfx(n) * lvl[n], max(0, t - (1.55 if n == 'riser' else 0)))
sf.write(D + 'sfx.wav', fx[:int(total * SR)].astype(np.float32), SR)
# 4. BGM: author tempo = target / 1.2 (whole mix is sped up 1.2x afterwards)
bg = build_bgm([tuple(c) for c in cues['music']], total, 96 / 1.2)
bg = bg / (np.max(np.abs(bg)) + 1e-9) * 0.7
sf.write(D + 'bgm_raw.wav', bg.astype(np.float32), SR)
# loudness of BGM alone -> set to about -33 LUFS (19 dB under the voice) before ducking
r = subprocess.run(f'ffmpeg -i {D}bgm_raw.wav -af ebur128 -f null -', shell=True, capture_output=True, text=True).stderr
bi = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1]); g = -31 - bi
# 5. mix: EQ'd BGM sidechain-ducked by voice, + SFX, limiter
fc = (f'[1:a]highpass=f=60,equalizer=f=2800:t=q:w=1.5:g=-4,volume={g:.2f}dB[m];'
      f'[0:a]asplit=2[v][vk];[m][vk]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[md];'
      f'[2:a]volume=-3dB[fx];[v][md][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.84:level=false[o]')
run(f'ffmpeg -v error -y -i {D}voice.wav -i {D}bgm_raw.wav -i {D}sfx.wav -filter_complex "{fc}" -map "[o]" -ar {SR} -ac 2 {D}mix.wav')
r = subprocess.run(f'ffmpeg -i {D}mix.wav -af ebur128=peak=true -f null -', shell=True, capture_output=True, text=True).stderr
print('BGM gain', round(g, 1), r[r.rfind('Summary'):])
