"""Coach Deepa faceless Meta ad: edit plan in FINAL time (voice already cut + 1.2x). python3 plan.py <workdir>"""
import json, sys
WD = sys.argv[1]; C = WD + '/clips/'; R = WD + '/real/'
TOTAL = 42.6
clips, items, caps, sfx = [], [], [], []
def clip(t0, t1, f, ss=0.3, rate=1.0, z0=1.0, z1=1.1, **k): clips.append(dict(t0=t0, t1=t1, file=f, ss=ss, rate=rate, z0=z0, z1=z1, **k))
def it(type, t0, t1, **k): items.append(dict(type=type, t0=t0, t1=t1, **k))
def cap(t0, t1, txt, hl=(), col=None):
    w = txt.split(' '); caps.append(dict(t0=t0, t1=t1, words=w, hl=[i for i, x in enumerate(w) if i in hl], **({'col': col} if col else {})))
# --- hook: city + who ---
clip(0.0, 1.5, C + 'D01.mp4', ss=3.2, rate=1.3, z1=1.12); it('vid', 0.0, 1.5, loc='திருவண்ணாமலை', ly=230, lt=.05, noflash=True)
clip(1.5, 2.45, C + 'D02.mp4', ss=2.6, rate=1.2); it('vid', 1.5, 2.45, big='WORKING<br><span class="y">WOMEN?</span>', by=230, bt=.05)
# --- pain ---
clip(2.45, 4.95, C + 'D03.mp4', ss=1.0); it('vid', 2.45, 4.95, cy=220, csz=60, ct=[.05, .55, 1.05, 1.55],
   chips=[['⚖️ OVERWEIGHT', '#2a1010', '#fff', '#FF3B30'], ['PCOD', '#2a1010', '#fff', '#FF3B30'], ['THYROID', '#2a1010', '#fff', '#FF3B30'], ['📈 WEIGHT GAIN', '#2a1010', '#fff', '#FF3B30']])
clip(4.95, 6.9, C + 'D04.mp4', ss=2.5, z0=1.42, z1=1.5, dx=-380, fy=820); it('vid', 4.95, 6.9, big='😔', bsz=150, by=240, bt=.3)
clip(6.9, 9.05, C + 'D05.mp4', ss=2.0); it('vid', 6.9, 9.05, cy=230, csz=62, ct=[.1, 1.1], chips=[['🥗 DIET ✓'], ['🏃‍♀️ EXERCISE ✓']])
clip(9.05, 11.15, C + 'D06.mp4', ss=1.5, rate=1.15, z1=1.12); it('vid', 9.05, 11.15, cy=230, csz=62, ct=[.5, 1.3],
   chips=[['RESULT ❌', '#2a1010', '#fff', '#FF3B30'], ['HOPE 📉', '#2a1010', '#fff', '#FF3B30']])
# --- turn ---
it('effort', 11.15, 13.65, cues=[.85, 1.45], nocap=True)
it('photo', 13.65, 14.8, src='coach.jpg', kb=[1.05, 1.16, 0, 0, 40, -20], pos='center 20%', title='<span class="y">COACH</span> DEEPA', ty=150, tsz=120, tag='🌿 RC WELLNESS CENTER', tgy=1060, tgt=.35)
it('collage', 14.8, 17.0, srcs=['group_centre.jpg', 'group_cups.jpg', 'session.jpg', 'consult.jpg'], gap=.22, title='LAST <span class="y">3 YEARS</span>', count={'n': 100, 'suf': '+', 'label': 'MEMBERS'}, ct=1.2, nocap=True)
it('pillars', 17.0, 20.05, cues=[.05, 1.0, 2.0], nocap=True)
clip(20.05, 22.05, R + 'centre24.mp4', ss=30.0, rate=1.0, z0=1.02, z1=1.1, fy=1000)
it('vid', 20.05, 22.05, cy=230, csz=58, ct=[.1], chips=[['✅ HEALTHY WEIGHT LOSS', '#00C896', '#04110c', '#00C896']])
it('fatfit', 22.05, 24.0, sw=.8, ssz=62, sub='நீங்களும் <span class="g">READY</span>-ஆ?', nocap=True)
clip(24.0, 27.1, R + 'centre23.mp4', ss=12.0, z1=1.08, fit='blur'); it('vid', 24.0, 27.1, big='MISS<br><span class="y">பண்ணாதீங்க!</span>', by=200, bsz=104, bt=.1, loc='RC WELLNESS CENTER', ly=520, lt=1.7, lsz=62)
# --- offer (graphics only, no B-roll) ---
it('seats', 27.1, 28.55, fill=7, nocap=True)
it('offer', 28.55, 33.75, title='3 DAYS <span class="y">WEIGHT LOSS</span><br>TRIAL PROGRAM', tsz=78, sub='FIRST 10 MEMBERS', value=1000, ky=600, tty=290,
   items=['FULL BODY CHECKUP', 'FAT CHECKUP'], cues={'items': [2.7, 3.9], 'strike': 4.45, 'free': 4.55}, nocap=True)
it('limited', 33.75, 35.8, title='LIMITED <span class="y">PERIOD</span>', sub='OFFER மட்டும்!', nocap=True)
# --- CTA ---
clip(35.8, 38.45, C + 'D18.mp4', ss=1.5, rate=1.1, z1=1.12)
it('cta', 35.8, 38.45, label='📅 BOOK APPOINTMENT', y=330, arrow='↓', badge='👇 LINK BELOW')
it('endcard2', 38.45, TOTAL, icon='🌿', name='RC WELLNESS CENTER', sub='3 DAYS WEIGHT LOSS TRIAL', line='FULL BODY CHECKUP + FAT CHECKUP', btn='📅 BOOK APPOINTMENT', badge='FIRST 10 MEMBERS • FREE', loc='திருவண்ணாமலை', nocap=True)
# --- captions (Tamil words in Tamil script, English in English) ---
cap(0.0, 1.5, 'வணக்கம் திருவண்ணாமலை மக்களே!', [1])
cap(1.5, 2.45, 'நீங்க WORKING WOMEN-ஆ?', [1, 2])
cap(2.45, 3.95, 'OVERWEIGHT, PCOD, THYROID', [0, 1, 2], '#FF6B60')
cap(3.95, 4.95, 'WEIGHT GAIN-ஆல கஷ்டப்பட்டு', [0, 1], '#FF6B60')
cap(4.95, 6.9, '"நான் எப்போ SLIM ஆவேன்?"', [2, 3])
cap(6.9, 8.0, 'DIET START பண்ணுவீங்க', [0])
cap(8.0, 9.05, 'EXERCISE-உம் START பண்ணுவீங்க', [0])
cap(9.05, 10.4, 'ஆனா EXPECTED RESULT கிடைக்காம', [2], '#FF6B60')
cap(10.4, 11.15, 'HOPE-ஏ போயிடுச்சா?', [0], '#FF6B60')
cap(13.65, 14.8, 'இவங்க தான் COACH DEEPA', [2, 3], '#FFD60A')
cap(20.05, 21.45, 'HEALTHY WEIGHT LOSS', [0, 1, 2])
cap(21.45, 22.05, 'GUIDE பண்ணியிருக்காங்க', [0])
cap(24.0, 25.6, 'இந்த OPPORTUNITY-ஐ MISS பண்ணாதீங்க!', [1], '#FFD60A')
cap(25.6, 27.1, 'நம்ம RC WELLNESS CENTER-ல', [1, 2, 3])
cap(35.8, 37.4, 'கீழே இருக்குற LINK-ஐ CLICK பண்ணி', [2, 3], '#FFD60A')
cap(37.4, 38.45, 'APPOINTMENT BOOK பண்ணுங்க', [0, 1], '#FFD60A')
# --- SFX (on the beat of each visual change) ---
for t in [1.5, 2.45, 4.95, 6.9, 9.05, 20.05, 24.0, 35.8]: sfx.append([t, 'whoosh'])
for t in [2.5, 3.0, 3.5, 4.0, 9.55, 10.35]: sfx.append([t, 'pop'])
sfx += [[0.0, 'hit'], [11.15, 'thud'], [12.6, 'thud'], [13.65, 'hit'], [14.95, 'pop'], [15.17, 'pop'], [15.39, 'pop'], [15.61, 'pop'], [16.0, 'cash'],
        [17.05, 'tick'], [18.0, 'tick'], [19.0, 'tick'], [22.85, 'ding'], [27.1, 'whoosh'], [28.55, 'whoosh'], [29.0, 'cash'], [31.25, 'tick'], [32.45, 'tick'],
        [33.0, 'thud'], [33.1, 'hit'], [33.75, 'whoosh'], [35.8, 'riser'], [38.45, 'hit']]
music = [[0, 2.45, 'pulse'], [2.45, 11.15, 'dark'], [11.15, 22.05, 'warm'], [22.05, 33.75, 'tech'], [33.75, TOTAL, 'uplift']]
json.dump(dict(total=TOTAL, clips=clips, items=items, captions=caps, sfx=sfx, music=music, voice_at=0.0), open(WD + '/timeline.json', 'w'), ensure_ascii=False, indent=1)
print(len(clips), 'clips', len(items), 'items', len(caps), 'captions')
