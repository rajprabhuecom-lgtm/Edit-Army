"""From a ₹200 cleaning job to IPL hero: never give up (967173915697291.mp4, 68.3 s). SRT 18065994860688649. Captions ~72%.
Only numbers that are spoken are shown."""
from kit import *
SRC = '967173915697291.mp4'; END, HOLD = 68.10, 1.5
CROP_Y0 = 380
BROLL = [
 ('B01', 6.5, 12.1, 'reframe', 'split', dict(title='WHERE HE STARTED', A=['🧹', 'CLEANER • ₹200'], B=['🏏', 'IPL HERO'], al='SALARY', bl='TODAY ✓', xc=99, bc=9.0), '"father delivered gas cylinders, he was a cleaner for ₹200"'),
 ('B02', 16.1, 31.0, 'growth', 'split', dict(title='THE <span class="r">STRUGGLE</span> YEARS', vals=[.15, .12, .2, .18, .25, .22], chip='2018–2022: ONLY 17 MATCHES'), '"picked in 2017, didn\'t play a year; 17 matches 2018-2022"'),
 ('B03', 50.2, 56.1, 'bullseye', 'split', dict(title='YOUR <span class="y">CENTRAL GOAL</span>', chips=['💪 NEVER GIVE UP', '🏏 LIKE RINKU'], hit=51.5, ccues=[52.0, 54.0]), '"never give up striving towards your central goal"'),
]
GFX = [slam(0.1, 3.5, '₹200 SALARY →<br><span class="y">IPL HERO</span> 🏏', 92), yb(3.5, 6.5, '⭐ RINKU SINGH'),
 db(12.5, 16.1, '😤 IMMENSE STRUGGLE'), badge(31.0, 35.4, '💪 HE NEVER GAVE UP'),
 slam(35.4, 40.4, '5 BALLS •<br><span class="y">5 SIXES NEEDED</span>', 96), boom(40.7, None, ['🏏', '6️⃣', '🔥', '💥']),
 stat(40.7, 44.4, 5, 'IN THE LAST 5 BALLS', suf=' SIXES', y=200, size=200, col='var(--em)'), slam(44.4, 47.5, 'HERO TO THE<br><span class="g">WHOLE WORLD</span> 🌍', 90),
 gb(56.1, 62.9, '🙏 "GOD\'S PLAN"'), yb(62.9, 67.3, '🔁 PERSISTENCE • CONSISTENCY'), slam(67.3, END, 'GOD\'S PLAN IS<br><span class="g">WAITING</span> 🙏', 90)] + end(END, HOLD, '🏏', 'NEVER GIVE UP', 'GOD\'S PLAN')
PUNCH = [(0.1, 3.5, 1.10), (35.4, 40.4, 1.08), (40.7, 44.4, 1.12), (67.3, 68.1, 1.10)]
DESAT = [(12.5, 16.1)]
MUSIC = [(0, 6.5, 'pulse'), (6.5, 35.4, 'dark'), (35.4, 47.5, 'tech'), (47.5, END + HOLD, 'uplift')]
SFX = [(0.1, 'hit'), (31.0, 'thud'), (35.4, 'riser'), (40.7, 'hit'), (44.4, 'hit')]
