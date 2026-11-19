"""Sadish (Sathish Kumar) faceless Meta ad: edit plan in FINAL time (voice cut + 1.2x). python3 plan.py <workdir>"""
import json, sys
WD = sys.argv[1]; C = WD + '/clips/'
TOTAL = 70.9
clips, items, caps, sfx = [], [], [], []
def clip(t0, t1, f, ss=0.3, rate=1.0, z0=1.0, z1=1.1, **k): clips.append(dict(t0=t0, t1=t1, file=f, ss=ss, rate=rate, z0=z0, z1=z1, **k))
def it(type, t0, t1, **k): items.append(dict(type=type, t0=t0, t1=t1, **k))
def cap(t0, t1, txt, hl=(), col=None):
    w = txt.split(' '); caps.append(dict(t0=t0, t1=t1, words=w, hl=list(hl), **({'col': col} if col else {})))
RED = ['#2a1010', '#fff', '#FF3B30']
# hook
clip(0.0, 1.45, C + 'S01.mp4', ss=2.0, rate=1.3, z1=1.12); it('vid', 0.0, 1.45, loc='மதுரை', ly=230, lt=.05, noflash=True)
clip(1.45, 4.4, C + 'S02.mp4', ss=1.5, rate=1.15); it('vid', 1.45, 4.4, big='😓', bsz=150, by=240, bt=1.6)
# story: Shobika's mother (REAL photos pending -> labelled placeholder)
it('story', 4.4, 8.9, title='ஷோபிகாவின் <span class="y">அம்மா</span>', badge='😓 இப்படித் தான் கஷ்டப்பட்டாங்க', nocap=True)
clip(8.9, 9.9, C + 'S04a.mp4', ss=2.0); it('vid', 8.9, 9.9, cy=250, csz=72, ct=[.1], chips=[['🥗 DIET'] + RED + [1]])
clip(9.9, 10.7, C + 'S04b.mp4', ss=4.0); it('vid', 9.9, 10.7, cy=250, csz=72, ct=[.05], chips=[['🏋️ WORKOUT'] + RED + [1]])
clip(10.7, 13.8, C + 'S04c.mp4', ss=1.0, z1=1.12); it('vid', 10.7, 13.8, cy=250, csz=72, ct=[.05], chips=[['⏱️ FASTING'] + RED + [1]], big='RESULT<br><span class="r">இல்ல ❌</span>', by=520, bsz=130, bt=2.0)
# turn: the centre
it('brand', 13.8, 16.5, icon='🦋', name='BUTTERFLY<br>WELLNESS', tsz=120, sub='NUTRITION CENTER', ssz=60, ly=330, chips=[], nocap=False)
clip(16.5, 19.5, C + 'S06.mp4', ss=4.5, rate=.9, z1=1.12, fy=900); it('vid', 16.5, 19.5, cy=240, csz=60, ct=[.8], chips=[['📊 BODY ANALYSIS', '#00C896', '#04110c', '#00C896']])
it('plan', 19.5, 22.7, title='<span class="y">SUITABLE</span> METHOD', head='PERSONAL PLAN', gap=.5)
clip(22.7, 24.6, C + 'S08.mp4', ss=3.5, z1=1.12); it('vid', 22.7, 24.6, cy=240, csz=60, ct=[.1], chips=[['🤝 PERSONALIZED GUIDANCE', '#00C896', '#04110c', '#00C896']])
it('story', 24.6, 29.5, title='ஷோபிகாவின் அம்மா <span class="g">இப்போ</span>', badge='✅ SUCCESSFUL WEIGHT LOSS', bg='#00A87E', bt=1.1, nocap=True)
it('fatfit', 29.5, 34.0, sw=3.1, sub='', ssz=60)
# who
it('brand', 34.0, 41.5, icon='🦋', name='SATHISH KUMAR', tsz=104, sub='BUTTERFLY WELLNESS<br>NUTRITION CENTER', ssz=56, ly=360)
it('pillars', 41.5, 45.0, title='<span class="y">TRUSTED</span> COACH', items=[['⏳', '7 YEARS', 'EXPERIENCE'], ['👥', '500+ PEOPLE', 'GUIDED']], cues=[.2, 1.9], nocap=True)
clip(45.0, 49.6, C + 'S06.mp4', ss=4.2, rate=.9, z1=1.1); it('vid', 45.0, 49.6, cy=240, csz=58, ct=[.1, 1.1, 1.7],
   chips=[['⚖️ WEIGHT LOSS ✓'], ['❤️ HEALTH ✓'], ['🌿 LIFESTYLE ✓']])
it('brand', 49.6, 52.0, icon='🏆', name='SUCCESS<br>STORIES', tsz=130, sub='நிறைய!', ssz=80, ly=380, nocap=True)
# offer (graphics only)
it('offer', 52.0, 62.9, title='<span class="y">3 DAYS</span> TRIAL', tsz=110, sub='BUTTERFLY WELLNESS', value=1500, ky=560, tty=320,
   items=['BMR', 'BMI', 'BODY FAT ANALYSIS', '3 DAYS TRIAL'], cues={'items': [2.6, 3.4, 4.1, 9.2], 'strike': 999, 'free': 999}, nocap=True)
it('seats', 62.9, 64.7, title='FIRST <span class="y">10</span>', fill=7, badge='⏳ HURRY!', nocap=True)
it('offer', 64.7, 66.4, title='<span class="y">3 DAYS</span> TRIAL', tsz=110, sub='BUTTERFLY WELLNESS', value=1500, ky=560, tty=320,
   items=['BMR', 'BMI', 'BODY FAT ANALYSIS', '3 DAYS TRIAL'], cues={'items': [0, 0, 0, 0], 'strike': .05, 'free': .15, 'vt': -1}, nocap=True)
# CTA
clip(66.4, 69.0, C + 'S16.mp4', ss=1.5, rate=1.1, z1=1.12); it('cta', 66.4, 69.0, label='📅 BOOK APPOINTMENT', y=330, arrow='↓', badge='👇 LINK BELOW')
it('endcard2', 69.0, TOTAL, icon='🦋', name='BUTTERFLY WELLNESS', nsz=104, sub='NUTRITION CENTER', line='BMR • BMI • BODY FAT • 3 DAYS TRIAL', btn='📅 BOOK APPOINTMENT', badge='FIRST 10 • FREE', loc='மதுரை', nocap=True)
# captions
cap(0.0, 1.45, 'HELLO மதுரை மக்களே!', [1])
cap(1.45, 3.0, 'WEIGHT LOSS TRY பண்ணி', [0, 1])
cap(3.0, 4.4, 'ரொம்ப கஷ்டப்படுறீங்களா?', [1], '#FF6B60')
cap(8.9, 11.4, 'DIET, WORKOUT, FASTING', [0, 1, 2], '#FF6B60')
cap(11.4, 13.8, 'TRY பண்ணியும் RESULT இல்ல', [2, 3], '#FF6B60')
cap(13.8, 16.5, 'எங்களைப் பத்தி கேள்விப்பட்டு வந்தாங்க', [2])
cap(16.5, 19.5, 'அவங்க BODY-ஐ ANALYSE பண்ணி', [1, 2])
cap(19.5, 22.7, 'அவங்களுக்கு SUITABLE METHOD சொல்லி', [1, 2])
cap(22.7, 24.6, 'PERSONALIZED GUIDANCE கொடுத்து', [0, 1])
cap(29.5, 34.0, 'FAT-ஆ இருந்தவங்க FIT-ஆ இருக்காங்க', [2])
cap(34.0, 37.3, 'YES, MYSELF SATHISH KUMAR', [2, 3], '#FFD60A')
cap(37.3, 40.4, 'BUTTERFLY WELLNESS NUTRITION CENTER', [0, 1])
cap(40.4, 41.5, 'பேசுறேன்', [])
cap(45.0, 47.8, 'WEIGHT LOSS, HEALTH, LIFESTYLE', [0, 1, 2, 3])
cap(47.8, 49.6, 'இதெல்லாம் சொல்லிக் கொடுத்து', [])
cap(66.4, 68.3, 'APPOINTMENT IMMEDIATELY BOOK பண்ணுங்க', [0, 1, 2], '#FFD60A')
cap(68.3, 69.0, 'THANK YOU!', [0, 1])
# sfx
for t in [1.45, 4.4, 8.9, 9.9, 10.7, 13.8, 16.5, 19.5, 22.7, 24.6, 41.5, 45.0, 49.6, 52.0, 62.9, 66.4]: sfx.append([t, 'whoosh'])
for t in [9.0, 9.95, 10.75, 17.3, 22.8, 45.1, 46.1, 46.7, 20.0, 20.5, 21.0, 21.5]: sfx.append([t, 'pop'])
sfx += [[0.0, 'hit'], [12.7, 'thud'], [32.6, 'ding'], [34.0, 'hit'], [41.7, 'tick'], [43.4, 'tick'], [49.7, 'ding'], [52.5, 'cash'],
        [54.6, 'tick'], [55.4, 'tick'], [56.1, 'tick'], [61.2, 'tick'], [64.75, 'thud'], [64.85, 'hit'], [66.4, 'riser'], [69.0, 'hit']]
music = [[0, 1.45, 'pulse'], [1.45, 13.8, 'dark'], [13.8, 34.0, 'warm'], [34.0, 62.9, 'tech'], [62.9, TOTAL, 'uplift']]
json.dump(dict(total=TOTAL, clips=clips, items=items, captions=caps, sfx=sfx, music=music, voice_at=0.0), open(WD + '/timeline.json', 'w'), ensure_ascii=False, indent=1)
print(len(clips), 'clips', len(items), 'items', len(caps), 'captions')
