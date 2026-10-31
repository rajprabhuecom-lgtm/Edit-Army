# Instructions for Claude in this repo

This repo is ProfitSoul's video editing kit (EDITING ARMY). Before editing any video:

1. Read `docs/b-roll-mandatory-rule.md`. Every talking-head video, Reel or ad gets animated B-roll automatically, without being asked.
2. Follow `docs/b-roll-framework.md` for coverage, timing, layouts, source hierarchy and compliance.
3. Reuse the engine in `engine/`. Pick the newest `engine.html` that has the scenes you need, use `engine/v3-lead-quality/plan.py` as the plan template and `engine/base/` for render, comp, audio and speed.
4. Put each video's files under `videos/<video-id>/` (see `videos/README.md`).
5. When you build a new scene, add it to `engine.html`, list it in the scene table in `docs/b-roll-mandatory-rule.md` and the README, and commit it.

Never fake proof, results, customers or testimonials. Never put B-roll over price, guarantee or CTA lines. Never invent numbers.
