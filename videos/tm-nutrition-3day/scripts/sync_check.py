"""Measure lip-sync in a finished video: mouth opening (MediaPipe) vs audio loudness, cross-correlated per window.
usage: python3 sync_check.py video.mp4 cx cy crop win_s  (cx,cy = face centre in the frame, crop = square crop size)
Prints, per window, the lag (ms) where mouth and voice line up best. Positive = audio LATE vs picture."""
import sys, numpy as np, cv2, subprocess, soundfile as sf, mediapipe as mp, os
from mediapipe.tasks.python import vision, BaseOptions
f, cx, cy, S, WIN = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path='/root/models/face_landmarker.task'),
     running_mode=vision.RunningMode.VIDEO, num_faces=1))
cap = cv2.VideoCapture(f); fps = cap.get(cv2.CAP_PROP_FPS); gaps = []; i = 0
while True:
    ok, fr = cap.read()
    if not ok: break
    H, W = fr.shape[:2]; x0 = max(0, min(W - S, cx - S // 2)); y0 = max(0, min(H - S, cy - S // 2))
    r = lm.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(cv2.resize(fr[y0:y0 + S, x0:x0 + S], (480, 480)), cv2.COLOR_BGR2RGB)), int(i * 1000 / fps) + 1)
    if r.face_landmarks:
        L = r.face_landmarks[0]; gaps.append(abs(L[14].y - L[13].y) / max(1e-6, abs(L[152].y - L[10].y)))
    else: gaps.append(np.nan)
    i += 1
g = np.array(gaps); t = np.arange(len(g)) / fps
tmp = '/tmp/claude-0/-home-user-Edit-Army/f554cbd9-9e2c-506f-bff0-44d48f2dbf76/scratchpad/sync_a.wav'
subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', f, '-vn', '-ac', '1', '-ar', '16000', tmp], check=True)
a, sr = sf.read(tmp, dtype='float32'); hop = sr / fps
env = np.array([np.sqrt(np.mean(a[int(k * hop):int((k + 1) * hop)] ** 2) + 1e-9) for k in range(len(g))])
env = np.log(env)
for w0 in np.arange(0, t[-1] - WIN, WIN):
    m = (t >= w0) & (t < w0 + WIN) & ~np.isnan(g)
    if m.sum() < WIN * fps * .6: print(f'{w0:6.1f}s  (face not visible)'); continue
    idx = np.where(m)[0]; best = None
    for lag in range(-15, 16):       # frames
        j = idx + lag; ok = (j >= 0) & (j < len(env));
        x = g[idx[ok]]; y = env[j[ok]]
        if x.std() < 1e-4 or y.std() < 1e-4: continue
        c = np.corrcoef(x, y)[0, 1]
        if best is None or c > best[1]: best = (lag, c)
    if best: print(f'{w0:6.1f}s  lag {best[0] * 1000 / fps:+5.0f} ms  (corr {best[1]:.2f})')
