#!/bin/bash
# 1.2x speed-up, then BGM mix in final time, then mux. Usage: bash speed.sh <out.mp4>
set -e
OUT=${1:-final.mp4}; cd /home/user/w; A=audio
ffmpeg -v error -y -i comp_1x.mkv -vn -af atempo=1.2 -ar 48000 $A/a12.wav
ffmpeg -v error -y -i $A/voice.wav -af atempo=1.2 -ar 48000 $A/voice12.wav
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $A/a12.wav)
python3 /home/user/w/mix.py music $DUR
ffmpeg -v error -y -i comp_1x.mkv -i $A/final_mix.wav -filter_complex "[0:v]setpts=PTS/1.2[v]" -map "[v]" -map 1:a -r 30 -shortest \
 -c:v libx264 -preset medium -crf 18 -profile:v high -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart $OUT
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 $OUT
ffmpeg -i $OUT -af ebur128=peak=true -f null - 2>&1 | grep -A12 Summary | grep -E "I:|Peak"
