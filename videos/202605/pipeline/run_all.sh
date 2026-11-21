#!/bin/bash
# full render of one video: build -> overlay frames (4 workers) -> audio -> composite -> finish
set -e; V=$1; O=$2; P=/home/user/Edit-Army/videos/202605/pipeline
python3 $P/build.py $V
rm -f /home/user/w/$V/ov/*.png
for k in 0 1 2 3; do node $P/render.js $V $k 4 & done; wait
python3 $P/mix.py $V
python3 $P/comp.py $V
bash $P/finish.sh $V $O
