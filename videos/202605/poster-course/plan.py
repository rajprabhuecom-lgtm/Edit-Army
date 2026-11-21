"""poster-course: ₹999 implementation program (1334058822124176.mp4, 75.8 s). Times = SOURCE seconds.
SRT 17932675128270179 is in sync up to ~50 s and runs ~2 s long by the end; cue times after 50 s are scaled by 0.92.
The source has burned-in red offer banners (top + bottom); they stay. No B-roll over price, fee-increase or CTA lines."""
SRC = '1334058822124176.mp4'
END, HOLD = 75.40, 1.6
BLUR = [1215, 1320]; CAPY, CAPH = 1185, 160
CTA_CAP_HI = False
NOZOOM = [(0.0, 99.0)]          # zooms would crop the burned-in offer banners
BROLL = [
 ('B01', 1.60, 6.12, 'posters', 'split', dict(chip='⚡ BETTER THAN A DESIGNER', cc=4.20), '"in AI, in 30 seconds, super posters, better than a designer"'),
 ('B02', 16.14, 22.74, 'posters', 'split', dict(title='<span class="y">UNLIMITED</span> POSTERS', chip='🤯 MIND-BLOWING', cc=19.6, gap=0.25), '"use AI properly - unlimited, mind-blowing posters"'),
 ('B03', 22.74, 27.90, 'camfear', 'split', dict(xc=24.60, bc=25.90), '"break your camera fear, turn your face into a brand"'),
 ('B04', 27.90, 32.56, 'growth', 'split', dict(title='ONLINE <span class="g">CLIENTS</span>', chip='📲 CONSISTENTLY'), '"bring clients online for your talent, consistently"'),
 ('B05', 45.04, 51.12, 'gbp', 'split', dict(chip='📞 LEADS FOR LIFE', cc=48.9), '"bonus: Google Business Profile top 3 ranks -> leads for life"'),
]
GFX = [
 ('badge', 0.40, 1.60, {'html': '🤖 AI POSTERS • 30 SEC', 'y': 260, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('text', 8.76, 11.10, {'html': 'WHY STILL<br><span class="y">WAITING?</span> ⏳', 'y': 250, 'size': 104}),
 ('badge', 11.10, 16.14, {'html': '😕 AI = CONFUSION?', 'y': 260, 'size': 62}),
 ('badge', 32.56, 37.00, {'html': '🎓 IMPLEMENTATION PROGRAM', 'y': 260, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 54}),
 ('price', 37.00, 40.84, {'val': 999, 'per': 'LAUNCHING PRICE', 'y': 240, 'size': 220}),
 ('badge', 40.84, 45.04, {'html': '🎁 + BONUS COURSE', 'y': 260, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('badge', 51.12, 54.00, {'html': '⏺️ RECORDING NOW', 'y': 260, 'bg': 'var(--rd)', 'size': 62}),
 ('price', 54.00, 57.03, {'val': 5000, 'per': 'COURSE FEE AFTER THAT', 'y': 240, 'size': 200, 'col': 'var(--rd)', 'psz': 54}),
 ('stamp', 57.03, 60.65, {'big': 'FREE', 'small': 'BONUS FOR<br>LAUNCH BUYERS', 'y': 230}),
 ('cta', 60.65, 67.00, {'label': '👆 LINK IN BIO', 'arrow': '', 'badge': '⏳ LIMITED TIME', 'y': 300}),
 ('text', 69.54, 72.14, {'html': 'YOUR TALENT<br>➜ <span class="g">ONLINE</span>', 'y': 250, 'size': 104}),
 ('badge', 72.14, END, {'html': '🔥 ALL THE BEST', 'y': 260, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
 ('flash', END, END + 0.12, {}),
 ('endcard2', END, END + HOLD, {'emo': '🎓', 'l1': 'AI POSTERS', 'l2': '+ CAMERA FEAR BREAK', 'ts': 120, 'ts2': 80, 'btn': '👆 LINK IN BIO • ₹999', 'l3': 'PROFITSOUL'}),
]
CAP = [
 (0.40, 3.84, [['*AI-ல', '^30', '^SECONDS-ல'], ['உங்க', 'BUSINESS-க்கு'], ['SUPER', '*POSTERS']]),
 (3.84, 6.12, [['ஒரு', '!DESIGNER-ஐ', 'விட'], ['SUPER-ஆ', 'CREATE', 'பண்ணலாம்']]),
 (6.12, 8.76, [['அப்படின்னா', 'இன்னும்'], ['எதுக்காக', 'POSTERS']]),
 (8.76, 11.10, [['CREATE', 'பண்ணாம'], ['!WAIT', 'பண்றீங்க?']]),
 (11.10, 13.56, [['*HONEST-ஆ', 'சொல்லணும்னா']]),
 (13.56, 16.14, [['AI-ஐ', 'எப்படி', 'USE', 'பண்றது'], ['அதுதான்', '!CONFUSION']]),
 (16.14, 17.94, [['இந்த', '*AI-ஐ', '*PROPER-ஆ'], ['USE', 'பண்ணா']]),
 (17.94, 20.76, [['*UNLIMITED', 'ஆன'], ['^MIND-BLOWING']]),
 (20.76, 22.74, [['*POSTERS', 'CREATE'], ['பண்ண', 'முடியும்']]),
 (22.74, 25.26, [['உங்க', '!CAMERA', '!FEAR-ஐ'], ['*BREAK', 'பண்ணி']]),
 (25.26, 27.90, [['உங்க', '^FACE-ஐ'], ['ஒரு', '*BRAND-ஆ', 'மாத்துறது']]),
 (27.90, 30.64, [['உங்க', '^TALENT-க்கு'], ['ONLINE-ல', '*CLIENTS']]),
 (30.64, 32.56, [['*CONSISTENT-ஆ', 'கொண்டுவர்றது']]),
 (32.56, 34.96, [['இந்த', '*IMPLEMENTATION', '*PROGRAM-ல'], ['சொல்லியிருக்கேன்']]),
 (34.96, 37.00, [['^BIO-ல', 'CLICK', 'பண்ணி']]),
 (37.00, 38.92, [['^LAUNCHING', '^PRICE-ல'], ['JUST', '*₹999']]),
 (38.92, 40.84, [['WATCH', 'பண்ணலாம்'], ['எவ்வளவு', '*POSTERS', 'வேணாலும்']]),
 (40.84, 43.00, [['CAMERA', 'FEAR', 'மட்டும்', 'இல்லாம']]),
 (43.00, 45.04, [['ஒரு', '^BONUS', '^COURSE'], ['LAUNCH', 'பண்ண', 'போறேன்']]),
 (45.04, 47.44, [['*GOOGLE', '*BUSINESS', '*PROFILE-ல'], ['^TOP 3', 'RANKS']]),
 (47.44, 51.12, [['எடுத்துட்டா', 'உங்க'], ['*LIFE', 'TIME-க்கு', '*LEADS'], ['வந்துட்டே', 'இருக்கும்']]),
 (51.12, 52.89, [['எப்படி', 'பண்றதுன்னு'], ['^சொல்லித்', 'தரப்போறேன்']]),
 (52.89, 54.82, [['அந்த', 'COURSE', '^RECORD'], ['பண்ணதுக்கு', 'அப்புறம்']]),
 (54.82, 57.03, [['FEES', '!₹5,000-க்கு'], ['!INCREASE', 'ஆகும்']]),
 (57.03, 60.65, [['^LAUNCHING', '^PRICE-ல', 'வாங்குற'], ['எல்லாருக்கும்', '*FREE']]),
 (60.65, 62.86, [['இப்பவே', '^BIO-ல', 'இருக்கிற'], ['^LINK-ஐ', 'USE', 'பண்ணி']]),
 (62.86, 64.63, [['*IMMEDIATE-ஆ', 'BUY'], ['பண்ணிக்கோங்க']]),
 (64.63, 67.00, [['இது', '!LIMITED', '!TIME'], ['CHANCE']]),
 (67.00, 69.54, [['இந்த', '*OPPORTUNITY-ஐ'], ['USE', 'பண்ணிக்கோங்க']]),
 (69.54, 72.14, [['உங்க', '^TALENT-ஓ', '^BUSINESS-ஓ'], ['ONLINE-ல', '*PROJECT', 'பண்ணி']]),
 (72.14, END, [['*CLIENTS-ஐ', 'CONSISTENT-ஆ'], ['எடுங்க', '^ALL', '^THE', '^BEST']]),
]
PUNCH = [(0.3, 1.6, 1.12), (8.7, 11.1, 1.16), (11.1, 16.1, 1.08), (32.5, 37.0, 1.08), (40.8, 45.0, 1.10), (51.1, 54.0, 1.12), (60.6, 67.0, 1.06), (69.5, 72.1, 1.12), (72.1, 75.4, 1.16)]
MUSIC = [(0.0, 16.1, 'pulse'), (16.1, 32.5, 'tech'), (32.5, 60.6, 'warm'), (60.6, END + HOLD, 'uplift')]
SFX = [(0.40, 'hit'), (8.76, 'thud'), (11.10, 'pop'), (32.56, 'ding'), (40.84, 'ding'), (51.12, 'pop'), (60.20, 'riser'), (60.65, 'hit'), (72.14, 'ding')]
