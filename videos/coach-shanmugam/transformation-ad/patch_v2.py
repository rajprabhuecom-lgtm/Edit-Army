"""Patch final mp4: (1) re-render N01/N02 top split panel with new photo, (2) re-render end card with logo, (3) logo bug on all other frames.
python3 patch.py jobs | preview j... | run"""
import json, sys, subprocess, numpy as np, cv2
F = '/home/user/w/v1.mp4'   # v1 final (git history: final/coach_shanmugam_transformation_ad.mp4)
OUT = '/home/user/w/final_v2.mp4'
W, H, OFF = 1080, 1920, -2          # final frame j shows 1x time (1.2*j + OFF)/30
tl = json.load(open('/home/user/w/gfx/timeline.json'))
win = {it.get('id') or it['type']: (it['t0'], it['t1']) for it in tl['items'] if it.get('id') in ('N01', 'N02') or it['type'] == 'clubend'}
NF = 2018
def t1x(j): return (1.2 * j + OFF) / 30
def kind(j):
    t = t1x(j)
    for k, (a, b) in win.items():
        if a <= t < b: return k
LS, LX, LY = 170, 1080 - 170 - 28, 890      # logo bug size / position
lg = cv2.imread('/home/user/w/photos/sk_logo.png', cv2.IMREAD_UNCHANGED); lg = cv2.resize(lg, (LS, LS), interpolation=cv2.INTER_AREA)
la = lg[..., 3:].astype(np.float32) / 255; lc = lg[..., :3].astype(np.float32)
sh = np.zeros((H, W), np.float32); cv2.circle(sh, (LX + LS // 2, LY + LS // 2 + 6), LS // 2 + 4, 1, -1); sh = cv2.GaussianBlur(sh, (0, 0), 8)[..., None] * 0.45
def logo(f):
    f = f.astype(np.float32); f = f * (1 - sh)
    r = f[LY:LY + LS, LX:LX + LS]; f[LY:LY + LS, LX:LX + LS] = lc * la + r * (1 - la)
    return np.clip(f, 0, 255).astype(np.uint8)
def ov(j):
    o = cv2.imread(f'/home/user/w/patch/{j:05d}.png', cv2.IMREAD_UNCHANGED)
    if o.shape[2] == 3: return o
    a = o[..., 3:].astype(np.float32) / 255; return (o[..., :3] * a).astype(np.uint8)
def fix(f, j):
    k = kind(j)
    if k == 'clubend': return ov(j)
    if k in ('N01', 'N02') and (f[858:862, 300:780].astype(int) - [150, 200, 0]).__abs__().mean() < 60:   # old frame shows the split border
        f = f.copy(); f[:864] = ov(j)[:864]
    return logo(f)
def frames():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', F, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: return
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
if __name__ == '__main__':
    m = sys.argv[1]
    if m == 'jobs':
        js = [[f'{j:05d}', t1x(j)] for j in range(NF) if kind(j)]
        json.dump(js, open('/home/user/w/jobs.json', 'w')); print(len(js), win)
    elif m == 'preview':
        want = set(int(x) for x in sys.argv[2:])
        for j, f in enumerate(frames()):
            if j in want: cv2.imwrite(f'/home/user/w/prev_{j:05d}.jpg', fix(f, j), [cv2.IMWRITE_JPEG_QUALITY, 88])
            if j > max(want): break
    else:
        enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-i', F,
            '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
            '-c:a', 'copy', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
        n = 0; patched = 0
        for j, f in enumerate(frames()):
            g = fix(f, j); patched += kind(j) is not None; enc.stdin.write(g.tobytes()); n += 1
        enc.stdin.close(); enc.wait(); print('frames', n, 'in windows', patched)
