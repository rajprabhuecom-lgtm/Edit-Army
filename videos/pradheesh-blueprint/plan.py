"""Coach Pradheesh: "Blueprint for Success" invite (vertical, Tamil + English). Source: C0073.MP4 (4K, camera on its side).
All times are SOURCE seconds in C0073.MP4. Engine: engine/v6-vertical-aurora. Run: python3 plan.py
Markup in text: *mint*  _yellow_  ~red~ ; Tamil runs get the Tamil font automatically."""
import sys
sys.path.insert(0, '/home/user/Edit-Army/engine/v6-vertical-aurora')
from planlib import Plan, build

# ---- best take of every line (retakes dropped) ----
KEEP = [(51.12, 59.77),   # hook: me + family, 18 years, no hospital visit, healthy lifestyle
        (74.69, 77.78),   # you can do it easily in 6 months (retake; "6 minutes" slip in take 8 dropped)
        (85.66, 88.44),   # you're asking what? Blueprint for Success
        (89.24, 92.95),   # transformation programme by my mentor Mr. Ravi Sundaram
        (105.60, 109.00), # in this programme my mentor, India's leading wellness coach
        (119.07, 121.72), # health, wealth, happiness - all three connected
        (141.77, 147.57), # learning through 26 years' experience guidance = big opportunity
        (161.66, 168.89), # in 26 years, 75 lakh families incl. mine - extraordinary person
        (178.11, 183.23), # last time I attended - learning & applying
        (191.91, 195.94), # I set 3 goals: health, wealth, happiness
        (212.13, 216.85), # didn't even try - it started happening automatically
        (223.25, 225.18), # you may ask: how, without trying?
        (231.32, 233.56), # that's where I understood something
        (267.75, 273.34), # don't chase the goal - become a person worthy of it
        (291.45, 295.53), # I changed myself - everything I wanted came looking for me
        (300.37, 302.29), # this time too I'm attending
        (325.87, 331.26), # to raise my standards, change myself, achieve bigger goals
        (337.60, 349.00)] # 2027 best version -> click link below, register now (+ end-card hold)
P = Plan(KEEP)

LAY = [(51.0, 52.55, 'full', {'z': 1.12}), (52.55, 59.9, 'card', {}),
       (74.6, 77.9, 'full', {'z': 1.38}),
       (85.6, 87.10, 'full', {'z': 1.55}), (87.10, 93.1, 'cardhi', {}),
       (105.5, 109.1, 'pip', {}), (119.0, 121.8, 'card', {}),
       (141.7, 147.7, 'cardhi', {}), (161.6, 169.0, 'pip', {}),
       (178.0, 183.3, 'full', {'z': 1.0}), (191.8, 217.0, 'card', {}),
       (223.2, 225.3, 'full', {'z': 1.5}), (231.2, 233.7, 'full', {'z': 1.08}),
       (267.7, 273.5, 'card', {}), (291.4, 295.6, 'pip', {}),
       (300.3, 302.4, 'full', {'z': 1.3}), (325.8, 331.4, 'card', {}),
       (337.5, 341.45, 'full', {'z': 1.15}), (341.45, 345.1, 'full', {'z': 1.32}), (345.1, 349.1, 'blur', {})]
ZOOM = []
FX = [(51.0, 52.5, {'spot': 1.0}), (74.69, 75.3, {'shake': 22}), (74.69, 74.95, {'zb': 1.0}),
      (85.66, 85.9, {'zb': 0.8}), (87.0, 87.4, {'gl': 1.0}), (164.54, 165.1, {'shake': 16}),
      (223.25, 223.5, {'zb': 0.8}), (231.32, 233.56, {'spot': 0.9}), (267.75, 268.0, {'shake': 26}),
      (300.37, 300.6, {'zb': 0.7}), (341.54, 341.8, {'zb': 0.8})]
SHATTER = [267.75]

G = 'glass'; T = 'pill'
ITEMS = [
 # ---------- HOOK ----------
 {'k': T, 'a': 51.15, 'b': 52.55, 'v': 'நானும் என் *குடும்பமும்*', 'y': 1560},
 {'k': 'tpill', 'a': 51.3, 'b': 52.5, 'v': '👨‍👩‍👧 FAMILY HEALTH', 'y': 90},
 {'k': G, 'a': 52.6, 'b': 54.85, 'y': 150, 'eb': 'ME + MY FAMILY', 'title': 'HEALTHY FOR', 'body': {'k': 'big', 'n': 18, 'from': 0, 'at': 52.7, 'd': 1.0, 'l': '*YEARS*', 'fs': 250}},
 {'k': G, 'a': 54.85, 'b': 59.85, 'y': 150, 'eb': '18 YEARS', 'title': 'ஒரு *HOSPITAL* VISIT கூட இல்லாம',
  'rows': [{'ic': '🏥', 'lb': 'Hospital visit', 'kind': 'x', 'on': 55.1, 'strike': 55.2, 'at': 54.95},
           {'ic': '🥗', 'lb': '*Healthy* lifestyle', 'on': 56.7, 'at': 56.6},
           {'ic': '👨‍👩‍👧', 'lb': 'Whole *family*', 'on': 58.4, 'at': 57.4}]},
 {'k': T, 'a': 52.6, 'b': 54.84, 'v': '*18* வருஷமா', 'y': 1660},
 {'k': T, 'a': 54.84, 'b': 56.56, 'v': '*HOSPITAL VISIT* இல்லாம', 'y': 1660},
 {'k': T, 'a': 56.58, 'b': 59.77, 'v': '*HEALTHY* LIFESTYLE', 'y': 1660},
 # ---------- 6 MONTHS ----------
 {'k': 'slam', 'a': 74.72, 'b': 77.78, 'v': '6 MONTHS', 'y': 170, 'fs': 165},
 {'k': 'lower', 'a': 75.2, 'b': 77.78, 'name': 'Coach *Pradheesh*', 'l2': 'TM Nutrition Centre', 'l3': '📍 Trichy', 'init': 'TM', 'y': 1300},
 {'k': T, 'a': 74.72, 'b': 77.78, 'v': '*6* மாசத்துல *EASY*-ஆ', 'y': 1600},
 # ---------- BLUEPRINT ----------
 {'k': 'tpill', 'a': 85.7, 'b': 87.1, 'v': '🤔 WHAT IS IT?', 'y': 140},
 {'k': T, 'a': 85.68, 'b': 87.1, 'v': 'என்னன்னு தானே *கேக்குறீங்க?*', 'y': 1560},
 {'k': 'flash', 'a': 87.12, 'b': 87.4, 'c': '#2EE59D', 'o': .55},
 {'k': G, 'a': 87.15, 'b': 89.3, 'y': 130, 'eb': 'THE PROGRAM', 'title': 'BLUEPRINT<br>FOR _SUCCESS_', 'body': {'k': 'lock', 'v': 'TRANSFORMATION', 'at': 87.2}},
 {'k': G, 'a': 89.3, 'b': 93.0, 'y': 130, 'eb': 'BLUEPRINT FOR SUCCESS', 'title': 'BY MY MENTOR<br>*MR. RAVI SUNDARAM*',
  'rows': [{'ic': '🧭', 'lb': 'My *mentor*', 'kind': 'check', 'at': 89.6, 'on': 89.8},
           {'ic': '🔥', 'lb': '*Transformation* program', 'kind': 'check', 'at': 91.4, 'on': 91.6}]},
 {'k': T, 'a': 87.15, 'b': 88.44, 'v': 'BLUEPRINT FOR *SUCCESS*', 'y': 1700},
 {'k': T, 'a': 89.24, 'b': 91.4, 'v': 'என்னோட MENTOR *RAVI SUNDARAM*', 'y': 1700},
 {'k': T, 'a': 91.4, 'b': 92.95, 'v': '*TRANSFORMATION* PROGRAM', 'y': 1700},
 # ---------- INDIA'S LEADING ----------
 {'k': G, 'a': 105.62, 'b': 109.05, 'y': 200, 'eb': 'MY MENTOR', 'title': "INDIA'S LEADING<br>*WELLNESS COACH*", 'body': {'k': 'big', 'v': '🇮🇳', 'fs': 200, 'at': 105.8}},
 {'k': T, 'a': 105.62, 'b': 107.0, 'v': 'இந்த *PROGRAM*-ல', 'y': 1150},
 {'k': T, 'a': 107.0, 'b': 109.0, 'v': "INDIA'S LEADING *COACH*", 'y': 1150},
 # ---------- HEALTH WEALTH HAPPINESS ----------
 {'k': 'stitle', 'a': 119.07, 'b': 121.75, 'v': 'மூணும் *CONNECTED*', 'y': 60},
 {'k': 'hub', 'a': 119.07, 'b': 121.75, 'y': 150, 'c': 'YOU', 'v': [{'e': '💪', 'n': 'Health', 'at': 119.1}, {'e': '💰', 'n': 'Wealth', 'at': 119.5}, {'e': '😊', 'n': 'Happiness', 'at': 119.85}]},
 {'k': 'words', 'a': 119.07, 'b': 121.75, 'y': 1520, 'w': [['HEALTH', 119.1, 0], ['WEALTH', 119.5, 1], ['HAPPINESS', 119.85, 0]]},
 # ---------- 26 YEARS ----------
 {'k': G, 'a': 141.8, 'b': 147.6, 'y': 110, 'eb': 'WHY THIS PROGRAM', 'bodyFirst': 1, 'body': {'k': 'big', 'n': 26, 'from': 0, 'at': 141.9, 'd': .9, 'suf': ' YRS', 'l': '*EXPERIENCE*', 'fs': 190},
  'rows': [{'ic': '🧭', 'lb': 'Experience *guidance*', 'at': 143.9, 'on': 144.1},
           {'ic': '📚', 'lb': '*Learn* from it', 'at': 144.9, 'on': 145.2},
           {'ic': '🚀', 'lb': 'Big *opportunity*', 'at': 145.9, 'on': 146.6}]},
 {'k': T, 'a': 141.8, 'b': 144.0, 'v': '*26 YEARS* EXPERIENCE', 'y': 1700},
 {'k': T, 'a': 144.03, 'b': 145.85, 'v': 'EXPERIENCE *GUIDANCE*', 'y': 1700},
 {'k': T, 'a': 145.85, 'b': 147.57, 'v': 'பெரிய *OPPORTUNITY*', 'y': 1700},
 # ---------- 75 LAKH FAMILIES ----------
 {'k': G, 'a': 161.7, 'b': 168.95, 'y': 150, 'eb': 'IN 26 YEARS', 'title': 'LIVES *CHANGED*', 'body': {'k': 'big', 'n': 75, 'from': 0, 'at': 164.54, 'd': 1.0, 'suf': ' LAKH', 'l': 'FAMILIES · *INCLUDING MINE*', 'fs': 200}},
 {'k': G, 'a': 165.75, 'b': 168.95, 'y': 820, 'h': 330, 'body': {'k': 'dots', 'n': 5, 'at': 165.8, 'v': '', 'e': '🏡'}},
 {'k': T, 'a': 161.7, 'b': 164.5, 'v': 'என்னோட *FAMILY*-யும் சேர்த்து', 'y': 1200},
 {'k': T, 'a': 164.54, 'b': 166.74, 'v': '*75 LAKH* FAMILIES', 'y': 1200},
 {'k': T, 'a': 166.76, 'b': 168.89, 'v': '*EXTRAORDINARY* PERSON', 'y': 1200},
 # ---------- LAST TIME ----------
 {'k': G, 'a': 178.15, 'b': 183.25, 'y': 70, 'eb': '⏪ LAST TIME', 'title': 'LEARN → *APPLY*'},
 {'k': T, 'a': 178.15, 'b': 180.7, 'v': 'LAST TIME *ATTEND* பண்ணப்போ', 'y': 1600},
 {'k': T, 'a': 180.7, 'b': 183.23, 'v': 'LEARN & *APPLY*', 'y': 1600},
 # ---------- 3 GOALS -> AUTOMATIC ----------
 {'k': G, 'a': 191.95, 'b': 212.1, 'y': 140, 'eb': 'MY GOALS', 'title': 'நான் SET பண்ண *3 GOALS*',
  'rows': [{'ic': '💪', 'lb': 'Health', 'at': 193.8}, {'ic': '💰', 'lb': 'Wealth', 'at': 194.3}, {'ic': '😊', 'lb': 'Happiness', 'at': 194.75}]},
 {'k': G, 'a': 212.13, 'b': 216.9, 'y': 140, 'eb': 'IN FACT…', 'title': 'IT JUST *HAPPENED* ⚡',
  'rows': [{'ic': '💪', 'lb': 'Health', 'at': 212.2, 'on': 215.47}, {'ic': '💰', 'lb': 'Wealth', 'at': 212.3, 'on': 215.62}, {'ic': '😊', 'lb': 'Happiness', 'at': 212.4, 'on': 215.77}]},
 {'k': T, 'a': 191.95, 'b': 193.15, 'v': '*3 GOALS* SET பண்ணேன்', 'y': 1700},
 {'k': 'words', 'a': 193.17, 'b': 195.95, 'y': 1520, 'w': [['HEALTH', 193.8, 0], ['WEALTH', 194.3, 1], ['HAPPINESS', 194.75, 0]]},
 {'k': T, 'a': 212.15, 'b': 213.9, 'v': 'IN FACT, *TRY* கூட பண்ணல', 'y': 1700},
 {'k': T, 'a': 213.93, 'b': 216.85, 'v': '*AUTOMATIC*-ஆ நடந்துச்சு', 'y': 1700},
 # ---------- QUESTION + REALISATION (face) ----------
 {'k': 'tpill', 'a': 223.3, 'b': 225.18, 'v': '🤔 HOW? WITHOUT TRYING?', 'y': 150},
 {'k': T, 'a': 223.27, 'b': 225.18, 'v': 'TRY பண்ணாம *எப்படி?*', 'y': 1600},
 {'k': T, 'a': 231.35, 'b': 233.56, 'v': 'அங்க தான் *புரிஞ்சுது*', 'y': 1600},
 # ---------- PIVOT: SHATTER ----------
 {'k': 'flash', 'a': 267.75, 'b': 268.05, 'c': '#FF3B30', 'o': .6},
 {'k': 'vs', 'a': 267.95, 'b': 273.4, 'y': 200, 'ra': 270.15, 'l': {'h': "DON'T", 'rows': ['Chase the goal']}, 'r': {'h': 'DO', 'rows': ['Become *worthy* of the goal']}},
 {'k': 'words', 'a': 267.8, 'b': 270.1, 'y': 1500, 'w': [["DON'T", 267.85, 0], ['CHASE', 268.5, 1], ['THE', 268.9, 0], ['GOAL', 269.29, 0]]},
 {'k': 'words', 'a': 270.15, 'b': 273.35, 'y': 1500, 'w': [['BECOME', 270.15, 0], ['WORTHY', 270.93, 1], ['OF', 271.6, 0], ['IT', 271.8, 0]]},
 # ---------- CAME LOOKING FOR ME ----------
 {'k': 'hub', 'a': 291.5, 'b': 295.6, 'y': 170, 'c': 'ME', 'v': [{'e': '💪', 'n': 'Health', 'at': 294.35}, {'e': '💰', 'n': 'Wealth', 'at': 294.55}, {'e': '😊', 'n': 'Happiness', 'at': 294.75}, {'e': '🎯', 'n': 'Goals', 'at': 294.95}]},
 {'k': 'stitle', 'a': 291.5, 'b': 295.6, 'v': 'I *CHANGED* MYSELF', 'y': 60},
 {'k': T, 'a': 291.5, 'b': 294.3, 'v': 'என்னை நான் *மாத்திக்கிட்டேன்*', 'y': 1200},
 {'k': T, 'a': 294.35, 'b': 295.53, 'v': 'என்னை *தேடி* வந்துச்சு', 'y': 1200},
 # ---------- THIS TIME ----------
 {'k': 'tpill', 'a': 300.4, 'b': 302.29, 'v': '🎟️ THIS TIME TOO', 'y': 150},
 {'k': T, 'a': 300.4, 'b': 302.29, 'v': 'இந்த தடவையும் *ATTEND* பண்றேன்', 'y': 1600},
 {'k': G, 'a': 325.9, 'b': 331.3, 'y': 140, 'eb': 'WHY I GO AGAIN', 'title': '*LEVEL UP* 📈',
  'rows': [{'ic': '📈', 'lb': 'My *standards*', 'at': 326.2, 'on': 326.5}, {'ic': '🔄', 'lb': '*Change* myself', 'at': 327.9, 'on': 328.2}, {'ic': '🚀', 'lb': '*Bigger* goals', 'at': 329.5, 'on': 329.9}]},
 {'k': T, 'a': 325.9, 'b': 328.05, 'v': 'என்னோட *STANDARDS*', 'y': 1700},
 {'k': T, 'a': 328.09, 'b': 329.55, 'v': 'என்னை *மாத்த*', 'y': 1700},
 {'k': T, 'a': 329.59, 'b': 331.26, 'v': '*BIGGER* GOALS', 'y': 1700},
 # ---------- CTA (face stays on) ----------
 {'k': G, 'a': 337.65, 'b': 341.45, 'y': 80, 'eb': 'YOUR NEXT LEVEL', 'title': '*2027*-ல உங்க<br>_BEST VERSION_'},
 {'k': T, 'a': 337.65, 'b': 339.35, 'v': '*2027*-ல', 'y': 1600},
 {'k': T, 'a': 339.38, 'b': 341.34, 'v': '*BEST VERSION* OF YOU', 'y': 1600},
 {'k': 'words', 'a': 341.54, 'b': 345.05, 'y': 160, 'w': [['CLICK', 341.6, 0], ['THE', 341.95, 0], ['LINK', 342.36, 1], ['BELOW', 342.7, 0], ['&', 343.38, 0], ['REGISTER', 343.5, 1], ['NOW', 343.95, 0]]},
 {'k': G, 'a': 341.55, 'b': 345.1, 'y': 1300, 'h': 470, 'body': {'k': 'btn', 'v': 'REGISTER NOW', 'at': 341.6, 'tag': '👇 LINK BELOW'}},
 # ---------- END CARD ----------
 {'k': G, 'a': 345.15, 'b': 349.0, 'y': 110, 'eb': 'TRANSFORMATION PROGRAM', 'title': 'BLUEPRINT<br>FOR _SUCCESS_', 'sub': 'by Mr. Ravi Sundaram',
  'body': {'k': 'btn', 'v': 'REGISTER NOW', 'at': 345.4, 'tag': '👇 LINK BELOW'}},
]
SFX = [(51.12, 'hit'), (52.55, 'swoosh'), (52.7, 'type'), (55.1, 'thud'), (56.7, 'toggle'), (58.4, 'toggle'),
       (74.69, 'boom'), (74.6, 'whoosh'), (75.2, 'swoosh'), (85.68, 'pop'), (87.0, 'glitch'), (87.12, 'hit'),
       (89.3, 'swoosh'), (89.8, 'pop'), (91.6, 'pop'), (105.6, 'swoosh'), (105.8, 'pop'),
       (119.07, 'swoosh'), (119.1, 'pop'), (119.5, 'pop'), (119.85, 'pop'),
       (141.8, 'swoosh'), (141.9, 'type'), (144.1, 'toggle'), (145.2, 'toggle'), (146.6, 'toggle'),
       (161.7, 'swoosh'), (164.54, 'cash'), (165.8, 'pop'), (178.1, 'whoosh'),
       (191.9, 'swoosh'), (193.8, 'pop'), (194.3, 'pop'), (194.75, 'pop'),
       (212.13, 'swoosh'), (215.47, 'toggle'), (215.62, 'toggle'), (215.77, 'toggle'), (216.0, 'ding'),
       (223.25, 'pop'), (231.32, 'clock'), (267.75, 'riser'), (267.75, 'glass'), (267.75, 'hit'), (270.15, 'ding'),
       (291.45, 'swoosh'), (294.35, 'pop'), (294.55, 'pop'), (294.75, 'pop'), (294.95, 'pop'),
       (300.37, 'whoosh'), (325.9, 'swoosh'), (326.5, 'toggle'), (328.2, 'toggle'), (329.9, 'toggle'),
       (337.6, 'swoosh'), (341.54, 'riser'), (341.6, 'hit'), (345.1, 'swoosh'), (345.4, 'boom')]
MUSIC = [(51.0, 87.0, 'pulse'), (87.0, 122.0, 'tech'), (141.7, 183.3, 'warm'), (191.8, 217.0, 'tech'), (223.2, 267.7, 'dark'),
         (267.7, 302.4, 'warm'), (325.8, 349.1, 'uplift')]

if __name__ == '__main__':
    build(P, LAY, ZOOM, FX, ITEMS, SFX, MUSIC, SHATTER)
