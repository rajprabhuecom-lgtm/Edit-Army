#!/bin/bash
# 1.3x speed + two-pass loudnorm -14 LUFS -> (1) 1080x1920 high-bitrate master, (2) 2160x3840 upload version (lanczos upscale + light sharpen)
set -e
cd /home/user/w; S=1.3; OUT=pradheesh_blueprint_for_success
ffmpeg -v error -y -i comp_1x.mkv -vn -af atempo=$S -ar 48000 a12.wav
J=$(ffmpeg -i a12.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
LN="loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true"
TAGS="-color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart"
ffmpeg -v error -y -i comp_1x.mkv -i a12.wav -filter_complex "[0:v]setpts=PTS/$S[v];[1:a]$LN,aresample=48000[a]" -map "[v]" -map "[a]" -r 30 \
 -c:v libx264 -preset slow -crf 14 -profile:v high -level 4.2 -pix_fmt yuv420p $TAGS -c:a aac -b:a 320k $OUT.mp4
ffmpeg -v error -y -i $OUT.mp4 -vf "scale=2160:3840:flags=lanczos,unsharp=3:3:0.3" -c:v libx264 -preset slow -crf 16 -profile:v high -level 5.1 -pix_fmt yuv420p $TAGS -c:a copy ${OUT}_4K.mp4
for f in $OUT.mp4 ${OUT}_4K.mp4; do ffprobe -v error -show_entries format=duration,bit_rate:stream=width,height -of default=nw=1 $f | tr '\n' ' '; echo; done
ffmpeg -i $OUT.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A12 Summary | grep -E "I:|Peak"
