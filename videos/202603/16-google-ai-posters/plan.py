"""Pro posters with Google AI + Google AI plans (17918222835301224.mp4, 76.9 s, 1080p). No SRT: graphics follow the screen. Prices on screen are left as they are (no numbers added)."""
from kit import *
SRC = '17918222835301224.mp4'; END, HOLD = 76.80, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '🖼️ MADE WITH GOOGLE AI'), slam(6.0, 11.0, 'PRO-LEVEL<br><span class="y">POSTERS</span>', 110),
 db(18.0, 24.0, '💳 GOOGLE AI PLANS'), gb(30.0, 36.0, '🎁 CHECK THE OFFER'), boom(60.0),
 slam(60.0, 66.0, 'POSTERS LIKE<br><span class="g">THIS</span> 🔥', 104), yb(70.0, END, '🚀 TRY IT NOW')] + end(END, HOLD, '🖼️', 'AI POSTERS', 'WITH GOOGLE AI')
PUNCH = [(6.0, 11.0, 1.08), (60.0, 66.0, 1.10)]
MUSIC = [(0, 18.0, 'pulse'), (18.0, 60.0, 'tech'), (60.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (6.0, 'thud'), (18.0, 'swipe'), (30.0, 'ding')]
