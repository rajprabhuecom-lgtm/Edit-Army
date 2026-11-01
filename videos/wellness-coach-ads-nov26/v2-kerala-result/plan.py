"""V2 'Kerala centre result' (VID_20260728_224059_148_bsl). Opens on the REAL WhatsApp update on his phone - kept on screen (face + phone)."""
W = '/home/user/work/v/1BB9_yoPvd08rbOaxsCvD0FTcKOMnaVis/'
CFG = dict(capTop=1290, capH=260, blur=[(100, 1370, 980, 1575)], cy=700)
BROLL = [
 ('B01', 3.20, 6.10, 'checklist', 'split', dict(title='📲 KERALA <span class="g">RESULT</span>', items=['📝 MONTHLY REGISTRATION • 1', '🔟 10-DAY REGISTRATION • 2', '📅 APPOINTMENTS • 3'], cues_s=[3.20, 4.32, 5.36]), '"monthly registration 1, 10-day registration 2, appointments 3" (numbers read from the real message on his phone)'),
 ('B02', 6.14, 11.30, 'walkin', 'split', dict(title='CONSISTENT <span class="g">WALK&#8209;INS</span>'), '"consistent walk-ins, appointments, registrations"'),
 ('B03', 14.08, 16.90, 'pin', 'full', dict(title='YOUR <span class="y">NEXT PIN</span>'), '"achieve our next pin level"'),
 ('B04', 27.08, 32.45, 'social', 'split', dict(title='NEW <span class="g">CLIENTS</span> 👥', chip='👥 CONSISTENT NEW CLIENTS', chipAt=2.6), '"bring consistent new clients from unknown circles to your centre"'),
]
GFX = [
 ('badge', 0.30, 2.95, {'html': '📲 REAL RESULT • KERALA', 'y': 270, 'bg': 'var(--yl)', 'fg': '#000', 'size': 60}),
 ('text', 11.32, 14.00, {'html': '<span class="g">ONLINE</span><br>GENERATED 🌐', 'y': 270, 'size': 110}),
 ('text', 16.98, 19.90, {'html': 'EVERY CENTRE<br><span class="g">NEEDS THIS ✅</span>', 'y': 270, 'size': 104}),
 ('flash', 19.90, 20.05, {}),
 ('cta', 19.94, 22.60, {'label': '👇 CLICK THE LINK', 'badge': '📅 BOOK APPOINTMENT', 'y': 1000}),
 ('badge', 22.66, 25.30, {'html': '💬 YOUR CENTRE • YOUR PLAN', 'y': 280, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 60}),
 ('text', 25.36, 27.00, {'html': '<span class="y">IMPLEMENT</span><br>THE SYSTEM ⚙️', 'y': 270, 'size': 104}),
 ('text', 32.50, 34.00, {'html': 'FIND THIS =<br><span class="g">ENOUGH ✓</span>', 'y': 270, 'size': 110}),
 ('text', 34.06, 36.45, {'html': 'NEXT PIN<br><span class="y">FAST 🚀</span>', 'y': 270, 'size': 120}),
 ('text', 36.50, 40.30, {'html': 'CENTRE →<br><span class="g">NEXT LEVEL 📈</span>', 'y': 270, 'size': 108}),
 ('flash', 40.30, 40.45, {}),
 ('cta', 40.34, 42.45, {'label': '📅 BOOK APPOINTMENT', 'badge': '👇 LINK BELOW', 'y': 1000}),
 ('endps', 42.50, 999, {}),
]
CAP = [
 (0.00, 2.95, [['கேரளாவுல', 'இருக்கிற'], ['*WELLNESS CENTRE-க்கு'], ['என்ன', '^RESULT?', 'பாருங்க']]),
 (3.20, 6.10, [['*MONTHLY', 'REGISTRATION', '^1'], ['*10 DAY', 'REGISTRATION', '^2'], ['*APPOINTMENTS', '^3']]),
 (6.14, 11.30, [['இந்த மாதிரி', '^CONSISTENT-ஆன'], ['*WALK-INS', '*APPOINTMENTS'], ['*REGISTRATIONS']]),
 (11.32, 14.00, [['^ONLINE', 'மூலமா'], ['நம்ம', '*GENERATE', 'பண்ணா', 'தான்']]),
 (14.08, 16.90, [['அடுத்தடுத்த', '^PIN LEVEL'], ['*ACHIEVE', 'பண்ண', 'முடியும்']]),
 (16.98, 19.90, [['இந்த மாதிரி', '*SYSTEM'], ['^ஒவ்வொரு', 'WELLNESS', 'CENTRE-க்கும்', 'தேவை']]),
 (19.94, 22.60, [['இப்பவே', '^கீழே', 'உள்ள', 'LINK'], ['^CLICK', 'பண்ணி'], ['*APPOINTMENT', 'BOOK', 'பண்ணிக்கோங்க']]),
 (22.66, 25.30, [['உங்க', '*WELLNESS CENTRE-க்கு'], ['^EXACTLY', 'என்ன', 'தேவை']]),
 (25.36, 27.00, [['இந்த', '*SYSTEM-ஐ', '^IMPLEMENT', 'பண்ணி']]),
 (27.08, 32.45, [['நம்ம', '*CENTRE-க்கும்', '^CONSISTENT-ஆ'], ['*NEW CLIENTS', 'ஐ'], ['^UNKNOWN CIRCLE-ல', 'இருந்து']]),
 (32.50, 34.00, [['அதை', 'கண்டுபிடிச்சாலே', '*போதும்']]),
 (34.06, 36.45, [['அடுத்தடுத்த', '^PIN LEVEL-ல'], ['*FAST-ஆ', 'ACHIEVE', 'பண்ணலாம்']]),
 (36.50, 40.30, [['இதை', '^DISCUSS', 'பண்ணி'], ['நம்ம', 'CENTRE-ஐ', '*NEXT LEVEL-க்கு']]),
 (40.34, 42.45, [['இப்பவே', '^LINK', 'CLICK', 'பண்ணி'], ['*APPOINTMENT', 'BOOK', 'பண்ணுங்க']]),
]
PUNCH = [(0.0, 3.0, 1.0), (11.32, 14.0, 1.12), (16.98, 19.9, 1.14), (19.9, 22.6, 1.10), (22.66, 25.3, 1.06), (32.5, 34.0, 1.14), (34.06, 36.45, 1.16), (40.3, 42.5, 1.12)]
MUSIC = [(0.0, 14.0, 'warm'), (14.0, 19.9, 'tech'), (19.9, 999, 'uplift')]
SFX = [(0.30, 'hit'), (11.32, 'pop'), (16.98, 'thud'), (19.50, 'riser'), (19.94, 'hit'), (40.34, 'hit')]
SCENE_SFX = {
 'checklist': [(1.0, 'pop'), (1.47, 'ding'), (2.1, 'pop'), (2.5, 'ding')],
 'walkin': [(.1, 'pop')] + [(.42 * i + 2.3, 'tick') for i in range(6)],
 'pin': [(.1, 'pop'), (.4, 'pop'), (.7, 'pop'), (1.0, 'whoosh'), (2.4, 'ding')],
 'social': [(.3, 'pop'), (.7, 'ding'), (1.2, 'tick'), (1.6, 'tick'), (2.0, 'tick'), (2.6, 'pop')],
}
