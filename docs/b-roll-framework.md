# ProfitSoul B-Roll Framework
*Version 1.0, 23 October 2026. A companion to the Video Editing Knowledge Base (DATA BLOCK). It applies to every talking-head sales video, Reel and ad edited in this project.*
 
---
 
## 1. Why B-roll, and the one rule that matters
 
B-roll is footage that cuts away from the speaker to **show** what he is saying. In short-form sales video it does three jobs:
 
- **Retains.** It gives the eye a new picture every few seconds.
- **Proves.** It shows the result instead of just claiming it.
- **Clarifies.** It makes an abstract idea concrete.
 
**The one rule: illustrate, never decorate.** A controlled retention test (Opus blog: three versions of one 8-minute video, single channel) gives the clearest numbers:
 
| Version | Avg view duration | Completion |
|---|---|---|
| No B-roll | 5:18 | 66% |
| About 40% B-roll, targeted | 6:42 | 84% |
| About 70% B-roll | 5:54 | 74% |
 
The gain only appeared where the footage *directly illustrated the line*. Generic stock showed no gain and sometimes caused small dips. The same test found calls to action delivered over B-roll converted about 40% worse than on-camera ones.
 
> If the right clip doesn't exist, **skip the insert**. Graphics or a zoom are better than irrelevant footage.
 
---
 
## 2. Coverage and timing rules (short-form, after 1.2×)
 
| Rule | Value |
|---|---|
| Coverage of runtime | **25–40%** for sales videos (never above 50%) |
| Inserts per 60 s | **5–8** |
| On-screen length of each insert | **1.5–3 s** (proof/demo shots up to 4 s) |
| Where it lands | 0.2–0.5 s **after** the keyword is spoken, cut on a pause, never mid-word |
| Visual change | Something new every 2–4 s; B-roll, zooms and graphics share this job |
| Generate/record length | 6–8 s of raw footage per insert; use the best 2–4 s |
 
### Keep the FACE on screen (no B-roll) during:
1. **The first 1.5 s of the hook.** Trust starts with the face.
2. **The price line and the guarantee line.**
3. **Every CTA line** ("click the link below", "book now").
4. **Personal or emotional moments**, such as a story or a vulnerable admission.
5. **Objection questions** ("how is this possible?"). The face carries the doubt.
 
### Put B-roll on:
- pain descriptions
- explanations of how it works
- proof claims ("already implemented", "results")
- lists and value stacks
- mentions of a tool, place or person
- testimonials
 
---
 
## 3. Source hierarchy (always try in this order)
 
| Priority | Source | Use for | Notes |
|---|---|---|---|
| **P1** | **Real proof**: screen recordings of VimanaOS, CRM pipelines, WhatsApp automations, Ads Manager results, Zoom challenge sessions | "We built it", "it works", "results" | Converts best. Record 5–10 s each, phone or OBS. Blur client phone numbers. |
| **P2** | **Real footage**: client centres, events, walk-ins, real testimonial clips (with permission) | Testimonials, "many centres", "events" | Testimonials must be real people, every time. Log written consent. |
| **P3** | **AI-generated** (Gemini Omni Flash / Veo 3.1 / Google Flow) | Abstract or scene-setting ideas: empty reception, busy centre, "growth", a coach planning | Never fake proof, results, customers or testimonials. Disclose as AI in Meta ads. |
| **P4** | **Stock** (Pixabay / Pexels) | Generic everyday scenes | Free for commercial use. Check each clip's licence. Avoid identifiable faces that imply endorsement. |
| **P5** | **Motion graphics** (our HTML overlay engine) | Numbers, checklists, flows, price, guarantee | Already built. Use when P1–P4 have nothing relevant. |
 
---
 
## 4. Layouts (pick one per insert)
 
1. **Full cutaway.** B-roll fills 1080×1920 and captions stay on top. Use for pain, scenes and proof shots of 1.5–3 s.
2. **Split screen.** B-roll on the top 45%, speaker on the bottom 55%. Use for demos, stacks and screen recordings over 3 s. This is already built in the editor.
3. **Picture-in-picture.** B-roll full screen with the speaker in a circle at the bottom-left, above the UI safe zone. Use for long screen demos.
4. **Floating card or phone mockup.** A screenshot or clip on a rounded card over the speaker. Use for WhatsApp chats, testimonial thumbnails and result screenshots.
 
---
 
## 5. The B-roll pipeline (Steps 2b and 5b of the edit)
 
### Step A: Build the B-roll map (Claude, after transcription)
 
For each beat, Claude writes one row in `broll_plan.csv`:
 
| ID | Source time | Beat | Keyword spoken | Visual idea | Source (P1–P5) | Layout | Prompt / recording instruction | Use length | Status | Licence |
|---|---|---|---|---|---|---|---|---|---|---|
 
Claude sends the map to Prabhuraj before rendering. Prabhuraj marks which P1/P2 clips he has.
 
### Step B: Collect or generate the clips
 
| Route | How | When |
|---|---|---|
| **A: Google Flow (works today)** | Claude writes the prompts. Prabhuraj generates in Flow and downloads the clips into `Videos/EDITING ARMY/<video-id>/broll/`, named by ID (`B03_walkins.mp4`). | Default for AI shots until the API route is open |
| **B: Gemini API (automated)** | Claude calls Omni Flash or Veo directly with Prabhuraj's API key and saves the clips to the same folder | Once network access to `generativelanguage.googleapis.com` is open (see Section 8) |
| **C: Screen recordings** | Prabhuraj records the 5–10 s screens listed in the map | Always, for P1 proof |
| **D: Stock** | Prabhuraj downloads from Pixabay or Pexels into the folder | Generic shots |
 
### Step C: Integrate (Claude, inside the composite)
 
- **Conform.** Scale and crop to fill 1080×1920 at 30 fps. Strip the clip's audio. Keep natural sound only if it helps, at −24 dB under the voice.
- **Match the look.** Apply the same colour LUT lightly, so AI or stock clips don't look pasted in.
- **Movement.** Add a slow push-in from 100% to 106% across every insert. Stills get the same push-in (Ken Burns).
- **Transitions.** Hard cut in and out on a pause, with a soft whoosh or pop SFX at −26 dB. No fancy wipes.
- **Captions** continue over the B-roll in the same safe zone.
- **Speed.** B-roll is placed in pre-speed time and speeds up 1.2× with everything else. That's why AI prompts ask for *slow* camera motion.
- **QA.** Check coverage, that no insert sits over a price, guarantee or CTA line, and that the licence log is complete.
 
---
 
## 6. AI B-roll prompt template (Omni Flash / Veo / Flow)
 
```
Vertical 9:16, 6 seconds, single continuous shot.
SUBJECT + ACTION: [what we see happening, specific and literal to the spoken line]
SETTING: [e.g. a modern wellness and nutrition centre in Tamil Nadu, clean reception, plants, natural light]
PEOPLE: [anonymous, seen from behind or mid-distance; Indian; everyday clothes] — or "no people"
CAMERA: slow smooth push-in (or slow pan), stable, eye level
LIGHT & LOOK: warm natural daylight, soft shadows, realistic documentary style, shallow depth of field
AUDIO: ambient room sound only, no dialogue, no music
AVOID: no on-screen text, no logos, no watermarks, no faces looking into the camera, no distorted hands
```
 
**Prompt rules**
- Keep it **literal**. Show the noun or action that was spoken.
- **One idea per clip.** Generate 2 takes per shot and pick the better one.
- Draft at 360p in Omni Flash (about $0.03/s), then render the chosen take at 720p or 1080p.
- Omni Flash also edits clips in follow-up turns ("make the lighting warmer, keep everything else the same").
 
---
 
## 7. Compliance (MANDATORY for ads and client work)
 
- **Never** use AI to create testimonials, customers, "results", before/after bodies, or real people saying things they didn't say. Meta prohibits fabricated testimonials and synthetic people presented as real customers.
- **Disclose AI.** Google video models embed SynthID, and Meta may apply its "AI info" label automatically. Where it doesn't, use Meta's AI-disclosure toggle when uploading ads that contain photorealistic AI footage.
- **No health claims in visuals.** No weight-loss transformations or medical-looking results in wellness ads.
- **Log every clip** (ID, source, date, licence or consent) in `broll_plan.csv`. Stock: check the individual clip page before paid use.
 
---
 
## 8. The API route: setup and security
 
1. **Create the key.** In Google AI Studio, turn on billing and create a Gemini API key in its own project.
2. **Protect the spend.** Set a **budget alert** on that project (for example ₹2,000 a month) and restrict the key to the Generative Language API.
3. **Never paste the key in chat.** Save it as a one-line file named `gemini.key` inside the connected `Videos/EDITING ARMY/` folder. Claude reads it from there, and you can rotate or delete it anytime.
4. **Open the network.** The cloud workspace currently blocks `generativelanguage.googleapis.com` (tested 23 Oct 2026: proxy 403). The host has to be allowed in the workspace's network settings, which on Team/Enterprise plans an owner manages under Admin settings → Capabilities. Alternatively, generation runs on the computer-side workspace if its allowlist permits the host.
5. **Pick the model.**
 
| Model | Price (Gemini API, Oct 2026) | Best for |
|---|---|---|
| `gemini-omni-1.1-flash` | ~$0.034/s at 360p, ~$0.10/s at 720p, ~$0.15/s at 1080p; no free tier | Fast generation and editing in follow-up turns; 9:16 supported |
| Veo 3.1 Lite | ~$0.05/s at 720p, ~$0.08/s at 1080p | Cheapest simple scene shots |
| Veo 3.1 Fast | ~$0.10/s at 720p, ~$0.12/s at 1080p | Higher quality with reference images ("Ingredients", 9:16) |
 
**Typical cost per video:** 4 AI shots × 6 s × 2 takes at 720p ≈ 48 s ≈ **$5 (about ₹420)** on Omni Flash. Drafting at 360p first cuts this further.
 
---
 
## 9. Worked example: "Walk-In Engine" video (10octwc2)
 
| ID | Source time | Line (meaning) | Visual | Source | Layout |
|---|---|---|---|---|---|
| B01 | 2.3–3.9 | "done many events" | Real clips or photos from your past wellness events | P2 | Full cutaway |
| B02 | 7.4–10.9 | "think you can't increase walk-ins?" | Empty wellness-centre reception, coach waiting, clock on the wall (desaturated) | P3 AI | Full cutaway |
| B03 | 13.3–16.9 | "your knowledge → 3-Day Challenge" | Zoom challenge session grid / WhatsApp community screen | P1 | Split screen |
| B04 | 18.3–20.8 | "increase walk-ins" | Families walking into a bright wellness centre, seen from behind | P3 AI | Full cutaway |
| B05 | 24.3–28.6 | "already implemented in many centres" | Real photos of client centres (with permission) + Ads Manager results | P1/P2 | Floating cards |
| B06 | 31.0–33.1 | "I'll implement the system for you" | VimanaOS CRM pipeline + WhatsApp automation screen recording | P1 | Split screen |
| B07 | 48.7–52.2 | "testimonial videos of centre owners" | 2 s muted snippets of REAL testimonial videos | P2 | Floating phone mockup |
| B08 | 58.3–63.1 | "your experience → walk-ins" | Busy centre, family health check in progress | P3 AI | Full cutaway |
 
Face stays on: the hook opening, "how is this possible?" (21–24 s), both CTAs (33–38 s, 56–58 s) and the close (69 s+). That's about 35% coverage.
 
**Prompt for B02 (ready to paste into Flow):**
```
Vertical 9:16, 6 seconds, single continuous shot. An empty reception desk of a small wellness and nutrition centre in Tamil Nadu in the late afternoon; a wall clock ticking; a lone coach in a polo shirt sits behind the desk looking at the door, seen from the side at mid-distance. Slow push-in, stable, eye level. Muted cool light, slightly desaturated, realistic documentary style, shallow depth of field. Ambient room sound only, no dialogue, no music. No on-screen text, no logos, no faces looking into the camera.
```
 
**Prompt for B04:**
```
Vertical 9:16, 6 seconds, single continuous shot. Three Indian families walking through the glass door into a bright, welcoming wellness and nutrition centre in Tamil Nadu, seen from behind; a smiling staff member greets them at the reception. Slow smooth push-in, stable, eye level. Warm natural daylight, plants, clean modern interior, realistic documentary style, shallow depth of field. Ambient sound only, no dialogue, no music. No on-screen text, no logos, no faces looking into the camera.
```
 
**Prompt for B08:**
```
Vertical 9:16, 6 seconds, single continuous shot. Inside a busy wellness centre in Tamil Nadu, a staff member in a uniform checks a smiling middle-aged woman's weight and body composition on a scale while her family watches; other visitors wait on chairs in the background. Slow pan left to right, stable. Warm natural light, realistic documentary style. Ambient sound only, no dialogue, no music. No on-screen text, no logos, no faces looking into the camera.
```
 
---
 
## 10. Sources (October 2026)
 
- Google, Gemini Omni Flash docs: https://ai.google.dev/gemini-api/docs/omni
- Google, Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- eesel, Gemini Omni 1.1 Flash pricing: https://www.eesel.ai/blog/gemini-omni-1-1-flash-pricing
- The Rundown, Gemini Omni 1.1 Flash: https://www.therundown.ai/tools/gemini-omni-1-1-flash
- CloudZero, Veo 3 pricing 2026: https://www.cloudzero.com/blog/veo-3-pricing/
- Ars Technica via Harvard TagTeam, Veo vertical "Ingredients to Video": https://tagteam.harvard.edu/hub_feeds/3382/feed_items/17181724
- Opus, Does B-roll increase watch time? (controlled test): https://www.opus.pro/blog/does-b-roll-increase-watch-time
- ClipSpeed, AI B-roll auto-matching for short-form: https://www.clipspeed.ai/blog/ai-b-roll-auto-generator-short-form-2026.html
- Cinerads, Meta AI-generated content policy for advertisers: https://www.cinerads.com/blog/ai-ugc-facebook-ad-policy
- Pixabay Terms of Service: https://pixabay.com/service/terms/
 