"""what-business: "What business are you really in?" (27175928192023440.mp4, 74.8 s). Times = SOURCE seconds.
SRT 18097698101234155 is in sync up to ~55 s and runs ~1.7 s long by the end; cue times after 55 s are scaled by 0.903."""
SRC = '27175928192023440.mp4'
END, HOLD = 74.40, 1.6
BLUR = [1255, 1350]; CAPY, CAPH = 1215, 180
BROLL = [
 ('B01', 1.90, 4.60, 'percent', 'split', dict(n=9, val=90, title='BUSINESS OWNERS', label='❓ என்ன BUSINESS-னே தெரியல', lc=2.6), '"90% of business owners don\'t know what business they are in"'),
 ('B02', 11.20, 18.20, 'reframe', 'split', dict(A=['🧴', 'SKIN CARE'], B=['😎', 'CONFIDENCE'], xc=15.10, bc=16.00), '"a skin care brand is really in the confidence business"'),
 ('B03', 29.40, 36.00, 'reframe', 'split', dict(A=['🏋️', 'GYM'], B=['💪', 'TRANSFORMATION'], xc=31.70, bc=34.10), '"you are not in the gym business, you are in the transformation business"'),
 ('B04', 46.60, 51.42, 'bullseye', 'split', dict(title='🧠 <span class="y">PSYCHOLOGY</span>', chips=['🎯 EXACT OUTCOME?', '👥 WHAT CLIENTS EXPECT'], hit=48.6, ccues=[49.4, 50.3]),
  '"what is the psychology behind your business, what exact outcome do people expect"'),
 ('B05', 53.50, 60.40, 'align', 'split', dict(ok='✅ ONE LINE = GROWTH'), '"your marketing and client expectation will be on the same line"'),
 ('B06', 60.40, 63.20, 'growth', 'split', dict(title='AUTOMATIC <span class="g">GROWTH</span> 📈', chip='🚀 SCALE'), '"growth comes automatically and you scale"'),
]
GFX = [
 ('badge', 0.36, 1.90, {'html': '⚠️ 90% BUSINESS OWNERS', 'y': 230, 'bg': 'var(--rd)', 'size': 62}),
 ('text', 4.60, 6.18, {'html': 'TOO <span class="r">HARSH?</span> 😬', 'y': 210, 'size': 120}),
 ('badge', 6.18, 8.20, {'html': '💡 REALITY', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
 ('cta', 8.20, 10.50, {'label': '➕ FOLLOW', 'arrow': '', 'badge': '📚 MORE BUSINESS VIDEOS', 'y': 1040}),
 ('badge', 18.90, 23.20, {'html': '💄 LOOK GOOD = FEEL CONFIDENT', 'y': 230, 'size': 52}),
 ('text', 23.30, 28.70, {'html': 'SELL THE<br><span class="g">CONFIDENCE</span>', 'y': 200, 'size': 112}),
 ('text', 36.00, 39.46, {'html': 'FITNESS TIPS <span class="r">✕</span>', 'y': 210, 'size': 104}),
 ('text', 39.46, 46.60, {'html': 'SELL THE<br><span class="g">TRANSFORMATION</span> ✓', 'y': 200, 'size': 96}),
 ('text', 66.10, 68.40, {'html': 'WHAT BUSINESS<br>ARE YOU <span class="y">REALLY</span> IN?', 'y': 190, 'size': 92}),
 ('badge', 68.40, 71.10, {'html': '🔁 ASK AGAIN & AGAIN', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 62}),
 ('badge', 71.10, END, {'html': '✅ YOU WILL GET THE ANSWER', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 56}),
 ('flash', END, END + 0.12, {}),
 ('endcard2', END, END + HOLD, {'emo': '🧠', 'l1': 'WHAT BUSINESS', 'l2': 'ARE YOU REALLY IN?', 'ts': 110, 'ts2': 84, 'btn': '➕ FOLLOW FOR MORE', 'l3': 'PROFITSOUL'}),
]
CAP = [
 (0.36, 2.04, [['*90%', 'BUSINESS', 'OWNERS']]),
 (2.04, 3.84, [['என்ன', 'BUSINESS', 'பண்றோம்னே'], ['!தெரியல']]),
 (3.84, 6.18, [['ரொம்ப', '!HARSH-ஆ', 'இருக்கா?'], ['^REALITY', 'சொல்றேன்']]),
 (6.18, 8.58, [['இந்த', 'மாதிரி', '*BUSINESS', '*VIDEOS'], ['வேணும்னா']]),
 (8.58, 10.50, [['உடனே', '^FOLLOW', 'பண்ணிக்கோங்க']]),
 (10.50, 13.80, [['ரொம்ப', '^IMPORTANT'], ['ஒரு', '*SKIN CARE', 'BRAND']]),
 (13.80, 15.54, [['*SKIN CARE', 'BUSINESS-ல'], ['இருக்கோம்னு', 'நினைக்கிறாங்க']]),
 (15.54, 18.24, [['BUT', 'அவங்க', 'ஒரு'], ['*CONFIDENCE', 'BUSINESS-ல']]),
 (18.24, 21.00, [['நான்', '*CONFIDENT-ஆ', 'இருக்க'], ['SKIN CARE,', 'COSMETICS']]),
 (21.00, 23.28, [['USE', 'பண்ணி', '^FACE-ஐ'], ['^REPRESENTABLE-ஆ', 'காட்டுறேன்']]),
 (23.28, 25.98, [['அப்போ', '*CONFIDENCE', 'பத்தி'], ['MARKETING-ல', 'பேசணும்']]),
 (25.98, 28.74, [['இப்படி', 'தான்', 'உங்க'], ['*BUSINESS-ஐ', 'பார்க்கணும்']]),
 (28.74, 30.88, [['நீங்க', 'ஒரு', '^GYM', 'RUN'], ['பண்றீங்களா?']]),
 (30.88, 33.54, [['நீங்க', '!GYM', 'BUSINESS-ல'], ['!கிடையாது']]),
 (33.54, 35.92, [['*TRANSFORMATION'], ['BUSINESS-ல', 'இருக்கீங்க']]),
 (35.92, 39.46, [['^FITNESS', 'எப்படி', 'பண்ணணும்னு'], ['PROJECT', 'பண்ணாதீங்க']]),
 (39.46, 41.50, [['*TRANSFORMATION-ஐ'], ['PROJECT', 'பண்ணுங்க']]),
 (41.50, 44.08, [['PEOPLE', 'ARE', 'LOOKING', 'FOR'], ['*TRANSFORMATION']]),
 (44.08, 46.60, [['உங்க', 'BUSINESS-க்கு'], ['பின்னாடி', 'இருக்கிற']]),
 (46.60, 49.42, [['*PSYCHOLOGY', 'என்ன?'], ['மக்கள்', 'உங்ககிட்ட']]),
 (49.42, 51.42, [['என்ன', '^EXACT', '^OUTCOME'], ['எதிர்பார்க்கிறாங்க?']]),
 (51.42, 54.90, [['அதை', 'யோசிச்சு'], ['உங்க', '*MARKETING-ல'], ['PRESENT', 'பண்ணுங்க']]),
 (54.90, 57.66, [['உங்க', '*MARKETING-ம்'], ['CLIENT', '*EXPECTATION-ம்']]),
 (57.66, 60.46, [['^ஒரே', '^LINE-ல', 'இருக்கும்']]),
 (60.46, 63.17, [['^AUTOMATIC-ஆ', '*GROWTH'], ['*SCALE', 'ஆகும்']]),
 (63.17, 66.10, [['இதை', 'உங்க', 'BUSINESS-ல'], ['^IMPLEMENT', 'பண்ணுங்க']]),
 (66.10, 68.40, [['WHAT', 'BUSINESS', 'ARE', 'YOU'], ['*REALLY', 'IN?']]),
 (68.40, 71.08, [['இந்த', 'கேள்வியை'], ['^மறுபடியும்', '^மறுபடியும்', 'கேளுங்க']]),
 (71.08, END, [['கண்டிப்பா', '*ANSWER', 'கிடைக்கும்'], ['அதுவரைக்கும்', '!விடாதீங்க']]),
]
PUNCH = [(0.3, 1.9, 1.12), (4.6, 6.2, 1.16), (18.9, 23.2, 1.08), (23.3, 28.7, 1.12), (36.0, 39.4, 1.14), (39.5, 46.6, 1.08), (66.1, 68.4, 1.18), (68.4, 71.1, 1.10), (71.1, 74.4, 1.14)]
DESAT = [(4.6, 6.18)]
MUSIC = [(0.0, 10.5, 'dark'), (10.5, 46.6, 'pulse'), (46.6, 63.2, 'tech'), (63.2, END + HOLD, 'uplift')]
SFX = [(0.36, 'hit'), (4.60, 'thud'), (6.18, 'ding'), (23.30, 'pop'), (36.00, 'thud'), (39.46, 'hit'), (66.10, 'hit'), (71.10, 'ding')]
