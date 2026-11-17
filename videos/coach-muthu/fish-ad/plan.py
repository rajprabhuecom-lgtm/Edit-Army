"""EDL for Coach Muthu fish ad. Source = IMG_2605.MOV (Drive: Coach Muthu/IMG_2605.MOV), 1080x1920 30 fps.
Only the coach's own takes are used; the off-camera prompter is never in the edit.
Times are SOURCE seconds. Final = output / 1.2."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from build_lib import build

W = '/home/user/w_fish/'
WAV = '/tmp/claude-0/-home-user-Edit-Army/17a3602b-8414-5147-9d72-5c4b390407cd/scratchpad/raw/IMG_2605.wav'

# coach takes (best take of each line; prompter reads, retakes and the coach's aside to the prompter at 176.9-181.2 are left out)
TAKES = [(6.40, 8.05), (16.40, 19.55), (21.30, 22.75), (23.30, 25.25), (28.30, 31.05), (35.20, 38.05), (45.60, 46.85),
         (53.40, 55.45), (58.20, 59.85), (65.40, 69.05), (75.80, 79.45), (82.90, 85.85), (86.10, 88.45),
         (105.80, 109.15), (109.40, 114.55), (123.80, 131.25), (138.70, 142.85), (189.10, 195.85), (200.20, 203.35),
         (207.40, 209.98), (209.98, 210.38, 'raw'), (214.40, 217.55), (228.60, 231.85), (234.80, 243.75)]
TAIL = (243.80, 246.00)   # silent room tone under the end card
END = TAIL[1]

BROLL = [
 ('F1', 16.40, 19.55, 'vid', 'full', dict(file='F1_feed.mkv', ss=0.6, big='🐟 அதிகமா <span class="y">FOOD?</span>', bcue=17.53, by=250, bsz=110), '"if you feed this fish this much, know what happens?"'),
 ('F2', 21.30, 25.25, 'vid', 'split', dict(file='F2_murky.mkv', ss=0.8, cy=60, csz=46,
      chips=[['💧 WATER கெட்டுப் போகும்', '#2a1010', '#FF3B30', '#FF3B30'], ['🐟 FISH SICK ஆகும்', '#2a1010', '#FF3B30', '#FF3B30']], ccues=[21.40, 23.40]), '"the water spoils, the fish gets sick"'),
 ('F3', 53.40, 59.85, 'vid', 'split', dict(file='F3_dinner.mkv', ss=0.3, cy=60, csz=44,
      chips=[['🌙 LATE NIGHT DINNER'], ['☕ 3 CUPS TEA', '#080A0D', '#FFD60A', '#FFD60A'], ['💧 WATER ✗', '#2a1010', '#FF3B30', '#FF3B30']], ccues=[53.50, 54.60, 58.30]), '"late-night dinner, three cups of tea, we forget water"'),
 ('G1', 75.80, 79.45, 'days', 'split', dict(dcues=[76.90, 77.50, 78.30], ftc=78.90), '"that\'s why the Family Health Reset 3 Day Challenge"'),
 ('S1', 82.90, 88.45, 'vid', 'split', dict(file='S1_zoom.mkv', ss=0.3, cy=60, csz=44,
      chips=[['💻 ZOOM • MORNING 1 HOUR'], ['🏠 FROM HOME', '#00C896', '#04110c', '#00C896']], ccues=[83.75, 86.15]), '"first 2 days on Zoom, morning 1 hour, from home"'),
 ('G2', 123.80, 129.75, 'checkup', 'split', dict(kcues=[126.55, 127.20, 128.00]), '"Day 3 - come to the centre, BMI, BMR, fat analysis"'),
 ('G3', 234.80, 241.45, 'mappin', 'split', dict(mcues=[235.10, 236.05, 238.40, 239.60]), '"centre: Guduvanchery, Nellikuppam Rd, Periyar Nagar, opp. SRM School"'),
]
GFX = [
 ('badge', 6.40, 8.05, {'html': '✋ ஒரு நிமிஷம்!', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
 ('badge', 28.30, 31.05, {'html': '🐟 FISH RULE', 'y': 230, 'size': 66}),
 ('badge', 35.20, 38.05, {'html': '✓ CORRECT FOOD', 'y': 200, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('badge', 36.00, 38.05, {'html': '✓ CLEAN WATER', 'y': 320, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('badge', 37.10, 38.05, {'html': '✓ CORRECT TIMING', 'y': 440, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('text', 45.60, 46.85, {'html': 'நம்ம <span class="r">BODY-க்கு?</span>', 'y': 230, 'size': 110}),
 ('text', 65.40, 69.05, {'html': 'FISH <span class="g">✓</span><br>நாம <span class="r">✗</span>', 'y': 200, 'size': 120}),
 ('badge', 105.80, 109.15, {'html': '🏥 NO HOSPITAL VISITS', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('text', 109.40, 114.55, {'html': '<span class="y">8+ YEARS</span><br>WELLNESS EXPERIENCE', 'y': 200, 'size': 84}),
 ('text', 129.75, 131.25, {'html': 'COMPLETELY<br><span class="g">FREE ✓</span>', 'y': 200, 'size': 140}),
 ('badge', 140.40, 142.85, {'html': '🎁 3 DAYS = FAMILY GIFT', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('flash', 189.10, 189.25, {}),
 ('badge', 189.10, 192.40, {'html': '🎁 HEALTH = GIFT', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 64}),
 ('cta', 192.40, 203.35, {'label': '👇 CLICK & REGISTER', 'badge': '💬 PREMIUM WHATSAPP GROUP', 'y': 1060}),
 ('badge', 207.40, 217.55, {'html': 'ONLY FIRST 10 FAMILIES 🔥', 'y': 200, 'size': 64}),
 ('text', 214.40, 217.55, {'html': 'AFTER THAT<br><span class="y">₹2,000</span>', 'y': 330, 'size': 110}),
 ('badge', 228.60, 231.85, {'html': '🤝 SEE YOU AT THE CENTRE', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('badge', 241.45, 243.75, {'html': '📍 LOCATION உங்களுக்கு வரும்', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 50}),
 ('endcard', 243.80, END, {'loc': 'COACH MUTHU • GUDUVANCHERY'}),
]
CAP = [
 (6.40, 8.05, [['குடுவாஞ்சேரி', 'மக்களே,'], ['ஒரு', '^நிமிஷம்!']]),
 (16.40, 18.10, [['இந்த', '*FISH-க்கு'], ['இப்படி', '!அதிகமா', '*FOOD']]),
 (18.10, 19.55, [['போட்டா', 'என்ன', 'ஆகும்'], ['^தெரியுமா?']]),
 (21.30, 22.75, [['*WATER', '!கெட்டுப்', '!போகும்']]),
 (23.30, 25.25, [['*FISH', '!SICK', 'ஆகும்']]),
 (28.30, 31.05, [['FISH', 'வளர்க்கிற'], ['எல்லாருக்குமே'], ['இந்த', '^RULE', 'தெரியும்']]),
 (35.20, 38.05, [['*CORRECT FOOD'], ['*CLEAN WATER'], ['*CORRECT TIMING']]),
 (45.60, 46.85, [['ஆனா', 'நம்ம', '!BODY-க்கு?']]),
 (53.40, 55.45, [['!LATE NIGHT', 'DINNER'], ['மூணு', '^CUP TEA']]),
 (58.20, 59.85, [['*WATER', 'குடிக்கவே'], ['!மறந்துடுவோம்']]),
 (65.40, 67.20, [['*FISH-க்கு', 'போடுற'], ['^RULE', 'கூட']]),
 (67.20, 69.05, [['நமக்கு', 'நாமே'], ['!போடுறதே', '!இல்ல']]),
 (75.80, 79.45, [['அதுக்குதான்'], ['*FAMILY HEALTH', '*RESET'], ['^3 DAY', '^CHALLENGE']]),
 (82.90, 85.85, [['முதல்', '2 DAYS', '*ZOOM-ல'], ['^MORNING', '^1 HOUR']]),
 (86.10, 88.45, [['வீட்டில', 'இருந்தே'], ['*ATTEND', 'பண்ணலாம்']]),
 (105.80, 109.15, [['நம்ம', 'FAMILY'], ['!HOSPITAL VISIT', 'இல்லாம'], ['இருக்க']]),
 (109.40, 114.55, [['ஒரு', '^FULL ROADMAP'], ['என்னோட', '*8+ YEARS', 'EXPERIENCE'], ['நான்', '^TRAIN', 'பண்ணிடுவேன்']]),
 (123.80, 125.40, [['^3RD DAY', 'நம்ம'], ['*CENTRE-க்கு', 'வாங்க']]),
 (125.40, 129.75, [['உங்க', 'FAMILY-ஓட'], ['*BMI', '*BMR'], ['*FAT', 'ANALYSIS']]),
 (129.75, 131.25, [['எல்லாமே', '*COMPLETE-ஆ'], ['*FREE-ஆ', 'பண்ணலாம்']]),
 (138.70, 140.40, [['இந்த', '*FISH-ஐ'], ['நான்', 'பாத்துக்கிறேன்']]),
 (140.40, 142.85, [['உங்க', 'FAMILY-க்கு', '^GIFT-ஆ'], ['இந்த', '*3 DAY', '*CHALLENGE'], ['நீங்க', 'குடுங்க']]),
 (189.10, 192.40, [['உங்க', 'FAMILY-க்கு'], ['*HEALTH-ஐ', '^GIFT-ஆ'], ['குடுக்க']]),
 (192.40, 195.85, [['கீழே', '^BUTTON-ஐ'], ['CLICK', 'பண்ணி'], ['*உடனே', '*REGISTER']]),
 (200.20, 203.35, [['அதோட', '*PREMIUM'], ['*WHATSAPP', 'GROUP-லயும்', 'JOIN']]),
 (207.40, 210.38, [['இந்த', 'OPPORTUNITY'], ['முதல்', '!10 FAMILY-க்கு', 'மட்டும்தான்']]),
 (214.40, 217.55, [['அதுக்கப்புறம்'], ['MINIMUM', '!₹2000'], ['CHARGE', 'பண்ணப்', 'போறோம்']]),
 (228.60, 231.85, [['உடனே', '^REGISTER', 'பண்ணுங்க'], ['நம்ம', '*CENTRE-ல'], ['MEET', 'பண்றேன்']]),
 (234.80, 238.30, [['நம்ம', 'CENTRE'], ['^குடுவாஞ்சேரி'], ['நெல்லிக்குப்பம்', 'ROAD']]),
 (238.30, 241.45, [['^பெரியார் நகர்'], ['*SRM SCHOOL', 'OPPOSITE']]),
 (241.45, 243.75, [['எல்லா', '*DETAILS'], ['நானே', 'அனுப்புறேன்']]),
]
PUNCH = [(6.4, 8.1, 1.12), (28.3, 31.1, 1.08), (45.6, 46.9, 1.16), (65.4, 69.1, 1.12), (105.8, 109.2, 1.06), (109.4, 114.6, 1.12),
         (129.7, 131.3, 1.18), (138.7, 142.9, 1.08), (189.1, 192.4, 1.10), (192.4, 196.0, 1.06), (200.2, 203.4, 1.12),
         (207.4, 210.4, 1.16), (214.4, 217.6, 1.10), (228.6, 231.9, 1.08), (241.4, 243.8, 1.12)]
DESAT = [(65.40, 69.05)]
MUSIC = [(6.40, 75.80, 'pulse'), (75.80, 139.0, 'tech'), (139.0, END, 'uplift')]
SFX = [(6.40, 'hit'), (45.60, 'thud'), (65.40, 'thud'), (129.75, 'hit'), (188.80, 'riser'), (189.10, 'hit'), (243.80, 'hit')]

if __name__ == '__main__':
    build(W, WAV, TAKES, TAIL, BROLL, GFX, CAP, PUNCH, DESAT, MUSIC, SFX, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'broll_plan.csv'))
