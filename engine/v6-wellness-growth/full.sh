#!/bin/bash
# full.sh <workdir> <outname.mp4>
set -e
WD=$1; cd $WD; T0=$(date +%s)
if [ -z "$SKIPOV" ]; then rm -rf ov; mkdir -p ov
for w in 0 1 2 3; do node /home/user/work/pipe/render.js $WD $w 4 > render_$w.log 2>&1 & done; fi
python3 /home/user/work/pipe/mix.py $WD > mix.log 2>&1
wait
grep -h ERR render_*.log || true
echo "overlays done $(( $(date +%s)-T0 ))s"
python3 /home/user/work/pipe/comp.py $WD > comp.log 2>&1
echo "comp done $(( $(date +%s)-T0 ))s"
/home/user/work/pipe/speed.sh $WD "$WD/$2"
echo "ALL DONE $(( $(date +%s)-T0 ))s"
