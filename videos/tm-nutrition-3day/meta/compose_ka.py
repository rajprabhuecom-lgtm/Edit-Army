"""Make 9:16 still clips of Kirthika & Anand's before/after photos for Ad 1 (KA_kirthika.mp4, KA_anand.mp4, KA_both.mp4).
Photos (client-supplied, kept out of git): source/clients/kirthika_before_after.jpg, anand_before_after.jpg"""
import cv2, numpy as np, subprocess, sys
SRC = '/home/user/Edit-Army/videos/tm-nutrition-3day/source/clients/'; OUT = sys.argv[1]
W, H = 1080, 1920
def bg():
    y, x = np.mgrid[0:H, 0:W]; r = np.sqrt(((x - 540) / 900) ** 2 + ((y - 900) / 1100) ** 2)
    c = np.clip(1 - r, 0, 1)[..., None]
    return (np.array([13, 11, 8]) * (1 - c) + np.array([30, 36, 19]) * c).astype(np.uint8)   # obsidian -> dark green glow (BGR)
def place(canvas, img, cx, cy, w, h, border=(150, 200, 0)):
    s = min(w / img.shape[1], h / img.shape[0]); im = cv2.resize(img, (int(img.shape[1] * s), int(img.shape[0] * s)), interpolation=cv2.INTER_AREA)
    ih, iw = im.shape[:2]; x0, y0 = int(cx - iw / 2), int(cy - ih / 2)
    sh = np.zeros((H, W), np.float32); sh[y0 + 16:y0 + ih + 16, x0 + 10:x0 + iw + 10] = 1; sh = cv2.GaussianBlur(sh, (0, 0), 22)[..., None]
    canvas[:] = (canvas * (1 - .65 * sh)).astype(np.uint8)
    cv2.rectangle(canvas, (x0 - 6, y0 - 6), (x0 + iw + 5, y0 + ih + 5), border, -1)
    canvas[y0:y0 + ih, x0:x0 + iw] = im
k = cv2.imread(SRC + 'kirthika_before_after.jpg')
a = cv2.imread(SRC + 'anand_before_after.jpg')[18:588, 195:702]      # crop to the photo pair (drops the white page + disclaimer bar)
for name, layout in [('kirthika', [(k, 540, 930, 1000, 1240)]), ('anand', [(a, 540, 930, 1000, 1150)]),
                     ('both', [(k, 540, 575, 1000, 690), (a, 540, 1250, 1000, 600)])]:
    c = bg()
    for img, cx, cy, w, h in layout: place(c, img, cx, cy, w, h)
    cv2.imwrite(f'{OUT}/KA_{name}.png', c)
    subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-loop', '1', '-i', f'{OUT}/KA_{name}.png', '-t', '8', '-r', '30', '-c:v', 'libx264', '-crf', '14',
                    '-pix_fmt', 'yuv420p', f'{OUT}/KA_{name}.mp4'], check=True)
print('ok')
