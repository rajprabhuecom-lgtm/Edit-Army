"""275+ clients in 1 year: 3 reasons (17865235014599014.mp4, 97.4 s). SRT 18042552539737461. Burned banners top+bottom, burned captions kept."""
from kit import *
SRC = '17865235014599014.mp4'; END, HOLD = 97.20, 1.5
CY, ALTZ, CROP_Y0 = 960, 1.04, 330          # small zooms around centre so the burned banners stay in frame
R = [['🔁', 'CONSISTENCY'], ['🧭', 'MENTORSHIP'], ['📚', 'LEARNING']]
BROLL = [
 ('B01', 12.2, 17.0, 'reasons', 'split', dict(items=R, cur=1), '"first one, consistency"'),
 ('B02', 17.2, 24.0, 'growth', 'split', dict(title='MARKETING • <span class="g">365 DAYS</span>', chip='🎥 ORGANIC VIDEOS, CONSISTENTLY'), '"marketing 365 days, organic videos"'),
 ('B03', 36.3, 43.6, 'reframe', 'split', dict(title='1 WEEK-ல WORK ஆகலையா?', A=['🛑', 'STOP'], B=['🔧', 'SOLVE IT'], al="DON'T", bl='THE PROBLEM ✓', xc=39.0, bc=40.4), '"solve the problem, never step back"'),
 ('B04', 43.8, 48.8, 'reasons', 'split', dict(items=R, cur=2), '"second reason, mentorship"'),
 ('B05', 50.7, 58.0, 'bullseye', 'split', dict(title='RIGHT <span class="y">MENTORS</span>', chips=['🔍 FIND THE EXPERTS', '💰 INVEST IN THEM'], hit=52.0, ccues=[52.6, 55.2]), '"I found and invested heavily in mentors"'),
 ('B06', 61.1, 66.5, 'reasons', 'split', dict(items=R, cur=3), '"third reason, learnings - lifelong learner"'),
 ('B07', 86.1, 91.6, 'reasons', 'split', dict(items=R, title='275+ = <span class="y">3 QUALITIES</span>'), '"these three qualities onboarded 275 clients"'),
]
GFX = [stat(1.5, 3.6, 275, 'CLIENTS • 1 YEAR', suf='+', y=480, size=170),
 yb(6.5, 9.3, '🔥 3 IMPORTANT REASONS', y=495), badge(9.3, 12.2, '➕ FOLLOW FOR DEEP BUSINESS TRICKS', size=46, y=495),
 slam(26.9, 31.9, '📞 CONSISTENT<br><span class="g">SALES CALLS</span>', 90, 480),
 slam(77.3, 83.1, '🤖 AI = MARKET<br><span class="y">CHANGES DAILY</span>', 90, 480), gb(83.1, 86.1, '📚 LIFELONG LEARNER', y=495),
 slam(94.1, END, '💯 BIG CHANGE', 110, 480), boom(94.1)] + end(END, HOLD, '🏆', '275+ CLIENTS', 'IN ONE YEAR')
PUNCH = [(1.5, 3.6, 1.05), (26.9, 31.9, 1.06), (94.1, 97.2, 1.06)]
MUSIC = [(0, 12.2, 'pulse'), (12.2, 61.1, 'tech'), (61.1, 86.1, 'warm'), (86.1, END + HOLD, 'uplift')]
SFX = [(6.5, 'hit'), (26.9, 'thud'), (77.3, 'riser'), (83.1, 'ding')]
