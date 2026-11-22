"""My little princess selling (18093267326024782.mp4, 33.0 s). Fun family clip with burned meme text: keep it light."""
from kit import *
SRC = '18093267326024782.mp4'; END, HOLD = 32.90, 1.2
JUMPCUT = False
BROLL = []
GFX = [yb(0.3, 3.0, '😂 WAIT FOR IT...'), boom(8.0, None, ['😂', '🤣', '🔥', '💖']), boom(18.0, None, ['😂', '🤣', '👑', '💸']),
 boom(28.0, None, ['🔥', '😂', '👑', '⭐'])] + end(END, HOLD, '👑', 'LITTLE PRINCESS', 'SALES QUEEN 😂', btn='➕ FOLLOW', ts=100, ts2=80)
PUNCH = [(8.0, 9.6, 1.10), (18.0, 19.6, 1.10), (28.0, 29.6, 1.12)]
MUSIC = [(0, END + HOLD, 'uplift')]
SFX = [(0.3, 'pop'), (8.0, 'hit'), (18.0, 'hit'), (28.0, 'hit')]
