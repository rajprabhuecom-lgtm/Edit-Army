"""TN elections: check every candidate before you vote (18006017165900135.mp4, 74.9 s). Screen video."""
from kit import *
SRC = '18006017165900135.mp4'; END, HOLD = 74.70, 1.5
BROLL = []
GFX = [yb(0.2, 4.3, '🗳️ CHECK BEFORE YOU VOTE'), slam(4.3, 8.7, 'TN ELECTIONS<br><span class="y">WEBSITE</span> 🏛️', 100),
 db(11.8, 14.8, '⭐ STAR CANDIDATES'), gb(14.8, 20.7, '📅 FULL ELECTION SCHEDULE'), db(22.5, 26.5, '🤝 ALLIANCES • CANDIDATES'),
 yb(29.5, 34.0, '📍 EVERY CONSTITUENCY'), db(38.5, 41.5, '👨 MALE • 👩 FEMALE CANDIDATES', 50), gb(41.5, 46.5, '📋 FULL CANDIDATE LIST'),
 slam(50.5, 55.0, 'EDUCATION<br><span class="y">DETAILS</span> 🎓', 104), slam(55.0, 59.0, 'ASSETS<br><span class="g">DECLARED</span> 💰', 104),
 boom(65.5, None, ['🗳️', '✅', '🇮🇳', '⭐']), slam(65.5, 67.5, 'VOTE<br><span class="g">CLEARLY</span> ✅', 130), yb(67.5, END, '💬 COMMENT FOR THE LINK → DM')] + end(END, HOLD, '🗳️', 'KNOW YOUR CANDIDATE', 'THEN VOTE', ts=96, ts2=90)
PUNCH = [(4.3, 8.7, 1.08), (50.5, 59.0, 1.06), (65.5, 67.5, 1.14)]
MUSIC = []          # source already has a music bed
SFX = [(0.2, 'hit'), (4.3, 'thud'), (29.5, 'swipe'), (50.5, 'pop'), (55.0, 'cash'), (65.5, 'hit')]
