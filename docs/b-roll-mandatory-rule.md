# B-Roll: MANDATORY on Every Edit (EDITING ARMY)
*Added 23 October 2026 at Prabhuraj's request. This rule sits on top of the DATA BLOCK (Video Editing Knowledge Base) and the B-ROLL FRAMEWORK. In any new chat in this project, every video edit includes animated B-roll automatically, without being asked.*
 
---
 
## 1. The rule
 
Every talking-head sales video, Reel or ad edited in this project ships with **animated B-roll**. A video with only captions and zooms is not finished.
 
- **Style:** Alex Hormozi / Russell Brunson. Jump cuts, at least 1.2× speed, karaoke captions, zoom punches, emotion-matched instrumental BGM, light SFX, a pulsing CTA button and a ProfitSoul end card.
- **Illustrate, never decorate.** Each scene shows the exact thing being said in that line: the noun, the number or the process.
- **Brand colours:** Obsidian `#080A0D`, Emerald `#00C896` for value, yellow `#FFD60A` for urgency and red `#FF3B30` for loss. Fonts are Montserrat Black, Noto Sans Tamil Black and Anton.
 
## 2. Where B-roll goes, and where the face stays
 
| Put B-roll on | Keep the face on screen |
|---|---|
| Pain, how it works, the system or method | First 1.5 s of the hook |
| Lists, value stacks, bonuses | Price line (use a price graphic over the face instead) |
| Proof claims, "many centres", results | Guarantee line (stamp over the face) |
| Tools, places, timelines, numbers | Objection questions ("what are these 4 agents?") |
| Testimonial mentions (real clips preferred) | Every CTA line (button + arrow over the face) |
 
**Layouts**
- **Split screen** is the default for inserts over 3 s. The animation fills the top 864 px and its content must end by about 640 px. The speaker sits in the bottom panel, cropped from source y = 230. Captions move to y = 668.
- **Full cutaway** is for short 2–3 s beats. Keep content clear of the caption band (y 1175–1475) or hide the captions with `nocap` when the scene title already says the line.
- **Coverage:** aim for 30–50% of runtime. Full cutaways stay small (about 5–6 s per video), because split screen keeps the face visible.
 
## 3. Animated scene library (reuse first, then extend)
 
Built so far in the overlay engine (see the doc **B-ROLL ANIMATION ENGINE**):
 
| Scene | Use for |
|---|---|
| `agents` | "4 AI agents": 2×2 robot cards popping in |
| `laptop` | "just a laptop + Wi-Fi": laptop opens, Wi-Fi pulses |
| `seats` | "only / first 50": seat grid filling |
| `voiceads` | "AI video + ads in your voice": waveform → phone ad |
| `live` | "live sessions, not a course": LIVE grid |
| `weeks` | "in 4 weeks": week cards + progress bar → result |
| `whatsapp` | WhatsApp automation chat + landing page assembling |
| `costs` | Monthly software bill → stamp ("₹0 EXTRA") |
| `affordable` | Price tag drop ("India's most affordable") |
| `walkin` | People walking into a wellness centre + walk-in counter |
| `days` | 3-Day Challenge cards (Zoom, Zoom, centre visit) |
| `centres` | Many centres lighting up with ticks ("every centre that used it") |
| `testis` | Testimonial video cards (placeholder, swap for real clips) |
| `transform` | "Your experience → 3-day event" before/after cards |
| `chart` | "More walk-ins": bars growing |
| `pin` | "Next pin, fast": rocket climbing a rank ladder |
| `vid` (v5) | Real or AI video clip as B-roll (full or split), with timed chips / big number overlay. Clip is composited by `comp.py` |
| `questions` (v5) | "Your BMI? Mother's BMR? Wife's body fat?": 3 question cards + "தெரியாது?" stamp |
| `checkup` (v5) | Day 3 centre visit: family walks in, BMI / BMR / FAT % rows tick |
| `mappin` (v5) | Centre location: road draws, pin drops, landmark appears |
| `days` (v5) | Family Health Reset 3-Day cards (Zoom, Zoom, centre) |
| `endcard` (v5) | Client end card: Family Health Reset + Send WhatsApp message |
| `tally` (v6, 16:9) | "How many times have you decided...?": plan cards crossed out one by one |
| `pain` (v6) | Pain beats, variants `diet` (3 days salad → biryani), `gym` (paid, 4 days then ✗), `midnight` (clock to 12 + phones glowing), `tomorrow` (calendar flipping) |
| `pattern` (v6) | "Problem isn't willpower, it's your home's pattern": WILL POWER struck out → house with loop |
| `q3days` (v6) | "Change in 3 days? Yes, possible": 3 day cards + YES ✓ POSSIBLE stamp |
| `agenda` (v6) | Day 1 / Day 2 / Day 3 / Bonus cards, optional focus on one |
| `habits` (v6) | Day 1: phone feed scrolling → stop hand → habit sliders tuned + hand-hold chip |
| `famhealth` (v6) | Day 2: one person → whole family gets health rings + ticks |
| `happy` (v6) | Day 3: routines tick, happiness fills the house |
| `money` (v6) | Bonus: steps to financial independence, first step |
| `stack` (v6) | Value stack rows dropping in (before a price line) |
| `testi` (v6) | Real testimonial clip label (REAL CLIENT, name, result); clip composited by comp.py as a portrait card |
| `stamp` (v6) | On-face guarantee stamp (100% MONEY BACK) |
| `lower` (v6) | Lower third: name + title |
| v7 (9:16) | Same scene set as v6 for vertical Meta ads; `stack` gains `bad:true` (red ✗ rows, e.g. "mobile / late dinner / no sleep / no walking"); `endcard` takes a `title` |
 
On-face graphics: `text` slam, `badge`, `price` (strike-through anchor + count-up), `stamp` (guarantee), `cta` (pulsing button, arrow and guarantee badge), `endcard`.
 
When a new video has a beat no scene covers, build a new scene function in `engine.html`, add it to this table and save the updated engine doc.
 
## 4. Workflow in every new chat
 
1. Transcribe. Use Whisper large-v3 via sherpa-onnx, load one recognizer at a time, and translate per phrase for meaning.
2. Map the beats, then write the **B-roll map** (`broll_plan.csv`): ID, source time, line, scene, layout, length, status, licence.
3. Reuse or extend scenes, then render 15–20 preview frames and check them **before** the full render.
4. Composite, speed to 1.2×, bring loudness to −14 LUFS, then run QA on a contact sheet.
5. Deliver the MP4 **plus the B-roll log**, and flag any placeholder scenes (testimonials, proof) to swap for real clips.
 
## 5. Never
 
- Never fake proof, results, customers or testimonials with animation or AI. Placeholders are labelled and flagged.
- Never put B-roll over a price, guarantee or CTA line.
- Never invent prices or figures in a scene. Show only numbers that are spoken in the video or that appear on the sales page.
 
## 6. QA additions
 
- [ ] Animated B-roll present, matched to the spoken line
- [ ] Face on screen for the hook opening, price, guarantee, objections and CTAs
- [ ] No scene content under the captions; split-scene content ends by about 640 px
- [ ] B-roll log delivered; placeholders flagged
 