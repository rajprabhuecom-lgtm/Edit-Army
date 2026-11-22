"""NotebookLM: turn any topic into slides (17916217008301224.mp4, 97.9 s). No SRT: graphics follow the screen."""
from kit import *
SRC = '17916217008301224.mp4'; END, HOLD = 97.80, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '🧪 LEARN LIKE A SCIENTIST'), slam(10.0, 16.0, 'NEVER STOP<br><span class="y">ASKING WHY?</span>', 100),
 gb(24.0, 30.0, '📚 NOTEBOOKLM'), db(36.0, 42.0, '📄 ADD YOUR PDF / SOURCES'), yb(48.0, 54.0, '✨ STUDIO → SLIDE DECK'),
 boom(72.0), slam(72.0, 78.0, 'PRESENTATION<br><span class="g">READY</span> 🤯', 100), db(84.0, 92.0, '🧠 ANY TOPIC → SLIDES')] + end(END, HOLD, '🧪', 'NOTEBOOKLM', 'LEARN ANYTHING')
PUNCH = [(10.0, 16.0, 1.08), (72.0, 78.0, 1.10)]
MUSIC = [(0, 24.0, 'pulse'), (24.0, 72.0, 'tech'), (72.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (10.0, 'thud'), (24.0, 'swipe'), (48.0, 'ding')]
