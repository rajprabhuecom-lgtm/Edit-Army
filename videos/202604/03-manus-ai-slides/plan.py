"""Manus AI: realistic futuristic slides (17948215146140475.mp4, 98.9 s). Screen video."""
from kit import *
SRC = '17948215146140475.mp4'; END, HOLD = 98.70, 1.5
BROLL = []
GFX = [yb(0.2, 2.7, '🖥️ FUTURISTIC SLIDES WITH AI'), slam(2.7, 5.9, 'NOT CLAUDE.<br><span class="y">NOT NANO BANANA.</span>', 84),
 db(17.5, 20.5, '1️⃣ GOOGLE → "MANUS"'), db(22.7, 28.0, '2️⃣ LOG IN WITH EMAIL'), stat(28.0, 32.0, 300, 'FREE POINTS DAILY', y=200, size=200, col='var(--em)'),
 gb(40.0, 46.0, '🌐 WEBSITES • SLIDES • DESKTOP APPS', 46), yb(47.0, 55.0, '💡 PROMPT FROM CHATGPT → PASTE'),
 stat(60.0, 65.0, 15, 'MINUTES • SLIDE BY SLIDE', suf=' MIN', y=200, size=190), db(71.0, 77.0, '🖼️ IMAGES FIRST → THEN CONTENT'),
 boom(80.0), slam(80.0, 86.0, 'VERY<br><span class="g">REALISTIC</span> 🤯', 120), slam(90.0, 94.0, 'MIND<br><span class="y">BLOWN</span> 🤯', 130),
 yb(94.0, END, '💬 COMMENT "AI" FOR THE LINK')] + end(END, HOLD, '🖥️', 'AI SLIDES', 'WITH MANUS')
PUNCH = [(2.7, 5.9, 1.10), (80.0, 86.0, 1.10), (90.0, 94.0, 1.14)]
MUSIC = [(0, 17.5, 'pulse'), (17.5, 80.0, 'tech'), (80.0, END + HOLD, 'uplift')]
SFX = [(0.2, 'hit'), (2.7, 'thud'), (28.0, 'cash'), (60.0, 'tick'), (90.0, 'hit')]
