# Coach Muthu: Family Health Reset, 3 Day Challenge

**Client:** Coach Muthu, Wellness Centre · **Prepared by:** Prabhuraj, ProfitSoul · **Cohort 1 starts:** Thursday 29 October 2026

**Brief:** [`Coach_Muthu_-_Family_Health_Reset_Blueprint.pdf`](Coach_Muthu_-_Family_Health_Reset_Blueprint.pdf) contains the full plan, the 3-day programme, the funnel, the follow-up system and the final scripts for the three Meta ads (section 11: Dog · Fish · City).

## Offer (from the blueprint)

- Day 1 and Day 2 are live Zoom sessions of 1 hour each, in the morning. Day 3 is a centre visit with a free BMI, BMR and full health check for the whole family, plus a 10-minute one-on-one with Coach Muthu.
- The challenge is free for the first 10 families each week and ₹2,000 per family after that.
- The audience is working families within 10 km of the centre.

## Raw videos

The originals are in Google Drive, `videos_raw/` (4K HEVC, 60 fps, portrait). They are too big for GitHub, which accepts files up to 100 MB. The 720p proxies in `source-proxies/` are for reviewing and planning only. Always render the final edit from the originals.

| File | Length | Drive |
|---|---|---|
| IMG_2533.MOV | 31.4 s | https://drive.google.com/file/d/1B2FXkJh3C9y8aa4trUFnudl9tf3nmepI/view |
| IMG_2538.MOV | 29.4 s | https://drive.google.com/file/d/1xR8F8j6oxW9mta_cNNgidtX7mtiNtl19/view |
| IMG_2540.MOV | 29.2 s | https://drive.google.com/file/d/1OHsq8m56fM4b46bvMyBOJcirdv-XOXz8/view |

### Fish and City ads (uploaded 17 Nov 2026, Drive: `For Client's editing / Coach Muthu/`)

| File | Ad | Length | Drive |
|---|---|---|---|
| IMG_2605.MOV | Fish | 4:06 | https://drive.google.com/file/d/162UKWfM1r7lFhIM_qYsRw7qg6bmBfCGl/view |
| IMG_2606.MOV | City | 3:33 | https://drive.google.com/file/d/1dwBAiPz4Zl45hrPRZbVzHCB9pDj0SEdH/view |

These were shot with an **off-camera prompter** who reads each line before the coach repeats it. **Only the coach's voice goes in the edit.**
- The coach's lav records him at about −17 dB. The prompter is about −33 dB on the same mic.
- `build_lib.py` keeps only the takes listed in each `plan.py`, and inside them cuts anything under −30 dB for more than 0.3 s.
- Two takes include quiet coach tails that were checked on camera by lip movement. Those are marked `'raw'` in `TAKES`.
- Takes that looked like the coach but were the prompter on the mic level: Fish 210–214 s (₹2,000 line, the coach's take is at 214.6 s) and City 200–202 s (location intro).
- Fish 176.9–181.2 s is the coach speaking to the prompter, so it's left out.
