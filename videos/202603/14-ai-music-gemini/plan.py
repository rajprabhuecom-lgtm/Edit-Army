"""Create your own music with Gemini (17917779795301224.mp4, 51.5 s). SRT 18020615819648604. The AI song plays ~12.7-21 s: BGM stays silent there."""
from kit import *
SRC = '17917779795301224.mp4'; END, HOLD = 51.40, 1.5
BROLL = []
GFX = [slam(1.2, 4.7, 'YOU = <span class="y">MUSIC DIRECTOR</span> 🎵', 92), yb(4.7, 9.0, '🎼 1 PROMPT → YOUR OWN MUSIC', 50),
 gb(10.9, 12.7, '🎉 MY FIRST AI SONG'), boom(12.7, 14.3, ['🎵', '🎶', '🥁', '🔥']), db(14.3, 21.0, '🔊 LISTEN 🎧'),
 db(21.0, 25.5, '1️⃣ OPEN GEMINI'), yb(25.5, 30.0, '2️⃣ TOOLS → CREATE MUSIC'), db(30.0, 34.6, '3️⃣ PRO + SIMPLE PROMPT'),
 slam(41.5, 46.3, 'CREATE • ENJOY<br><span class="g">EXPLORE</span> 🎶', 96), yb(46.3, END, '🚀 TRY IT NOW')] + end(END, HOLD, '🎵', 'AI MUSIC', 'WITH GEMINI')
PUNCH = [(1.2, 4.7, 1.10), (41.5, 46.3, 1.08)]
MUSIC = [(0, 12.5, 'pulse'), (21.0, END + HOLD, 'uplift')]
SFX = [(1.2, 'hit'), (12.7, 'pop'), (21.0, 'swipe'), (41.5, 'hit')]
