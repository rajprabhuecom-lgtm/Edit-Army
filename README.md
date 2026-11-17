# Edit Army: ProfitSoul video editing kit

Everything needed to edit talking-head sales videos, Reels and ads in the ProfitSoul style: jump cuts, 1.2× speed, karaoke captions, zoom punches, animated B-roll, original BGM and SFX, pulsing CTA and end card.

**Rule #1:** every edit ships with animated B-roll. See [`docs/b-roll-mandatory-rule.md`](docs/b-roll-mandatory-rule.md).

## What's in here

```
docs/
  b-roll-mandatory-rule.md     The rule: B-roll on every edit, where the face stays, workflow, QA
  b-roll-framework.md          Full framework: coverage/timing, source hierarchy P1–P5, layouts, AI prompts, compliance
  b-roll-animation-engine.md   Pipeline + layout rules, and an index of the engine files
  originals/                   The files exactly as uploaded (.docx and .txt)
engine/
  base/                        Full pipeline (comm4 / 10octwc, 23 Oct 2026)
    plan.py                    EDL: cuts, BROLL, GFX, CAP, PUNCH, MUSIC, SFX
    gfx/engine.html            Scenes: agents laptop seats voiceads live weeks whatsapp costs affordable
                               walkin days centres testis transform chart pin + text price stamp cta badge endcard
    gfx/render.py              Playwright -> transparent PNG overlay frames
    comp.py                    Grade + zoom + split layout + desat + overlay
    audio/synth.py, mix.py     Original BGM moods + SFX, voice chain, ducking, loudness
    speed.sh                   1.2× + two-pass loudnorm −14 LUFS -> final MP4
  v3-lead-quality/             sun_ads (26 Oct 2026): engine.html + plan.py
                               clientmsg leadrain methods cpl pipeline chatq filter crm booking revenue
                               testi livedemo implement time + flash item, per-scene SFX (SCENE_SFX)
  v4-sleep-wellness/           Naheed Khan (28 Oct 2026): engine.html
                               nightcity years awake hotac clockwatch targets battery retrain career creds
                               protocol zoomlive hypno steps seats guide name lightsoff house awake2 mindloop
                               alarm sleepback twocountry indiacities sleepcurve care + client endcard
  v5-family-health/            Coach Muthu (31 Oct 2026): engine.html (v3 + Tamil font) + render.js (Node Playwright)
                               + comp.py with video B-roll support. New: vid questions checkup mappin days client endcard
  v6-vsl-landscape/            TM Nutrition VSL (16 Nov 2026): first 16:9 (1920x1080) engine for landscape VSLs.
                               Layouts: full, side (animation 0-1152 + speaker panel), tside (portrait testimonial card + speaker).
                               engine.html scenes: tally pain(diet/gym/midnight/tomorrow) pattern q3days agenda habits famhealth
                               happy money stack testi vid + text badge price stamp cta lower flash endcard.
                               render.js <workdir>, comp.py (portrait clips -> card on blurred copy), mix.py (testimonial bites
                               with their own audio), speed.sh <workdir> <out.mp4>
  v7-meta-portrait/            TM Nutrition Meta ads (17 Nov 2026): 9:16 (1080x1920) port of v6. All scenes use the panel
                               layout and sit in the middle band (y 360-1590); captions on the chest band. comp.py reads the
                               frame size from comp_cfg.json. Built by videos/tm-nutrition-3day/meta/make_ad.py.
videos/                        One folder per video (see videos/README.md)
```

Each `engine.html` version is standalone, with its own scene set. To use a scene from another version, copy its `S.<name>=` function into the engine you're using.

## Pipeline

1. **Transcribe.** silencedetect, then Whisper large-v3. On CPU, faster-whisper int8 (`videos/tm-nutrition-3day/scripts/transcribe.py`) runs about real time with word timings; sherpa-onnx was ~15x slower. For Tamil, turn temperature fallback off, and re-check garbled stretches in short windows. Translate per phrase for meaning.
   **If someone off camera prompts the lines** (the speaker repeats after a friend), separate the voices before cutting: `scripts/face_track.py` (mouth movement) + `who_speaks.py`, then `voice_id.py` (ECAPA speaker embeddings) to put every cut in the silent gap after the prompter, and `voice_check.py` on the finished voice track. See `videos/tm-nutrition-3day/notes.md`.
2. **Plan.** Copy `engine/base/plan.py` (or `v3-lead-quality/plan.py`, which is newer) and fill in BROLL / GFX / CAP / PUNCH / MUSIC / SFX for the new video. Write `broll_plan.csv`.
3. **Preview.** Render 15–20 overlay frames with `gfx/render.py` and composite them with `comp.py <idx...>`. Check them before the full render.
4. **Render.** `gfx/render.py` (2 workers), `audio/mix.py`, `comp.py`, then `speed.sh`.
5. **Deliver.** The MP4 plus the B-roll log, with placeholder scenes (testimonials, proof) flagged.

The scripts expect a work folder at `/home/claude/w/` containing `src.mp4`, `segs.json`, `gfx/`, `audio/`, `ov/` and `prev/`. Change those paths if you run it somewhere else.

**Dependencies:** ffmpeg, Python 3 with numpy, scipy, soundfile, opencv-python and playwright (Chromium), and Node `@fontsource/montserrat`, `@fontsource/anton` and `@fontsource/noto-sans-tamil` (`engine.html` loads fonts from `node_modules/`).

## Brand

Obsidian `#080A0D` · Emerald `#00C896` (value) · Yellow `#FFD60A` (urgency) · Red `#FF3B30` (loss) · Montserrat Black, Noto Sans Tamil Black, Anton.
