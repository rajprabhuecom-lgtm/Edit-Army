# Naheed Khan: Tonight Wind-Down (webinar live-attendance bonus)

**Client:** Naheed Khan (Sleep webinar) · **Edited:** 3 Nov 2026 · **Engine:** `engine/v6-meditation/`

**Brief:** Turn Naheed's recorded wind-down audio (WhatsApp audio, 6:31) into a calm bonus video for women who join the Sleep webinar live ("Type CALM in the chat"). Soothing, not attention-grabbing. Add original meditation music, soft subtitles, a nature background and a small client photo in a corner. The source is the recording guide `Tonight-Wind-Down-Audio-Recording-Guide-for-Naheed.docx` (2 Nov 2026).

**This is not a sales edit.** The B-roll / Hormozi rules are switched off on purpose (see `docs/b-roll-mandatory-rule.md` §4b): no speed-up, cuts, punches, SFX or CTA. The voice runs untouched at 1.0×.

## What's in the video (7:03, 1920×1080, 30 fps)

| Time | Section | On screen |
|---|---|---|
| 0:00–0:09 | Intro (music only) | "LIVE WEBINAR BONUS · Tonight Wind-Down · A gentle relaxation practice with Naheed · Not while driving" |
| 0:08–0:53 | Opening (safety lines) | Night ocean, subtitles |
| 0:53–2:12 | Settling (1 of 5) | Section label fades in and out |
| 2:12–3:50 | Breathing (2 of 5) | Breath ring timed to her counts (in 4, out 6, three rounds) |
| 3:50–5:16 | Body softening (3 of 5) | Warm light band drifts head → feet |
| 5:16–6:04 | Letting go (4 of 5) | Lantern set on the water drifts to the horizon |
| 6:04–6:37 | Ending (5 of 5) | Final breath ring on "one deep breath in… and out" |
| 6:38–7:03 | Tail | "Good night · You can come back to this any evening" + disclaimer, fades to black |

Throughout: small round photo + "Naheed / TONIGHT WIND-DOWN" in the top-left corner. The whole scene slowly gets darker as the practice goes on.

**Audio:** voice cleaned (high-pass, light denoise, gentle compression, a little room reverb). The music bed is original and procedural (`soundtrack.py`, no licences): a slow D-major pad, ocean swell, sparse soft bells, singing bowls on each section change, a pad swell that follows the breath counts, and a low drone. Music sits about 17 dB under the voice with a 3.5 dB duck. Final level −16 LUFS integrated.

## Subtitles

`captions.srt` comes from Whisper `medium.en` word timestamps. Subtitles follow what she actually said, which differs a little from the script ("Hello sisters", "belly breathing…", "I acknowledge you. I appreciate you."). Changes:
- **"I recommend closing more"** (video 1:28): unclear ad-lib, left **without a subtitle** rather than guessed. Check with the team.
- "Three, two, three, four…" in the second out-breath was a Whisper error; shown as "Two, three, four, five, six."
- "It will be still there" shown as "It will still be there".

## Compliance

The safety lines are kept (not while driving; not medical advice; speak to your doctor). The video makes no promise of sleep. The closing card shows the delivery line from the guide: "General relaxation guidance; individual experiences vary. Please don't listen while driving."

## Files

- `timeline.json`: cues, sections, breath phases, bowl and lantern times (video time; voice offset 8 s)
- `segs.json`: Whisper segments with word timestamps (voice time)
- `captions.srt`: subtitles (video time)
- `source/naheed_face.png`: 360×360 crop of the supplied portrait
- Final MP4/MP3 are too big for git. Upload them to Drive `Videos/EDITING ARMY/naheed-wind-down/`.
