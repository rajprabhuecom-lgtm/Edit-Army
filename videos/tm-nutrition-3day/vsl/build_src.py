"""Cut the selected speaker takes out of the working copies and join them: src.mkv (1920x1080, 30 fps) + src48.wav.
Testimonial bites are cut to broll/ (their own video + audio). Writes takes.json (each take's offset in src time)."""
import json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(__file__)); import importlib
SEL = importlib.import_module(os.environ.get('SELECTS', 'selects')).SEL
W = os.environ.get('WD', '/home/user/w/vsl/');
SPK = {f: json.load(open(f'/home/user/w/tm/speak/{f}L.json'))['client'] for f in ('C0007', 'C0008') if os.path.exists(f'/home/user/w/tm/speak/{f}L.json')}
M = '/home/user/w/tm/mezz/'; T = '/home/user/Edit-Army/videos/tm-nutrition-3day/source/testimonials/'
os.makedirs(W + 'parts', exist_ok=True); os.makedirs(W + 'broll', exist_ok=True)
run = lambda c: subprocess.run(c, check=True)
takes = []; off = 0.0; lst = []
for sid, f, a, b, txt, mean in SEL:
    if f.startswith('T_'):
        out = W + f'broll/{sid}_{f}.mp4'
        run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a}', '-t', f'{b-a}', '-i', T + f + '.mp4', '-vf', 'fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2',
             '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '1', out.replace('.mp4', '.mkv')])
        takes.append(dict(id=sid, kind='bite', file=f, a=a, b=b, dur=round(b - a, 3), clip=os.path.basename(out.replace('.mp4', '.mkv')), text=txt))
        continue
    p = W + f'parts/{sid}.mkv'
    n = round((b - a) * 30); d = n / 30       # exact frame count; audio padded/trimmed to the same length so offsets never drift
    run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a}', '-i', M + f + 'L.mp4', '-vf', 'fps=30', '-frames:v', str(n), '-c:v', 'libx264', '-crf', '12',
         '-preset', 'fast', '-af', f'atrim=end={d},apad=whole_dur={d}', '-c:a', 'pcm_s16le', '-ar', '48000', '-ac', '1', p])
    # coach-speaking stretches inside this take (relative to take start): jump cuts follow the mouth, not the audio
    cl = [[round(max(a, x) - a, 3), round(min(b, y) - a, 3)] for x, y in SPK.get(f, []) if y > a and x < b]
    takes.append(dict(id=sid, kind='take', file=f, a=a, b=b, off=round(off, 3), dur=round(d, 3), text=txt, client=cl)); off += d; lst.append(p)
open(W + 'parts/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in lst))
run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', W + 'parts/list.txt', '-c', 'copy', W + 'src.mkv'])
run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', W + 'src.mkv', '-vn', '-ac', '1', '-ar', '48000', W + 'src48.wav'])
json.dump(takes, open(W + 'takes.json', 'w'), ensure_ascii=False, indent=1)
print('src', round(off, 2), 's,', len(lst), 'takes,', sum(t['kind'] == 'bite' for t in takes), 'bites')
