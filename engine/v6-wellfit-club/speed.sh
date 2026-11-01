#!/bin/bash
set -e
cd /home/user/w
ffmpeg -v error -y -i comp_1x.mkv -vn -af atempo=1.2 -ar 48000 a12.wav
J=$(ffmpeg -i a12.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
ffmpeg -v error -y -i comp_1x.mkv -i a12.wav -filter_complex "[0:v]setpts=PTS/1.2[v];[1:a]$LN,aresample=48000[a]" -map "[v]" -map "[a]" -r 30 \
-c:v libx264 -preset medium -crf 18 -profile:v high -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart coach_shanmugam_wellfit_ad.mp4
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 coach_shanmugam_wellfit_ad.mp4
ffmpeg -i coach_shanmugam_wellfit_ad.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A12 Summary | grep -E "I:|Peak"
