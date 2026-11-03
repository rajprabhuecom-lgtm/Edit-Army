"""v3 patch over the v2 final: (1) N02 split panel (top 864 px) re-rendered with the client's new 46 kg photo sk46b,
(2) 'வயிறு நிறைய' caption + VEG/NON-VEG card: frames rebuilt from the 2nd clip (grade + punch zoom + engine overlay + logo).
python3 patch_v3.py jobs | preview j... | run"""
import json, sys, subprocess, numpy as np, cv2
sys.path.insert(0, '/home/user/Edit-Army/engine/v6-wellfit-club'); import comp   # grade(), zoom()
F, OUT = '/home/user/w/v2.mp4', '/home/user/w/final_v3.mp4'
CLIP, CLIP0 = '/home/user/w/src/2nd.mp4', 14.957      # 2nd v starts at 14.957 s in src.mkv
W, H, OFF, NF = 1080, 1920, -2, 2018
sys.path.insert(0, '/home/user/Edit-Army/videos/coach-shanmugam/transformation-ad'); import plan
tl = json.load(open('/home/user/w/gfx/timeline.json')); frames = json.load(open('/home/user/w/frames.json'))
n02 = next((i['t0'], i['t1']) for i in tl['items'] if i.get('id') == 'N02')
vay = next((i['t0'], i['t1']) for i in tl['items'] if 'வயிறு' in i.get('html', ''))
def t1x(j): return (1.2 * j + OFF) / 30
def kind(j):
    t = t1x(j)
    if n02[0] <= t < n02[1]: return 'N02'
    if vay[0] <= t < vay[1]: return 'VAY'
LS, LX, LY = 170, 1080 - 170 - 28, 890
lg = cv2.resize(cv2.imread('/home/user/w/photos/sk_logo.png', cv2.IMREAD_UNCHANGED), (LS, LS), interpolation=cv2.INTER_AREA)
la = lg[..., 3:].astype(np.float32) / 255; lc = lg[..., :3].astype(np.float32)
sh = np.zeros((H, W), np.float32); cv2.circle(sh, (LX + LS // 2, LY + LS // 2 + 6), LS // 2 + 4, 1, -1); sh = cv2.GaussianBlur(sh, (0, 0), 8)[..., None] * 0.45
def logo(f):
    f = f.astype(np.float32) * (1 - sh); r = f[LY:LY + LS, LX:LX + LS]; f[LY:LY + LS, LX:LX + LS] = lc * la + r * (1 - la)
    return np.clip(f, 0, 255).astype(np.uint8)
def ovl(j):
    return cv2.imread(f'/home/user/w/patch/{j:05d}.png', cv2.IMREAD_UNCHANGED)
def blend(f, o):
    a = o[..., 3:].astype(np.float32) / 255; return (o[..., :3] * a + f * (1 - a)).astype(np.uint8)
def clipframe(ts):
    """src.mkv frame: clip scaled to 1080 wide, cropped 1080x1920 from the top"""
    k = int(round((ts - CLIP0) * 30))
    if k not in CF: raise KeyError(k)
    return CF[k]
CF = {}
GAIN = np.array(json.load(open('/home/user/w/gain.json'))) if __import__('os').path.exists('/home/user/w/gain.json') else None
def load_clip():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', CLIP, '-vf', 'scale=1080:-2,crop=1080:1920:0:0', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    k = 0
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: return
        CF[k] = np.frombuffer(b, np.uint8).reshape(H, W, 3); k += 1
def fix(f, j):
    k = kind(j)
    if k == 'N02':
        f = f.copy(); f[:864] = blend(np.zeros((864, W, 3), np.float32), ovl(j)[:864]); return f
    if k == 'VAY':
        t = t1x(j); i = min(len(frames) - 1, int(round(t * 30))); ts = plan.o2s(t)
        g = comp.zoom(comp.grade(clipframe(ts).copy()), frames[i]['z'])
        if GAIN is not None: g = np.clip(g * GAIN, 0, 255).astype(np.uint8)   # match v2's colour (re-encode drift)
        return logo(blend(g.astype(np.float32), ovl(j)))
    return f
def vframes():
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', F, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: return
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
if __name__ == '__main__':
    m = sys.argv[1]
    if m == 'jobs':
        js = [[f'{j:05d}', t1x(j)] for j in range(NF) if kind(j)]; json.dump(js, open('/home/user/w/jobs.json', 'w')); print(len(js), n02, vay); sys.exit()
    load_clip()
    if m == 'preview':
        want = set(int(x) for x in sys.argv[2:])
        for j, f in enumerate(vframes()):
            if j in want:
                cv2.imwrite(f'/home/user/w/prev/{j:05d}_v3.jpg', fix(f, j), [cv2.IMWRITE_JPEG_QUALITY, 88]); cv2.imwrite(f'/home/user/w/prev/{j:05d}_v2.jpg', f, [cv2.IMWRITE_JPEG_QUALITY, 88])
            if j >= max(want): break
    else:
        enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-i', F,
            '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
            '-c:a', 'copy', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
        n = p = 0
        for j, f in enumerate(vframes()):
            enc.stdin.write(fix(f, j).tobytes()); n += 1; p += kind(j) is not None
        enc.stdin.close(); enc.wait(); print('frames', n, 'patched', p)
