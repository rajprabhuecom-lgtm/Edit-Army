# TM Nutrition: 3-Day Family Wellness Challenge (Coach Pradheesh Mutharasu, Trichy)

**Client:** TM Nutrition Centre, Trichy · **Offer:** 3-day live challenge, ₹555, 100% money-back, only 5 couples in Trichy for this batch
**Script doc:** `TM-Nutrition-3-Day-Secret-v2.docx` (VSL secret segment + Meta ad script)
**Drive (raw):** For Client's editing → `VSL/` (C0006–C0008) and `META ADS/` (C0001–C0003). Testimonials: `Pradheesh's contents/` (2 images, 5 videos).

## Deliverables

| Video | Folder | Status |
|---|---|---|
| VSL v2, 16:9 1920×1080, 1:42 | `vsl/` | Re-edit, coach-only cut (`vsl/final/tm_nutrition_vsl_v2.mp4`); Google Flow clips pending (`vsl/flow_shotlist.md`) |
| VSL v1 | `vsl/` | Superseded: it used silence detection, so prompter lines and idle moments got in |
| VSL v6, 2:04 | `vsl/final/tm_nutrition_vsl_v6.mp4` | Current VSL: voice-ID trimmed, longer client testimonials; Joseph line with mismatched lips at 1:00-1:02 removed |
| Meta Ad 1, 1:19, 9:16 | `meta/final/tm_meta_ad1_kirthika_anand.mp4` | Opens with 8 s of real client transformations (Sivakarthik, Jones, Krishna Priya), then Kirthika & Anand with their before/after photos (client-supplied, kept in source/clients/) |
| Meta Ad 2, 1:16, 9:16 | `meta/final/tm_meta_ad2_joseph_raj.mp4` | Hook: couples fail → Joseph Raj, 62 (real clip) |
| Meta Ad 3, 1:04, 9:16 | `meta/final/tm_meta_ad3_jones_92_67.mp4` | Hook: apple catch → Jones 92→67 kg (real clip) |

## Raw footage (Sony, 4K 25 fps)

| File | Length | What it is |
|---|---|---|
| VSL/C0006 | 5.8 s | Test clip, no audio. Unused |
| VSL/C0007 | 6:11 | VSL part 1, landscape: hook, intro, pain, testimonial call-outs (many retakes + chatter) |
| VSL/C0008 | 10:17 | VSL part 2, landscape: testimonials, "3 days possible?", Day 1–3, bonus, price, guarantee, scarcity, CTA |
| META ADS/C0001–C0003 | 2.5–6 GB each | Shot with the camera on its side (rotate 90° clockwise for 9:16). C0002 is 3:26 |

The VSL is cut from working copies (rotated/scaled, CRF 15), not committed. To rebuild: download from Drive and convert with `scripts/fetch_mezz.sh` (that script rotates for the portrait ad clips; for the landscape VSL clips drop `transpose=1` and scale to 1920:1080), then `vsl/build_src.py` → `vsl/plan.py` → engine v6 `render.js`, `mix.py`, `comp.py`, `speed.sh`.

## VSL edit (story, as spoken)

Hook "how many times have you both decided to lose weight?" → watch fully → Coach Pradheesh, TM Nutrition Centre Trichy, 18 years, hundreds of families → new batch for couples only → pain: 3-day diet then biryani, gym not even 2 weeks, mobile till midnight, "let's start tomorrow" → the problem is the home's pattern, not willpower → clients (58, Erode 32 with 26 kg excess, 48) → "everyone thought it won't work" → change started in just 3 days → 2 client bites in their own voice → "3 days, how?" → Yes, possible → Day 1 habits → Day 2 family health → Day 3 family happiness → bonus: first step to financial independence → just ₹555 → 100% money back, risk on me → only 5 couples in Trichy, I train personally → click the button below.

**v2 cut method (coach only):** the footage was recorded with a friend off camera reading each line first and the coach repeating it.
1. `scripts/face_track.py` tracks the coach's face (MediaPipe) on every frame: lip opening.
2. `scripts/who_speaks.py` labels each 40 ms: voice + mouth moving = coach; voice + mouth still = prompter; no voice = idle.
3. `scripts/transcribe_client.py` transcribes only the coach's stretches; takes are matched to the script in `vsl/selects_v2.py`.
4. `vsl/plan_v2.py` cuts inside each take where the coach's mouth and voice both stop, alternates wide/close framing on every cut, and reserves Flow slots F01–F15.
The final audio was transcribed again: only the coach's lines remain, in script order.

## Confirm before publishing

1. **"18 வருஷமா"** (18 years) and "hundreds of families": spoken by the coach, shown as a graphic. Confirm it is accurate.
2. **"Change started in just 3 days"** is said over real clients whose posted results took 26 days to 8 months. Their bites used here only speak about early change (Day 1 relief, feeling active and fresh). Keep the "Individual results vary" note.
3. **Testimonial consent:** written consent from Raveendran, Sivakarthik, Krishna Priya and the clients in clips 0613/0615. Name spellings come from what they say in their clips.
4. **T_vid_0606 (Raveendran)** ends with a *Coach Thilaga* end card, and image 2 (146→96 kg) credits @coach_thilaga and @nutrition_center_trichy. Confirm both are TM Nutrition clients before using them.
5. **Booking link / button text** for the CTA and end card ("BOOK NOW"), and whether the price is per couple or per family.
6. The Day 1–3 format (Zoom or at the centre) is not spoken in the VSL, so no graphic shows it.

## Meta ads

The three raws are three different ad scripts (not the doc's): C0001 = Ad 1 (full script incl. the offer), C0002 = Ad 2, C0003 = Ad 3. Ads 2 and 3 end with Ad 1's offer section, as the coach said on camera. Cut with the same coach-only method as the VSL (`meta/selects_meta.py`, `meta/trims_meta.json`, `meta/make_ad.py`). Google Flow clips: `meta/flow_shotlist_meta.md` (M01–M13).

Testimonials: every client thanks "my coach Thilagavathi Mutharasu" (TM Nutrition), so all are TM Nutrition clients.
