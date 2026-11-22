"""200 days of Instagram content: 3 learnings (18023747183815312.mp4, 149.4 s). Talking head, captions ~58% (single words)."""
from kit import *
SRC = '18023747183815312.mp4'; END, HOLD = 149.20, 1.5
CROP_Y0 = 330
R = [['🎯', 'RIGHT INTENTION'], ['🤝', 'COMMITMENT'], ['📝', 'DOCUMENT, NO PRESSURE']]
BROLL = [
 ('B01', 4.0, 8.7, 'reasons', 'split', dict(items=R, title='<span class="y">3</span> LEARNINGS'), '"3 important learnings"'),
 ('B02', 18.7, 25.6, 'reasons', 'split', dict(items=R, cur=1), '"first learning - not for views and likes"'),
 ('B03', 29.2, 36.5, 'reframe', 'split', dict(title='WHY I POSTED', A=['👀', 'VIEWS & LIKES'], B=['🏛️', 'VISIBILITY • AUTHORITY'], al='❌ NOT FOR', bl='+ A DAILY HABIT ✓', xc=31.0, bc=32.8), '"to build a habit, visibility and authority"'),
 ('B04', 52.3, 59.4, 'reasons', 'split', dict(items=R, cur=2), '"second learning - commitment, no matter what"'),
 ('B05', 84.8, 93.3, 'growth', 'split', dict(title='CONSISTENCY = <span class="g">CLIENTS</span>', chip='🌍 INTERNATIONAL CLIENTS'), '"consistency brought international clients automatically"'),
 ('B06', 93.3, 102.0, 'reasons', 'split', dict(items=R, cur=3), '"third - see it as simple documentation, not pressure"'),
 ('B07', 117.0, 124.2, 'percent', 'split', dict(n=0, val=200, title='DAY CHALLENGE', label='🙏 THANK YOU FOR THE SUPPORT', lc=121.0), '"start your 200-day challenge"'),
]
GFX = [stat(1.6, 4.0, 200, 'DAYS OF INSTAGRAM CONTENT', y=200, size=200), badge(8.7, 10.0, '💾 SAVE THIS'),
 yb(10.0, 16.6, '🎁 200-DAY CONTENT PROMPT AT THE END', 46), db(38.7, 43.8, '📉 NO VIEWS • NO FOLLOWERS AT FIRST', 46),
 gb(43.8, 48.7, '🔥 STRONG INSPIRATION POINT'), slam(48.7, 52.3, 'START WITH THE<br><span class="y">RIGHT INTENTION</span>', 84),
 slam(63.3, 68.1, 'NEVER MISSED<br><span class="g">A SINGLE DAY</span>', 90), slam(71.4, 74.6, 'POSTED EVEN FROM<br><span class="r">HOSPITAL</span> 🏥', 84),
 yb(81.4, 84.8, '💪 POST NO MATTER WHAT'), slam(104.0, 108.3, '20-30 DAYS<br><span class="r">→ YOU STOP</span>', 92),
 gb(108.3, 114.7, '📚 DOCUMENT YOUR LIFELONG LEARNING', 46), yb(124.2, 130.5, '💬 COMMENT "200" FOR THE PROMPT', 50),
 slam(142.9, 146.9, 'NOT FOR VIEWS.<br><span class="g">FOR YOUR CHANGE.</span>', 84), boom(146.9), yb(146.9, END, '🚀 ACCEPT THE CHALLENGE')] + end(END, HOLD, '📅', '200-DAY CHALLENGE', 'START TODAY')
PUNCH = [(48.7, 52.3, 1.08), (63.3, 68.1, 1.10), (71.4, 74.6, 1.12), (104.0, 108.3, 1.08), (142.9, 146.9, 1.10)]
MUSIC = [(0, 18.7, 'pulse'), (18.7, 84.8, 'warm'), (84.8, 124.2, 'tech'), (124.2, END + HOLD, 'uplift')]
SFX = [(8.7, 'pop'), (48.7, 'hit'), (63.3, 'hit'), (71.4, 'thud'), (104.0, 'thud'), (142.9, 'hit')]
