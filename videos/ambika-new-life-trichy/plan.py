"""Coach Ambika, New Life Nutrition (Trichy): talking-head 3-day trial ad.
src.mkv = ambika 1.mp4 upscaled to 1080x1920 (53.5 s). Times are SOURCE seconds. Run: W=<work> python3 plan.py
Render with CROP_Y0=350 CY=750 LOOK=fresh BGM=base. src.mkv is reframed (1.35x zoom, face moved up) because she sits low in her phone frame."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine', 'v7-themed'))
from planlib import build

KEEP = [(0.0, 26.30), (26.55, 28.78), (29.06, 31.12), (31.34, 47.52), (47.69, 51.60),
        (51.60, 53.40)]                                           # tail under the end card
BROLL = [
 ('A01', 3.00, 7.56, 'vid', 'split', dict(file='A-1.mkv', ss=0.2, cy=900, ai=True, note='AI (Google Flow) - disclose in Meta'), '"trying to lose weight? not sure what works?"'),
 ('A02', 7.56, 10.50, 'vid', 'split', dict(file='A-2.mkv', ss=2.5, cy=700, ai=True, note='AI (Google Flow) - disclose in Meta'), '"tried diet and workout…"'),
 ('A02b', 10.50, 12.59, 'stuck', 'split', dict(cues=[10.50, 10.55], scue=10.70, e='⚖️', tags=['🥗 DIET ✓', '🏃 WORKOUT ✓'], stamp='NO RESULT ✗'), '"…still no result?"'),
 ('A02c', 12.60, 15.50, 'vid', 'split', dict(file='A-4.mkv', ss=0.3, cy=900, ai=True, note='AI (Google Flow) - disclose in Meta'), '"our clients struggled like this too"'),
 ('A03', 15.50, 18.90, 'vid', 'split', dict(file='p0604_1.mkv', ss=0.5, cy=960, chip='PROPER GUIDANCE'), '"now with proper nutrition & fitness guidance" (real centre photo)'),
 ('A04', 18.90, 20.30, 'vid', 'split', dict(file='p1149.mkv', ss=0.5, cy=960, chip='OUR CLIENTS ✓'), '"they got healthy results" (real client photo, consent to confirm)'),
 ('A05', 20.30, 21.50, 'vid', 'split', dict(file='p1207.mkv', ss=0.5, cy=960, chip='OUR CLIENTS ✓'), '"they got healthy results" (real client photo, consent to confirm)'),
 ('A06', 26.55, 31.12, 'vid', 'split', dict(file='p0603.mkv', ss=0.5, cy=960, chip='YOUR FITNESS JOURNEY'), '"I support your fitness journey" (real centre photo)'),
 ('A07', 31.34, 33.30, 'vid', 'split', dict(file='A-5.mkv', ss=0.5, cy=980, ai=True, note='AI (Google Flow) - disclose in Meta'), '"for your lifestyle and fitness goals"'),
 ('A07b', 33.30, 36.40, 'vid', 'split', dict(file='A-6.mkv', ss=0.3, cy=900, ai=True, note='AI (Google Flow) - disclose in Meta'), '"step by step, and follow it"'),
 ('A08', 42.30, 45.50, 'vid', 'split', dict(file='A-3.mkv', ss=0.3, cy=960, chip='TRICHY 📍', ai=True, note='AI (Google Flow) - disclose in Meta'),
      '"in Trichy, ready to start your fitness journey?"'),
]
GFX = [
 ('slam', 0.10, 3.00, dict(html='⚠ Important Update', y=300)),
 ('chips', 3.00, 7.56, dict(items=['🥑 KETO?', '⏰ FASTING?', '🏋️ GYM?', '📋 DIET CHART?'], cues=[3.30, 4.70, 5.80, 6.40], y=240)),
 ('chips', 7.56, 10.50, dict(items=['🥗 DIET ✓', '🏃 WORKOUT ✓'], cues=[7.60, 8.30], y=240)),
 ('chips', 33.30, 36.40, dict(items=['🎯 YOUR GOALS', '📋 YOUR PLAN', '✅ DAILY FOLLOW-UP'], cues=[33.30, 34.70, 35.20], y=240)),
 ('badge', 21.50, 26.30, dict(html='COACH AMBIKA <i>·</i> 8 YEARS EXPERIENCE', y=1075)),
 ('slam', 36.50, 42.20, dict(html='3-Day Trial ✚', y=300)),
 ('badge', 37.20, 42.20, dict(html='NEW LIFE NUTRITION <i>·</i> OFFER ON NOW', y=1075)),
 ('cta', 47.69, 51.60, dict(label='BOOK APPOINTMENT', arrow='⬇', y=1040)),
]
CAPSTYLE = 'A'
CAP = [
 (0.00, 3.00, 'WEIGHT LOSS STRUGGLE?', 'Important Update!'),
 (3.00, 5.30, 'TRYING TO', 'Lose Weight?'),
 (5.30, 7.56, 'CONFUSED ABOUT', 'What Works?'),
 (7.56, 10.00, 'TRIED', 'Diet & Workout?'),
 (10.00, 12.59, 'STILL', 'No Results?'),
 (12.60, 15.50, 'OUR CLIENTS TOO', 'Struggled Like This'),
 (15.50, 18.90, 'BUT WITH PROPER', 'Nutrition + Fitness'),
 (18.90, 21.50, 'THEY ACHIEVED', 'Healthy Results'),
 (21.50, 24.00, "I'M YOUR COACH", 'Ambika'),
 (24.00, 26.30, 'WITH', '8 Years Experience'),
 (26.55, 31.12, 'SUPPORTING YOUR', 'Fitness Journey'),
 (31.34, 33.30, 'FOR YOUR LIFESTYLE &', 'Fitness Goals'),
 (33.30, 36.40, 'A PLAN YOU FOLLOW', 'Step by Step'),
 (36.50, 39.00, 'NOW AT NEW LIFE NUTRITION', 'Offer On Now'),
 (39.00, 42.20, '', '3-Day Trial Package'),
 (42.30, 45.50, 'IN TRICHY?', 'Start Your Journey'),
 (45.50, 47.52, '', 'Ready?'),
 (47.69, 51.60, 'TAP THE LINK BELOW &', 'Book Appointment'),
]
PUNCH = [(0.0, 3.0, 1.10), (12.6, 15.5, 1.08), (21.5, 24.0, 1.12), (36.5, 42.2, 1.06), (45.5, 47.52, 1.14)]
MUSIC = [(0.0, 'pulse'), (3.0, 'dark'), (12.6, 'warm'), (36.5, 'uplift')]
SFX = [(0.10, 'hit'), (10.60, 'thud'), (12.60, 'swipe'), (36.50, 'hit'), (47.60, 'riser')]
BRAND = dict(badge='NEW LIFE NUTRITION', star='✚', motif='rings', name='Coach Ambika',
             title='NUTRITION & FITNESS COACH · NEW LIFE NUTRITION, TRICHY',
             end=dict(top='NEW LIFE NUTRITION · TRICHY', main='3-Day', main2='Trial Package', by='with Coach Ambika',
                      title='NUTRITION + FITNESS GUIDANCE · STEP BY STEP', btn='BOOK APPOINTMENT'))

if __name__ == '__main__':
    build(dict(KEEP=KEEP, END_TAIL=1, BROLL=BROLL, GFX=GFX, CAP=CAP, CAPSTYLE=CAPSTYLE, PUNCH=PUNCH, MUSIC=MUSIC, SFX=SFX, BRAND=BRAND),
          os.path.dirname(os.path.abspath(__file__)))
