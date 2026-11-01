#!/bin/bash
# preview.sh <workdir> : render ~18 frames, composite, contact sheet -> <wd>prev/sheet.jpg
WD=$1; cd $WD
N=$(python3 -c "import json;print(len(json.load(open('frames.json'))['frames']))")
python3 -c "
import json;n=$N;tl=json.load(open('timeline.json'))
idx=set(int(n*k/14) for k in range(14))
for it in tl['items']:
    if it.get('layout'): idx.add(int((it['t0']+min(2.2,(it['t1']-it['t0'])*.8))*30))
idx={min(n-1,i) for i in idx}; json.dump(sorted(idx),open('prev/idx.json','w')); print(len(idx))"
rm -f prev/*.jpg
node /home/user/work/pipe/render.js $WD 0 1 prev/idx.json
python3 /home/user/work/pipe/comp.py $WD $(python3 -c "import json;print(' '.join(map(str,json.load(open('prev/idx.json')))))")
ffmpeg -v error -y -pattern_type glob -i 'prev/0*.jpg' -vf "scale=270:-1,tile=8x3:padding=4" -frames:v 1 prev/sheet.jpg
