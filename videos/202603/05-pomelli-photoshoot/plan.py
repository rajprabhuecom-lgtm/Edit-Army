"""Google Labs Pomelli: product photoshoot from one image (17915922441301224.mp4, 126.0 s). SRT 18054635177479983."""
from kit import *
SRC = '17915922441301224.mp4'; END, HOLD = 125.90, 1.5
BROLL = []
GFX = [slam(1.2, 3.0, 'NO PROMPT.<br><span class="y">JUST 1 IMAGE</span>', 100), stat(3.0, 9.1, 4, 'PHOTOSHOOT IMAGES', y=200),
 yb(11.8, 17.5, '🆕 GOOGLE LABS • POMELLI'), badge(17.5, 19.5, '➕ FOLLOW FOR EASY AI'),
 db(23.8, 31.7, '1️⃣ CLICK "GET STARTED"'), gb(31.7, 34.0, '🧬 BUSINESS DNA • CAMPAIGNS • PHOTOSHOOT', 42),
 db(34.0, 45.9, '🎨 COLOURS • FONTS • TAGLINE • BRAND', 46), yb(57.1, 65.2, '📸 PHOTOSHOOT → UPLOAD PRODUCT', 50),
 db(80.5, 95.0, '🧾 PICK THE IMAGE TYPES YOU WANT', 48), boom(102.4),
 slam(102.4, 108.2, 'SUPER<br><span class="g">QUALITY</span> 🤯', 110), slam(111.5, 117.1, 'NO PHOTOSHOOT.<br><span class="y">NO PROMPT.</span>', 96),
 yb(119.4, END, '💬 COMMENT "GOOGLE" FOR THE LINK', 48)] + end(END, HOLD, '📸', 'AI PHOTOSHOOT', 'FROM ONE IMAGE')
PUNCH = [(1.2, 3.0, 1.10), (102.4, 108.2, 1.10), (111.5, 117.1, 1.08)]
MUSIC = [(0, 11.8, 'pulse'), (11.8, 102.4, 'tech'), (102.4, END + HOLD, 'uplift')]
SFX = [(1.2, 'hit'), (23.8, 'swipe'), (57.1, 'swipe'), (111.5, 'thud')]
