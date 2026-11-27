#!/bin/bash
# Quality pass on the jump-cut source (v6.2): temporal denoise -> exposure/midtone lift -> warm skin, keep cool shadows -> saturation -> light sharpen.
# Tuned on Coach Pradheesh C0073 (face L 43 -> 51 on dark curtain). Then run comp.py with NOGRADE=1.
set -e; cd /home/user/w
[ -f cut_raw.mkv ] || mv cut.mkv cut_raw.mkv
G="hqdn3d=1.5:1.2:3:3,curves=master='0/0 0.05/0.045 0.2/0.235 0.42/0.53 0.65/0.76 0.85/0.92 1/1',colorbalance=rs=-0.02:bs=0.03:rm=0.035:bm=-0.03:rh=0.01:bh=-0.01,eq=saturation=1.1:contrast=1.03,unsharp=5:5:0.55:5:5:0"
ffmpeg -v error -y -i cut_raw.mkv -vf "$G" -c:v libx264 -preset fast -crf 10 -r 25 cut.mkv
