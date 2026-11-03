# v6-meditation: calm relaxation-audio video

For guided relaxation / sleep / visualisation audio (no face video). Not a sales edit, so jump cuts, speed-up, punches and SFX are off. See `docs/b-roll-mandatory-rule.md` section 4b.

Work folder layout (copy these files in): `winddown.html render.js soundtrack.py cues.py`, plus `face.png` (360×360 square crop of the client photo), `voice_raw.wav`, and `node_modules/` with `@fontsource/cormorant-garamond` and `@fontsource/montserrat`.

1. **Transcribe** with faster-whisper `medium.en`, word timestamps → `segs.json` (pass a numpy array; this pyav build fails on file paths).
2. **Cues + timeline:** `python3 cues.py` → `timeline.json` (cues, sections, breath phases, bowl hits, lantern window; 8 s intro and 26 s tail). Edit the section/breath times by hand from the word timestamps.
3. **Voice clean:** `ffmpeg -i voice_raw.wav -af "highpass=f=75,lowpass=f=11000,afftdn=nf=-32:nr=8,acompressor=threshold=-22dB:ratio=2:attack=20:release=300" -ac 1 voice_clean.wav`
4. **Soundtrack:** `python3 soundtrack.py` → `mix_pre.wav`, then apply a linear gain to −16 LUFS + `alimiter` (not single-pass loudnorm).
5. **Preview:** `node render.js prev 30 0 1 "3,9,160,330,402"` writes JPEGs at those times. Check them first.
6. **Render:** `for i in 0 1 2 3; do node render.js chunks 30 $i 4 & done`, then concat the chunks and mux `mix.wav` (AAC 192k).

Launch Chromium with `--allow-file-access-from-files`, otherwise the photo taints the canvas and `toDataURL` fails.
