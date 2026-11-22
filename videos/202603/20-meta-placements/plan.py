"""My winning Meta ads placements (18119410852530507.mp4, 80.4 s). SRT 18061468073672263. Burned banner top: graphics at ~25%."""
from kit import *
SRC = '18119410852530507.mp4'; END, HOLD = 80.30, 1.5
CY, ALTZ = 960, 1.04
BROLL = []
GFX = [stat(0.3, 4.7, 81, 'SPENT • LAST 40 DAYS', pre='₹', suf='K', y=480, size=170), db(13.2, 19.3, '📍 MY EXACT PLACEMENTS', y=495),
 gb(25.6, 29.4, '✅ FEEDS: FACEBOOK + INSTAGRAM', 48, 495), badge(29.4, 32.0, '❌ EXPLORE OFF', y=495), gb(32.0, 36.2, '✅ ALL STORIES', y=495),
 db(36.2, 38.4, '🎬 INSTANT VIDEOS: FB ONLY', 48, 495), badge(38.4, 42.4, '❌ SEARCH RESULTS OFF', y=495), badge(45.0, 52.3, '❌ EVERYTHING ELSE OFF', y=495),
 slam(56.0, 61.2, '📱 ONLY<br><span class="y">MOBILE</span>', 104, 480), slam(61.2, 65.7, '📶 ONLY ON<br><span class="g">WI-FI</span>', 104, 480),
 gb(65.7, 70.9, '🎯 HIGH-QUALITY LEADS', y=495), badge(70.9, 75.9, '🖥️ NO DESKTOP', y=495),
 slam(75.9, END, 'SMALL FIXES =<br><span class="g">HIGH-PERFORMING AD</span>', 80, 480)] + end(END, HOLD, '🏆', 'WINNING PLACEMENTS', 'META ADS', ts=96, ts2=90)
PUNCH = [(0.3, 4.7, 1.05), (56.0, 65.7, 1.05)]
MUSIC = [(0, 13.2, 'pulse'), (13.2, 56.0, 'tech'), (56.0, END + HOLD, 'uplift')]
SFX = [(13.2, 'swipe'), (29.4, 'thud'), (38.4, 'thud'), (56.0, 'hit'), (61.2, 'hit')]
