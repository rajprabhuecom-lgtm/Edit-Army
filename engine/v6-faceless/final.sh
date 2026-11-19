#!/bin/bash
# Mux composite + mix into the delivery MP4, then QA: loudness + 20-frame contact sheet.  final.sh <workdir> <out.mp4>
set -e; W=$1; O=$2
ffmpeg -v error -y -i $W/video.mp4 -i $W/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -shortest -movflags +faststart "$O"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 "$O" | tr '\n' ' '; echo
ffmpeg -i "$O" -af ebur128=peak=true -f null - 2>&1 | grep -A14 Summary | grep -E "I:|Peak:"
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$O")
ffmpeg -v error -y -i "$O" -vf "fps=20/$D,scale=216:384,tile=10x2" -frames:v 1 "${O%.mp4}_qa.jpg"
