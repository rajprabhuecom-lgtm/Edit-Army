"""Happy Money (Ken Honda) - gratitude to money (17893466715425658.mp4, 106.6 s). No SRT. Captions burned low (~83%): no split B-roll (it would cut them); graphics on top."""
from kit import *
SRC = '17893466715425658.mp4'; END, HOLD = 106.50, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '📖 HAPPY MONEY • KEN HONDA', y=120), slam(24.0, 28.0, 'HAPPY<br><span class="g">MONEY?</span> 💸', 110, 110),
 gb(30.0, 36.0, '🙏 GRATITUDE APPROACH', y=120), slam(48.0, 53.0, '"ARIGATO" 🙏', 120, 110),
 db(66.0, 71.0, '🏦 EVERY RUPEE = THANK YOU', y=120), slam(72.0, 76.0, 'ARIGATO 🙏', 120, 110),
 yb(78.0, 84.0, '😊 FEEL THE GRATITUDE', y=120), gb(96.0, 103.0, '💛 MONEY + GRATITUDE = HAPPY MONEY', 46, 120)] + end(END, HOLD, '💸', 'HAPPY MONEY', 'GRATITUDE FIRST')
PUNCH = [(24.0, 28.0, 1.10), (48.0, 53.0, 1.12), (72.0, 76.0, 1.12)]
MUSIC = [(0, 24.0, 'warm'), (24.0, 90.0, 'warm'), (90.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (48.0, 'ding'), (72.0, 'ding')]
