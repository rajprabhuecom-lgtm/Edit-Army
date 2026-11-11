"""Original Carnatic-fusion BGM for Lakshmi Rising (raga Mohanam, Sa = D). Generated from scratch with numpy,
so there is no third-party licence. Instruments: tanpura, veena (plucked, with gamaka slides), bansuri, mridangam,
strings, piano, temple bell. Moods follow the ad's arc: intro -> lift -> groove -> break -> rise -> finale."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'base', 'audio'))
from synth import SR, t_, lp, hp, bp, env, midi, add, pad, piano, sub, shaker, reverb, riser, boom, sfx as base_sfx
rng = np.random.default_rng(11)
SA = 62                                    # D
MOH = [0, 2, 4, 7, 9]                      # S R2 G3 P D2
def deg(i):                                # scale degree index -> midi (wraps octaves)
    o, k = divmod(i, 5); return SA + 12 * o + MOH[k]

def tanpura(d, amp=0.10):
    """four-string cycle P S S S(low), rich buzzing partials, slow swells"""
    out = np.zeros(int((d + 3) * SR)); cyc = 2.4; notes = [SA - 5, SA, SA, SA - 12]
    k = 0; t0 = 0.0
    while t0 < d + 1:
        m = notes[k % 4]; dur = 3.0; t = t_(dur); f = midi(m); x = np.zeros(len(t))
        for h in range(1, 14):
            x += (1 / h ** 0.9) * np.sin(2 * np.pi * f * h * t * (1 + 0.0003 * h)) * (0.6 + 0.4 * np.sin(2 * np.pi * (0.7 + 0.13 * h) * t + h))
        x = lp(x, 3200) * env(len(t), 0.03, 1.6, 0.25, 0.6)
        add(out, x * amp, t0); t0 += cyc / 4; k += 1
    return out[:int(d * SR)]

def veena(m, d=0.9, amp=0.20, slide=0.0):
    t = t_(d); f = midi(m) * 2 ** ((-slide * np.exp(-t / 0.06)) / 12)
    ph = 2 * np.pi * np.cumsum(f) / SR; x = np.zeros(len(t))
    for h, g in ((1, 1), (2, .55), (3, .35), (4, .22), (5, .14), (6, .08)):
        x += g * np.sin(h * ph) * np.exp(-t * (2.2 + h * 1.4))
    x += 0.15 * np.exp(-t / 0.004) * rng.standard_normal(len(t))
    return lp(x, 4200) * env(len(t), 0.002, 99, 1, 0.05) * amp

def bansuri(m, d=1.0, amp=0.12, slide=1.0):
    t = t_(d); vib = 1 + 0.004 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.25) / 0.3, 0, 1)
    f = midi(m) * vib * 2 ** ((-slide * np.exp(-t / 0.07)) / 12); ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    br = bp(rng.standard_normal(len(t)), midi(m) * 0.9, midi(m) * 3.5) * 0.10
    return (x + br) * env(len(t), 0.08, 99, 1, min(0.25, d / 3)) * amp

def mridangam(kind, amp=0.5):
    if kind == 'thom':                     # low bass head
        t = t_(0.45); f = 70 + 45 * np.exp(-t / 0.05)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16) * amp
    if kind == 'tha':                      # dry slap
        t = t_(0.12); return bp(rng.standard_normal(len(t)), 700, 4000) * np.exp(-t / 0.018) * amp * 0.8
    if kind == 'ki':
        t = t_(0.08); return bp(rng.standard_normal(len(t)), 1500, 6000) * np.exp(-t / 0.01) * amp * 0.45
    if kind == 'nam':                      # ringing treble head
        t = t_(0.6); f = midi(SA + 12)
        x = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 2.01 * t) * np.exp(-t / 0.1) + 0.3 * np.sin(2 * np.pi * f * 2.98 * t) * np.exp(-t / 0.06)
        return (x * np.exp(-t / 0.22) + bp(rng.standard_normal(len(t)), 2000, 7000) * np.exp(-t / 0.006) * 0.4) * amp * 0.5
    raise KeyError(kind)

def tbell(amp=0.35, d=3.0):
    """temple bell: inharmonic partials, long decay, slow beating"""
    t = t_(d); f = 520; x = np.zeros(len(t))
    for r, g, dec in ((1, 1, 1.6), (2.76, .5, .9), (5.40, .3, .5), (8.93, .15, .3), (1.5, .3, 1.2)):
        x += g * np.sin(2 * np.pi * f * r * t) * np.exp(-t / dec) * (1 + 0.15 * np.sin(2 * np.pi * 3.1 * t))
    return x * amp * 0.5

CH = {'I': [62, 66, 69], 'vi': [59, 62, 66], 'IV': [55, 59, 62], 'V': [57, 61, 64]}
PROG = ['I', 'vi', 'IV', 'V']
ROOT = {'I': 50, 'vi': 47, 'IV': 43, 'V': 45}
# melodies: (beat offset in a 2-bar phrase, scale degree index, length beats, slide)
RIFF = [(0, 5, .5, 1), (.5, 7, .5, 0), (1, 8, 1, 1), (2, 7, .5, 0), (2.5, 6, .5, 0), (3, 5, 1, 1), (4, 6, .5, 0), (4.5, 7, .5, 0),
        (5, 9, 1, 2), (6, 8, .5, 0), (6.5, 7, .5, 0), (7, 6, 1, 1)]
FLUTE_SAD = [(0, 7, 2.5), (3, 6, 1), (4, 5, 3.5)]
FLUTE_UP = [(0, 8, 1.5), (1.5, 9, .5), (2, 10, 2), (4, 9, 1), (5, 8, 1), (6, 7, 2)]

def render_mood(mood, dur, bpm):
    b = 60.0 / bpm; buf = np.zeros(int((dur + 3) * SR)); nb = int(np.ceil(dur / b)) + 1; bars = nb // 4 + 1
    def chords(level, bright):
        for br in range(bars):
            c = PROG[br % 4]; t0 = br * 4 * b
            add(buf, pad(CH[c], 4 * b, level, bright, 0.5), t0)
    def drums(dense):
        pat = ['thom', 'ki', 'tha', 'ki', 'nam', 'ki', 'tha', 'ki'] if dense else ['thom', None, 'tha', None, 'nam', None, 'tha', None]
        for i in range(nb * 2):
            k = pat[i % 8]
            if k: add(buf, mridangam(k, 0.55 if k == 'thom' else 0.45), i * b / 2)
            if dense and i % 2: add(buf, shaker(0.035), i * b / 2)
    def bass():
        for br in range(bars): add(buf, sub(ROOT[PROG[br % 4]] - 12, 4 * b * .95, 0.30), br * 4 * b)
    def riff(level, oct_=0):
        for ph in range(0, nb, 8):
            for off, dg, ln, sl in RIFF: add(buf, veena(deg(dg) + oct_, ln * b * 1.6, level, sl), (ph + off) * b)
    def flute(phr, level, every=8):
        for ph in range(0, nb, every):
            for off, dg, ln in phr: add(buf, bansuri(deg(dg), ln * b, level), (ph + off) * b)
    if mood == 'intro':
        add(buf, tanpura(dur + 1, 0.09), 0); chords(0.05, 900); flute(FLUTE_SAD, 0.10, 8)
        buf = reverb(buf, 0.35, 2.6)
    elif mood == 'lift':
        add(buf, tanpura(dur + 1, 0.07), 0); chords(0.07, 1500); drums(False); bass(); riff(0.13)
        buf = reverb(buf, 0.25, 2.0)
    elif mood == 'groove':
        add(buf, tanpura(dur + 1, 0.05), 0); chords(0.06, 2000); drums(True); bass(); riff(0.15); flute(FLUTE_UP, 0.07, 16)
        buf = reverb(buf, 0.18, 1.6)
    elif mood == 'break':
        add(buf, tanpura(dur + 1, 0.09), 0)
        for br in range(bars):
            c = CH[PROG[br % 4]]; t0 = br * 4 * b; add(buf, piano(c[0] - 12, 4 * b, 0.22), t0)
            for i, m in enumerate(c): add(buf, piano(m, 4 * b, 0.10), t0 + 0.02 * i)
        flute(FLUTE_SAD, 0.08, 8); buf = reverb(buf, 0.35, 2.6)
    elif mood == 'rise':
        add(buf, tanpura(dur + 1, 0.05), 0); chords(0.07, 2400); drums(True); bass(); riff(0.15)
        for br in range(bars): add(buf, mridangam('thom', 0.5), br * 4 * b + 2 * b)
        buf = reverb(buf, 0.18, 1.6)
    elif mood == 'finale':
        add(buf, tanpura(dur + 1, 0.05), 0); chords(0.09, 3000); drums(True); bass(); riff(0.16); riff(0.06, 12)
        flute(FLUTE_UP, 0.10, 8); add(buf, tbell(0.30), 0)
        buf = reverb(buf, 0.2, 1.8)
    return buf[:int(dur * SR)]

def build_bgm(cues, total, bpm):
    out = np.zeros(int((total + 1) * SR)); xf = 0.5
    for i, (s, e, mood) in enumerate(cues):
        s0 = max(0, s - (xf / 2 if i else 0)); e0 = e + xf / 2
        seg = render_mood(mood, e0 - s0, bpm); n = len(seg); w = np.ones(n); f = int(xf * SR)
        if i: w[:f] = np.linspace(0, 1, f)
        if i < len(cues) - 1: w[-f:] = np.minimum(w[-f:], np.linspace(1, 0, f))
        else:
            f2 = int(1.2 * SR); w[-f2:] = np.minimum(w[-f2:], np.linspace(1, 0, f2))
        add(out, seg * w, s0)
    return out[:int(total * SR)]

def sfx(name):
    if name == 'shimmer':
        x = np.zeros(int(1.4 * SR))
        for k, m in enumerate([deg(10), deg(11), deg(12), deg(13), deg(15)]):
            t = t_(1.0); add(x, np.sin(2 * np.pi * midi(m) * t) * np.exp(-t / 0.35) * 0.18, k * 0.06)
        return reverb(x, 0.4, 1.4)
    if name == 'bell': return tbell(0.5)
    return base_sfx(name)
