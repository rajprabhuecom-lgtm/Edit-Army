"""Coach Pradheesh: "Blueprint for Success" invite, v3 (v3: "6 HOURS" (3-day challenge) not 6 months; wide head-and-shoulders
card back in 4 places at natural scale). v2 (vertical, Tamil + English). Source C0073.MP4 (4K, camera on its side).
v2 changes (client feedback 27 Nov): no face-crop cards / PIP / face zooms; presenter stays in his natural full frame
(only a slow 3-4% whole-frame drift); graphics live in the empty zones (TOP band above his head y 40-420,
BOTTOM band over his lap y 1250-1880, captions over the chest); 9 full-screen animated scenes with swipe
transitions; ending = animated CTA only (presenter cut once he stops talking); speed 1.3x, tighter cuts.
All times are SOURCE seconds. Markup: *mint* _yellow_ ~red~. Run: python3 plan.py"""
import sys
sys.path.insert(0, '/home/user/Edit-Army/engine/v6-vertical-aurora')
from planlib import Plan, build

KEEP = [(51.12, 59.77), (74.69, 77.78), (85.66, 88.44), (89.24, 92.95), (105.60, 109.00), (119.07, 121.72),
        (141.77, 147.57), (161.66, 168.89), (178.11, 183.23), (191.91, 195.94), (212.13, 216.85), (223.25, 225.18),
        (231.32, 233.56), (267.75, 273.34), (291.45, 295.53), (300.37, 302.29), (325.87, 331.26), (337.60, 348.60)]
P = Plan(KEEP, pre=0.04, post=0.06)

# ---- layouts: 'nat' = presenter, natural frame (z drift), 'gfx' = full-screen animation ----
D_IN, D_OUT = {'z': (1.0, 1.035)}, {'z': (1.035, 1.0)}
GFX = [(52.60, 54.84, 'sc_years'), (74.69, 77.80, 'sc_hours'), (87.12, 88.50, 'sc_blue'), (119.07, 121.75, 'sc_triad'),
       (164.54, 168.90, 'sc_fam'), (213.93, 216.90, 'sc_rings'), (267.75, 270.12, 'sc_chase'), (292.57, 295.60, 'sc_magnet'),
       (345.00, 348.65, 'sc_cta')]
KEEPB = [(a, b) for a, b in KEEP]
LAY = []
for i, (a, b) in enumerate(KEEPB):
    LAY.append((a - 0.1, b + 0.1, 'nat', D_IN if i % 2 == 0 else D_OUT))
CARDW = {'z': 1.0, 'fdy': 150}
for a, b in [(105.5, 109.1), (141.7, 147.7), (191.8, 213.93), (325.8, 331.4)]:
    LAY.append((a, b, 'cardhi', CARDW))
for a, b, _ in GFX:
    LAY.append((a, b, 'gfx', {}))
ZOOM = []
FX = [(51.0, 52.5, {'spot': 0.85}), (231.32, 233.56, {'spot': 0.8})]
for a, b, _ in GFX:  # whip blur on the A-roll at each cut into / out of a scene
    FX.append((a, a + 0.01, {'wh': 1.0}))
    if b < 345: FX.append((b, b + 0.01, {'wh': -1.0}))
SHATTER = [267.75]

def wipes():
    out = []
    for i, (a, b, _) in enumerate(GFX):
        out.append({'k': 'wipe', 'a': a - 0.16, 'b': a + 0.20, 'dir': 1 if i % 2 == 0 else -1, 'z': 60})
        if b < 345: out.append({'k': 'wipe', 'a': b - 0.16, 'b': b + 0.20, 'dir': -1 if i % 2 == 0 else 1, 'z': 60})
    return [w for w in out if abs(w['a'] - 267.59) > 0.05]  # the pivot uses the shatter instead

G = 'glass'; T = 'pill'; CAP = 1080; BOT = 1270; CW = 1720  # CW = caption inside the wide card
ITEMS = [
 # ===== HOOK (face first 1.5 s) =====
 {'k': 'kin', 'a': 51.15, 'b': 52.58, 'v': 'ME + MY FAMILY', 'y': 140, 'fs': 130, 'mode': 'pop'},
 {'k': T, 'a': 51.15, 'b': 52.58, 'v': 'நானும் என் *குடும்பமும்*', 'y': CAP},
 {'k': 'sc_years', 'a': 52.60, 'b': 54.84, 'v': '18', 'l': 'YEARS', 'x': '*ZERO* HOSPITAL VISITS'},
 {'k': 'kin', 'a': 54.86, 'b': 59.80, 'v': 'ஒரு HOSPITAL VISIT|கூட இல்லாம', 'y': 90, 'fs': 96, 'c': '#fff'},
 {'k': G, 'a': 54.9, 'b': 59.85, 'y': BOT, 'eb': 'IN 18 YEARS',
  'rows': [{'ic': '🏥', 'lb': 'Hospital visit', 'kind': 'x', 'on': 55.1, 'strike': 55.2, 'at': 54.95},
           {'ic': '🥗', 'lb': '*Healthy* lifestyle', 'on': 56.7, 'at': 56.6},
           {'ic': '👨‍👩‍👧', 'lb': 'Whole *family*', 'on': 58.4, 'at': 57.4}]},
 {'k': T, 'a': 54.86, 'b': 56.56, 'v': '*HOSPITAL VISIT* இல்லாம', 'y': CAP},
 {'k': T, 'a': 56.58, 'b': 59.77, 'v': '*HEALTHY* LIFESTYLE', 'y': CAP},
 # ===== 6 HOURS (3-day challenge, full scene) =====
 {'k': 'sc_hours', 'a': 74.69, 'b': 77.80, 'e': 'EASY-ஆ ✓'},
 # ===== BLUEPRINT =====
 {'k': 'tpill', 'a': 85.7, 'b': 87.1, 'v': '🤔 WHAT IS IT?', 'y': 330},
 {'k': 'kin', 'a': 85.68, 'b': 87.1, 'v': 'என்னன்னு தானே|கேக்குறீங்க?', 'y': 90, 'fs': 92},
 {'k': 'lower', 'a': 85.7, 'b': 87.1, 'name': 'Coach *Pradheesh*', 'l2': 'TM Nutrition Centre', 'l3': '📍 Trichy', 'init': 'TM', 'y': 1560},
 {'k': 'sc_blue', 'a': 87.12, 'b': 88.50},
 {'k': 'kin', 'a': 89.24, 'b': 92.98, 'v': 'MY MENTOR', 'y': 70, 'fs': 120, 'c': '#2EE59D'},
 {'k': 'kin', 'a': 89.6, 'b': 92.98, 'v': 'MR. RAVI SUNDARAM', 'y': 220, 'fs': 104, 'c': '#FFD60A', 'mode': 'pop'},
 {'k': G, 'a': 90.9, 'b': 92.98, 'y': BOT + 60, 'eb': 'BLUEPRINT FOR SUCCESS', 'title': '*TRANSFORMATION*<br>PROGRAM 🔥'},
 {'k': T, 'a': 89.24, 'b': 91.4, 'v': 'என்னோட MENTOR *RAVI SUNDARAM*', 'y': CAP},
 {'k': T, 'a': 91.4, 'b': 92.95, 'v': '*TRANSFORMATION* PROGRAM', 'y': CAP},
 # ===== INDIA'S LEADING =====
 {'k': 'kin', 'a': 105.62, 'b': 109.05, 'v': "INDIA'S LEADING", 'y': 80, 'fs': 120},
 {'k': 'kin', 'a': 106.4, 'b': 109.05, 'v': 'WELLNESS COACH', 'y': 225, 'fs': 120, 'c': '#2EE59D', 'mode': 'drop'},
 {'k': G, 'a': 106.9, 'b': 109.05, 'y': 450, 'eb': 'MY MENTOR', 'body': {'k': 'big', 'v': '🇮🇳 🏆', 'fs': 200, 'at': 107.0}},
 {'k': T, 'a': 105.62, 'b': 107.0, 'v': 'இந்த *PROGRAM*-ல', 'y': CW},
 {'k': T, 'a': 107.0, 'b': 109.0, 'v': "INDIA'S LEADING *COACH*", 'y': CW},
 # ===== HEALTH WEALTH HAPPINESS (full scene) =====
 {'k': 'sc_triad', 'a': 119.07, 'b': 121.75, 'at': [119.1, 119.5, 119.85], 'c': 'மூணும் CONNECTED'},
 # ===== 26 YEARS =====
 {'k': G, 'a': 141.8, 'b': 147.6, 'y': 40, 'h': 370, 'eb': 'WHY THIS PROGRAM', 'body': {'k': 'big', 'n': 26, 'from': 0, 'at': 141.9, 'd': .9, 'suf': ' YRS', 'l': '*EXPERIENCE*', 'fs': 190}},
 {'k': G, 'a': 143.9, 'b': 147.6, 'y': 440,
  'rows': [{'ic': '🧭', 'lb': 'Experience *guidance*', 'at': 143.95, 'on': 144.1},
           {'ic': '📚', 'lb': '*Learn* from it', 'at': 144.9, 'on': 145.2},
           {'ic': '🚀', 'lb': 'Big *opportunity*', 'at': 145.9, 'on': 146.6}]},
 {'k': T, 'a': 141.8, 'b': 144.0, 'v': '*26 YEARS* EXPERIENCE', 'y': CW},
 {'k': T, 'a': 144.03, 'b': 145.85, 'v': 'EXPERIENCE *GUIDANCE*', 'y': CW},
 {'k': T, 'a': 145.85, 'b': 147.57, 'v': 'பெரிய *OPPORTUNITY*', 'y': CW},
 # ===== 75 LAKH (face then full scene) =====
 {'k': 'kin', 'a': 161.7, 'b': 164.52, 'v': 'IN 26 YEARS', 'y': 110, 'fs': 140, 'c': '#FFD60A'},
 {'k': G, 'a': 162.1, 'b': 164.52, 'y': BOT + 60, 'eb': 'INCLUDING', 'title': 'MY *FAMILY* ❤️'},
 {'k': T, 'a': 161.7, 'b': 164.5, 'v': 'என்னோட *FAMILY*-யும் சேர்த்து', 'y': CAP},
 {'k': 'sc_fam', 'a': 164.54, 'b': 168.90, 'at2': 166.76},
 # ===== LAST TIME =====
 {'k': 'kin', 'a': 178.15, 'b': 183.26, 'v': '⏪ LAST TIME', 'y': 120, 'fs': 140},
 {'k': 'flow', 'a': 178.6, 'b': 183.26, 'y': 1420, 'v': [['📚', 'LEARN', 180.7], ['⚙️', '*APPLY*', 181.6]]},
 {'k': T, 'a': 178.15, 'b': 180.7, 'v': 'LAST TIME *ATTEND* பண்ணப்போ', 'y': CAP},
 {'k': T, 'a': 180.7, 'b': 183.23, 'v': 'LEARN & *APPLY*', 'y': CAP},
 # ===== 3 GOALS -> AUTOMATIC =====
 {'k': 'kin', 'a': 191.95, 'b': 213.9, 'v': 'MY 3 GOALS', 'y': 120, 'fs': 150, 'c': '#FFD60A', 'mode': 'drop'},
 {'k': G, 'a': 193.0, 'b': 213.93, 'y': 330,
  'rows': [{'ic': '💪', 'lb': 'Health', 'at': 193.8}, {'ic': '💰', 'lb': 'Wealth', 'at': 194.3}, {'ic': '😊', 'lb': 'Happiness', 'at': 194.75}]},
 {'k': T, 'a': 191.95, 'b': 193.15, 'v': '*3 GOALS* SET பண்ணேன்', 'y': CW},
 {'k': 'words', 'a': 193.17, 'b': 195.95, 'y': CW - 120, 'w': [['HEALTH', 193.8, 0], ['WEALTH', 194.3, 1], ['HAPPINESS', 194.75, 0]]},
 {'k': T, 'a': 212.15, 'b': 213.9, 'v': 'IN FACT, *TRY* கூட பண்ணல', 'y': CW},
 {'k': 'sc_rings', 'a': 213.93, 'b': 216.90, 'at': [215.0, 215.47, 215.77]},
 # ===== QUESTION + REALISATION (face) =====
 {'k': 'kin', 'a': 223.27, 'b': 225.2, 'v': 'HOW? 🤔', 'y': 110, 'fs': 190, 'c': '#FFD60A', 'mode': 'drop'},
 {'k': T, 'a': 223.27, 'b': 225.18, 'v': 'TRY பண்ணாம *எப்படி?*', 'y': CAP},
 {'k': 'kin', 'a': 231.35, 'b': 233.58, 'v': 'அங்க தான்|புரிஞ்சுது 💡', 'y': 100, 'fs': 100},
 # ===== PIVOT: shatter -> chase scene -> face =====
 {'k': 'flash', 'a': 267.75, 'b': 268.05, 'c': '#FF3B30', 'o': .6},
 {'k': 'sc_chase', 'a': 267.78, 'b': 270.12},
 {'k': 'kin', 'a': 270.15, 'b': 273.38, 'v': 'BECOME WORTHY|OF THE GOAL', 'y': 70, 'fs': 120, 'c': '#2EE59D'},
 {'k': G, 'a': 270.5, 'b': 273.38, 'y': BOT + 40, 'rows': [{'ic': '🏃', 'lb': '~Chase~ the goal', 'kind': 'x', 'at': 270.55, 'on': 270.6, 'strike': 270.7},
                                                       {'ic': '🌟', 'lb': 'Become *worthy*', 'kind': 'check', 'at': 270.93, 'on': 271.0}]},
 {'k': 'words', 'a': 270.15, 'b': 273.35, 'y': CAP - 20, 'w': [['BECOME', 270.15, 0], ['WORTHY', 270.93, 1]]},
 # ===== I CHANGED -> magnet =====
 {'k': 'kin', 'a': 291.5, 'b': 292.6, 'v': 'I CHANGED|MYSELF', 'y': 90, 'fs': 130},
 {'k': T, 'a': 291.5, 'b': 292.55, 'v': 'என்னை நான் *மாத்திக்கிட்டேன்*', 'y': CAP},
 {'k': 'sc_magnet', 'a': 292.57, 'b': 295.60},
 # ===== THIS TIME =====
 {'k': 'kin', 'a': 300.4, 'b': 302.32, 'v': 'THIS TIME TOO 🎟️', 'y': 120, 'fs': 130, 'c': '#FFD60A', 'mode': 'pop'},
 {'k': T, 'a': 300.4, 'b': 302.29, 'v': 'இந்த தடவையும் *ATTEND* பண்றேன்', 'y': CAP},
 {'k': 'kin', 'a': 325.9, 'b': 331.3, 'v': 'LEVEL UP 📈', 'y': 40, 'fs': 130, 'c': '#2EE59D', 'mode': 'drop'},
 {'k': 'stairs', 'a': 325.9, 'b': 331.3, 'y': 330, 'v': [['MY *STANDARDS*', 326.3], ['*CHANGE* ME', 328.1], ['*BIGGER* GOALS', 329.6]]},
 {'k': T, 'a': 325.9, 'b': 328.05, 'v': 'என்னோட *STANDARDS*', 'y': CW},
 {'k': T, 'a': 328.09, 'b': 329.55, 'v': 'என்னை *மாத்த*', 'y': CW},
 {'k': T, 'a': 329.59, 'b': 331.26, 'v': '*BIGGER* GOALS', 'y': CW},
 # ===== CTA (face on while he speaks) =====
 {'k': 'kin', 'a': 337.65, 'b': 341.45, 'v': '2027', 'y': 40, 'fs': 230, 'c': '#FFD60A', 'mode': 'drop'},
 {'k': 'kin', 'a': 339.38, 'b': 341.45, 'v': 'BEST VERSION', 'y': 290, 'fs': 110, 'c': '#2EE59D', 'mode': 'pop'},
 {'k': T, 'a': 337.65, 'b': 339.35, 'v': '*2027*-ல உங்க', 'y': CAP},
 {'k': T, 'a': 339.38, 'b': 341.34, 'v': '*BEST VERSION* OF YOU', 'y': CAP},
 {'k': 'words', 'a': 341.54, 'b': 345.0, 'y': 90, 'w': [['CLICK', 341.6, 0], ['THE', 341.95, 0], ['LINK', 342.36, 1], ['BELOW', 342.7, 0], ['&', 343.38, 0], ['REGISTER', 343.5, 1]]},
 {'k': G, 'a': 341.55, 'b': 345.0, 'y': BOT + 40, 'h': 470, 'body': {'k': 'btn', 'v': 'REGISTER NOW', 'at': 341.6, 'tag': '👇 LINK BELOW'}},
 # ===== END: animated CTA only (presenter cut) =====
 {'k': 'sc_cta', 'a': 345.0, 'b': 348.65},
] + wipes()
SFX = [(51.12, 'hit'), (52.60, 'swoosh'), (52.65, 'type'), (53.5, 'boom'), (54.86, 'swoosh'), (55.1, 'thud'), (56.7, 'toggle'), (58.4, 'toggle'),
       (74.69, 'swoosh'), (74.95, 'tick'), (75.12, 'tick'), (75.29, 'tick'), (75.46, 'tick'), (75.63, 'tick'), (75.8, 'tick'), (76.4, 'ding'), (77.8, 'swoosh'),
       (85.68, 'pop'), (87.12, 'swoosh'), (87.15, 'hit'), (87.6, 'type'), (88.5, 'swoosh'), (89.6, 'pop'), (90.9, 'pop'),
       (105.62, 'whoosh'), (106.4, 'pop'), (107.0, 'pop'),
       (119.07, 'swoosh'), (119.1, 'pop'), (119.5, 'pop'), (119.85, 'pop'), (120.3, 'hit'), (121.75, 'swoosh'),
       (141.8, 'whoosh'), (141.9, 'type'), (144.1, 'toggle'), (145.2, 'toggle'), (146.6, 'toggle'),
       (161.7, 'whoosh'), (162.1, 'pop'), (164.54, 'swoosh'), (164.6, 'cash'), (165.9, 'ding'), (166.76, 'pop'), (168.9, 'swoosh'),
       (178.15, 'whoosh'), (180.7, 'pop'), (181.4, 'swoosh'), (181.6, 'pop'),
       (191.95, 'thud'), (193.8, 'pop'), (194.3, 'pop'), (194.75, 'pop'),
       (213.93, 'swoosh'), (214.0, 'boom'), (215.0, 'riser'), (215.9, 'ding'), (216.2, 'ding'), (216.5, 'ding'), (216.9, 'swoosh'),
       (223.27, 'thud'), (231.32, 'clock'), (267.75, 'riser'), (267.75, 'glass'), (267.75, 'hit'), (268.9, 'whoosh'), (270.12, 'swoosh'), (270.7, 'thud'), (271.0, 'ding'),
       (291.5, 'whoosh'), (292.57, 'swoosh'), (292.9, 'whoosh'), (294.0, 'hit'), (295.6, 'swoosh'),
       (300.4, 'pop'), (325.9, 'thud'), (326.3, 'pop'), (328.1, 'pop'), (329.6, 'pop'), (330.2, 'whoosh'),
       (337.65, 'boom'), (339.38, 'pop'), (341.54, 'riser'), (341.6, 'hit'), (345.0, 'swoosh'), (345.1, 'boom'), (345.6, 'pop'), (346.0, 'ding')]
MUSIC = [(51.0, 87.0, 'pulse'), (87.0, 122.0, 'tech'), (141.7, 183.3, 'warm'), (191.8, 217.0, 'tech'), (223.2, 267.7, 'dark'),
         (267.7, 302.4, 'warm'), (325.8, 348.7, 'uplift')]

if __name__ == '__main__':
    build(P, LAY, ZOOM, FX, ITEMS, SFX, MUSIC, SHATTER)
