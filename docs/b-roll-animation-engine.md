# B-Roll Animation Engine (ProfitSoul EDITING ARMY) — reusable code bundle
 
Built 23 Oct 2026 for comm4 (AI Agents community) and 10octwc (Walk-In Engine). Every new edit reuses these files: only plan.py's BROLL / GFX / CAP / PUNCH / MUSIC / SFX lists change, plus any new scene functions added to engine.html.
 
**Pipeline:** silencedetect → whisper large-v3 (sherpa-onnx, GitHub release; load ONE recognizer at a time or it runs out of memory) translate per phrase → plan.py (jump cuts + timeline) → gfx/render.py (Playwright, 2 workers, transparent PNG per frame) → audio/mix.py (voice chain, SFX, original BGM from synth.py, sidechain duck) → comp.py (grade, zoom, split layout, desat, overlay) → speed.sh (1.2x + two-pass loudnorm −14 LUFS).
 
**Layout rules baked in:** split = scene in top 864 px (content must end by ~640 px), speaker crop from source y=230 in the bottom; captions move to y=668 in split, y=235 during CTAs, 1175 otherwise; full-cutaway scenes keep content clear of 1175–1475 or set nocap.

## Where the code lives

The Word doc held the code with its indentation stripped. The working, re-indented copies are in this repo:

| File | What it does |
|---|---|
| [`engine/base/gfx/engine.html`](../engine/base/gfx/engine.html) | Overlay engine: scenes, on-face graphics, karaoke captions |
| [`engine/base/plan.py`](../engine/base/plan.py) | EDL: jump cuts, B-roll map, GFX, captions, zooms, music, SFX (example data: comm4) |
| [`engine/base/gfx/render.py`](../engine/base/gfx/render.py) | Playwright renderer, transparent PNG per frame |
| [`engine/base/comp.py`](../engine/base/comp.py) | Composite: grade, zoom, split layout, desat, overlay |
| [`engine/base/audio/synth.py`](../engine/base/audio/synth.py) | Original procedural BGM moods + SFX (no licence needed) |
| [`engine/base/audio/mix.py`](../engine/base/audio/mix.py) | Voice chain, SFX bus, BGM, sidechain duck, loudnorm |
| [`engine/base/speed.sh`](../engine/base/speed.sh) | 1.2x speed + two-pass loudnorm to −14 LUFS, final MP4 |

The original .docx is kept in [`docs/originals/`](originals/).
