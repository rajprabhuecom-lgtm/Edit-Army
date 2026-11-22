"""21-min video on beating addiction (Japanese methods) -> one mind map + image with NotebookLM (17917437813301224.mp4, 85.4 s). SRT 18460214362103624."""
from kit import *
SRC = '17917437813301224.mp4'; END, HOLD = 85.30, 1.5
BROLL = []
GFX = [yb(0.3, 4.6, '📺 MY FAVOURITE CHANNEL'), slam(4.6, 9.2, 'BEAT ANY<br><span class="g">ADDICTION</span> 🇯🇵', 100),
 stat(9.2, 13.0, 21, 'MINUTE VIDEO', y=200, size=200), gb(13.0, 17.7, '🧠 → ONE MIND MAP'),
 db(17.7, 24.5, '❓ PROBLEMS • 🇯🇵 PRINCIPLES', 50), slam(32.0, 36.7, '→ ONE<br><span class="y">IMAGE</span> 🖼️', 110),
 yb(36.7, 42.1, '⏱️ 20-30 MIN DAILY • 1% BETTER', 48), gb(43.8, 49.7, '🍱 80% RULE (HARA HACHI BU)', 48),
 db(52.0, 61.3, '🔁 MISSED A DAY? DO YOUR BEST', 50), boom(61.3), yb(71.5, 79.7, '💬 COMMENT "NOTEBOOK" → FREE PDF', 46),
 slam(79.7, END, 'ALL THE<br><span class="g">BEST</span> 🙌', 110)] + end(END, HOLD, '🧠', 'NOTEBOOKLM', 'ANY VIDEO → MIND MAP')
PUNCH = [(4.6, 9.2, 1.08), (32.0, 36.7, 1.10), (79.7, 85.3, 1.08)]
MUSIC = [(0, 13.0, 'pulse'), (13.0, 61.3, 'warm'), (61.3, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (4.6, 'thud'), (32.0, 'hit'), (71.5, 'ding')]
