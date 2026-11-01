"""V6 'Walk & Talk online' (WC NEW.mp4). Clean source (no burned text)."""
W = '/home/user/work/v/1stCiGzZQc_nxlURRd86cqjA5tUKRJgJq/'
CFG = dict(capTop=1175, capH=300, blur=[], cy=700)
BROLL = [
 ('B01', 7.15, 10.10, 'walktalk', 'split', dict(title='🚶 WALK <span class="g">&amp;</span> TALK', chip='📍 OFFLINE • SO FAR', chipAt=1.0), '"so far we have done this through walk & talk"'),
 ('B02', 11.03, 13.60, 'social', 'split', dict(title='WALK &amp; TALK <span class="g">ONLINE</span>', chip='🌐 SAME ACTIVITY • ONLINE', chipAt=1.4), '"we can do this walk & talk online"'),
 ('B03', 14.57, 19.50, 'checklist', 'split', dict(title='📢 PROPER <span class="g">ADS</span>', items=['📢 RUN ADS • THE RIGHT WAY', '⚖️ WANT TO LOSE WEIGHT', '📍 IN YOUR AREA'], cues=[.3, 1.9, 3.6]), '"run an ad the proper way and tell people in your area who want to lose weight"'),
 ('B04', 22.40, 25.00, 'centres', 'full', dict(title='MANY WELLNESS<br><span class="g">CENTRES ✓</span>'), '"already implemented this strategy in many wellness centres"'),
 ('B05', 25.00, 29.44, 'walkin', 'split', dict(title='NEW GUEST <span class="g">WALK&#8209;INS</span>'), '"generating consistent new guest walk-ins"'),
 ('B06', 49.18, 53.60, 'chart', 'split', dict(title='2026 • <span class="g">ONLINE</span> WALK&#8209;INS'), '"consistent new walk-ins using online in 2026"'),
]
GFX = [
 ('text', 1.50, 6.15, {'html': 'NEW GUESTS FROM<br><span class="y">UNKNOWN CIRCLES</span> 👥', 'y': 200, 'size': 88}),
 ('text', 30.70, 32.90, {'html': 'YOUR CENTRE<br><span class="y">NEEDS THIS?</span>', 'y': 200, 'size': 110}),
 ('flash', 32.95, 33.10, {}),
 ('cta', 33.02, 35.90, {'label': '👇 CLICK THE LINK', 'badge': '📅 BOOK APPOINTMENT', 'y': 1060}),
 ('text', 36.00, 43.18, {'html': '<span class="g">10+</span> WALK-INS<br>EVERY <span class="y">WEEK?</span>', 'y': 200, 'size': 112}),
 ('flash', 43.75, 43.90, {}),
 ('cta', 43.80, 48.90, {'label': '📅 BOOK APPOINTMENT', 'badge': '👇 READY TO INVEST? LINK BELOW', 'y': 1060}),
 ('text', 53.70, 56.60, {'html': '<span class="g">ONLINE</span> = 2026<br>MUST-HAVE ✅', 'y': 200, 'size': 104}),
 ('text', 56.66, 59.00, {'html': 'NEXT STEP<br><span class="y">FASTER 🚀</span>', 'y': 200, 'size': 120}),
 ('cta', 59.05, 61.30, {'label': '📅 BOOK APPOINTMENT', 'badge': '👇 LINK BELOW', 'y': 1060}),
 ('endps', 61.35, 999, {}),
]
CAP = [
 (0.91, 3.40, [['ஒரு', '*WELLNESS COACH-ஆ'], ['^UNKNOWN CIRCLE-ல', 'இருந்து']]),
 (3.40, 6.15, [['^CONSISTENT-ஆன', '*NEW GUESTS'], ['நம்ம', 'CENTRE-க்கு', 'வர்றது', '^ரொம்ப முக்கியம்']]),
 (7.15, 10.10, [['இதுவரைக்கும்', 'இதை'], ['*WALK & TALK', 'மூலமா', 'பண்ணோம்']]),
 (11.03, 13.60, [['இந்த', '*WALK & TALK-ஐ'], ['^ONLINE-ல', 'பண்ணலாம்']]),
 (14.57, 19.50, [['ஒரு', '^PROPER', '*AD', 'RUN', 'பண்ணி'], ['உங்க', '^AREA-ல'], ['*WEIGHT LOSS', 'வேணும்னு', 'நினைக்கிறவங்களுக்கு']]),
 (22.40, 25.00, [['ALREADY', '^நிறைய', '*WELLNESS CENTRES-ல'], ['இந்த', 'STRATEGY', 'IMPLEMENT', 'பண்ணிருக்கோம்']]),
 (25.00, 29.44, [['^CONSISTENT-ஆ', '*NEW GUEST'], ['*WALK-INS', 'GENERATE', 'ஆகிட்டு', 'இருக்கு']]),
 (30.70, 32.90, [['உங்க', '*WELLNESS CENTRE-க்கு'], ['இது', '^தேவையா?']]),
 (33.02, 35.90, [['இப்பவே', '^கீழே', 'LINK', 'CLICK', 'பண்ணி'], ['*APPOINTMENT', 'BOOK', 'பண்ணுங்க']]),
 (36.00, 43.18, [['நம்ம', 'CENTRE-ல'], ['^ஒவ்வொரு WEEK-உம்'], ['*10+ WALK-INS'], ['எப்படி', 'GENERATE', 'பண்றது'], ['^IN DEPTH', '*DISCUSS', 'பண்ணுவோம்']]),
 (43.80, 48.90, [['^INVEST', 'பண்ண', 'READY-ஆ', 'இருந்தா'], ['^கீழே', 'LINK', 'CLICK', 'பண்ணி'], ['*APPOINTMENT', 'BOOK', 'பண்ணுங்க']]),
 (49.18, 53.60, [['^2026-ல', 'நம்ம', 'CENTRE-க்கு'], ['*ONLINE', 'மூலமா'], ['^CONSISTENT', '*NEW WALK-INS']]),
 (53.70, 56.60, [['^ONLINE', 'ரொம்ப', '*தேவை']]),
 (56.66, 59.00, [['நம்ம', '^NEXT STEP-ஐ'], ['^இன்னும்', '*FAST-ஆ', 'ACHIEVE', 'பண்ணலாம்']]),
]
PUNCH = [(0.0, 1.5, 1.0), (1.5, 6.15, 1.08), (30.7, 32.9, 1.14), (33.02, 35.9, 1.10), (36.0, 39.5, 1.06), (39.5, 43.18, 1.14), (43.8, 48.9, 1.10), (53.7, 56.6, 1.10), (56.66, 59.0, 1.16), (59.05, 61.3, 1.10)]
MUSIC = [(0.0, 11.0, 'pulse'), (11.0, 32.95, 'tech'), (32.95, 43.6, 'warm'), (43.6, 999, 'uplift')]
SFX = [(1.50, 'hit'), (30.70, 'thud'), (32.60, 'riser'), (33.02, 'hit'), (36.00, 'pop'), (43.80, 'hit'), (56.66, 'hit'), (59.05, 'hit')]
SCENE_SFX = {
 'walktalk': [(.3, 'pop'), (.8, 'whoosh'), (1.3, 'pop'), (1.6, 'pop'), (1.9, 'pop')],
 'social': [(.3, 'pop'), (.7, 'ding'), (1.2, 'tick'), (1.6, 'tick'), (2.0, 'tick')],
 'checklist': [(.65, 'ding'), (2.25, 'ding'), (3.95, 'ding')],
 'centres': [(.2 + .22 * i, 'tick') for i in range(9)] + [(2.3, 'ding')],
 'walkin': [(.1, 'pop')] + [(.42 * i + 2.3, 'tick') for i in range(5)],
 'chart': [(.15 + .18 * i, 'tick') for i in range(6)] + [(1.4, 'ding')],
}
