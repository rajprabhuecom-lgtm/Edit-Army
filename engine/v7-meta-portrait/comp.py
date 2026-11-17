"""v7 portrait (size from comp_cfg.json) / v6 landscape composite: grade + punch-in zooms + side layout + portrait testimonial cards + overlay PNGs.
WD=<workdir>/ python3 comp.py [preview frame idx ...]
Inputs (work dir /home/user/w):
  src.mkv            joined speaker footage, 1920x1080, FPS
  frames.json        per output frame: {ts: source time, L: 'face'|'side'|'full'|'tside', z: zoom, V: [clip, clip_t, progress] or null, des: bool}
  ov/NNNNN.png       overlay frames from render.js (transparent)
  broll/<clip>       B-roll clips (any size; landscape fills, portrait becomes a card on a blurred copy of itself)
  audio/mix.wav      final mix
"""
import json, sys, os, subprocess, numpy as np, cv2
FPS = 30
WD = os.environ.get('WD', '/home/user/w/vsl/')
frames = json.load(open(WD + 'frames.json'))
cfg = json.load(open(WD + 'comp_cfg.json')) if os.path.exists(WD + 'comp_cfg.json') else {}
W, H = cfg.get('size', [1920, 1080])
CX, CY = cfg.get('face', [910, 330])       # speaker face centre in the source frame (for zooms and the side crop)
PANEL_X = 1152                              # side layout: animation 0..1152, speaker panel 1152..1920 (768 wide)
SIDE_SRC_X = int(min(W - 768, max(0, CX - 384)))

x = np.arange(256) / 255.0
def curve(v):
    s = v + 0.08 * np.sin(2 * np.pi * v) * (-0.5)
    s = np.where(s > 0.82, 0.82 + (s - 0.82) * 0.6, s)       # roll off the white shirt
    return np.clip(s, 0, 1)
LUT = np.dstack([np.clip(curve(x * 0.97) * 255, 0, 255).astype(np.uint8),
                 np.clip(curve(x * 0.99) * 255, 0, 255).astype(np.uint8),
                 np.clip(curve(np.minimum(1, x * 1.03 + 0.01)) * 255, 0, 255).astype(np.uint8)]).reshape(256, 1, 3)
def grade(f, lift=True):
    g = cv2.LUT(f, LUT)
    if lift:   # the room is dark: lift shadows a touch
        g = cv2.convertScaleAbs(g, alpha=1.04, beta=4)
    hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV); hsv[..., 1] = np.clip(hsv[..., 1] * 1.06, 0, 255).astype(np.uint8)
    g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    bl = cv2.GaussianBlur(g, (0, 0), 1.4)
    return cv2.addWeighted(g, 1.3, bl, -0.3, 0)
def zoom(f, z, cx=CX, cy=CY):
    if abs(z - 1) < 1e-3: return f
    M = np.float32([[z, 0, cx - z * cx], [0, z, cy - z * cy]])
    return cv2.warpAffine(f, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
def desat(f, k=0.7):
    gr = cv2.cvtColor(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    return cv2.convertScaleAbs(cv2.addWeighted(f, 1 - k, gr, k, 0), alpha=0.9, beta=-6)

BR = {}
def broll(name, ct):
    """frame of a B-roll clip at clip time ct (sequential reader; restarts on seek back). Native size, BGR."""
    want = int(round(ct * FPS)); r = BR.get(name)
    if r is None or want < r['k']:
        if r: r['p'].kill()
        p = WD + 'broll/' + name
        w, h = [int(v) for v in subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', p],
                                                capture_output=True, text=True).stdout.strip().split(',')[:2]]
        w, h = w - w % 2, h - h % 2
        r = BR[name] = dict(p=subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'fps={FPS},crop={w}:{h}:0:0', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'],
                                               stdout=subprocess.PIPE), k=-1, f=None, w=w, h=h)
    while r['k'] < want:
        buf = r['p'].stdout.read(r['w'] * r['h'] * 3)
        if len(buf) < r['w'] * r['h'] * 3: break
        r['f'] = np.frombuffer(buf, np.uint8).reshape(r['h'], r['w'], 3); r['k'] += 1
    return r['f']
def cover(img, w, h, p=0.0, z1=1.05):
    """scale to cover w x h, slow push-in by progress p"""
    ih, iw = img.shape[:2]; s = max(w / iw, h / ih) * (1 + (z1 - 1) * p)
    r = cv2.resize(img, (int(iw * s + 1), int(ih * s + 1)), interpolation=cv2.INTER_AREA if s < 1 else cv2.INTER_LINEAR)
    y0 = (r.shape[0] - h) // 2; x0 = (r.shape[1] - w) // 2
    return r[y0:y0 + h, x0:x0 + w]
def card(img, w, h, p):
    """portrait clip as a rounded card on a blurred, darkened copy of itself (fills w x h)"""
    bg = cv2.GaussianBlur(cover(img, w // 4, h // 4), (0, 0), 6); bg = cv2.resize(bg, (w, h)); bg = cv2.convertScaleAbs(bg, alpha=.45, beta=0)
    ih, iw = img.shape[:2]; ch = int(h * 0.9); cw = int(iw * ch / ih); s = 1 + 0.03 * p
    c = cv2.resize(img, (int(cw * s), int(ch * s)), interpolation=cv2.INTER_LINEAR); ch, cw = c.shape[:2]
    y0, x0 = (h - ch) // 2, (w - cw) // 2
    m = np.zeros((ch, cw), np.uint8); r = 28
    cv2.rectangle(m, (r, 0), (cw - r, ch), 255, -1); cv2.rectangle(m, (0, r), (cw, ch - r), 255, -1)
    for cx_, cy_ in [(r, r), (cw - r, r), (r, ch - r), (cw - r, ch - r)]: cv2.circle(m, (cx_, cy_), r, 255, -1)
    sh = np.zeros((h, w), np.float32); sh[y0 + 14:y0 + ch + 14, x0 + 8:x0 + cw + 8] = m / 255.0; sh = cv2.GaussianBlur(sh, (0, 0), 18)[..., None]
    bg = (bg * (1 - .6 * sh)).astype(np.uint8)
    roi = bg[y0:y0 + ch, x0:x0 + cw]; a = (m / 255.0)[..., None]
    bg[y0:y0 + ch, x0:x0 + cw] = (c * a + roi * (1 - a)).astype(np.uint8)
    cv2.rectangle(bg, (x0 - 3, y0 - 3), (x0 + cw + 3, y0 + ch + 3), (150, 200, 0), 0)
    return bg
def visual(V, w, h):
    img = broll(V[0], V[1]); p = V[2]
    if img is None: return np.zeros((h, w, 3), np.uint8)
    if img.shape[0] > img.shape[1] * 1.1 and w > h * 0.9:      # portrait clip into a wide box -> card
        return card(img, w, h, p)
    return grade(cover(img, w, h, p), lift=False)

def compose(src, fr, i):
    f = grade(src)
    if fr.get('des'): f = desat(f)
    V = fr.get('V'); L = fr['L']
    if L in ('side', 'tside'):
        out = np.zeros_like(f)
        sp = zoom(f, fr.get('z', 1.0))
        out[:, PANEL_X:] = sp[:, SIDE_SRC_X:SIDE_SRC_X + (W - PANEL_X)]
        if V: out[:, :PANEL_X] = visual(V, PANEL_X, H)
        f = out
    elif L == 'full':
        if V: f = visual(V, W, H)
    else:
        f = zoom(f, fr.get('z', 1.0))
    p = f'{WD}ov/{i:05d}.png'
    if os.path.exists(p):
        ov = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if ov.shape[2] == 3: return ov
        a = ov[..., 3:4].astype(np.float32) / 255.0
        f = (ov[..., :3].astype(np.float32) * a + f.astype(np.float32) * (1 - a)).astype(np.uint8)
    return f

def reader():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', WD + 'src.mkv', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
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
        os.makedirs(WD + 'prev', exist_ok=True)
        for i in sorted(prev):
            src = rd.send(int(round(frames[i]['ts'] * FPS)))
            cv2.imwrite(f'{WD}prev/{i:05d}.jpg', compose(src.copy(), frames[i], i), [cv2.IMWRITE_JPEG_QUALITY, 85])
        sys.exit()
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
        '-i', WD + 'audio/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
        '-pix_fmt', 'yuv420p', '-c:a', 'pcm_s16le', '-shortest', WD + 'comp_1x.mkv'], stdin=subprocess.PIPE)
    for i, fr in enumerate(frames):
        src = rd.send(int(round(fr['ts'] * FPS)))
        enc.stdin.write(compose(src.copy(), fr, i).tobytes())
        if i % 600 == 0: print(i, len(frames), flush=True)
    enc.stdin.close(); enc.wait()
