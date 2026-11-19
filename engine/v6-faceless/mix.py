"""Mix: studio voice (already processed + sped) + original synth BGM (emotion cues) sidechain-ducked + SFX -> -14 LUFS. python3 mix.py <workdir>"""
import json, sys, subprocess, re, numpy as np, soundfile as sf
sys.path.insert(0, '/home/user/Edit-Army/engine/base/audio')
from synth import build_bgm, sfx, SR, add
WD = sys.argv[1]; TL = json.load(open(WD + '/timeline.json')); total = TL['total']
run = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)
v, _ = sf.read(WD + '/voice.wav', dtype='float32'); voice = np.zeros(int(total * SR), np.float32)
o = int(TL.get('voice_at', 0) * SR); voice[o:o + len(v)] = v[:len(voice) - o]; sf.write(WD + '/voice_pl.wav', voice, SR)
fx = np.zeros(int((total + 2) * SR)); lvl = {'hit': .5, 'cash': .45, 'thud': .55, 'riser': .4, 'whoosh': .32, 'swipe': .25, 'pop': .3, 'ding': .28, 'tick': .28}
for t, n in TL['sfx']: add(fx, sfx(n) * lvl[n], max(0, t - (1.55 if n == 'riser' else 0)))
sf.write(WD + '/sfx.wav', fx[:int(total * SR)].astype(np.float32), SR)
bpm = {'pulse': 100, 'tech': 116, 'warm': 92, 'dark': 78, 'uplift': 122}
bg = build_bgm([tuple(c) for c in TL['music']], total, bpm); bg = bg / (np.max(np.abs(bg)) + 1e-9) * .7
sf.write(WD + '/bgm.wav', bg.astype(np.float32), SR)
r = subprocess.run(f'ffmpeg -i {WD}/bgm.wav -af ebur128 -f null -', shell=True, capture_output=True, text=True).stderr
g = -31 - float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1])
fc = (f'[1:a]highpass=f=60,equalizer=f=2800:t=q:w=1.5:g=-4,volume={g:.2f}dB[m];[0:a]asplit=2[v][vk];'
      f'[m][vk]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];[2:a]volume=-2dB[fx];'
      f'[v][md][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.84:level=false[o]')
run(f'ffmpeg -v error -y -i {WD}/voice_pl.wav -i {WD}/bgm.wav -i {WD}/sfx.wav -filter_complex "{fc}" -map "[o]" -ar {SR} -ac 2 {WD}/mix_raw.wav')
r = subprocess.run(f'ffmpeg -i {WD}/mix_raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -', shell=True, capture_output=True, text=True).stderr
m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
ln = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
run(f'ffmpeg -v error -y -i {WD}/mix_raw.wav -af "{ln}" -ar {SR} {WD}/mix.wav')
r = subprocess.run(f'ffmpeg -i {WD}/mix.wav -af ebur128=peak=true -f null -', shell=True, capture_output=True, text=True).stderr
print('BGM gain', round(g, 1), re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1], 'LUFS, peak', re.findall(r'Peak:\s+(-?[\d.]+)', r)[-1])
