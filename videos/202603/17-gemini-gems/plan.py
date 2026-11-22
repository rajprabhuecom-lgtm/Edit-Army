"""Gemini Gems: your own AI assistants (17918372355301224.mp4, 77.9 s, 1080p). No SRT: graphics follow the screen."""
from kit import *
SRC = '17918372355301224.mp4'; END, HOLD = 77.80, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '💎 GEMINI GEMS'), slam(6.0, 11.0, 'YOUR OWN<br><span class="y">AI ASSISTANTS</span>', 96),
 db(12.0, 18.0, '🗂️ GEM MANAGER'), gb(18.0, 24.0, '⚡ PLANNER • GYM • STORY', 50), yb(48.0, 54.0, '💡 BRAINSTORMER GEM'),
 boom(54.0), slam(54.0, 60.0, 'MULTIPLE<br><span class="g">IDEAS</span> ⚡', 110), yb(70.0, END, '🚀 CREATE YOUR GEM')] + end(END, HOLD, '💎', 'GEMINI GEMS', 'YOUR AI ASSISTANTS')
PUNCH = [(6.0, 11.0, 1.08), (54.0, 60.0, 1.10)]
MUSIC = [(0, 12.0, 'pulse'), (12.0, 54.0, 'tech'), (54.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (6.0, 'thud'), (12.0, 'swipe'), (48.0, 'ding')]
