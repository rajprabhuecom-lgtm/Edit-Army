"""Composite: grade + zoom + split layout + desat + overlay. python3 comp.py [preview idx...]"""
import json, sys, os, subprocess, numpy as np, cv2
WD = os.environ.get('W', '/home/user/w').rstrip('/')
W, H, FPS = 1080, 1920, 30
frames = json.load(open(WD + '/frames.json'))
# ---------- colour LUT: warm WB, gentle S-curve, highlight roll-off ----------
x = np.arange(256) / 255.0
def curve(v):
    s = v + 0.10 * np.sin(2 * np.pi * v) * (-0.5) # gentle S
    s = np.where(s > 0.80, 0.80 + (s - 0.80) * 0.65, s) # roll off highlights (shirt)
    return np.clip(s, 0, 1)
lut_b = np.clip(curve(x * 0.93) * 255, 0, 255).astype(np.uint8)
lut_g = np.clip(curve(x * 0.985) * 255, 0, 255).astype(np.uint8)
lut_r = np.clip(curve(np.minimum(1, x * 1.045 + 0.012)) * 255, 0, 255).astype(np.uint8)
LUT = np.dstack([lut_b, lut_g, lut_r]).reshape(256, 1, 3)
CX, CY = 540, 640 # face centre for zooms
SPLIT_Y, CROP_Y0 = 864, 180
def grade(f):
    g = cv2.LUT(f, LUT)
    hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV); hsv[..., 1] = np.clip(hsv[..., 1] * 1.04, 0, 255).astype(np.uint8)
    g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bl = cv2.GaussianBlur(g, (0, 0), 1.2)
    return cv2.addWeighted(g, 1.25, bl, -0.25, 0)
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
        r = BR[name] = dict(p=subprocess.Popen(['ffmpeg', '-v', 'error', '-i', WD + '/broll/' + name, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE), k=-1, f=None)
    while r['k'] < want:
        buf = r['p'].stdout.read(W * H * 3)
        if len(buf) < W * H * 3: break
        r['f'] = np.frombuffer(buf, np.uint8).reshape(H, W, 3); r['k'] += 1
    return r['f']
def pushin(f, p, cy=H // 2, z0=1.0, z1=1.06):
    z = z0 + (z1 - z0) * p
    M = np.float32([[z, 0, W / 2 - z * W / 2], [0, z, cy - z * cy]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
def compose(src, fr, i):
    f = grade(src)
    V = fr.get('V')
    if fr['L'] == 'split':
        out = np.zeros_like(f); out[SPLIT_Y:] = f[CROP_Y0:CROP_Y0 + H - SPLIT_Y]
        if V:
            b = pushin(broll(V[0], V[1]), V[2], cy=V[3] if len(V) > 3 else H // 2); cy = V[3] if len(V) > 3 else 960
            y0 = max(0, min(H - SPLIT_Y, cy - SPLIT_Y // 2)); out[:SPLIT_Y] = b[y0:y0 + SPLIT_Y]
        f = out
    elif fr['L'] == 'full':
        if V: f = pushin(broll(V[0], V[1]), V[2])
    else:
        f = zoom(f, fr['z'])
    p = f'{WD}/ov/{i:05d}.png'
    if os.path.exists(p):
        ov = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if ov.ndim == 2: ov = cv2.cvtColor(ov, cv2.COLOR_GRAY2BGR)
        if ov.shape[2] == 3: return ov
        a = ov[..., 3:4].astype(np.float32) / 255.0
        f = (ov[..., :3].astype(np.float32) * a + f.astype(np.float32) * (1 - a)).astype(np.uint8)
    return f
def reader():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', WD + '/src.mkv', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
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
            cv2.imwrite(f'{WD}/prev/{i:05d}.jpg', compose(src.copy(), frames[i], i), [cv2.IMWRITE_JPEG_QUALITY, 85])
        sys.exit()
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-i', WD + '/audio/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-shortest', WD + '/comp_1x.mkv'], stdin=subprocess.PIPE)
    for i, fr in enumerate(frames):
        src = rd.send(int(round(fr['ts'] * FPS)))
        enc.stdin.write(compose(src.copy(), fr, i).tobytes())
        if i % 300 == 0: print(i, len(frames), flush=True)
    enc.stdin.close(); enc.wait()
