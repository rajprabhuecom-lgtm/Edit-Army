"""Meta cuts 10%: AI is the new electricity (1912369309410251.mp4, 99.7 s). SRT 17862234969625564. Captions ~72%."""
from kit import *
SRC = '1912369309410251.mp4'; END, HOLD = 99.50, 1.5
CROP_Y0 = 380
BROLL = [
 ('B01', 12.5, 22.5, 'reframe', 'split', dict(title='THE FUNNY COMMENT 😂', A=['📉', 'EVERYONE LOSES JOBS'], B=['🛒', 'WHO BUYS YOUR PRODUCT?'], al='IF', bl='VALID POINT?', xc=99, bc=16.0), '"if everyone loses jobs, who will buy your product?"'),
 ('B02', 33.1, 43.6, 'percent', 'split', dict(n=9, val=90, title='WERE FARMERS 🌾', label='TODAY: MAX 5%', lc=37.0), '"90% were farmers - now maximum 5%"'),
 ('B03', 43.6, 52.5, 'growth', 'split', dict(title='NEW <span class="g">JOBS</span> EVOLVED', chip='🏭 INDUSTRY • 🎥 YOUTUBER ECONOMY'), '"they moved to industrial jobs; a YouTuber economy emerged"'),
 ('B04', 57.7, 70.0, 'reframe', 'split', dict(title='AI IS LIKE', A=['💡', 'ELECTRICITY'], B=['🤖', 'AI'], al='→ INVENTIONS', bl='→ NEW JOBS ✓', xc=99, bc=60.0), '"AI is like electricity - many inventions followed"'),
]
GFX = [stat(0.2, 4.2, 10, 'META WORKFORCE CUT', suf='%', y=200, size=210, col='var(--rd)'), db(4.2, 8.0, '📉 MANY JOBS WILL BE LOST'),
 yb(8.0, 12.5, '😂 THIS COMMENT IS HILARIOUS'), slam(23.2, 27.2, 'WHO WILL<br><span class="y">BUY?</span> 🤔', 120),
 db(27.3, 33.1, '🌍 HOW THE WORLD EVOLVED'), slam(73.3, 77.3, 'AI WILL<br><span class="g">CREATE JOBS</span>', 100),
 gb(77.3, 86.8, '🚀 BE AN EARLY ADOPTER'), badge(86.8, 92.2, '😨 NO FEAR MINDSET'), boom(92.2),
 slam(92.2, 97.0, 'AI = THE NEW<br><span class="y">ELECTRICITY</span> ⚡', 92), yb(97.0, END, '💡 A NEW OPPORTUNITY')] + end(END, HOLD, '⚡', 'AI IS THE NEW', 'ELECTRICITY', ts=110, ts2=96)
PUNCH = [(0.2, 4.2, 1.10), (23.2, 27.2, 1.12), (73.3, 77.3, 1.08), (92.2, 97.0, 1.12)]
MUSIC = [(0, 12.5, 'dark'), (12.5, 57.7, 'pulse'), (57.7, 86.8, 'tech'), (86.8, END + HOLD, 'uplift')]
SFX = [(0.2, 'thud'), (8.0, 'pop'), (23.2, 'hit'), (73.3, 'hit'), (92.2, 'hit')]
