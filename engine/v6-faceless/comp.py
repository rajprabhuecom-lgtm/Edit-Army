"""Faceless composite: per frame, base = graded video clip (with push-in) if a clip is active, else black;
then alpha-blend the HTML overlay/scene PNG. python3 comp.py <workdir> [preview frame idx ...]"""
import json, sys, os, subprocess, numpy as np, cv2
W_, H, FPS = 1080, 1920, 30
WD = sys.argv[1]; TL = json.load(open(WD + '/timeline.json')); N = round(TL['total'] * FPS)
x = np.arange(256) / 255.0
def curve(v): s = v - 0.05 * np.sin(2 * np.pi * v); return np.clip(np.where(s > .85, .85 + (s - .85) * .7, s), 0, 1)
LUT = np.dstack([np.clip(curve(x * .97) * 255, 0, 255), np.clip(curve(x) * 255, 0, 255), np.clip(curve(np.minimum(1, x * 1.03 + .01)) * 255, 0, 255)]).astype(np.uint8).reshape(256, 1, 3)
def grade(f):
    g = cv2.LUT(f, LUT); hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV); hsv[..., 1] = np.clip(hsv[..., 1] * 1.1, 0, 255).astype(np.uint8)
    g = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR); bl = cv2.GaussianBlur(g, (0, 0), 1.4); return cv2.addWeighted(g, 1.3, bl, -.3, 0)
def prep(c, k):
    """normalise one clip use to 1080x1920@30, speed applied, Veo sparkle cropped out (bottom-right)"""
    out = f"{WD}/clipcache/{k:02d}.mkv"
    if os.path.exists(out): return out
    os.makedirs(WD + '/clipcache', exist_ok=True); r = c.get('rate', 1.0); dur = (c['t1'] - c['t0']) * r + .3
    if c.get('fit') == 'blur':  # landscape / low-res real footage: blurred fill + sharp band in the middle
        fh = c.get('fh', 1150)
        vf = (f"setpts=PTS/{r},fps=30,split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=40:2,eq=brightness=-0.12[bg];"
              f"[b]scale=-2:{fh},crop=min(iw\\,1080):{fh}[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2")
    else: vf = f"setpts=PTS/{r},fps=30,scale=1210:2150:force_original_aspect_ratio=increase,crop=1080:1920:(iw-1080)*{c.get('cx',.2)}:(ih-1920)*{c.get('cyf',.2)}"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(c.get('ss', 0)), '-t', str(dur), '-i', c['file'], '-an', '-vf', vf, '-c:v', 'ffv1', out], check=True)
    return out
RD = {}
def clipframe(k, c, j):
    r = RD.get(k)
    if r is None or j < r['j']:
        if r: r['p'].kill()
        r = RD[k] = dict(p=subprocess.Popen(['ffmpeg', '-v', 'error', '-i', prep(c, k), '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE), j=-1, f=None)
    while r['j'] < j:
        b = r['p'].stdout.read(W_ * H * 3)
        if len(b) < W_ * H * 3: break
        r['f'] = np.frombuffer(b, np.uint8).reshape(H, W_, 3); r['j'] += 1
    return r['f']
def frame(i):
    t = i / FPS; f = np.zeros((H, W_, 3), np.uint8)
    for k, c in enumerate(TL['clips']):
        if c['t0'] <= t < c['t1']:
            src = clipframe(k, c, int((t - c['t0']) * FPS))
            if src is not None:
                p = (t - c['t0']) / (c['t1'] - c['t0']); z = c.get('z0', 1.0) + (c.get('z1', 1.08) - c.get('z0', 1.0)) * p
                cy = c.get('fy', H / 2); dx = c.get('dx', 0) + c.get('pan', 0) * p
                M = np.float32([[z, 0, W_ / 2 - z * W_ / 2 + dx], [0, z, cy - z * cy]])
                f = grade(cv2.warpAffine(src, M, (W_, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT))
            break
    p = f'{WD}/ov/{i:05d}.png'
    if os.path.exists(p):
        ov = cv2.imread(p, cv2.IMREAD_UNCHANGED)
        if ov.ndim == 2: ov = cv2.cvtColor(ov, cv2.COLOR_GRAY2BGR)
        if ov.shape[2] == 3: return ov
        a = ov[..., 3:4].astype(np.float32) / 255
        f = (ov[..., :3] * a + f * (1 - a)).astype(np.uint8)
    return f
if __name__ == '__main__':
    prev = [int(a) for a in sys.argv[2:]]
    if prev:
        for i in prev: cv2.imwrite(f'{WD}/prev_{i:05d}.jpg', frame(i))
        sys.exit()
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W_}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', WD + '/video.mp4'], stdin=subprocess.PIPE)
    for i in range(N):
        enc.stdin.write(frame(i).tobytes())
        if i % 300 == 0: print('comp', i, N, flush=True)
    enc.stdin.close(); enc.wait()
