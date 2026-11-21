# 202605 batch (Prabhuraj talking-head Reels)

Source: Google Drive folder `202605` (https://drive.google.com/drive/folders/1QyvVSU-PJg1qLHyYr7HrOGRG2ZiC97rW).
Raw MP4s are kept out of git (`source/*.mp4` is git-ignored); the `.srt` files are committed.

## Duplicate check (done before editing)

The folder holds 13 MP4s but only **5 unique videos**. Four videos were exported three times each
(same duration, PSNR ≈ 38–41 dB between copies across every frame = the same edit re-encoded). Each unique
video is edited **once**, from the first copy listed below.

| Video ID (folder) | Edited from | Duplicates skipped | Length | Matching subtitle | Topic |
|---|---|---|---|---|---|
| `ai-3-levels` | 970146912533185.mp4 | 970146919199851, 970146925866517 | 68.1 s | 18321070603257751.srt | AI in 3 levels: chat, automation, agents |
| `bmw-mercedes` | 989137733604641.mp4 | — | 83.2 s | 18092278709351392.srt | Positioning: BMW vs Mercedes |
| `what-business` | 27175928192023440.mp4 | 27175928285356764, 27175928288690097 | 74.8 s | 18097698101234155.srt | "What business are you really in?" |
| `poster-course` | 1334058822124176.mp4 | 1334058825457509, 1334058832124175 | 75.8 s | 17932675128270179.srt | ₹999 implementation program: AI posters + camera fear |
| `wellness-ads-result` | 2257328278428999.mp4 | 2257328285095665, 2257328291762331 | 85.1 s | 18199983001360017.srt | Case study: wellness centre ads, 39 enquiries, ₹113/enquiry |

The other 7 `.srt` files in the folder have no matching video in it (they belong to other Reels).

## Notes for every video in this batch

- The sources already have burned-in Tamil captions (and, on `poster-course`, red offer banners). The new
  karaoke captions sit on a soft blurred strip placed exactly over the old caption line, so the two never double up.
- `wellness-ads-result` shows real proof (Ads Manager, calendar, client WhatsApp update). That proof is kept on
  screen untouched; B-roll is used only outside those stretches.
- All B-roll is original animation (engine v6). No AI clips, stock or fake proof.
- Pipeline: `pipeline/run_all.sh <video-id> <out.mp4>` (build → overlay render → audio → composite → 1.2× + −14 LUFS).
