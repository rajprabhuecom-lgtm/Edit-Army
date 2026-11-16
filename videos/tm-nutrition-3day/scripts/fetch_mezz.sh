#!/bin/bash
# Download each raw Sony clip from Drive, rotate to portrait, write a 1080x1920 CRF16 working copy + 16k wav, delete the 4K original.
# The originals are shot sideways (3840x2160), so transpose=1 turns them upright.
set -u
SRC=/home/user/Edit-Army/videos/tm-nutrition-3day/source
M=/home/user/w/tm/mezz; mkdir -p $M
while read id name; do
  [ -z "$id" ] && continue
  if [ -f $M/$name.mp4 ]; then echo "skip $name"; continue; fi
  f=$SRC/$name.MP4
  if [ ! -f $f ]; then
    for try in 1 2 3 4 5; do
      curl -sSL --retry 4 -o $f "https://drive.usercontent.google.com/download?id=$id&export=download&confirm=t"
      [ "$(stat -c%s $f 2>/dev/null || echo 0)" -gt 100000 ] && break
      echo "retry $name ($try)"; rm -f $f; sleep $((try*20))
    done
    [ -f $f ] || { echo "FAIL download $name"; continue; }
  fi
  echo "downloaded $name $(stat -c%s $f)"
  ffmpeg -nostdin -v error -y -i $f -vf "transpose=1,scale=1080:1920:flags=lanczos,format=yuv420p" -r 25 -c:v libx264 -preset fast -crf 16 -c:a aac -b:a 320k -ac 2 $M/$name.mp4 \
    && ffmpeg -nostdin -v error -y -i $f -vn -ac 1 -ar 16000 $M/$name.16k.wav \
    || { echo "FAIL mezz $name"; continue; }
  d0=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f </dev/null); d1=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $M/$name.mp4 </dev/null)
  if python3 -c "import sys; sys.exit(0 if abs($d0-$d1)<0.5 else 1)"; then rm -f $f; echo "mezz ok $name $d1"; else echo "FAIL mezz $name duration $d0 vs $d1 (original kept)"; rm -f $M/$name.mp4; fi
done <<LIST
1eYvIF7jw8toUaynhB-vB3wWb1Yam9xlq C0006
1kox57ogurHO6zo68Ke5QUG-pMaUojLfo C0007
1Y2GaoXV_mq0f5FOzn_YMc2nBfH9A29xR C0008
local C0002
1ls0xm_wF7-z9saZCp9kXYooF9QCZ0WNw C0003
1gDrnbpSM3tMsT2RbOm9FwOQdB5M72dcF C0001
LIST
echo ALL DONE
