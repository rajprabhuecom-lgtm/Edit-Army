"""V1 'Walk & Talk' (VID_20260728_223422_561_bsl). Source time; final = output/1.2.
Already tight-cut source, burned header (y 65-215), burned small captions (y 1458-1512, blurred), burned banner (y 1566-1836)."""
W = '/home/user/work/v/15QigsqdRaJRRGs-XKo2LQtdrSC6c79W_/'
CFG = dict(capTop=1290, capH=260, blur=[(100, 1370, 980, 1575)], cy=700)
BROLL = [
 ('B01', 4.70, 9.30, 'walktalk', 'split', dict(chip='📱 + MODERN SOCIAL MEDIA', chipAt=0.6), '"modern way of social media - walk & talk activity"'),
 ('B02', 11.00, 16.00, 'social', 'split', dict(chip='👥 UNKNOWN CIRCLE → YOUR CENTRE', chipAt=2.4), '"through social media, from unknown circles, to your wellness centre"'),
 ('B03', 16.08, 19.90, 'walkin', 'split', dict(title='NEW GUESTS <span class="g">CONSISTENTLY</span>'), '"bring new guests consistently into your centre"'),
 ('B04', 19.96, 23.70, 'centres', 'full', dict(title='<span class="y">50+</span> WELLNESS<br>CENTRES ✓'), '"already implemented in 50+ wellness centres and got results"'),
]
GFX = [
 ('text', 0.20, 2.00, {'html': '<span class="g">WALK &amp; TALK</span> 🚶', 'y': 270, 'size': 120}),
 ('text', 2.04, 4.65, {'html': 'CLIENT BASE<br><span class="y">INCREASE?</span> 📈', 'y': 270, 'size': 110}),
 ('badge', 23.84, 26.90, {'html': '💬 LET\'S DISCUSS', 'y': 280, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 70}),
 ('text', 26.97, 27.80, {'html': 'SAME <span class="g">SYSTEM</span><br>FOR YOU?', 'y': 270, 'size': 110}),
 ('flash', 27.80, 27.95, {}),
 ('cta', 27.81, 30.45, {'label': '👇 CLICK THE LINK', 'badge': '📅 BOOK APPOINTMENT', 'y': 1000}),
 ('badge', 30.50, 33.30, {'html': '📞 IN THIS APPOINTMENT', 'y': 280, 'bg': 'var(--yl)', 'fg': '#000', 'size': 64}),
 ('text', 33.35, 36.85, {'html': 'EXTRA<br><span class="g">NEW GUESTS</span>', 'y': 270, 'size': 120}),
 ('text', 36.93, 40.50, {'html': 'DISCUSS →<br><span class="y">IMPLEMENT ⚡</span>', 'y': 270, 'size': 110}),
 ('flash', 40.55, 40.70, {}),
 ('cta', 40.59, 45.70, {'label': '📅 BOOK APPOINTMENT', 'badge': 'WELLNESS COACHING GROWTH PROGRAM', 'y': 1000}),
 ('endps', 45.75, 999, {}),
]
CAP = [
 (0.00, 2.00, [['ஒரு', '*WELLNESS', '*COACH-ஆ'], ['^WALK & TALK']]),
 (2.04, 4.70, [['உங்க', '^CLIENT BASE'], ['*INCREASE', 'பண்ணனுமா?']]),
 (4.78, 7.00, [['^MODERN WAY', 'OF'], ['*SOCIAL MEDIA']]),
 (7.00, 9.30, [['இந்த', '^WALK & TALK'], ['*ACTIVITY', 'நம்மால', 'முடியும்']]),
 (9.38, 11.00, [['இந்த மாதிரி', '*ACTIVITY'], ['செஞ்சு']]),
 (11.04, 13.40, [['உங்க', '*WELLNESS CENTRE'], ['^SOCIAL MEDIA', 'மூலமா']]),
 (13.48, 16.00, [['^தெரியாத', 'வட்டத்துல', 'இருந்து']]),
 (16.08, 19.90, [['*NEW GUESTS', '^CONSISTENT-ஆ'], ['உங்க', 'சென்டருக்குள்'], ['இந்த', '*METHOD', 'மூலமா']]),
 (19.96, 23.70, [['ALREADY', '^50+', '*WELLNESS'], ['*CENTRES-க்கு', 'IMPLEMENT'], ['பண்ணி', '*RESULT', 'எடுத்து', 'கொடுத்தது']]),
 (23.84, 26.90, [['அப்புறம்', 'தான்', 'உங்ககிட்ட'], ['^DISCUSS', 'பண்றேன்']]),
 (26.97, 27.80, [['இதே', '*SYSTEM', 'வேணுமா?']]),
 (27.81, 30.45, [['இப்பவே', '^கீழே', 'LINK'], ['^CLICK', 'பண்ணி'], ['*APPOINTMENT', 'BOOK', 'பண்ணுங்க']]),
 (30.50, 33.30, [['இந்த', '^APPOINTMENT-ல'], ['இந்த', '*ONLINE SYSTEM', 'மூலமா']]),
 (33.35, 36.85, [['உங்க', 'சென்டருக்கு'], ['^EXTRA', '*NEW GUESTS'], ['எப்படி', 'கொண்டு வரலாம்']]),
 (36.93, 40.50, [['இதை', '^DISCUSS', 'பண்ணி'], ['உடனே', '*IMPLEMENT', 'பண்ணலாம்']]),
 (40.59, 45.70, [['இப்பவே', 'உங்களுக்கான'], ['^WELLNESS COACHING'], ['*GROWTH PROGRAM']]),
 (45.77, 47.20, [['*APPOINTMENT', 'BOOK', 'பண்ணுங்க']]),
]
PUNCH = [(0.0, 2.0, 1.12), (2.0, 4.7, 1.06), (9.38, 11.0, 1.14), (23.84, 26.9, 1.06), (26.97, 27.8, 1.16), (27.8, 30.5, 1.10),
         (33.35, 36.9, 1.12), (36.9, 40.5, 1.06), (40.59, 45.7, 1.14)]
MUSIC = [(0.0, 9.3, 'pulse'), (9.3, 27.8, 'tech'), (27.8, 999, 'uplift')]
SFX = [(0.20, 'hit'), (2.04, 'pop'), (26.97, 'thud'), (27.40, 'riser'), (27.81, 'hit'), (40.59, 'hit')]
SCENE_SFX = {
 'walktalk': [(.3, 'pop'), (.8, 'whoosh'), (1.3, 'pop'), (1.6, 'pop'), (1.9, 'pop'), (2.2, 'ding')],
 'social': [(.3, 'pop'), (.7, 'ding'), (1.2, 'tick'), (1.6, 'tick'), (2.0, 'tick'), (2.6, 'pop')],
 'walkin': [(.1, 'pop')] + [(.42 * i + 2.3, 'tick') for i in range(6)],
 'centres': [(.2 + .22 * i, 'tick') for i in range(9)] + [(2.4, 'ding')],
}
