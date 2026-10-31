# Videos

One folder per video, named by video ID (for example `sun_ads`, `10octwc2`):

```
videos/<video-id>/
  notes.md          Brief: client, goal, CTA, anything special
  plan.py           This video's EDL (copied from the engine template)
  engine.html       Only if this video needed new scenes
  broll_plan.csv    B-roll log (ID, times, line, scene, layout, status, licence)
  broll/            Real or AI B-roll clips, named by ID (B03_walkins.mp4)
  source/           Raw footage
  final/            Delivered MP4
```

**Large files:** GitHub rejects files over 100 MB, and the repo gets slow beyond a few GB. Keep raw footage and big MP4s in Google Drive (`Videos/EDITING ARMY/<video-id>/`) and put the link in `notes.md`, or set up Git LFS before committing them. Plans, logs and engine changes always go in git.
