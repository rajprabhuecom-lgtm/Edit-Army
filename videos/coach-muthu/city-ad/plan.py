"""EDL for Coach Muthu city ad. Source = IMG_2606.MOV (Drive: Coach Muthu/IMG_2606.MOV), 1080x1920 30 fps.
Only the coach's own takes are used; the off-camera prompter is never in the edit.
Times are SOURCE seconds. Final = output / 1.2."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from build_lib import build

W = '/home/user/w_city/'
WAV = '/tmp/claude-0/-home-user-Edit-Army/17a3602b-8414-5147-9d72-5c4b390407cd/scratchpad/raw/IMG_2606.wav'

TAKES = [(10.40, 13.15), (19.50, 22.05), (24.20, 25.35), (28.60, 30.95), (36.90, 40.75), (43.80, 46.55), (53.20, 57.35),
         (57.80, 58.65), (64.30, 66.35), (66.70, 68.25), (75.60, 79.45), (91.20, 98.55), (109.30, 114.15), (114.40, 117.35),
         (143.40, 145.55), (152.50, 156.45), (156.70, 160.25), (166.60, 171.95), (177.60, 178.95), (179.40, 182.45),
         (188.40, 191.05), (195.50, 198.50), (198.50, 198.95, 'raw'), (202.30, 210.30), (210.30, 210.85, 'raw')]
TAIL = (210.90, 212.80)   # silent room tone under the end card
END = TAIL[1]

BROLL = [
 ('C1', 36.90, 40.75, 'vid', 'full', dict(file='C1_traffic.mkv', ss=0.3, big='🕘 9 AM • <span class="r">1 HOUR</span>', bcue=39.57, by=250, bsz=104), '"9 AM on this same GST Road, one hour of traffic"'),
 ('C2', 43.80, 46.55, 'vid', 'split', dict(file='C2_office.mkv', ss=1.0, cy=60, csz=46,
      chips=[['💻 8 மணி நேரம் SITTING', '#2a1010', '#FF3B30', '#FF3B30']], ccues=[44.67]), '"then 8 hours sitting in the office"'),
 ('C3', 53.20, 57.35, 'vid', 'split', dict(file='C3_kaalan.mkv', ss=0.5, cy=60, csz=46,
      chips=[['🍄 காளான் கடை'], ['1 PLATE', '#080A0D', '#FFD60A', '#FFD60A'], ['2 PLATES 😋', '#080A0D', '#FFD60A', '#FFD60A']], ccues=[55.17, 56.21, 56.57]), '"evening, our favourite kaalan shop, one plate, two plates"'),
 ('G1', 64.30, 68.25, 'days', 'split', dict(dcues=[65.40, 65.80, 67.40], ftc=67.70), '"that\'s why the Family Health Reset 3 Day Challenge"'),
 ('S1', 75.60, 79.45, 'vid', 'split', dict(file='S1_zoom.mkv', ss=0.3, cy=60, csz=44,
      chips=[['💻 ZOOM • MORNING 1 HOUR'], ['🏠 FROM HOME', '#00C896', '#04110c', '#00C896']], ccues=[75.75, 77.90]), '"attend on Zoom from your home"'),
 ('G2', 109.30, 115.90, 'checkup', 'split', dict(kcues=[112.10, 112.65, 113.45]), '"Day 3 - come to the centre, BMI, BMR, fat"'),
 ('G3', 202.30, 208.20, 'mappin', 'split', dict(mcues=[202.45, 202.60, 205.40, 206.25]), '"centre: Guduvanchery, Nellikuppam Rd, Periyar Nagar, opp. SRM School"'),
]
GFX = [
 ('badge', 10.40, 13.15, {'html': '🏆 நம்ம ஊர் = BEST', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('badge', 19.50, 25.35, {'html': '🛕 நந்தீஸ்வரர் கோயில்', 'y': 200, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 56}),
 ('badge', 20.75, 25.35, {'html': '🍚 தேவஸ்தான புட்டு', 'y': 320, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 56}),
 ('badge', 24.20, 25.35, {'html': '💼 நல்ல JOB', 'y': 440, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 56}),
 ('text', 28.60, 30.95, {'html': 'ஒரு விஷயத்துல<br><span class="r">பின்னாடி</span>', 'y': 200, 'size': 100}),
 ('badge', 57.80, 58.65, {'html': '😄 நானும் சாப்பிடுவேன்', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 58}),
 ('badge', 91.20, 94.00, {'html': '🏥 NO HOSPITAL VISITS', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('text', 94.00, 98.55, {'html': '<span class="y">8+ YEARS</span><br>WELLNESS EXPERIENCE', 'y': 200, 'size': 84}),
 ('text', 115.90, 117.35, {'html': 'COMPLETELY<br><span class="g">FREE ✓</span>', 'y': 200, 'size': 140}),
 ('badge', 143.40, 145.55, {'html': '❤️ நம்ம குடுவாஞ்சேரி', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('badge', 152.50, 160.25, {'html': '🎁 3 DAYS = FAMILY GIFT', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('flash', 166.60, 166.75, {}),
 ('cta', 166.60, 171.95, {'label': '👇 CLICK & REGISTER', 'badge': '💬 PREMIUM WHATSAPP GROUP', 'y': 1060}),
 ('badge', 177.60, 191.05, {'html': 'ONLY FIRST 10 FAMILIES 🔥', 'y': 200, 'size': 64}),
 ('text', 188.40, 191.05, {'html': 'AFTER THAT<br><span class="y">₹2,000</span>', 'y': 330, 'size': 110}),
 ('badge', 195.50, 198.95, {'html': '🤝 SEE YOU AT THE CENTRE', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('badge', 208.20, 210.85, {'html': '🤝 வாங்க, அங்க MEET பண்ணலாம்', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 54}),
 ('endcard', 210.90, END, {'loc': 'COACH MUTHU • GUDUVANCHERY'}),
]
CAP = [
 (10.40, 13.15, [['குடுவாஞ்சேரி', 'மக்களே,'], ['நம்ம', 'ஊர்ல', 'எல்லாமே', '^BEST-தான்']]),
 (19.50, 22.05, [['*நந்தீஸ்வரர்', 'கோயில்'], ['*தேவஸ்தான', 'புட்டு']]),
 (24.20, 25.35, [['நல்ல', '*JOB']]),
 (28.60, 30.95, [['ஆனா', 'ஒரு', 'விஷயத்துல', 'மட்டும்'], ['நாம', '!பின்னாடி', 'இருக்கோம்']]),
 (36.90, 38.60, [['^MORNING', '^9 மணிக்கு']]),
 (38.60, 40.75, [['இதே', '*GST ROAD-ல'], ['!ONE HOUR', '!TRAFFIC']]),
 (43.80, 46.55, [['அப்புறம்', 'OFFICE-ல'], ['!8 மணி நேரம்'], ['உட்காந்துட்டே', 'இருக்கோம்']]),
 (53.20, 55.10, [['EVENING', 'ஆனா'], ['நமக்கு', 'பிடிச்ச']]),
 (55.10, 57.35, [['^காளான்', 'கடையில'], ['ஒரு', 'PLATE,', '!ரெண்டு PLATE']]),
 (57.80, 58.65, [['நானும்', '^சாப்பிடுவேன்']]),
 (64.30, 68.25, [['அதுக்குதான்'], ['*FAMILY HEALTH', '*RESET'], ['^3 DAY', '^CHALLENGE']]),
 (75.60, 77.75, [['முதல்', '2 DAYS'], ['^MORNING', '^1 HOUR']]),
 (77.75, 79.45, [['வீட்டிலிருந்தே'], ['*ZOOM-ல', 'ATTEND']]),
 (91.20, 94.00, [['நம்ம', 'FAMILY'], ['!HOSPITAL VISIT', 'இல்லாம'], ['இருக்க']]),
 (94.00, 98.55, [['^FULL ROADMAP'], ['என்னோட', '*8+ YEARS', 'EXPERIENCE'], ['நான்', '^TRAIN', 'பண்ணிடுவேன்']]),
 (109.30, 111.40, [['^3RD DAY', 'நம்ம'], ['*CENTRE-க்கு', 'வாங்க']]),
 (111.40, 114.15, [['உங்க', 'FAMILY-ஓட'], ['*BMI', '*BMR', '*FAT']]),
 (114.40, 117.35, [['எல்லா', 'TEST-உம்'], ['*COMPLETE-ஆ', '*FREE-ஆ'], ['பாத்துக்கலாம்']]),
 (143.40, 145.55, [['நம்ம', '^குடுவாஞ்சேரி'], ['நமக்கு', 'எல்லாமே', 'குடுக்குது']]),
 (152.50, 156.45, [['இப்போ', 'உங்க', 'FAMILY-க்கு'], ['^GIFT-ஆ', 'இந்த', '*3 DAYS'], ['குடுங்க']]),
 (156.70, 160.25, [['நான்', 'உங்க', 'FAMILY-க்கு'], ['*HEALTH-ஐ', '^GIFT-ஆ'], ['திருப்பித்', 'தர்றேன்']]),
 (166.60, 169.30, [['இப்பவே', 'கீழே', '^BUTTON-ஐ'], ['CLICK', 'பண்ணி', '^REGISTER']]),
 (169.30, 171.95, [['நம்ம', '*PREMIUM'], ['*WHATSAPP', 'GROUP-ல', 'JOIN']]),
 (177.60, 178.95, [['ஆனா', 'இந்த', 'வாய்ப்பு']]),
 (179.40, 182.45, [['முதல்', '!10 FAMILY-க்கு'], ['மட்டும்தான்']]),
 (188.40, 191.05, [['அதுக்கப்புறம்'], ['MINIMUM', '!₹2000'], ['CHARGE', 'பண்ணப்', 'போறோம்']]),
 (195.50, 198.95, [['இப்பவே', '^REGISTER', 'பண்ணுங்க'], ['நம்ம', '*CENTRE-ல'], ['MEET', 'பண்றேன்']]),
 (202.30, 205.30, [['நம்ம', 'CENTRE'], ['^குடுவாஞ்சேரி'], ['நெல்லிக்குப்பம்', 'ROAD']]),
 (205.30, 208.20, [['^பெரியார் நகர்'], ['*SRM SCHOOL', 'OPPOSITE']]),
 (208.20, 210.85, [['வாங்க', 'ஒருத்தர', 'ஒருத்தர்'], ['அங்க', '*MEET', 'பண்ணலாம்']]),
]
PUNCH = [(10.4, 13.2, 1.10), (28.6, 31.0, 1.16), (57.8, 58.7, 1.14), (91.2, 94.0, 1.06), (94.0, 98.6, 1.12), (115.9, 117.4, 1.18),
         (143.4, 145.6, 1.10), (152.5, 156.5, 1.06), (156.7, 160.3, 1.12), (166.6, 172.0, 1.06), (177.6, 182.5, 1.14),
         (188.4, 191.1, 1.10), (195.5, 199.0, 1.08), (208.2, 210.9, 1.12)]
DESAT = [(28.60, 30.95)]
MUSIC = [(10.40, 64.30, 'pulse'), (64.30, 143.40, 'tech'), (143.40, END, 'uplift')]
SFX = [(10.40, 'hit'), (28.60, 'thud'), (115.90, 'hit'), (166.30, 'riser'), (166.60, 'hit'), (210.90, 'hit')]

if __name__ == '__main__':
    build(W, WAV, TAKES, TAIL, BROLL, GFX, CAP, PUNCH, DESAT, MUSIC, SFX, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'broll_plan.csv'))
