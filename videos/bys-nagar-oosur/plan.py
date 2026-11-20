"""BYS Nagar @ Oosur (SS Properties, V. Lokesh Amarnath): faceless plot ad.
src.mkv = black 1080x1920 + Voiceover.mp4 (61 s). Every second is covered by real site footage, the client's
brochures or animation. Times are VOICE-OVER seconds. Run: W=<work> python3 plan.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine', 'v7-themed'))
from planlib import build

KEEP = [(0.78, 14.62), (15.27, 21.57), (22.14, 28.31), (28.44, 32.53), (33.49, 47.68), (47.91, 51.29), (51.37, 56.62),
        (56.62, 60.97)]                                            # last range = tagline under the end card
BROLL = [
 ('L01', 0.78, 1.90, 'vid', 'full', dict(file='site.mkv', ss=0.0), '"Hello Vellore makkalae!"'),
 ('L02', 1.90, 10.31, 'choice', 'full', dict(cues=[2.00, 6.55], title='10 Years Later…',
      left=dict(e='😔', t='"அப்பவே ஒரு plot<br>வாங்கியிருந்தா…"', s='REGRET?'),
      right=dict(e='😊', t='"Correct time-ல<br>invest பண்ணிட்டேன்!"', s='HAPPY!'), status='animated stand-in for Flow L-A/L-B'),
      '"10 years later: regret, or happy you invested on time?"'),
 ('L03', 10.31, 14.62, 'vid', 'full', dict(file='i23_3.mkv', ss=0.0, chip='SS PROPERTIES PRESENTS'), '"a good investment for your family\'s future: BYS Nagar @ Oosur"'),
 ('L04', 15.27, 18.00, 'pinmap', 'full', dict(cues=[15.40, 16.20, 17.10], pins=['வேலூர் மாவட்டம்', 'அணைக்கட்டு வட்டம்', 'ஊசூர்'], title='Location'), '"Vellore district, Anaicut taluk, Oosur"'),
 ('L05', 18.00, 21.57, 'stamps', 'full', dict(cues=[18.00, 18.90], items=[['DTCP', 'GOVT'], ['RERA', 'REGISTERED']], title='Approved Plots'), '"DTCP & RERA approved plots"'),
 ('L06', 22.14, 28.31, 'vid', 'full', dict(file='site.mkv', ss=46.5, chip='OOSUR SITE'), '"quality ground water, avenue trees, premium facilities"'),
 ('L07', 28.44, 32.53, 'vid', 'full', dict(file='site.mkv', ss=14.6), '"schools, hospitals, Golden Temple: all nearby"'),
 ('L08', 33.49, 39.24, 'cards', 'full', dict(cues=[34.40, 35.60, 36.40], cols=1, tick=True, title='We Do It All For You',
      items=[['📍', 'FREE SITE VISIT'], ['🚗', 'CAR FACILITY'], ['🏦', 'BANK LOAN FACILITY']]), '"free site visit, car, bank loan: we do it all"'),
 ('L09', 39.24, 42.96, 'vid', 'full', dict(file='site.mkv', ss=74.0), '"the right time to buy your own plot"'),
 ('L10', 42.96, 47.68, 'offer', 'full', dict(top='FIRST 10 BOOKINGS ONLY', e='🪙', big='8 g Silver Coin', tag='FREE'), '"first 10 bookings: 8 g silver coin free" (offer graphic)'),
 ('L11', 47.91, 51.29, 'offer', 'full', dict(top='AND', e='🛠️', big='3 Years Maintenance', size=84, tag='FREE'), '"3 years free maintenance" (offer graphic)'),
 ('L12', 51.37, 56.62, 'vid', 'full', dict(file='i23.mkv', ss=0.0), '"click the link, book your free site visit" (CTA over brochure)'),
]
GFX = [
 ('chips', 22.14, 28.31, dict(items=['💧 QUALITY GROUND WATER', '🌳 AVENUE TREES', '🏡 COMFORTABLE LIVING'], cues=[22.40, 23.70, 25.90], y=250)),
 ('chips', 28.44, 32.53, dict(items=['🏫 SCHOOLS', '🏥 HOSPITALS', '🛕 GOLDEN TEMPLE', '✓ ALL NEARBY'], cues=[29.10, 29.60, 30.30, 31.60], y=250)),
 ('slam', 40.00, 42.96, dict(html='Correct Time ✓', y=640)),
 ('cta', 51.37, 56.62, dict(label='BOOK SITE VISIT', arrow='⬇', y=1530)),
]
CAPSTYLE = 'B'
CAP = [
 (0.78, 1.90, '', 'Hello Vellore!'),
 (1.90, 6.40, '"I should have bought a plot back then…"', '10 Years Later…'),
 (6.50, 10.31, '"I invested at the right time!"', 'Or Will You Say'),
 (10.31, 14.62, "a smart investment for your family's future", 'BYS Nagar @ Oosur'),
 (15.27, 18.00, 'Vellore district, Anaicut taluk', 'Oosur'),
 (18.00, 21.57, 'plots ready for you now', 'DTCP & RERA Approved'),
 (22.14, 25.00, 'and avenue trees', 'Quality Ground Water'),
 (25.00, 28.31, 'for comfortable living', 'Premium Facilities'),
 (28.44, 32.53, 'schools · hospitals · Golden Temple', 'Everything Nearby'),
 (33.49, 36.30, 'with car pick-up', 'Free Site Visit'),
 (36.30, 39.24, 'we arrange everything', 'Bank Loan Facility'),
 (39.24, 42.96, 'to buy your own plot', 'This Is The Right Time'),
 (42.96, 47.68, '8 g silver coin FREE', 'First 10 Bookings'),
 (47.91, 51.29, 'free maintenance', '+ 3 Years'),
 (51.37, 56.62, 'tap the link below', 'Book Free Site Visit'),
]
MUSIC = [(0.0, 'intro'), (10.31, 'lift'), (15.27, 'groove'), (42.96, 'finale')]
SFX = [(10.31, 'shimmer'), (42.96, 'riser'), (51.37, 'bell')]
BRAND = dict(badge='BYS NAGAR', star='◆', motif='grid', name='SS Properties',
             title='BYS NAGAR @ OOSUR · DTCP & RERA APPROVED PLOTS',
             end=dict(img='i23_3.jpg', imgw=430, top_y=150, top='SS PROPERTIES PRESENTS', main='BYS NAGAR', main2='@ OOSUR', size=130, size2=100,
                      by='A plot today, a beautiful future', title='FREE SITE VISIT · CAR FACILITY · BANK LOAN', btn='BOOK SITE VISIT', btn_y=1640))

if __name__ == '__main__':
    build(dict(KEEP=KEEP, END_TAIL=1, BROLL=BROLL, GFX=GFX, CAP=CAP, CAPSTYLE=CAPSTYLE, MUSIC=MUSIC, SFX=SFX, BRAND=BRAND),
          os.path.dirname(os.path.abspath(__file__)))
