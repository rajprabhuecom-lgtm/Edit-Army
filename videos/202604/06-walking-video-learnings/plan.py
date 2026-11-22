"""14-min walking video -> 2-min learnings with one ChatGPT prompt (18058457672469397.mp4, 142.2 s). Screen video."""
from kit import *
SRC = '18058457672469397.mp4'; END, HOLD = 142.00, 1.5
BROLL = []
GFX = [yb(0.2, 3.9, '📺 NEW VIDEO • ALMOST EVERYTHING'), stat(3.9, 6.4, 14, 'MINUTE VIDEO', y=200, size=200), slam(6.4, 9.7, 'WHY WALKING<br><span class="g">MATTERS</span> 🚶', 100),
 stat(11.9, 14.1, 2, 'MINUTES TO LEARN IT ALL', suf=' MIN', y=200, size=190, col='var(--em)'), db(19.7, 25.6, '🔗 PASTE THE VIDEO LINK IN THE PROMPT', 46),
 boom(29.9), slam(32.9, 37.2, 'BODY + MIND<br><span class="g">CHANGE</span> 🔄', 104), yb(37.2, 40.8, '⚖️ WEIGHT • 😌 STRESS • ⚡ ENERGY • 😴 SLEEP', 42),
 gb(43.6, 47.3, '🌿 HEAL NATURALLY'), db(52.1, 56.1, '✅ IMPLEMENTATION, NOT JUST LEARNING', 44),
 stat(63.7, 68.7, 15, 'MIN DAILY = STRONGER HEART', suf=' MIN', y=200, size=180), stat(70.8, 78.0, 10, 'MIN AFTER LUNCH = BETTER SLEEP', suf=' MIN', y=200, size=180, col='var(--em)'),
 yb(88.4, 92.4, '🔁 BE CONSISTENT'), db(93.3, 102.1, '⏰ ACTION TRIGGERS: MORNING • STRESS • LUNCH', 42),
 stat(102.1, 106.4, 20, 'MIN DAILY • SAME TIME', suf=' MIN', y=200, size=180), gb(110.4, 119.6, '🖼️ BEFORE / AFTER IMAGE PROMPT', 48),
 slam(123.7, 129.2, 'ANY VIDEO →<br><span class="y">YOUR LEARNING</span>', 96), yb(129.2, 136.2, '💬 COMMENT "PROMPT" → DM'), slam(140.1, END, 'ALL THE<br><span class="g">BEST</span> 🙌', 110)] + end(END, HOLD, '🚶', 'WALK DAILY', 'LEARN FASTER WITH AI')
PUNCH = [(6.4, 9.7, 1.08), (32.9, 37.2, 1.08), (123.7, 129.2, 1.08)]
MUSIC = [(0, 19.7, 'pulse'), (19.7, 63.7, 'tech'), (63.7, 110.4, 'warm'), (110.4, END + HOLD, 'uplift')]
SFX = [(0.2, 'hit'), (6.4, 'thud'), (29.9, 'hit'), (88.4, 'ding'), (123.7, 'hit')]
