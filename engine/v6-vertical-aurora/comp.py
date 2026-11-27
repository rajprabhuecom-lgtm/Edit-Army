"""v6 compositor: python3 comp.py [frame ...]   (no args = full render -> comp_1x.mkv)
Reads   W/cut.mkv      (A-roll already jump-cut, upright, 1440x2560, 25 fps, cut time)
        W/gfx/timeline.json  lay[f]=[x,y,w,h,r,mode]  view[f]=[cx,cy,k]  fx[f]={bw,spot,gl,shx,shy}  shatter=[t..]
        W/ov/NNNNN.png + ov/blur_*.json (glass rects to frost)   W/stage/NNN.jpg (neon stage loop)
Per frame: grade -> place A-roll in layout rect (affine from view) over stage -> fx -> frost glass rects -> overlay.
"""
import json, glob, os, subprocess, sys, numpy as np, cv2
W = '/home/user/w'
TL = json.load(open(f'{W}/gfx/timeline.json')); FPS = TL['fps']; N = len(TL['lay'])
SW, SH = 1440, 2560; F = SW / 1080
blur = {}
for f in glob.glob(f'{W}/ov/blur_*.json'):
    blur.update({int(k): v for k, v in json.load(open(f)).items()})
stage = [cv2.imread(p) for p in sorted(glob.glob(f'{W}/stage/*.jpg'))]
# ---- grade: gentle S-curve, lift skin warmth, keep the cool curtain (AuroraGlass: no heavy LUT)
x = np.arange(256) / 255.0
curve = np.clip(x + 0.10 * np.sin(2 * np.pi * (x - 0.5)) * (x * (1 - x)) * 4 * 0.5 + 0.02 * (1 - x), 0, 1)
LUT = np.stack([np.clip(curve * 255 * g, 0, 255) for g in (0.985, 1.0, 1.035)], 1).astype(np.uint8)  # B,G,R gains
GRADE_OFF = os.environ.get('NOGRADE') == '1'  # set when cut.mkv is already graded by grade.sh
def grade(img):
    if GRADE_OFF: return img
    out = np.empty_like(img)
    for c in range(3): out[..., c] = cv2.LUT(img[..., c], LUT[:, c])
    return out
def rrect_mask(x, y, w, h, r, shape=(1920, 1080), feather=1.5):
    m = np.zeros(shape, np.uint8); x, y, w, h, r = map(int, (x, y, w, h, r)); r = max(1, min(r, w // 2, h // 2))
    cv2.rectangle(m, (x + r, y), (x + w - r, y + h), 255, -1); cv2.rectangle(m, (x, y + r), (x + w, y + h - r), 255, -1)
    for cx, cy in ((x + r, y + r), (x + w - r, y + r), (x + r, y + h - r), (x + w - r, y + h - r)): cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
    return cv2.GaussianBlur(m, (0, 0), feather) if feather else m
_rng = np.random.default_rng(7)
def shards(n=46):
    pts = [(0, 0), (1079, 0), (0, 1919), (1079, 1919)] + [(int(v[0]), int(v[1])) for v in _rng.uniform([0, 0], [1079, 1919], (n, 2))]
    pts += [(540 + int(220 * np.cos(a)), 760 + int(220 * np.sin(a))) for a in np.linspace(0, 6.28, 9)[:-1]]
    sd = cv2.Subdiv2D((0, 0, 1080, 1920)); [sd.insert(p) for p in pts]
    tris = [t.reshape(3, 2) for t in sd.getTriangleList() if (t >= -1).all() and (t[::2] <= 1081).all() and (t[1::2] <= 1921).all()]
    return [(t, t.mean(0), _rng.uniform(-0.6, 0.6)) for t in tris]
SHARDS = shards()
def shatter(base, frozen, p):
    """frozen frame breaks into shards flying out over base; p 0..1"""
    out = base.copy(); c0 = np.array([540, 760.0])
    for tri, c, rot in SHARDS:
        d = c - c0; dist = np.linalg.norm(d) + 1; v = d / dist * (900 + 600 * (1 - dist / 1500))
        off = v * p ** 1.6; ang = rot * p * 90
        M = cv2.getRotationMatrix2D(tuple(c), ang, 1 - 0.25 * p); M[:, 2] += off
        m = np.zeros((1920, 1080), np.uint8); cv2.fillConvexPoly(m, tri.astype(np.int32), 255)
        tw = cv2.warpAffine(frozen, M, (1080, 1920)); mw = cv2.warpAffine(m, M, (1080, 1920))
        a = (mw.astype(np.float32) / 255 * (1 - p ** 2))[..., None]
        out = (tw * a + out * (1 - a)).astype(np.uint8)
        if p < 0.5:
            cv2.polylines(out, [cv2.transform(tri[None].astype(np.float32), M)[0].astype(np.int32)], True, (255, 255, 255), 2, cv2.LINE_AA)
    return out
def compose(src, f, prev_frame=None):
    x, y, w, h, r, mode = TL['lay'][f]; cx, cy, k = TL['view'][f]; fx = TL['fx'][f]
    src = grade(src)
    if fx.get('bw'):
        g = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY); g = cv2.convertScaleAbs(g, alpha=1.15, beta=-12)
        src = cv2.addWeighted(src, 1 - fx['bw'], cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), fx['bw'], 0)
    sx, sy = fx.get('shx', 0), fx.get('shy', 0)
    M = np.float32([[k / F, 0, x + w / 2 - k * cx + sx], [0, k / F, y + h / 2 - k * cy + sy]])
    full = w >= 1075 and h >= 1915
    if mode == 4:  # full-screen motion graphic: neon stage only, A-roll hidden
        out = stage[f % len(stage)].copy()
    elif full:
        out = cv2.warpAffine(src, M, (1080, 1920), flags=cv2.INTER_AREA if k / F < 1 else cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    else:
        bg = stage[f % len(stage)].copy()
        if mode == 3:  # blurred, darkened copy of the A-roll as background (testimonial/offer look)
            bgv = cv2.warpAffine(src, np.float32([[1.25 / F, 0, 540 - 1.25 * 560], [0, 1.25 / F, 960 - 1.25 * 900]]), (1080, 1920), borderMode=cv2.BORDER_REPLICATE)
            bg = (cv2.GaussianBlur(cv2.resize(bgv, (270, 480)), (0, 0), 6)); bg = cv2.resize(bg, (1080, 1920)); bg = (bg * 0.45).astype(np.uint8)
        fg = cv2.warpAffine(src, M, (1080, 1920), flags=cv2.INTER_AREA if k / F < 1 else cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        m = (rrect_mask(x, y, w, h, r).astype(np.float32) / 255)[..., None]
        out = (fg * m + bg * (1 - m)).astype(np.uint8)
    if fx.get('spot'):
        s = fx['spot']; yy, xx = np.ogrid[:1920, :1080]
        fcx, fcy = x + w / 2 + k * (fx.get('scx', 560) - cx), y + h / 2 + k * (fx.get('scy', 640) - cy)
        d = ((xx - fcx) / (330 * k)) ** 2 + ((yy - fcy) / (420 * k)) ** 2
        v = np.clip(1.0 - s * 0.85 * np.clip((np.sqrt(d) - 0.65) / 0.9, 0, 1), 0.12, 1).astype(np.float32)
        out = (out * v[..., None]).astype(np.uint8)
    if fx.get('gl'):  # RGB split + slice jitter
        g = fx['gl']; o = out.copy(); dx = int(18 * g)
        o[..., 2] = np.roll(out[..., 2], dx, 1); o[..., 0] = np.roll(out[..., 0], -dx, 1)
        rr = np.random.default_rng(f)
        for _ in range(int(6 * g)):
            y0 = rr.integers(0, 1800); hh = rr.integers(20, 120); o[y0:y0 + hh] = np.roll(o[y0:y0 + hh], int(rr.integers(-80, 80) * g), 1)
        out = o
    if fx.get('wh'):  # whip pan: horizontal shift + motion blur
        v = fx['wh']; sh = int(v * 260); kl = int(abs(v) * 90) | 1
        out = np.roll(out, sh, 1); ker = np.zeros((1, kl), np.float32); ker[0, :] = 1.0 / kl; out = cv2.filter2D(out, -1, ker)
    if fx.get('zb'):  # zoom blur (transition punch)
        z = fx['zb']; acc = out.astype(np.float32); n = 6
        for i in range(1, n):
            s = 1 + z * 0.05 * i; Mz = cv2.getRotationMatrix2D((540, 800), 0, s); acc += cv2.warpAffine(out, Mz, (1080, 1920), borderMode=cv2.BORDER_REPLICATE)
        out = (acc / n).astype(np.uint8)
    for b in blur.get(f, []):  # frosted glass under cards
        bx, by, bw, bh, br, bo = b; bx, by, bw, bh = int(max(0, bx)), int(max(0, by)), int(min(1080 - bx, bw)), int(min(1920 - by, bh))
        if bw < 10 or bh < 10: continue
        reg = out[by:by + bh, bx:bx + bw]; sm = cv2.resize(reg, (max(1, bw // 8), max(1, bh // 8)), interpolation=cv2.INTER_AREA)
        sm = cv2.GaussianBlur(sm, (0, 0), 2.2); bl = cv2.resize(sm, (bw, bh), interpolation=cv2.INTER_LINEAR)
        m = (rrect_mask(0, 0, bw, bh, br, (bh, bw)).astype(np.float32) / 255 * bo)[..., None]
        out[by:by + bh, bx:bx + bw] = (bl * m + reg * (1 - m)).astype(np.uint8)
    return out
def overlay(img, f):
    p = f'{W}/ov/{f:05d}.png'
    if not os.path.exists(p): return img
    ov = cv2.imread(p, cv2.IMREAD_UNCHANGED); a = ov[..., 3:4].astype(np.uint16)
    return ((ov[..., :3].astype(np.uint16) * a + img.astype(np.uint16) * (255 - a)) // 255).astype(np.uint8)
def reader(start=0):
    cmd = ['ffmpeg', '-v', 'error', '-ss', f'{start / FPS:.3f}', '-i', f'{W}/cut.mkv', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=SW * SH * 3 * 2)
    while True:
        b = p.stdout.read(SW * SH * 3)
        if len(b) < SW * SH * 3: break
        yield np.frombuffer(b, np.uint8).reshape(SH, SW, 3)
SH_T = [round(t * FPS) for t in TL.get('shatter', [])]; SH_LEN = 14
def run(frames=None):
    if frames:  # preview stills
        os.makedirs(f'{W}/prev', exist_ok=True)
        for f in frames:
            src = next(reader(f)); img = overlay(compose(src, f), f)
            cv2.imwrite(f'{W}/prev/c_{f:05d}.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 88])
        return
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', '1080x1920', '-r', str(FPS), '-i', '-',
                            '-i', f'{W}/audio/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '12',
                            '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-shortest', f'{W}/comp_1x.mkv'], stdin=subprocess.PIPE)
    frozen = None
    for f, src in enumerate(reader()):
        if f >= N: break
        img = compose(src, f)
        for s in SH_T:
            if f == s - 1: frozen = img.copy()
            if s <= f < s + SH_LEN and frozen is not None: img = shatter(img, frozen, (f - s) / SH_LEN)
        img = overlay(img, f); enc.stdin.write(img.tobytes())
        if f % 250 == 0: print('comp', f, N, flush=True)
    enc.stdin.close(); enc.wait()
if __name__ == '__main__':
    run([int(a) for a in sys.argv[1:]] or None)
