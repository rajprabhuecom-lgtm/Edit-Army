"""Audio for v6 (licensed / supplied BGM, mixed AFTER the 1.2x speed-up so the music keeps its own tempo and pitch).

  python3 mix.py voice   -> audio/mix.wav  (1x: jump-cut voice + SFX, used by comp.py)
  python3 mix.py music   -> audio/final_mix.wav (final time: voice+SFX at 1.2x + BGM, voice-keyed ducking, -14 LUFS)

BGM rules (Prabhuraj, 10 Nov 2026):
  * the voice is always on top; the music carries the hype underneath
  * the music dips just BEFORE each word (look-ahead) and swells back in the gaps and under the end card
  * rises in the track are levelled (slow compressor) so they never step over the voice
  * the voice band (1-4 kHz) is carved out of the music so words stay clear even at bed level
"""
import json, re, subprocess, sys, numpy as np, soundfile as sf
sys.path.insert(0, '/home/user/w/audio')
from synth import sfx, SR, add
D = '/home/user/w/audio/'
run = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True, text=True)
def lufs(p):
    r = subprocess.run(f'ffmpeg -i {p} -af ebur128 -f null -', shell=True, capture_output=True, text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r)[-1])

# ---- BGM edit (seconds in the original track) ----
BGM = D + 'bgm_full.wav'
START = 10.19            # "start from 10 seconds": first downbeat after 10 s
LOOP_OUT, LOOP_IN = 58.770, 32.578   # 48-beat jump back (beat-matched, 0.976 chroma/MFCC similarity) to stretch 60 s of music to the edit
BED_LUFS = -16.5         # music level when nobody is speaking (gaps, end card)
DUCK_DB = 7.0            # extra dip under speech -> about 12-13 dB under the voice
MARGIN = 10.0            # never let the music get closer than this to the voice while he speaks (rise guard)
LOOK = 0.06              # dip starts 60 ms before a word
ATT, REL = 0.05, 0.35    # duck attack / release (s)

def voice_stage():
    cues = json.load(open(D + 'cues.json')); total = cues['total']
    run(f'ffmpeg -v error -y -i /home/user/w/src.mkv -vn -ac 1 -ar {SR} {D}src48.wav')
    a, _ = sf.read(D + 'src48.wav', dtype='float32')
    xf = int(0.006 * SR); out = np.zeros(int((total + 1) * SR), np.float32); pos = 0
    for s, e in cues['keep']:
        seg = a[int(s * SR):int(e * SR)].copy(); n = int((e - s) * SR)
        if len(seg) > 2 * xf: seg[:xf] *= np.linspace(0, 1, xf); seg[-xf:] *= np.linspace(1, 0, xf)
        out[pos:pos + len(seg)] += seg; pos += n          # hold segment past the source end stays silent
    sf.write(D + 'voice_cut.wav', out[:int(total * SR)], SR)
    chain = ('highpass=f=85,afftdn=nf=-30:nr=10,acompressor=threshold=0.08:ratio=3:attack=8:release=120:makeup=2,'
             'deesser=i=0.4,equalizer=f=220:t=q:w=1:g=-1.5,equalizer=f=4000:t=q:w=1.2:g=3')
    r = subprocess.run(f'ffmpeg -y -i {D}voice_cut.wav -af "{chain},loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json" -f null -', shell=True, capture_output=True, text=True).stderr
    m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    run(f'ffmpeg -v error -y -i {D}voice_cut.wav -af "{chain},{ln}" -ar {SR} -ac 1 {D}voice.wav')
    fx = np.zeros(int((total + 3) * SR))
    lvl = {'hit': 0.5, 'cash': 0.45, 'thud': 0.5, 'riser': 0.35, 'whoosh': 0.3, 'swipe': 0.25, 'pop': 0.28, 'ding': 0.28, 'tick': 0.25, 'click': 0.25}
    for t, n in cues['sfx']:
        n = {'click': 'tick', 'riser_s': 'swipe'}.get(n, n)
        add(fx, sfx(n) * lvl[n], max(0, t - (1.55 if n == 'riser' else 0)))
    sf.write(D + 'sfx.wav', fx[:int(total * SR)].astype(np.float32), SR)
    run(f'ffmpeg -v error -y -i {D}voice.wav -i {D}sfx.wav -filter_complex "[1:a]volume=-4dB[f];[0:a][f]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=false" -ar {SR} -ac 2 {D}mix.wav')
    print('voice + sfx ->', D + 'mix.wav')

def smooth_gain(target_db, att, rel):
    """one-pole attack/release smoothing of a per-sample gain curve (dB); attack = getting quieter"""
    g = np.empty_like(target_db); a_c = np.exp(-1 / (att * SR)); r_c = np.exp(-1 / (rel * SR)); cur = 0.0
    for i, x in enumerate(target_db):
        c = a_c if x < cur else r_c
        cur = c * cur + (1 - c) * x; g[i] = cur
    return g

def music_stage(dur):
    # 1. cut the BGM: START -> LOOP_OUT, then LOOP_IN -> end, 50 ms equal-power crossfade on the beat
    b, sr0 = sf.read(BGM, dtype='float32'); assert sr0 == SR
    s1 = b[int(START * SR):int(LOOP_OUT * SR)]; s2 = b[int(LOOP_IN * SR):]
    xf = int(0.05 * SR); t = np.linspace(0, np.pi / 2, xf)[:, None]
    mus = np.concatenate([s1[:-xf], s1[-xf:] * np.cos(t) + s2[:xf] * np.sin(t), s2[xf:]])
    n = int(dur * SR)
    mus = np.pad(mus, ((0, max(0, n - len(mus))), (0, 0)))[:n]
    mus[:int(.03 * SR)] *= np.linspace(0, 1, int(.03 * SR))[:, None]
    fo = int(2.2 * SR); mus[-fo:] *= np.linspace(1, 0, fo)[:, None] ** 1.5      # ride out under the end card
    sf.write(D + 'bgm_cut.wav', mus, SR)
    # 2. level the rises + carve the voice band, then set the bed level
    eq = ('highpass=f=45,acompressor=threshold=0.12:ratio=3.5:attack=40:release=500:makeup=1,'
          'equalizer=f=350:t=q:w=1:g=-2,equalizer=f=1200:t=q:w=1.2:g=-3,equalizer=f=2800:t=q:w=1.3:g=-5,equalizer=f=5000:t=q:w=1:g=-2')
    run(f'ffmpeg -v error -y -i {D}bgm_cut.wav -af "{eq}" -ar {SR} {D}bgm_eq.wav')
    g = BED_LUFS - lufs(D + 'bgm_eq.wav')
    mus, _ = sf.read(D + 'bgm_eq.wav', dtype='float32'); mus *= 10 ** (g / 20)
    # 3. voice-keyed ducking with look-ahead (voice at final speed)
    v, _ = sf.read(D + 'voice12.wav', dtype='float32'); v = v if v.ndim == 1 else v.mean(1)
    v = np.pad(v, (0, max(0, n - len(v))))[:n]
    hop = int(0.01 * SR); fr = len(v) // hop
    rms = np.sqrt(np.mean(v[:fr * hop].reshape(fr, hop) ** 2, 1) + 1e-12); db = 20 * np.log10(rms)
    act = db > -42                                               # speech (voice sits at -14 LUFS)
    k = int(0.12 / 0.01)                                         # bridge micro-gaps < 120 ms so the music doesn't pump between syllables
    act = np.convolve(act.astype(float), np.ones(k), 'same') > 0
    shift = int(LOOK / 0.01); act = np.concatenate([act[shift:], np.zeros(shift, bool)])   # look-ahead
    tgt = np.repeat(np.where(act, -DUCK_DB, 0.0), hop); tgt = np.pad(tgt, (0, n - len(tgt)), constant_values=0.0)
    gdb = smooth_gain(tgt, ATT, REL)
    mus *= (10 ** (gdb / 20))[:, None]
    # 3b. rise guard: wherever a swell in the track gets within MARGIN dB of the voice, pull it down (300 ms windows, 50 ms hop)
    w, h = int(0.3 * SR), int(0.05 * SR); mm = mus.mean(1); extra = np.zeros(n)
    for i in range(0, n - w, h):
        if not act[min(len(act) - 1, i // hop)]: continue
        vl = 10 * np.log10(np.mean(v[i:i + w] ** 2) + 1e-12); ml = 10 * np.log10(np.mean(mm[i:i + w] ** 2) + 1e-12)
        if vl > -32: extra[i:i + w] = np.minimum(extra[i:i + w], max(-6.0, min(0.0, (vl - ml) - MARGIN)))   # capped so it never pumps
    gx = smooth_gain(extra, 0.03, 0.25); mus *= (10 ** (gx / 20))[:, None]
    print(f'rise guard active on {np.mean(extra < -0.5) * 100:.0f}% of samples, max cut {extra.min():.1f} dB')
    sf.write(D + 'bgm_ducked.wav', mus, SR)
    # 4. sum with voice+SFX, limit, two-pass loudnorm to -14 LUFS / -1.5 dBTP
    run(f'ffmpeg -v error -y -i {D}a12.wav -i {D}bgm_ducked.wav -filter_complex "[0:a][1:a]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=false" -ar {SR} {D}sum.wav')
    r = subprocess.run(f'ffmpeg -i {D}sum.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -', shell=True, capture_output=True, text=True).stderr
    m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    run(f'ffmpeg -v error -y -i {D}sum.wav -af "{ln}" -ar {SR} {D}final_mix.wav')
    sp = act.mean() * 100
    print(f'BGM gain {g:+.1f} dB | bed {BED_LUFS} LUFS, -{DUCK_DB} dB under speech ({sp:.0f}% of runtime) | final mix ->', D + 'final_mix.wav')

if __name__ == '__main__':
    if sys.argv[1] == 'voice': voice_stage()
    else: music_stage(float(sys.argv[2]))
