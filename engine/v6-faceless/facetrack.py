"""Build a talking-head track that matches voice.py's cuts + speed exactly (each kept span + 0.12 s, then sped up).
python3 facetrack.py <source.mp4> <spans.json> <speed> <out.mkv>"""
import json, sys, subprocess
src, sp, speed, out = sys.argv[1], json.load(open(sys.argv[2])), float(sys.argv[3]), sys.argv[4]
f = ''.join(f'[0:v]trim={s:.3f}:{e + 0.12:.3f},setpts=PTS-STARTPTS[v{i}];' for i, (s, e) in enumerate(sp))
f += ''.join(f'[v{i}]' for i in range(len(sp))) + f'concat=n={len(sp)}:v=1:a=0,setpts=PTS/{speed},fps=30[o]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-filter_complex', f, '-map', '[o]', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast', out], check=True)
print(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout.strip(), 's')
