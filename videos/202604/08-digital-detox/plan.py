"""One-day digital detox: shocking results (18546223243070394.mp4, 101.5 s). Banners top+bottom, no captions."""
from kit import *
SRC = '18546223243070394.mp4'; END, HOLD = 101.30, 1.5
CY, ALTZ, CROP_Y0 = 960, 1.04, 330
BROLL = [
 ('B01', 8.0, 17.0, 'reframe', 'split', dict(title='MY OLD HABIT', A=['📱', 'PHONE FOR EVERYTHING'], B=['🔁', 'ENDLESS SCROLLING'], al='"FOR BUSINESS"', bl='30-40 MIN GONE', xc=99, bc=12.0), '"I always used my phone for business"'),
 ('B02', 29.0, 39.0, 'growth', 'split', dict(title='DIGITAL DETOX = <span class="g">FOCUS</span>', chip='⚡ 2-3 DAYS OF WORK IN 1 DAY'), '"I completed 2-3 days of work in one day"'),
 ('B03', 45.0, 57.0, 'reframe', 'split', dict(title='THE KEY POINT', A=['📱', 'MOBILE'], B=['💻', 'LAPTOP'], al='SCROLL TRAP', bl='ONLY WHAT YOU NEED ✓', xc=48.0, bc=50.0), '"open what you need on the laptop instead"'),
 ('B04', 57.0, 66.0, 'percent', 'split', dict(n=8, val=40, suf=' MIN', title='LOST TO SCROLLING', label='😵 WITHOUT EVEN KNOWING', lc=62.0), '"you consume time without knowing the scrolling effect"'),
]
GFX = [slam(1.0, 8.0, '1 DAY<br><span class="r">NO PHONE</span> 📵', 120, 480), stat(20.0, 26.0, 40, 'MINUTES SCROLLING', suf=' MIN', y=480, size=170, col='var(--rd)'),
 gb(34.0, 39.0, '🚀 2-3 DAYS OF WORK IN ONE DAY', 46, 495), db(66.0, 74.0, '🛋️ "RELAXING" = DEEP SCROLLING', 48, 495),
 boom(75.0), slam(75.0, 81.0, 'YOUR REAL<br><span class="g">POTENTIAL</span> 🔥', 100, 480), yb(83.0, 88.0, '📵 1-DAY DIGITAL DETOX CHALLENGE', 46, 495),
 gb(88.0, 97.0, '💬 COMMENT "1 DAY" FOR THE ROAD MAP', 46, 495), slam(97.0, END, 'MAXIMUM<br><span class="y">POTENTIAL</span> 🚀', 100, 480)] + end(END, HOLD, '📵', 'DIGITAL DETOX', '1-DAY CHALLENGE')
PUNCH = [(1.0, 8.0, 1.05), (75.0, 81.0, 1.05), (97.0, 101.3, 1.06)]
MUSIC = [(0, 8.0, 'dark'), (8.0, 29.0, 'pulse'), (29.0, 75.0, 'tech'), (75.0, END + HOLD, 'uplift')]
SFX = [(1.0, 'hit'), (20.0, 'thud'), (66.0, 'thud'), (75.0, 'hit'), (97.0, 'hit')]
