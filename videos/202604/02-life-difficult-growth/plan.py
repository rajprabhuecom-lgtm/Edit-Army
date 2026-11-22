"""Why is my life so difficult? Discomfort = growth (17922651333301224.mp4, 82.7 s). SRT 18214066465323028. Captions ~70%."""
from kit import *
SRC = '17922651333301224.mp4'; END, HOLD = 82.50, 1.5
CROP_Y0 = 360
BROLL = [
 ('B01', 2.2, 9.2, 'reasons', 'split', dict(title='EVERYONE ELSE <span class="y">SEEMS</span>', items=[['😊', 'HAPPY'], ['🧘', 'CALM'], ['💰', 'RICH']], cues=[2.4, 4.0, 5.4]), '"everyone here is happy, calm, earns a lot"'),
 ('B02', 18.2, 29.5, 'reframe', 'split', dict(title='YOUR STRUGGLE IS', A=['😣', 'DISCOMFORT'], B=['🌱', 'GROWTH'], al='= BAD?', bl='= WHAT IT REALLY IS ✓', xc=21.0, bc=23.5), '"people in uncomfortable situations are the ones growing"'),
 ('B03', 36.5, 46.5, 'bullseye', 'split', dict(title='YOUR <span class="y">BIG GOAL</span>', chips=['🎯 CENTRE OF YOUR MIND', '👁️ FULL ATTENTION'], hit=38.0, ccues=[40.0, 44.5]), '"put your big goal at the centre of your mind"'),
 ('B04', 50.5, 57.5, 'growth', 'split', dict(title='DAILY • <span class="g">CONTINUOUS</span>', chip='🔁 EVERY SINGLE DAY'), '"whatever you do, daily and continuous"'),
]
GFX = [slam(0.2, 2.2, 'WHY IS MY LIFE<br><span class="r">SO DIFFICULT?</span>', 86), badge(9.2, 14.2, '😔 WHY NOT ME?'), yb(14.2, 18.2, '👉 THIS VIDEO IS FOR YOU'),
 gb(29.5, 36.5, '✅ YOU DON\'T NEED TO WORRY'), db(57.5, 63.5, '💪 NO MATTER HOW HARD IT GETS'),
 slam(67.5, 71.5, 'YOU WILL BECOME<br><span class="g">THAT PERSON</span>', 90), yb(71.5, 74.5, '🙏 TRUST YOUR GOAL'),
 slam(74.5, 78.5, 'DON\'T STEP BACK<br><span class="y">MOVE AHEAD</span> ➜', 90), boom(78.5), slam(78.5, END, 'YOUR GOAL<br><span class="g">IS NEAR</span> 🏁', 104)] + end(END, HOLD, '🌱', 'DISCOMFORT', '= GROWTH')
PUNCH = [(0.2, 2.2, 1.12), (67.5, 71.5, 1.08), (74.5, 78.5, 1.10), (78.5, 82.5, 1.14)]
DESAT = [(9.2, 14.2)]
MUSIC = [(0, 18.2, 'dark'), (18.2, 67.5, 'warm'), (67.5, END + HOLD, 'uplift')]
SFX = [(0.2, 'hit'), (9.2, 'thud'), (67.5, 'hit'), (74.5, 'thud')]
