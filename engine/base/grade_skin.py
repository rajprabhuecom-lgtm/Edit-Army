"""Skin-glow grade (face-aware), for talking-head footage. Works per frame (BGR uint8) and is fast enough for comp.py.
Steps:
  1. base look: gentle exposure lift, soft S-curve, warm white balance, highlight roll-off (keeps a white shirt from clipping)
  2. skin mask: YCrCb skin range AND a feathered region around the face/neck (MediaPipe landmarks if given, else skin range only)
  3. on skin only: +luminance (glow), warmer/golden hue, mild saturation, edge-preserving smoothing (bilateral, ~35%), soft bloom
  4. elsewhere: slight teal in the shadows for separation (orange-teal, subtle)
usage (test): python3 grade_skin.py in.jpg out.jpg"""
import cv2, numpy as np

def _curve(x, lift=0.02, s=0.10, roll=0.90):
    y = x + lift * (1 - x)                                   # lift shadows a little
    y = y + s * np.sin(np.pi * (y - .5)) * .25 * 0 + s * (y - .5) * (1 - abs(2 * y - 1)) * .9   # soft S
    y = np.where(y > roll, roll + (y - roll) * .75, y)      # roll off only the very top (shirt stays white)
    return np.clip(y, 0, 1)
_x = np.arange(256) / 255.0
_LUT = np.dstack([np.clip(_curve(_x * .985) * 255, 0, 255), np.clip(_curve(_x * 1.0) * 255, 0, 255),
                  np.clip(_curve(np.minimum(1, _x * 1.02)) * 255, 0, 255)]).astype(np.uint8).reshape(256, 1, 3)   # B,G,R: warm WB

def skin_mask(img, face_box=None):
    ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    m = cv2.inRange(ycc, (40, 135, 80), (245, 178, 130)).astype(np.float32) / 255
    if face_box is not None:                                 # keep skin near the face/neck/hands, ignore skin-coloured walls/lamps
        x0, y0, x1, y1 = face_box; reg = np.zeros(m.shape, np.float32)
        w, h = x1 - x0, y1 - y0
        cv2.rectangle(reg, (int(x0 - .9 * w), int(y0 - .4 * h)), (int(x1 + .9 * w), int(y1 + 2.8 * h)), 1, -1)
        m *= cv2.GaussianBlur(reg, (0, 0), w * .25 + 1)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    return cv2.GaussianBlur(m, (0, 0), 6)[..., None]

def grade(img, face_box=None, glow=1.0):
    base = cv2.LUT(img, _LUT)
    hsv = cv2.cvtColor(base, cv2.COLOR_BGR2HSV).astype(np.float32); hsv[..., 1] *= 1.04
    base = cv2.cvtColor(np.clip(hsv, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)
    # subtle teal in deep shadows (not on skin)
    lum = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)[..., None] / 255
    sh = np.clip(1 - lum / .35, 0, 1) * .06
    base = base * (1 - sh) + sh * np.array([150, 120, 40], np.float32)
    m = skin_mask(img, face_box) * glow
    # skin: smooth (edge-preserving), brighten, warm, bloom
    sm = cv2.bilateralFilter(base.astype(np.uint8), 9, 28, 9).astype(np.float32)
    sk = base * .70 + sm * .30
    sk = sk * 1.035 + 3                                      # small luminance lift (glow, not whitening)
    sk += np.array([-5, 1, 6], np.float32)                   # B,G,R: golden warmth
    hs = cv2.cvtColor(np.clip(sk, 0, 255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32); hs[..., 1] *= 1.08   # healthy colour
    sk = cv2.cvtColor(np.clip(hs, 0, 255).astype(np.uint8), cv2.COLOR_HSV2BGR).astype(np.float32)
    bloom = cv2.GaussianBlur(sk, (0, 0), 14)
    sk = 255 - (255 - sk) * (255 - bloom * .14) / 255        # soft screen glow
    out = base * (1 - m) + np.clip(sk, 0, 255) * m
    # keep neutral whites (shirt) clean: undo warmth on low-saturation bright pixels
    hsv0 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32); wm = (np.clip((hsv0[..., 2] - 170) / 60, 0, 1) * np.clip((40 - hsv0[..., 1]) / 30, 0, 1))[..., None]
    neutral = out.mean(axis=2, keepdims=True); out = out * (1 - wm * .7) + neutral * wm * .7
    # gentle overall clarity
    bl = cv2.GaussianBlur(out, (0, 0), 1.2)
    out = cv2.addWeighted(out, 1.18, bl, -0.18, 0)
    return np.clip(out, 0, 255).astype(np.uint8)

if __name__ == '__main__':
    import sys
    im = cv2.imread(sys.argv[1]); fb = tuple(int(v) for v in sys.argv[3].split(',')) if len(sys.argv) > 3 else None
    cv2.imwrite(sys.argv[2], grade(im, fb))
