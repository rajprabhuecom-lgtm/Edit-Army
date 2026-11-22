"""Oracle layoffs: adapt to AI now (18111518212809510.mp4, 66.5 s). Source already stacked (news top, face below, captions ~24%): graphics on the chest area."""
from kit import *
SRC = '18111518212809510.mp4'; END, HOLD = 66.30, 1.5
NOZOOM = [(0, 99)]
PROGRESS = False
BROLL = []
Y = 1480
GFX = [stat(0.5, 8.0, 30000, 'JOBS CUT GLOBALLY (ORACLE)', y=1400, size=150, col='var(--rd)'),
 badge(8.0, 15.3, '🚨 USE THIS AS AN ALERT', y=Y), yb(15.3, 24.1, '🧠 UPSKILL AI • OR START A BUSINESS', 46, Y),
 slam(24.1, 27.1, 'CRUCIAL<br><span class="r">TIME</span> ⏰', 110, 1420), stat(27.6, 37.7, 40, 'CAGR • AI AUTOMATION', suf='%', y=1400, size=170, col='var(--em)'),
 gb(37.7, 43.7, '🔥 TRENDING INDUSTRY', y=Y), db(43.7, 56.1, '🤖 UPSKILL • SHIFT • ADAPT TO AI', 50, Y),
 boom(56.1, None, None, 1500), slam(56.1, 62.0, 'BE<br><span class="g">PROACTIVE</span> ⚡', 110, 1420), yb(62.0, END, '✅ TAKE A QUICK DECISION', y=Y)] + end(END, HOLD, '🤖', 'ADAPT TO AI', 'BEFORE IT\'S TOO LATE', ts=110, ts2=70)
PUNCH = []
MUSIC = [(0, 24.1, 'dark'), (24.1, 56.1, 'tech'), (56.1, END + HOLD, 'uplift')]
SFX = [(0.5, 'thud'), (8.0, 'thud'), (24.1, 'hit'), (27.6, 'cash'), (56.1, 'hit')]
