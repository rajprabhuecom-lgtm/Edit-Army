"""v6 plan library. A video's plan.py authors everything in SOURCE time (seconds in the raw take) and calls build().
build() snaps cuts to the 25 fps grid, maps source->cut time, builds per-frame layout/view/fx tracks
(face-tracked, eased transitions) and writes W/gfx/timeline.json + W/audio/cues.json.

Layout modes (LAY entries: (s0, s1, mode, opts)):
  'full'  A-roll fills 1080x1920. opts z = zoom (1.0 = whole seated shot), fy = where the face sits on screen (y px)
  'card'  neon stage + face in rounded card at bottom (ads look); opts z, box=(x,y,w,h)
  'pip'   neon stage, face in small LIVE bubble bottom-right
  'blur'  blurred A-roll background + face card (offer / testimonial look)
"""
import json, os, numpy as np
W = '/home/user/w'; FPS = 25
TIMEKEYS = {'a', 'b', 'at', 'on', 'strike', 'sat', 'ra', 'xat'}
BOX = {'card': (90, 880, 900, 960, 46), 'cardhi': (90, 1000, 900, 840, 46), 'pip': (650, 1330, 380, 520, 40), 'blur': (140, 760, 800, 1060, 46)}

def snap(t): return round(t * FPS) / FPS

class Plan:
    def __init__(self, keep, pre=0.06, post=0.09):
        k = sorted([[snap(max(0, a - pre)), snap(b + post)] for a, b in keep])
        m = [k[0]]
        for a, b in k[1:]:
            if a <= m[-1][1]: m[-1][1] = max(m[-1][1], b)
            else: m.append([a, b])
        self.keep = m; self.cum = np.cumsum([0] + [b - a for a, b in m]); self.total = float(self.cum[-1])
    def o(self, t):
        """source -> cut time (times inside a removed gap snap to the next kept start)"""
        for (a, b), c in zip(self.keep, self.cum):
            if t < a: return float(c)
            if t <= b: return float(c + t - a)
        return self.total
    def conv(self, x):
        if isinstance(x, dict):
            return {k: (self.o(v) if k in TIMEKEYS and isinstance(v, (int, float)) else
                        [self.o(u) for u in v] if k in TIMEKEYS and isinstance(v, list) else self.conv(v)) for k, v in x.items()}
        if isinstance(x, list): return [self.conv(v) for v in x]
        return x

def face_track(plan):
    """per cut-frame face centre (1080x1920 source space), smoothed"""
    fj = json.load(open(f'{W}/face.json'))
    ts = np.array([r[0] for r in fj]); ok = np.array([r[1] is not None for r in fj])
    cx = np.interp(ts, ts[ok], [r[1] for r in fj if r[1] is not None]); cy = np.interp(ts, ts[ok], [r[2] for r in fj if r[2] is not None])
    n = int(round(plan.total * FPS)); out = np.zeros((n, 2)); f = 0
    for a, b in plan.keep:
        for i in range(int(round((b - a) * FPS))):
            if f >= n: break
            s = a + i / FPS; out[f] = [np.interp(s, ts, cx), np.interp(s, ts, cy)]; f += 1
    # smooth within each kept segment boundaries hard (jump cuts), heavy within
    k = 25; ker = np.ones(k) / k
    sm = np.stack([np.convolve(np.pad(out[:, j], k, mode='edge'), ker, 'same')[k:-k] for j in range(2)], 1)
    return sm

def build(plan, LAY, ZOOM, FX, ITEMS, SFX, MUSIC, shatter=()):
    n = int(round(plan.total * FPS)); face = face_track(plan)
    # ---- layout per frame
    lay = []; view = []; mode_of = ['full'] * n; opt_of = [{}] * n
    for s0, s1, m, opt in LAY:
        for f in range(int(round(plan.o(s0) * FPS)), min(n, int(round(plan.o(s1) * FPS)))): mode_of[f] = m; opt_of[f] = opt
    zkey = sorted((plan.o(t), z) for t, z in ZOOM)  # full-frame zoom keyframes (hard cut on jump cuts, eased otherwise)
    def zoom_at(t):
        z = 1.0
        for tk, zk in zkey:
            if tk <= t: z = zk
        return z
    def target(f):
        m = mode_of[f]; opt = opt_of[f]; fx_, fy_ = face[f]
        if m == 'full':
            z = opt.get('z') or zoom_at(f / FPS); fy = opt.get('fy', 640 if z <= 1.05 else 780)
            k = z; cx = fx_ + opt.get('dx', 0); cy = fy_ + (960 - fy) / k
            hw, hh = 540 / k, 960 / k; cx = min(max(cx, hw), 1080 - hw); cy = min(max(cy, hh), 1920 - hh)
            return [0, 0, 1080, 1920, 0, 0], [cx, cy, k]
        x, y, w, h, r = opt.get('box') or BOX[m]; k = opt.get('z', 1.55 if m != 'pip' else 1.9)
        cy = fy_ + opt.get('fdy', 150) / k * (h / 960); cx = fx_
        hw, hh = w / 2 / k, h / 2 / k; cx = min(max(cx, hw), 1080 - hw); cy = min(max(cy, hh), 1920 - hh)
        return [x, y, w, h, r, {'card': 1, 'cardhi': 1, 'pip': 2, 'blur': 3}[m]], [cx, cy, k]
    T = [target(f) for f in range(n)]
    # ease layout changes over 8 frames (0.32 s) - rect + view interpolate together
    lay = [list(t[0]) for t in T]; view = [list(t[1]) for t in T]; D = 8
    for f in range(1, n):
        if mode_of[f] != mode_of[f - 1]:
            a_l, a_v = T[f - 1];
            for i in range(D):
                if f + i >= n: break
                p = 1 - (1 - (i + 1) / D) ** 3; b_l, b_v = T[f + i]
                lay[f + i] = [a_l[j] + (b_l[j] - a_l[j]) * p for j in range(5)] + [b_l[5]]
                view[f + i] = [a_v[j] + (b_v[j] - a_v[j]) * p for j in range(3)]
    # ---- fx per frame
    fx = [dict() for _ in range(n)]
    for s0, s1, d in FX:
        a, b = int(round(plan.o(s0) * FPS)), int(round(plan.o(s1) * FPS))
        for f in range(a, min(n, b)):
            for kk, v in d.items():
                if kk == 'shake': fx[f]['shx'] = v * np.sin(f * 2.7) * np.exp(-(f - a) / 6); fx[f]['shy'] = v * np.cos(f * 3.3) * np.exp(-(f - a) / 6)
                elif kk in ('gl', 'zb'): fx[f][kk] = v * max(0, 1 - (f - a) / max(1, b - a))
                else: fx[f][kk] = v
        for f in range(max(0, a - 3), a):  # soft in for bw / spot
            for kk in ('bw', 'spot'):
                if kk in d: fx[f][kk] = d[kk] * (f - a + 4) / 4
    for f in range(n):
        fx[f]['scx'], fx[f]['scy'] = face[f][0], face[f][1]
    items = sorted(plan.conv(ITEMS), key=lambda it: it['a'])
    for it in items:
        if it['b'] <= it['a']: it['b'] = it['a'] + 0.5
        if it.get('k') == 'words': it['w'] = [[w[0], plan.o(w[1])] + w[2:] for w in it['w']]
    tl = {'fps': FPS, 'total': plan.total, 'lay': lay, 'view': view, 'fx': fx, 'items': items, 'shatter': [plan.o(t) for t in shatter]}
    os.makedirs(f'{W}/gfx', exist_ok=True); json.dump(tl, open(f'{W}/gfx/timeline.json', 'w'), ensure_ascii=False)
    cues = {'total': plan.total, 'keep': plan.keep, 'sfx': sorted([[plan.o(t), nm] for t, nm in SFX]),
            'music': [[plan.o(a), plan.o(b), m] for a, b, m in MUSIC]}
    json.dump(cues, open(f'{W}/audio/cues.json', 'w'))
    print(f'cut {plan.total:.1f}s ({plan.total / 1.2:.1f}s at 1.2x), {len(plan.keep)} segments, {len(items)} items, {n} frames')
    return tl
