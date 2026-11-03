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
  v6-weight-loss/              New Life Nutritions (3 Nov 2026): v5 + two joined sources (coach + testimonial) with per-source
                               split crop / zoom centre in comp.py. New: ba (before/after photo reveal) struggle (X or ✓ cards)
                               steps (personalized path) ticket (offer coupon over face) nlend (end card)
videos/                        One folder per video (see videos/README.md)
```

Each `engine.html` version is standalone, with its own scene set. To use a scene from another version, copy its `S.<name>=` function into the engine you're using.

## Pipeline

1. **Transcribe.** silencedetect, then Whisper (large-v3 or medium.en via sherpa-onnx; load one recognizer at a time). Translate per phrase for meaning.
2. **Plan.** Copy `engine/base/plan.py` (or `v3-lead-quality/plan.py`, which is newer) and fill in BROLL / GFX / CAP / PUNCH / MUSIC / SFX for the new video. Write `broll_plan.csv`.
3. **Preview.** Render 15–20 overlay frames with `gfx/render.py` and composite them with `comp.py <idx...>`. Check them before the full render.
4. **Render.** `gfx/render.py` (2 workers), `audio/mix.py`, `comp.py`, then `speed.sh`.
5. **Deliver.** The MP4 plus the B-roll log, with placeholder scenes (testimonials, proof) flagged.

The scripts expect a work folder at `/home/claude/w/` containing `src.mp4`, `segs.json`, `gfx/`, `audio/`, `ov/` and `prev/`. Change those paths if you run it somewhere else.

**Dependencies:** ffmpeg, Python 3 with numpy, scipy, soundfile, opencv-python and playwright (Chromium), and Node `@fontsource/montserrat`, `@fontsource/anton` and `@fontsource/noto-sans-tamil` (`engine.html` loads fonts from `node_modules/`).

## Brand

Obsidian `#080A0D` · Emerald `#00C896` (value) · Yellow `#FFD60A` (urgency) · Red `#FF3B30` (loss) · Montserrat Black, Noto Sans Tamil Black, Anton.
