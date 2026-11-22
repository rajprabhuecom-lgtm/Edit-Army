"""10th exams: study with AI in 3 steps (18013977311675391.mp4, 106.0 s). No SRT. Burned STEP labels at ~17%: our graphics sit at ~29%."""
from kit import *
SRC = '18013977311675391.mp4'; END, HOLD = 105.90, 1.5
BROLL = []
GFX = [yb(0.3, 4.0, '📚 10TH EXAMS? STUDY WITH AI', y=560), db(12.0, 22.0, '📋 COPY THE TIMETABLE', y=560),
 gb(30.0, 36.0, '🔗 ADD YOUTUBE / WEBSITE / PDF', 46, 560), yb(54.0, 60.0, '🃏 FLASHCARDS + QUIZ', y=560),
 boom(66.0), slam(66.0, 72.0, 'SELF-TEST<br><span class="g">EVERY TOPIC</span>', 96, 540), yb(96.0, END, '💬 COMMENT "10" FOR THE LINK', 50, 560)] + end(END, HOLD, '📚', 'STUDY WITH AI', '3 SIMPLE STEPS')
PUNCH = [(66.0, 72.0, 1.08)]
MUSIC = [(0, 12.0, 'pulse'), (12.0, 66.0, 'tech'), (66.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (12.0, 'swipe'), (30.0, 'swipe'), (54.0, 'ding')]
