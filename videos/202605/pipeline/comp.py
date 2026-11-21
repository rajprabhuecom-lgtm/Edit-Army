"""Composite: grade + burned-caption blur band + zoom/punch + split layout + overlay.  python3 comp.py <vid> [preview idx...]"""
import json, sys, os, subprocess, numpy as np, cv2
VID = sys.argv[1]; Wd = f'/home/user/w/{VID}/'
W, H, FPS = 1080, 1920, 30
frames = json.load(open(Wd + 'frames.json')); C = json.load(open(Wd + 'comp.json'))
x = np.arange(256) / 255.0
def curve(v):
    s = v + 0.10 * np.sin(2 * np.pi * v) * (-0.5)
    s = np.where(s > 0.80, 0.80 + (s - 0.80) * 0.65, s)
    return np.clip(s, 0, 1)
LUT = np.dstack([np.clip(curve(x * 0.96) * 255, 0, 255).astype(np.uint8), np.clip(curve(x * 0.99) * 255, 0, 255).astype(np.uint8),
                 np.clip(curve(np.minimum(1, x * 1.03 + 0.008)) * 255, 0, 255).astype(np.uint8)]).reshape(256, 1, 3)
CX, CY = C['cx'], C['cy']; SPLIT_Y, CROP_Y0 = 864, C['crop_y0']
BL = C.get('blur')
if BL:   # feathered mask for the burned-in caption strip
    y0, y1 = BL; m = np.zeros((H, 1), np.float32); m[y0:y1] = 1
    m = cv2.GaussianBlur(m, (1, 51), 0); MASK = np.repeat(m[:, :, None], 1, 1)
def unburn(f):
    """frosted obsidian bar over the burned-in caption strip: desaturate + heavy blur + darken, feathered edges"""
    if not BL: return f
    y0, y1 = max(0, BL[0] - 50), min(H, BL[1] + 50)
    band = f[y0:y1].copy(); g = cv2.cvtColor(cv2.cvtColor(band, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    b = cv2.GaussianBlur(cv2.addWeighted(band, 0.25, g, 0.75, 0), (0, 0), sigmaX=45, sigmaY=18)
    b = b * 0.34 + np.array([13, 10, 8], np.float32) * 0.5
    a = MASK[y0:y1]; f[y0:y1] = (b * a + band * (1 - a)).astype(np.uint8); return f
    y0, y1 = max(0, BL[0] - 40), min(H, BL[1] + 40)
    band = f[y0:y1]; b = cv2.GaussianBlur(band, (0, 0), 22); b = cv2.convertScaleAbs(b, alpha=0.74, beta=0)
    a = MASK[y0:y1]; f[y0:y1] = (b * a + band * (1 - a)).astype(np.uint8); return f
def grade(f):
    g = cv2.LUT(f, LUT)
    hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV); hsv[..., 1] = np.clip(hsv[..., 1] * 1.06, 0, 255).astype(np.uint8)
    g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR); bl = cv2.GaussianBlur(g, (0, 0), 1.2)
    return cv2.addWeighted(g, 1.25, bl, -0.25, 0)
def zoom(f, z):
    if abs(z - 1) < 1e-3: return f
    M = np.float32([[z, 0, CX - z * CX], [0, z, CY - z * CY]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
def desat(f, k=0.7):
    gr = cv2.cvtColor(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    return cv2.convertScaleAbs(cv2.addWeighted(f, 1 - k, gr, k, 0), alpha=0.9, beta=-6)
def compose(src, fr, i):
    f = grade(unburn(src))
    if fr['des']: f = desat(f)
    if fr['L'] == 'split':
        out = np.zeros_like(f); out[SPLIT_Y:] = f[CROP_Y0:CROP_Y0 + H - SPLIT_Y]; f = out
    elif fr['L'] != 'full':
        f = zoom(f, fr['z'])
    p = f'{Wd}ov/{i:05d}.png'
    if os.path.exists(p):
        ov = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if ov.shape[2] == 3: return ov
        a = ov[..., 3:4].astype(np.float32) / 255.0
        f = (ov[..., :3].astype(np.float32) * a + f.astype(np.float32) * (1 - a)).astype(np.uint8)
    return f
def reader():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', C['src'], '-vf', 'fps=30', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    k = -1; cur = None
    while True:
        want = yield cur
        while k < want:
            buf = p.stdout.read(W * H * 3)
            if len(buf) < W * H * 3: break
            cur = np.frombuffer(buf, np.uint8).reshape(H, W, 3); k += 1
if __name__ == '__main__':
    prev = [int(a) for a in sys.argv[2:]]
    rd = reader(); next(rd)
    if prev:
        for i in sorted(prev):
            src = rd.send(int(round(frames[i]['ts'] * FPS)))
            cv2.imwrite(f'{Wd}prev/{i:05d}.jpg', compose(src.copy(), frames[i], i), [cv2.IMWRITE_JPEG_QUALITY, 85])
        sys.exit()
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-i', Wd + 'audio/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
        '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-shortest', Wd + 'comp_1x.mkv'], stdin=subprocess.PIPE)
    for i, fr in enumerate(frames):
        src = rd.send(int(round(fr['ts'] * FPS)))
        enc.stdin.write(compose(src.copy(), fr, i).tobytes())
        if i % 600 == 0: print(VID, i, len(frames), flush=True)
    enc.stdin.close(); enc.wait()
