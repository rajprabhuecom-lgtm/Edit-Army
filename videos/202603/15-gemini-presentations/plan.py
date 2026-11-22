"""AI presentations with Gemini (17917785297301224.mp4, 54.2 s). No SRT. Source is already stacked (screen top, face bottom; captions ~39%): graphics sit between."""
from kit import *
SRC = '17917785297301224.mp4'; END, HOLD = 54.10, 1.5
NOZOOM = [(0, 99)]
BROLL = []
GFX = [yb(0.3, 3.5, '🎤 AI PRESENTATIONS IN MINUTES', y=880), gb(18.0, 24.0, '🤖 GEMINI: "WHERE SHOULD WE START?"', 44, 880),
 db(24.0, 30.0, '💡 GIVE YOUR TOPIC', y=880), boom(36.0, None, None, 1200), slam(36.0, 42.0, 'PRESENTATION<br><span class="g">READY</span> ✅', 90, 860),
 yb(48.0, END, '🚀 TRY IT TODAY', y=880)] + end(END, HOLD, '🎤', 'AI PRESENTATIONS', 'WITH GEMINI', ts=100, ts2=76)
PUNCH = []
MUSIC = [(0, 36.0, 'tech'), (36.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (18.0, 'swipe'), (24.0, 'pop')]
