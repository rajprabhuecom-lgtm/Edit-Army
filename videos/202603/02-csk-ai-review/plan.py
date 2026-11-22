"""CSK team review with AI / NotebookLM (17869989468594250.mp4, 127.2 s). No SRT: graphics follow what is on screen. Source already has music: no BGM added."""
from kit import *
SRC = '17869989468594250.mp4'; END, HOLD = 127.10, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '🏏 CSK TEAM REVIEW • WITH AI'), db(6.0, 11.5, '📺 ALL REVIEW VIDEOS'),
 slam(18.0, 23.0, 'ALL REVIEWS<br><span class="y">IN ONE PLACE</span>', 100), gb(24.0, 30.0, '📚 NOTEBOOKLM SOURCES'),
 db(42.0, 48.0, '🧠 MIND MAP'), yb(54.0, 60.0, '⚔️ TACTICAL STRATEGIES'), boom(78.0),
 slam(78.0, 84.0, 'INFOGRAPHIC<br><span class="g">READY</span> 📊', 100), db(90.0, 96.0, '🏟️ CSK 2.0 BLUEPRINT'),
 gb(102.0, 108.0, '🔍 SEARCH WEB FOR MORE SOURCES', 48), yb(114.0, 121.0, '🧠 DEEP ANALYSIS IN MINUTES')] + end(END, HOLD, '🏏', 'CSK REVIEW', 'WITH AI')
PUNCH = [(18.0, 23.0, 1.08), (78.0, 84.0, 1.10)]
MUSIC = []
SFX = [(0.3, 'hit'), (18.0, 'thud'), (42.0, 'swipe'), (102.0, 'swipe')]
