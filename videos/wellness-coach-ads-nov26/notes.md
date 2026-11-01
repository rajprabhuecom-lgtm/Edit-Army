# Wellness-coach growth ads (Prabhuraj / ProfitSoul), batch of 6, edited 1 Nov 2026

**Source:** Google Drive folder `my videos` (6 MP4s, 1080x1920, 30 fps). Edited versions are named `<original>_edited.mp4`.
**Offer in every video:** book an appointment (link below) to discuss and implement an online system that brings wellness centres consistent new guests / walk-ins / appointments.
**Engine:** `engine/v6-wellness-growth/` (one plan module per video, `common.py` builds the EDL).

| Folder | Original file | Final length | B-roll | Notes |
|---|---|---|---|---|
| v1-walk-talk | VID_20260728_223422_561_bsl.mp4 | 41.0 s | 35% | Walk & Talk online, 50+ centres (spoken) |
| v2-kerala-result | VID_20260728_224059_148_bsl.mp4 | 37.2 s | 36% | Opens on the real WhatsApp update on his phone (kept on screen) |
| v3-andhra-result | VID_20261031_203748_724_bsl.mp4 | 46.5 s | 37% | Opens on the real message on his phone (kept on screen) |
| v4-ai-followup | VID_20261031_203507_985_bsl.mp4 | 48.4 s | 30% | Silent transformation, AI follow-up, "extra 10 to 20 quality appointments" (spoken) |
| v5-proven-system | VID_20260703_065638_816_bsl.mp4 | 40.6 s | 38% | Real WhatsApp screenshot at the start kept clear (captions moved up), 35+ centres (spoken) |
| v6-walk-talk-online | WC NEW.mp4 | 50.2 s | 36% | Clean source; ads to people who want to lose weight, 10+ walk-ins/week (spoken) |

## How the sources differed
Five of the six sources were already edited: burned-in headers ("WELLNESS COACHES ONLY!" etc.), bottom banners ("GET NEW 20+ GUEST WALKINS EVERY MONTH", "BOOK YOUR APPOINTMENT NOW") and, in v1/v2, small burned captions. These cannot be removed. So:
- Karaoke captions, text slams and CTAs are placed per video to clear the burned header/banner (`CFG.capTop`, text `y`).
- v1/v2: the old small burned captions are blurred (`CFG.blur`) and the new captions sit over that area.
- v5: split-screen crop starts lower (`cropY=285`) so the burned header doesn't show in the speaker panel.
- The "20+" in the burned banners is from the original creative; no new figures were added. Every number in the new graphics is spoken in that video.

## Flags for review
- Sources were already tight-cut, so jump cuts removed almost nothing; 1.2x speed was applied to all.
- Tamil transcription was rough in places (Whisper); captions were written from the meaning, in Tamil + English. Skim them before running ads.
- No testimonial or proof placeholders were used. The real WhatsApp proof in v2, v3 and v5 stays on screen and is not covered.
