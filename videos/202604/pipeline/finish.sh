#!/bin/bash
# speed to 1.2x, loudness -14 LUFS, H.264 delivery.  finish.sh <vid> <outname>
set -e; V=$1; O=$2; D=/home/user/w/$V; cd $D
SP=$(python3 -c "import json;print(json.load(open('audio/cues.json'))['speed'])")
ffmpeg -v error -y -i comp_1x.mkv -vn -af atempo=$SP -ar 48000 a12.wav
J=$(ffmpeg -i a12.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
ffmpeg -v error -y -i comp_1x.mkv -i a12.wav -filter_complex "[0:v]setpts=PTS/$SP[v];[1:a]$LN,aresample=48000[a]" -map "[v]" -map "[a]" -r 30 \
 -c:v libx264 -preset medium -crf 21 -maxrate 6M -bufsize 12M -profile:v high -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart $O
ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 $O | tr '\n' ' '
ffmpeg -i $O -af ebur128=peak=true -f null - 2>&1 | grep -A12 Summary | grep -E " I:|Peak:" | tr -s ' ' | tr '\n' ' '; echo
