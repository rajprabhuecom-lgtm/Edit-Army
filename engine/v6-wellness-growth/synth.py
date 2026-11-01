"""Original procedural instrumental BGM + SFX (numpy). Everything here is generated from scratch,
so there is no third-party licence involved."""
import numpy as np
from scipy.signal import lfilter, butter, sosfilt

SR = 48000
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(d * SR)) / SR
def lp(x, fc, order=2):
    sos = butter(order, min(fc, SR/2-100) / (SR/2), 'low', output='sos'); return sosfilt(sos, x)
def hp(x, fc, order=2):
    sos = butter(order, fc / (SR/2), 'high', output='sos'); return sosfilt(sos, x)
def bp(x, lo, hi, order=2):
    sos = butter(order, [lo/(SR/2), hi/(SR/2)], 'band', output='sos'); return sosfilt(sos, x)
def env(n, a=0.005, d=0.2, s=0.0, r=0.05, hold=None):
    """simple exponential-ish AD(S)R envelope of n samples"""
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4))
    dec = np.exp(-(t - a).clip(0) / max(d, 1e-4))
    e = e * (s + (1 - s) * dec)
    rl = int(r * SR)
    if rl > 0 and n > rl: e[-rl:] *= np.linspace(1, 0, rl)
    return e
def midi(m): return 440.0 * 2 ** ((m - 69) / 12)
def add(buf, x, at):
    i = int(at * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(x)); buf[i:j] += x[:j - i]

# ---------------- instruments ----------------
def kick(d=0.35, f0=130, f1=42, amp=1.0):
    t = t_(d); f = f1 + (f0 - f1) * np.exp(-t / 0.045)
    ph = 2*np.pi*np.cumsum(f)/SR
    x = np.sin(ph) * np.exp(-t / 0.18)
    x += 0.25 * np.exp(-t/0.004) * rng.standard_normal(len(t))
    return np.tanh(1.6*x) * amp
def clap(d=0.25, amp=0.5):
    t = t_(d); n = rng.standard_normal(len(t))
    e = np.exp(-t/0.06)
    for k in (0.0, 0.011, 0.022): e += 0.6*np.exp(-np.maximum(t-k,0)/0.008)*(t>=k)
    return bp(n, 900, 5000) * e * amp * 0.5
def hat(d=0.06, amp=0.18, open_=False):
    t = t_(0.25 if open_ else d); n = rng.standard_normal(len(t))
    return hp(n, 7000, 4) * np.exp(-t/(0.09 if open_ else 0.018)) * amp
def shaker(amp=0.08):
    t = t_(0.09); n = rng.standard_normal(len(t))
    e = np.sin(np.pi*np.clip(t/0.09,0,1))**2
    return bp(n, 4000, 11000) * e * amp
def sub(m, d, amp=0.5):
    t = t_(d); x = np.sin(2*np.pi*midi(m)*t) + 0.15*np.sin(4*np.pi*midi(m)*t)
    return np.tanh(1.3*x) * env(len(t), 0.005, 9, 0.85, 0.06) * amp
def saw(f, t, det=0.0):
    return 2*((f*(1+det)*t) % 1) - 1
def pad(notes, d, amp=0.12, bright=1800, a=0.6):
    t = t_(d); x = np.zeros(len(t))
    for m in notes:
        for det in (-0.006, 0.0, 0.007):
            x += saw(midi(m), t, det)
    x = lp(x, bright) / (3*len(notes))
    return x * env(len(t), a, 99, 1.0, min(0.6, d/3)) * amp
def pluck(m, d=0.4, amp=0.22, bright=3200):
    t = t_(d); x = saw(midi(m), t) + 0.5*saw(midi(m+12), t, 0.003)
    x = lp(x * np.exp(-t/0.12), bright)
    return x * env(len(t), 0.002, 0.14, 0.0, 0.03) * amp
def piano(m, d=1.6, amp=0.22):
    t = t_(d); f = midi(m); x = np.zeros(len(t))
    for h, (g, dec) in enumerate([(1, 1.2), (0.55, 0.8), (0.3, 0.5), (0.18, 0.35), (0.1, 0.25), (0.06, 0.18)], 1):
        fh = f*h*np.sqrt(1+0.0004*h*h)
        x += g*np.sin(2*np.pi*fh*t)*np.exp(-t/dec)
    x *= env(len(t), 0.003, 99, 1.0, 0.12)
    return x * amp * 0.5
def bell(m, d=1.2, amp=0.12):
    t = t_(d); f = midi(m)
    mod = np.sin(2*np.pi*f*3.5*t) * 2.0*np.exp(-t/0.3)
    return np.sin(2*np.pi*f*t + mod) * np.exp(-t/0.45) * amp
def drone(m, d, amp=0.12):
    t = t_(d); x = np.zeros(len(t))
    for k, g in ((0, 1), (7, 0.5), (12, 0.35), (-12, 0.6)):
        x += g*saw(midi(m+k), t, 0.003*k)
    lfo = 500 + 300*np.sin(2*np.pi*0.15*t)
    y = lp(x, 700) * (0.8+0.2*np.sin(2*np.pi*0.2*t))
    return y * env(len(t), 1.2, 99, 1.0, 1.0) * amp / 2.5
def riser(d=2.0, amp=0.35):
    t = t_(d); n = rng.standard_normal(len(t))
    out = np.zeros(len(t)); seg = int(0.05*SR)
    for i in range(0, len(t), seg):
        fc = 400 + 9000*(i/len(t))**2
        out[i:i+seg] = bp(n[i:i+seg], fc*0.7, min(fc*1.3, 20000))
    f = 200 + 1400*(t/d)**2
    tone = 0.3*np.sin(2*np.pi*np.cumsum(f)/SR)
    return (out + tone) * (t/d)**1.6 * amp
def boom(amp=0.9):
    t = t_(1.6)
    f = 30 + 70*np.exp(-t/0.08)
    x = np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.5)
    n = lp(rng.standard_normal(len(t)), 3000)*np.exp(-t/0.35)*0.35
    return np.tanh(1.5*(x+n))*amp
def reverb(x, mix=0.25, decay=1.6):
    n = int(decay*SR); t = np.arange(n)/SR
    ir = rng.standard_normal(n)*np.exp(-t/(decay/5)); ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir**2))
    from scipy.signal import fftconvolve
    w = fftconvolve(x, ir)[:len(x)]
    return x*(1-mix) + w*mix

# ---------------- moods ----------------
# progressions (midi roots), A minor family and C/F major family
def render_mood(mood, dur, bpm):
    """render `dur` seconds of a mood at bpm (author tempo, pre-speed)."""
    b = 60.0/bpm; buf = np.zeros(int((dur+2)*SR)); nbeats = int(np.ceil(dur/b))+1
    if mood == 'pulse': # hook: dark trap-lite pulse
        prog = [57, 53, 55, 52] # Am F G Em (roots)
        chords = {57:[57,60,64],53:[53,57,60],55:[55,59,62],52:[52,55,59]}
        for bt in range(nbeats):
            t0 = bt*b; bar = bt//4; r = prog[bar % 4]
            if bt % 4 in (0,) or (bt % 8 == 6): add(buf, kick(), t0)
            if bt % 4 == 2: add(buf, clap(amp=0.35), t0)
            for k in range(2): add(buf, hat(amp=0.10 if k else 0.14), t0+k*b/2)
            if bt % 8 == 7: [add(buf, hat(amp=0.08), t0+b/2+k*b/8) for k in range(4)]
            if bt % 4 == 0:
                add(buf, sub(r-24, 4*b*0.95, 0.42), t0)
                add(buf, pad(chords[r], 4*b, 0.09, 1200), t0)
            if bt % 2 == 1: add(buf, bell(r+12+[0,3,7,10][bt%4], 0.8, 0.05), t0+b/2)
    elif mood == 'tech': # value stack: driving tech pulse
        prog = [57, 53, 48, 55]
        chords = {57:[57,60,64],53:[53,57,60],48:[48,52,55],55:[55,59,62]}
        for bt in range(nbeats):
            t0 = bt*b; bar = bt//4; r = prog[bar % 4]; ch = chords[r]
            add(buf, kick(amp=0.9), t0)
            if bt % 2 == 1: add(buf, clap(amp=0.32), t0)
            add(buf, hat(amp=0.11, open_=True), t0+b/2)
            for k in range(4):
                add(buf, pluck(ch[(bt*4+k) % 3]+12, 0.3, 0.13), t0+k*b/4)
            add(buf, sub(r-24, b/2*0.9, 0.38), t0+b/2)
            if bt % 4 == 0: add(buf, pad(ch, 4*b, 0.06, 2200, 0.3), t0)
    elif mood == 'warm': # trust / proof / guarantee: warm piano + shaker
        prog = [48, 55, 57, 53] # C G Am F
        chords = {48:[60,64,67],55:[59,62,67],57:[60,64,69],53:[60,65,69]}
        for bt in range(nbeats):
            t0 = bt*b; bar = bt//4; r = prog[bar % 4]; ch = chords[r]
            if bt % 4 == 0:
                add(buf, piano(r-12, 4*b, 0.32), t0)
                for i, m in enumerate(ch): add(buf, piano(m, 4*b, 0.16), t0+0.012*i)
            add(buf, kick(amp=0.45, f0=90, f1=40), t0)
            if bt % 4 == 2: add(buf, kick(amp=0.3, f0=90, f1=40), t0)
            add(buf, shaker(0.06), t0+b/2); add(buf, shaker(0.035), t0)
            if bt % 2 == 1: add(buf, piano(ch[(bt//2) % 3]+12, 1.2, 0.08), t0+b/2)
        buf = reverb(buf, 0.22, 1.8)
    elif mood == 'dark': # cost / pain: drone + low minor piano
        add(buf, drone(45, dur+1, 0.22), 0)
        for bt in range(0, nbeats, 4):
            t0 = bt*b; m = [57, 53, 52, 57][(bt//4) % 4]
            add(buf, piano(m-12, 4*b, 0.25), t0); add(buf, piano(m, 4*b, 0.1), t0+0.02)
            add(buf, kick(amp=0.35, f0=70, f1=35), t0)
        buf = reverb(buf, 0.35, 2.4)
    elif mood == 'uplift': # CTA: uplifting four-on-floor
        prog = [53, 48, 55, 57] # F C G Am
        chords = {53:[65,69,72],48:[64,67,72],55:[62,67,71],57:[64,69,72]}
        for bt in range(nbeats):
            t0 = bt*b; bar = bt//4; r = prog[bar % 4]; ch = chords[r]
            add(buf, kick(amp=0.95), t0)
            if bt % 2 == 1: add(buf, clap(amp=0.38), t0)
            add(buf, hat(amp=0.12, open_=True), t0+b/2)
            add(buf, hat(amp=0.06), t0+b/4); add(buf, hat(amp=0.06), t0+3*b/4)
            add(buf, sub(r-24, b/2*0.9, 0.36), t0+b/2)
            if bt % 4 == 0: add(buf, pad(ch, 4*b, 0.11, 3200, 0.05), t0)
            add(buf, pluck(ch[bt % 3]+12, 0.25, 0.08, 4500), t0)
            add(buf, pluck(ch[(bt+1) % 3]+12, 0.25, 0.06, 4500), t0+b/2)
        buf = reverb(buf, 0.15, 1.2)
    return buf[:int(dur*SR)]

def build_bgm(cues, total, bpm_map):
    """cues: list of (start, end, mood). Crossfade 0.45 s between moods. Returns mono float."""
    out = np.zeros(int((total+1)*SR)); xf = 0.45
    for i, (s, e, mood) in enumerate(cues):
        if mood == 'silence': continue
        s0 = max(0, s - (xf/2 if i else 0)); e0 = e + xf/2
        seg = render_mood(mood, e0 - s0, bpm_map[mood])
        n = len(seg); w = np.ones(n); f = int(xf*SR)
        if i: w[:f] = np.linspace(0, 1, f)
        prev_hit = False
        w[-f:] = np.minimum(w[-f:], np.linspace(1, 0, f))
        add(out, seg*w, s0)
    return out[:int(total*SR)]

# ---------------- SFX ----------------
def sfx(name):
    if name == 'pop':
        t = t_(0.09); f = 900 - 500*t/0.09
        return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.025)*0.5
    if name == 'tick':
        t = t_(0.05); return (np.sin(2*np.pi*2400*t)+0.5*np.sin(2*np.pi*3700*t))*np.exp(-t/0.008)*0.35
    if name == 'whoosh':
        t = t_(0.45); n = rng.standard_normal(len(t)); out = np.zeros(len(t)); seg = 1200
        for i in range(0, len(t), seg):
            fc = 600 + 5000*np.sin(np.pi*i/len(t)); out[i:i+seg] = bp(n[i:i+seg], fc*0.6, fc*1.4)
        return out*np.sin(np.pi*t/0.45)**2*0.35
    if name == 'cash':
        x = np.zeros(int(0.9*SR))
        add(x, sfx('tick')*1.2, 0); add(x, sfx('tick'), 0.05)
        for m, at in ((88, 0.09), (93, 0.13), (96, 0.17)): add(x, bell(m, 0.7, 0.22), at)
        return x
    if name == 'thud':
        return boom(0.75)[:int(0.9*SR)]
    if name == 'hit':
        return reverb(boom(0.95), 0.3, 1.5)
    if name == 'riser':
        return riser(1.6, 0.3)
    if name == 'ding':
        return bell(84, 1.0, 0.25) + bell(91, 1.0, 0.12)
    if name == 'swipe':
        return sfx('whoosh')[:int(0.3*SR)]*0.8
    raise KeyError(name)
