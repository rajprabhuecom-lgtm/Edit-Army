"""Claude prospecting: HR contacts for jobs (17916383046301224.mp4, 96.1 s). No SRT: graphics follow the screen."""
from kit import *
SRC = '17916383046301224.mp4'; END, HOLD = 96.00, 1.5
BROLL = []
GFX = [yb(0.3, 3.5, '💼 FIND JOBS WITH AI'), slam(12.0, 18.0, 'HR CONTACTS<br><span class="g">IN ONE SHEET</span> 📋', 96),
 gb(30.0, 36.0, '🤖 CLAUDE → CONNECTORS'), db(42.0, 48.0, '🔍 VIBE PROSPECTING'), boom(78.0),
 slam(78.0, 84.0, 'CONSOLIDATED<br><span class="y">REPORT</span> ✅', 100), yb(88.0, END, '💬 COMMENT "JOBS" FOR THE PROMPT', 48)] + end(END, HOLD, '💼', 'AI JOB HUNT', 'HR CONTACTS IN MINUTES', ts=110, ts2=70)
PUNCH = [(0.3, 3.5, 1.10), (12.0, 18.0, 1.08), (78.0, 84.0, 1.10)]
MUSIC = [(0, 12.0, 'pulse'), (12.0, 78.0, 'tech'), (78.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (12.0, 'thud'), (30.0, 'swipe'), (88.0, 'ding')]
