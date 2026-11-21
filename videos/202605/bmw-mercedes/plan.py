"""bmw-mercedes: positioning lesson (989137733604641.mp4, 83.2 s). Times = SOURCE seconds (SRT 18092278709351392 is in sync)."""
SRC = '989137733604641.mp4'
END, HOLD = 82.70, 1.6
BLUR = [1255, 1350]; CAPY, CAPH = 1215, 180
BROLL = [
 ('B01', 2.00, 8.90, 'versus', 'split', dict(title='⚔️ <span class="r">COMPETITION</span>', A=['🏎️', 'BMW', []], B=['🚘', 'MERCEDES', []], tb=2.00, ta=4.00, tv=4.40),
  '"only two compete: Mercedes-Benz and BMW"'),
 ('B02', 18.30, 30.08, 'versus', 'split', dict(title='<span class="y">POSITIONING</span>', A=['🏎️', 'BMW', ['⚡ SPEED', '🏁 PERFORMANCE']], B=['🚘', 'MERCEDES', ['🛋️ COMFORT', '💼 BUSINESS CLASS']],
  ta=18.60, tb=25.30, tv=25.60, ca=[21.90, 22.70], cb=[28.00, 29.10]), '"BMW = speed, performance; Mercedes = comfort, business class"'),
 ('B03', 33.04, 38.32, 'bullseye', 'split', dict(title='YOUR <span class="y">POSITION</span> 🎯', chips=['✅ SET PROPERLY', '😌 NO COMPETITOR TENSION'], hit=34.60, ccues=[35.0, 36.9]),
  '"set your position properly -> no need to think about competitors"'),
 ('B04', 41.42, 48.20, 'bullseye', 'split', dict(title='<span class="y">TARGET</span> AUDIENCE', chips=['⚔️ COMPETITION?', '👥 TARGET AUDIENCE?', '✅ CLEARLY DEFINED'], hit=44.40, ccues=[42.6, 44.6, 46.3]),
  '"who is their competition, who is their target audience - clearly defined"'),
 ('B05', 51.20, 58.14, 'growth', 'split', dict(title='HIGH <span class="y">CLARITY</span> = <span class="g">SALES</span>', chip='💰 SELLS VERY EASILY'),
  '"whoever has high clarity, their product sells very easily"'),
 ('B06', 63.92, 68.84, 'bullseye', 'split', dict(title='THEIR <span class="r">PAIN POINT</span>', chips=['🎯 EXACT PAIN POINT', '🗣️ TALK ABOUT IT'], hit=64.6, ccues=[65.0, 66.4]),
  '"talk exactly about your target audience\'s pain point"'),
 ('B07', 77.04, 80.34, 'foundation', 'split', dict(B=[['📢 MARKETING', '#00C896', '#04110c'], ['📈 SALES', '#FFD60A', '#000']], cues=[78.20, 78.90]),
  '"positioning statement is the basic foundation of a business"'),
]
GFX = [
 ('badge', 0.47, 2.00, {'html': '🏎️ BMW vs MERCEDES 🚘', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('text', 9.40, 11.20, {'html': 'LUXURY? <span class="r">✕</span>', 'y': 210, 'size': 130}),
 ('badge', 11.20, 14.40, {'html': '🧠 BUSINESS STRATEGY', 'y': 230, 'size': 62}),
 ('cta', 14.40, 18.20, {'label': '➕ FOLLOW', 'arrow': '', 'badge': '📚 MORE BUSINESS STRATEGIES', 'y': 1040}),
 ('text', 31.30, 33.04, {'html': 'THIS IS<br><span class="y">POSITIONING</span>', 'y': 200, 'size': 110}),
 ('badge', 59.60, 63.90, {'html': '❓ YOUR TARGET AUDIENCE?', 'y': 230, 'size': 58}),
 ('text', 70.66, 74.06, {'html': 'MARKETING<br><span class="g">= EASY ✓</span>', 'y': 200, 'size': 112}),
 ('text', 74.06, 77.04, {'html': 'SALES COME<br><span class="y">TO YOU 🧲</span>', 'y': 200, 'size': 112}),
 ('badge', 80.34, END, {'html': '🏎️ LIKE BMW M SERIES', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('flash', END, END + 0.12, {}),
 ('endcard2', END, END + HOLD, {'emo': '🎯', 'l1': 'POSITIONING', 'l2': 'BUSINESS STRATEGIES', 'btn': '➕ FOLLOW FOR MORE', 'l3': 'PROFITSOUL'}),
]
CAP = [
 (0.47, 2.30, [['ரெண்டே', 'பேருக்கு', 'நடுவுல', 'தான்'], ['!போட்டி']]),
 (2.30, 3.70, [['ஒண்ணு', '*MERCEDES-BENZ']]),
 (3.70, 5.40, [['இன்னொன்னு', '^BMW']]),
 (5.40, 8.94, [['AUTOMOBILE', 'INDUSTRY-ல'], ['ஒரு', '!பயங்கர', '!COMPETITION']]),
 (8.94, 11.20, [['^LUXURY-ல', 'னு', 'நினைக்கிறோம்'], ['BUT', '!அது', '!இல்ல']]),
 (11.20, 13.86, [['இதை', '*DEEP-ஆ', 'EXPLAIN'], ['பண்ண', 'போறேன்']]),
 (13.86, 17.24, [['இந்த', 'மாதிரி', '*BUSINESS', '*STRATEGIES'], ['வேணும்னா', 'இப்பவே']]),
 (17.24, 18.70, [['^FOLLOW', 'பண்ணிக்கோங்க']]),
 (18.70, 20.98, [['*BMW', 'அப்படிங்கிற'], ['வார்த்தையை', 'கேட்டா']]),
 (20.98, 24.42, [['^SPEED,', '^PERFORMANCE'], ['ஞாபகத்துக்கு', 'வருதா?']]),
 (24.42, 27.10, [['*MERCEDES-BENZ'], ['கேட்ட', 'உடனே']]),
 (27.10, 30.08, [['^COMFORT,'], ['^BUSINESS', 'CLASS', 'வாங்குவாங்க']]),
 (30.08, 33.04, [['இதுதான்', 'அவங்களோட'], ['*POSITIONING']]),
 (33.04, 36.06, [['உங்க', 'BUSINESS-க்கு'], ['*POSITION', 'சரியா', 'SET', 'பண்ணா']]),
 (36.06, 38.32, [['*COMPETITOR', 'பத்தி'], ['!யோசிக்கவே', 'வேண்டாம்']]),
 (38.32, 41.42, [['இதே', 'மாதிரி', 'தான்'], ['*BMW-ம்', '*MERCEDES-ம்']]),
 (41.42, 45.48, [['அவங்க', '^COMPETITION', 'யாரு?'], ['*TARGET', '*AUDIENCE', 'யாரு?']]),
 (45.48, 48.20, [['*CLEAR-ஆ', 'DEFINE'], ['பண்ணியிருக்காங்க']]),
 (48.20, 51.62, [['யாரோட', 'PRODUCT'], ['^SUPER-ஆ', 'SELL', 'ஆகும்?']]),
 (51.62, 55.08, [['*HIGH', '*CLARITY', 'இருக்கிறவங்க'], ['அவங்க', 'PRODUCT']]),
 (55.08, 58.14, [['ரொம்ப', '*EASY-ஆ'], ['*SALE', 'ஆயிடும்']]),
 (58.14, 61.84, [['உங்க', '^TARGET', '^AUDIENCE'], ['யாருன்னு']]),
 (61.84, 63.92, [['*CLEAR-ஆ', 'POINT', 'பண்ணிருக்கீங்களா?']]),
 (63.92, 68.84, [['அவங்க', '!PAIN', '!POINT', 'பத்தி'], ['*EXACT-ஆ', 'பேசுறீங்களா?'], ['அதுதான்', 'முக்கியம்']]),
 (68.84, 70.66, [['*POSITIONING', '*STATEMENT-ல'], ['WORK', 'பண்ணா']]),
 (70.66, 74.06, [['உங்க', '*MARKETING'], ['ரொம்ப', '^EASY']]),
 (74.06, 77.04, [['*SALES', 'உங்களை'], ['^தேடி', '^வரும்']]),
 (77.04, 80.34, [['*POSITIONING', 'தான்'], ['BUSINESS-ஓட', '^அஸ்திவாரம்']]),
 (80.34, END, [['வேலை', 'ஆரம்பிங்க'], ['*BMW', '*M', '*SERIES', 'மாதிரி']]),
]
PUNCH = [(0.4, 2.0, 1.12), (9.0, 11.2, 1.16), (11.2, 14.4, 1.08), (30.1, 33.0, 1.12), (58.2, 63.9, 1.10), (70.6, 74.0, 1.12), (74.0, 77.0, 1.16), (80.3, 82.7, 1.12)]
MUSIC = [(0.0, 18.3, 'pulse'), (18.3, 58.2, 'tech'), (58.2, 68.8, 'dark'), (68.8, END + HOLD, 'uplift')]
SFX = [(0.47, 'hit'), (9.40, 'thud'), (31.30, 'hit'), (59.60, 'thud'), (70.66, 'ding'), (74.06, 'cash'), (80.34, 'pop')]
