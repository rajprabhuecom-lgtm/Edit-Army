"""One prompt -> my own diet app (3 kg in a month plan) (17917118595301224.mp4, 74.2 s). SRT 18137255998510664."""
from kit import *
SRC = '17917118595301224.mp4'; END, HOLD = 74.10, 1.5
BROLL = []
GFX = [stat(0.3, 3.2, 3, 'WEIGHT-LOSS PLAN • 1 MONTH', suf=' KG', y=200, size=200), yb(3.2, 7.5, '🤖 1 PROMPT → MY OWN APP'),
 db(14.0, 19.1, '🪑 SITTING JOB • NEED WEIGHT LOSS', 50), slam(19.1, 22.1, 'AGE • HEIGHT<br>WEIGHT • <span class="y">BMI</span>', 96),
 db(25.6, 27.5, '💧 WATER • 🚶 WALKING'), yb(27.5, 38.4, '🍽️ BREAKFAST • LUNCH • DINNER', 50), badge(38.4, 43.2, '🚫 FOODS TO AVOID'),
 gb(43.2, 47.7, '⏰ BEST INTERMITTENT FASTING TIME', 46), boom(47.7), slam(47.7, 52.5, 'MY OWN<br><span class="g">ACTION PLAN</span> ✅', 100),
 yb(57.9, 63.2, '💬 COMMENT "DIET"'), slam(65.4, END, 'LIKE A<br><span class="y">20-YR NUTRITIONIST</span>', 84)] + end(END, HOLD, '🥗', 'AI DIET PLAN', 'ONE PROMPT')
PUNCH = [(19.1, 22.1, 1.08), (47.7, 52.5, 1.10), (65.4, 74.1, 1.06)]
MUSIC = [(0, 14.0, 'pulse'), (14.0, 47.7, 'tech'), (47.7, END + HOLD, 'uplift')]
SFX = [(3.2, 'pop'), (19.1, 'thud'), (38.4, 'thud'), (57.9, 'ding')]
