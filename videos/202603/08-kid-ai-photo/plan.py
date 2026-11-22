"""Simple photo -> AI glam photo of my kid (17916561171301224.mp4, 15.9 s). No SRT."""
from kit import *
SRC = '17916561171301224.mp4'; END, HOLD = 15.80, 1.2
BROLL = []
GFX = [yb(0.2, 3.0, '📸 SIMPLE PHOTO → AI MAGIC ✨'), boom(3.6, 5.2, ['✨', '🌟', '💖', '📸']),
 slam(5.0, 8.5, '1 SIMPLE<br><span class="y">PROMPT</span>', 110), gb(11.5, END, '💬 COMMENT "PROMPT"')] + end(END, HOLD, '✨', 'AI PHOTO', 'ONE SIMPLE PROMPT')
PUNCH = [(3.6, 5.2, 1.10), (5.0, 8.5, 1.06)]
MUSIC = [(0, END + HOLD, 'uplift')]
SFX = [(0.2, 'hit'), (5.0, 'thud')]
