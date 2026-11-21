"""Composite: grade + zoom + split layout + desat + overlay. python3 comp.py [preview idx...]"""
import json, sys, os, subprocess, numpy as np, cv2
W, H, FPS = 1080, 1920, 30
frames = json.load(open('/home/user/w/frames.json'))
# ---------- colour LUT: warm WB, gentle S-curve, highlight roll-off ----------
x = np.arange(256) / 255.0
def curve(v):
    s = v + 0.10 * np.sin(2 * np.pi * v) * (-0.5) # gentle S
    s = np.where(s > 0.80, 0.80 + (s - 0.80) * 0.65, s) # roll off highlights (shirt)
    return np.clip(s, 0, 1)
lut_b = np.clip(curve(x * 0.95) * 255, 0, 255).astype(np.uint8)
lut_g = np.clip(curve(x * 0.985) * 255, 0, 255).astype(np.uint8)
lut_r = np.clip(curve(np.minimum(1, x * 1.035 + 0.01)) * 255, 0, 255).astype(np.uint8)
LUT = np.dstack([lut_b, lut_g, lut_r]).reshape(256, 1, 3)
CX, CY = 540, 560 # face centre for zooms
SPLIT_Y, CROP_Y0 = 864, 230
def grade(f):
    g = cv2.LUT(f, LUT)
    hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV); hsv[..., 1] = np.clip(hsv[..., 1] * 1.08, 0, 255).astype(np.uint8)
    g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bl = cv2.GaussianBlur(g, (0, 0), 1.2)
    return cv2.addWeighted(g, 1.35, bl, -0.35, 0)
def zoom(f, z):
    if abs(z - 1) < 1e-3: return f
    M = np.float32([[z, 0, CX - z * CX], [0, z, CY - z * CY]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
def desat(f, k=0.7):
    gr = cv2.cvtColor(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    out = cv2.addWeighted(f, 1 - k, gr, k, 0)
    return cv2.convertScaleAbs(out, alpha=0.9, beta=-6)
BR = {}
def broll(name, ct):
    """frame of a B-roll clip at clip time ct (sequential reader, restarts on seek back)"""
    want = int(round(ct * FPS)); r = BR.get(name)
    if r is None or want < r['k']:
        if r: r['p'].kill()
        r = BR[name] = dict(p=subprocess.Popen(['ffmpeg', '-v', 'error', '-i', '/home/user/w/broll/' + name, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE), k=-1, f=None)
    while r['k'] < want:
        buf = r['p'].stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        r['f'] = np.frombuffer(buf, np.uint8).reshape(H, W, 3); r['k'] += 1
    return r['f']
def pushin(f, p, cy=H // 2, z0=1.0, z1=1.06):
    z = z0 + (z1 - z0) * p
    M = np.float32([[z, 0, W / 2 - z * W / 2], [0, z, cy - z * cy]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
SPLIT_CY = {'B01_dog_scale.mkv': 1100, 'B02_food_card.mkv': 900, 'B04_brushing.mkv': 980, 'B05_zoom_family.mkv': 900, 'B06_park_walk.mkv': 1000}

# ---------- v6 signature effects ----------
YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)
def spotlight(f, p):
    """theatre spotlight finds the face: dark frame, soft ellipse grows onto the face"""
    r = 120 + 900 * (p ** 1.6); d = np.sqrt(((XX - 540) / 1.0) ** 2 + ((YY - 520) / 1.25) ** 2)
    m = np.clip((r - d) / 160, 0, 1)[..., None]; base = 0.15 + 0.85 * max(0, (p - 0.75) / 0.25)
    m = np.maximum(m, base)
    return (f.astype(np.float32) * m).astype(np.uint8)
RNG = np.random.default_rng(7)
SHK = RNG.normal(0, 1, (4000, 2))
def shake(f, p, i):
    a = 18 * (1 - p); dx, dy = SHK[i % 4000] * a
    M = np.float32([[1.04, 0, -0.02 * W + dx], [0, 1.04, -0.02 * H + dy]])
    return cv2.warpAffine(f, M, (W, H), borderMode=cv2.BORDER_REFLECT)
def glitch(f, i):
    o = f.copy(); s = 14 + (i % 3) * 8
    o[..., 2] = np.roll(f[..., 2], s, axis=1); o[..., 0] = np.roll(f[..., 0], -s, axis=1)
    for k in range(5):
        y = int(SHK[(i * 7 + k) % 4000, 0] * 300 + 900) % (H - 80); h = 20 + (k * 13) % 60
        o[y:y + h] = np.roll(o[y:y + h], int(SHK[(i + k) % 4000, 1] * 60), axis=1)
    return o
def whip(f, d):
    a = 1 - abs(d); k = int(9 + 120 * a) | 1
    b = cv2.blur(f, (k, 1)); sh = int(-d * 260)
    return np.roll(b, sh, axis=1)
GRID = None
def grid(f, p):
    """grid-dive: pull back to a 3x3 wall of moments, dive back into the centre tile"""
    global GRID
    if GRID is None:
        GRID = []
        for t in [2.5, 9.0, 11.0, 13.0, 16.5, 29.0, 34.8, 40.0]:
            r = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', '/home/user/w/1121.mp4', '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
            GRID.append(grade(np.frombuffer(r, np.uint8).reshape(H, W, 3)))
    k = 1 - 0.68 * np.sin(np.pi * p) ** 0.8          # tile scale 1 -> 0.32 -> 1
    tw, th = max(2, int(W * k)), max(2, int(H * k)); gap = int(24 * k)
    out = np.full((H, W, 3), 12, np.uint8); tiles = GRID[:4] + [f] + GRID[4:]
    for n, tile in enumerate(tiles):
        cx = W // 2 + (n % 3 - 1) * (tw + gap); cy = H // 2 + (n // 3 - 1) * (th + gap)
        x0, y0 = cx - tw // 2, cy - th // 2; x1, y1 = x0 + tw, y0 + th
        if x1 <= 0 or y1 <= 0 or x0 >= W or y0 >= H: continue
        t = cv2.resize(tile, (tw, th), interpolation=cv2.INTER_AREA)
        if n != 4: t = (t * 0.7).astype(np.uint8)
        a0, b0 = max(0, x0), max(0, y0); a1, b1 = min(W, x1), min(H, y1)
        out[b0:b1, a0:a1] = t[b0 - y0:b1 - y0, a0 - x0:a1 - x0]
    return out
def apply_fx(f, fr, i):
    fx = fr.get('fx') or {}
    if 'spot' in fx: f = spotlight(f, fx['spot'])
    if 'shake' in fx: f = shake(f, fx['shake'], i)
    if 'glitch' in fx: f = glitch(f, fx['glitch'])
    if 'whip' in fx: f = whip(f, fx['whip'])
    if 'grid' in fx: f = grid(f, fx['grid'])
    return f
def compose(src, fr, i):
    f = grade(src)
    if fr['des']: f = desat(f)
    V = fr.get('V')
    if fr['L'] == 'split':
        out = np.zeros_like(f); out[SPLIT_Y:] = f[CROP_Y0:CROP_Y0 + H - SPLIT_Y]
        if V:
            b = grade(pushin(broll(V[0], V[1]), V[2])); cy = SPLIT_CY.get(V[0], 960)
            y0 = max(0, min(H - SPLIT_Y, cy - SPLIT_Y // 2)); out[:SPLIT_Y] = b[y0:y0 + SPLIT_Y]
        f = out
    elif fr['L'] == 'full':
        if V: f = grade(pushin(broll(V[0], V[1]), V[2]))
    else:
        f = zoom(f, fr['z'])
    f = apply_fx(f, fr, i)
    p = f'/home/user/w/ov/{i:05d}.png'
    if os.path.exists(p):
        ov = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if ov.ndim == 2: ov = cv2.cvtColor(ov, cv2.COLOR_GRAY2BGR)
        if ov.shape[2] == 3: return ov
        a = ov[..., 3:4].astype(np.float32) / 255.0
        f = (ov[..., :3].astype(np.float32) * a + f.astype(np.float32) * (1 - a)).astype(np.uint8)
    return f
def reader():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', '/home/user/w/1121.mp4', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    k = -1; cur = None
    while True:
        want = yield cur
        while k < want:
            buf = p.stdout.read(W * H * 3)
            if len(buf) < W * H * 3: break
            cur = np.frombuffer(buf, np.uint8).reshape(H, W, 3); k += 1
if __name__ == '__main__':
    prev = [int(a) for a in sys.argv[1:]]
    rd = reader(); next(rd)
    if prev:
        for i in sorted(prev):
            src = rd.send(int(round(frames[i]['ts'] * FPS)))
            cv2.imwrite(f'/home/user/w/prev/{i:05d}.jpg', compose(src.copy(), frames[i], i), [cv2.IMWRITE_JPEG_QUALITY, 85])
        sys.exit()
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-i', '/home/user/w/audio/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-shortest', '/home/user/w/comp_1x.mkv'], stdin=subprocess.PIPE)
    for i, fr in enumerate(frames):
        src = rd.send(int(round(fr['ts'] * FPS)))
        enc.stdin.write(compose(src.copy(), fr, i).tobytes())
        if i % 300 == 0: print(i, len(frames), flush=True)
    enc.stdin.close(); enc.wait()
