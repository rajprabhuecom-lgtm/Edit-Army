#!/bin/bash
# build -> overlay frames (4 workers) -> audio -> composite in 4 parallel chunks -> concat -> finish
set -e; V=$1; O=$2; P=/home/user/Edit-Army/videos/202603/pipeline; D=/home/user/w/$V
python3 $P/build.py $V
rm -f $D/ov/*.png $D/part*.mkv
for k in 0 1 2 3; do node $P/render.js $V $k 4 & done; wait
python3 $P/mix.py $V
for k in 0 1 2 3; do python3 $P/comp.py $V --part $k 4 & done; wait
printf "file '%s'\n" $D/part0.mkv $D/part1.mkv $D/part2.mkv $D/part3.mkv > $D/parts.txt
ffmpeg -v error -y -f concat -safe 0 -i $D/parts.txt -i $D/audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a pcm_s16le -shortest $D/comp_1x.mkv
bash $P/finish.sh $V $O
rm -f $D/part*.mkv
