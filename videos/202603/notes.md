# 202603 batch (Prabhuraj Reels)

Source: Google Drive folder `202603` (https://drive.google.com/drive/folders/1Wal9OCQblefPHjecdUbrEl75babOG8Ch).
Raw MP4s stay out of git (`source/*.mp4` is git-ignored); the 16 `.srt` files are committed.

## Duplicate check

49 MP4s = **20 unique videos**. Two passes:
1. Same length + same frames at 20/50/80% → exact re-exports.
2. Same frames at the same timestamps but a slightly different length (0.1–0.7 s, re-trimmed exports) → also duplicates.
   Their audio waveforms differ only because of re-encoding; the picture matches frame for frame.

Each unique video is edited **once**, from the first file listed.

| # | Folder | Edited from | Duplicates skipped | SRT |
|---|---|---|---|---|
| 01 | 01-275-clients | 17865235014599014 | — | 18042552539737461 |
| 02 | 02-csk-ai-review | 17869989468594250 | 17917622127301224, 17917622136301224, 17917622139301224 | none |
| 03 | 03-happy-money | 17893466715425658 | 17916562182301224 | none |
| 04 | 04-royal-enfield-notebooklm | 17915616921301224 | — | 17979391448994034 |
| 05 | 05-pomelli-photoshoot | 17915922441301224 | 17931789006214709 | 18054635177479983 |
| 06 | 06-notebooklm-science | 17916217008301224 | 18007131209704460 | none |
| 07 | 07-claude-job-prospecting | 17916383046301224 | 17916383049301224, 17952736419096731 | none |
| 08 | 08-kid-ai-photo | 17916561171301224 | 17916561180301224, 18059884454397713 | none |
| 09 | 09-ai-saas-agency | 17916567354301224 | 17916567363301224, 18089759311915584 | 18098033044964571 |
| 10 | 10-diet-app-3kg | 17917118595301224 | 17917118604301224, 18199167469344913 | 18137255998510664 |
| 11 | 11-meta-ads-2026 | 17917267080301224 | 17917267083301224, 18088075468964454 | 18343334362245375 |
| 12 | 12-notebooklm-habits | 17917437813301224 | 17917437816301224, 17917437819301224, 17994268805762654 | 18460214362103624 |
| 13 | 13-gemini-deep-research | 17917775409301224 | — | 18050169794508666 |
| 14 | 14-ai-music-gemini | 17917779795301224 | 17917779801301224, 17950723998119740 | 18020615819648604 |
| 15 | 15-gemini-presentations | 17917785297301224 | 17917785300301224, 17917785303301224, 17917785306301224, 18111938635707133 | none |
| 16 | 16-google-ai-posters | 17918222835301224 | 17918222838301224, 17998060076870137 | none |
| 17 | 17-gemini-gems | 17918372355301224 | 17918372358301224, 18404944834178063 | none |
| 18 | 18-exam-study-ai | 18013977311675391 | — | none |
| 19 | 19-little-princess | 18093267326024782 | — | none |
| 20 | 20-meta-placements | 18119410852530507 | — | 18061468073672263 |

SRTs with no video in this folder: 17900177367244619 (interior designer), 17945023569129039 (IT jobs/recession),
17967362094040284 (70+ clients), 18058075988403662 (World Cup lessons), 18206736280323494 (one-line positioning),
18395752537197207 (villain to your company).

## How this batch is edited

- Every source is already a finished Reel with accurate, styled burned-in captions (and some banners / stickers).
  Those captions are **kept** (not covered). Transcribing Tamil-English by Whisper or OCR was not reliable enough to replace them.
- Added on top: hook title / stat count-ups, keyword slams and badges, step labels, comment-keyword CTAs, animated
  split-screen B-roll on the talking-head videos (01, 09), emoji bursts, zoom punches on every cut, a progress bar,
  SFX, original BGM (not on 02 and 09, which already carry music), 1.2× speed, −14 LUFS, ProfitSoul end card.
- Split-screen crops keep the burned caption inside the bottom panel (CROP_Y0 = 330).
- Banner videos (01, 09, 20) use gentle 1.04–1.06 zooms around the centre so banners stay in frame; 15 (already stacked) has no zoom.
- 19 (kid clip) keeps its natural pauses (no jump cuts).
- Pipeline: `pipeline/run_all.sh <folder> <out.mp4>` (composite runs in 4 parallel chunks).
