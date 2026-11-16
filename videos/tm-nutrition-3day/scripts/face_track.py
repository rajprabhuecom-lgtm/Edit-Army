"""Per-frame face analysis of the coach (MediaPipe FaceLandmarker on a crop around the head).
usage: python3 face_track.py video.mp4 out.json t_start t_end
Writes [[t, present, lip_gap, jawOpen, cx, cy], ...]  lip_gap = inner-lip distance / face height (mouth opening).
Model: /root/models/face_landmarker.task (storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/)."""
import sys, json, cv2, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
f, out, t0, t1 = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path='/root/models/face_landmarker.task'),
     running_mode=vision.RunningMode.VIDEO, num_faces=1, output_face_blendshapes=True))
cap = cv2.VideoCapture(f); cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000)
cx, cy, S = 910, 360, 700          # crop centre follows the face
res = []; last = -1
while True:
    ok, fr = cap.read()
    if not ok: break
    t = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
    if t > t1: break
    H, W = fr.shape[:2]; x0 = int(min(W - S, max(0, cx - S / 2))); y0 = int(min(H - S, max(0, cy - S / 2)))
    c = cv2.resize(fr[y0:y0 + S, x0:x0 + S], (480, 480))
    ms = int(t * 1000)
    if ms <= last: ms = last + 1
    last = ms
    r = lm.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(c, cv2.COLOR_BGR2RGB)), ms)
    if not r.face_landmarks: res.append([round(t, 3), 0, 0, 0, cx, cy]); continue
    L = r.face_landmarks[0]; sc = S / 480 * 480   # landmarks are normalised to the crop
    gap = abs(L[14].y - L[13].y) / max(1e-6, abs(L[152].y - L[10].y))
    jaw = next(b.score for b in r.face_blendshapes[0] if b.category_name == 'jawOpen')
    fx = x0 + L[1].x * S; fy = y0 + L[1].y * S
    cx, cy = 0.9 * cx + 0.1 * fx, 0.9 * cy + 0.1 * fy
    res.append([round(t, 3), 1, round(gap, 4), round(jaw, 4), round(fx), round(fy)])
json.dump(res, open(out, 'w'))
print('done', f, t0, t1, len(res), sum(r[1] for r in res))
