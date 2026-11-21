"""wellness-ads-result: case study, wellness centre ads (2257328278428999.mp4, 85.1 s). Times = SOURCE seconds (SRT 18199983001360017 in sync).
REAL PROOF is burned into the source and must stay visible: Ads Manager 0-14 s, May calendar 14-34 s, client WhatsApp update 35-54 s.
So: no B-roll before 54 s; the spoken numbers get on-face callouts at the top instead."""
SRC = '2257328278428999.mp4'
END, HOLD = 84.60, 1.6
BLUR = [1040, 1130]; CAPY, CAPH = 1000, 170
CTA_CAP_HI = False
NOZOOM = [(0.0, 54.0)]          # zooms would crop the proof screenshots
BROLL = [
 ('B01', 55.20, 59.60, 'booking', 'split', dict(title='ONLINE <span class="g">CALENDAR</span> 📅', head='YOUR CENTRE'), '"consistent inquiries - your own online calendar"'),
 ('B02', 59.60, 62.18, 'walkin', 'split', dict(), '"generate walk-ins consistently"'),
 ('B03', 68.60, 72.62, 'allday', 'split', dict(cues=[69.4, 70.2, 71.0]), '"an online system that works 24/7 for you"'),
]
B = lambda h, s0, s1, bg='var(--ob)', fg='#fff', size=56: ('badge', s0, s1, {'html': h, 'y': 150, 'bg': bg, 'fg': fg, 'size': size})
GFX = [
 B('📢 ADS • WELLNESS CENTRE', 0.20, 5.10, 'var(--yl)', '#000', 52),
 ('text', 5.60, 8.16, {'html': '<span class="g">39</span> ENQUIRIES', 'y': 140, 'size': 120}),
 ('text', 8.16, 12.24, {'html': '<span class="y">₹113</span> / ENQUIRY', 'y': 140, 'size': 110}),
 B('🤔 TOO HIGH?', 12.24, 13.90, 'var(--rd)', '#fff', 66),
 B('❌ NO!', 13.90, 15.96, 'var(--rd)', '#fff', 70),
 B('📅 LOOK AT HIS CALENDAR', 15.96, 18.24, 'var(--em)', '#04110c', 56),
 B('✅ QUALITY ENQUIRIES', 18.24, 21.06, 'var(--em)', '#04110c', 58),
 B('📅 MAY • FIRST 20 DAYS', 21.06, 27.00, 'var(--yl)', '#000', 58),
 B('🌿 YOUR CENTRE TOO?', 27.00, 33.00, 'var(--ob)', '#fff', 58),
 B('💬 CLIENT UPDATE', 35.26, 37.36, 'var(--wa)', '#04110c', 62),
 B('🛍️ 2 SALES AT MRP', 37.36, 43.78, 'var(--em)', '#04110c', 62),
 B('🩺 1 NEW HEALTH CHECK-UP', 43.78, 48.58, 'var(--em)', '#04110c', 56),
 B('📈 MORE ENQUIRIES & WALK-INS', 48.58, 53.80, 'var(--yl)', '#000', 52),
 ('cta', 62.18, 66.92, {'label': '📅 BOOK APPOINTMENT', 'y': 1210, 'badge': '👇 LINK BELOW'}),
 B('💬 1-ON-1 ONLINE MEETING', 72.62, 77.60, 'var(--ob)', '#fff', 54),
 B('🚀 NEXT LEVEL', 77.60, 79.46, 'var(--yl)', '#000', 70),
 ('cta', 79.46, END, {'label': '📅 BOOK NOW', 'y': 1210, 'badge': '👇 LINK BELOW'}),
 ('flash', END, END + 0.12, {}),
 ('endcard2', END, END + HOLD, {'emo': '🌿', 'l1': 'WELLNESS CENTRE', 'l2': 'ONLINE ENQUIRY SYSTEM', 'ts': 100, 'ts2': 76, 'btn': '📅 BOOK APPOINTMENT', 'l3': 'PROFITSOUL'}),
]
CAP = [
 (0.00, 2.16, [['ஒரு', '*WELLNESS', '*COACH-க்கு'], ['^பட்டுக்கோட்டை']]),
 (2.16, 5.10, [['அவரோட', 'WELLNESS', 'CENTRE-க்கு'], ['ONLINE-ல', '*ADS', 'RUN', 'பண்ணோம்']]),
 (5.10, 8.16, [['இதுதான்', '*RESULT'], ['*39', '*ENQUIRY']]),
 (8.16, 12.24, [['COST', 'PER', 'ENQUIRY'], ['^₹113']]),
 (12.24, 15.96, [['ரொம்ப', '!அதிகம்னு', 'நினைப்பீங்க'], ['BUT', 'அது', '!இல்லை']]),
 (15.96, 18.24, [['அவரோட', '*CALENDAR', 'பாருங்க']]),
 (18.24, 21.06, [['*QUALITY', 'ENQUIRY', 'வந்தா'], ['இதுதான்', 'நடக்கும்']]),
 (21.06, 23.82, [['^MAY', 'மாசம்', '^FIRST', '^20', '^DAYS'], ['இவ்வளவு', '*APPOINTMENTS']]),
 (23.82, 27.00, [['BOOK', 'பண்ணி', 'CENTRE-க்கு'], ['போயிருக்காங்க']]),
 (27.00, 30.16, [['உங்க', 'CENTRE-க்கும்'], ['ஒரு', '*ONLINE', '*CALENDAR']]),
 (30.16, 32.98, [['ONLINE', '*ENQUIRY', 'GENERATE'], ['பண்ணணும்']]),
 (32.98, 35.26, [['*WALK-INS', 'INCREASE'], ['பண்ணணும்']]),
 (35.26, 37.36, [['என்ன', 'RESULT?'], ['CLIENT', '^UPDATE', 'பண்ணிருக்காங்க']]),
 (37.36, 41.02, [['^ரெண்டு', '^CLIENT'], ['*MRP', 'PRICE-ல', 'வாங்கிருக்காங்க']]),
 (41.02, 43.78, [['LAST', 'ONE', 'WEEK-ல'], ['ஒரு', '*NEW', 'CLIENT']]),
 (43.78, 45.66, [['*HEALTH', '*CHECK-UP', 'பண்ணிருக்காரு']]),
 (45.66, 48.58, [['நாளைக்கு', '^CONTINUE'], ['பண்ணப்', 'போறாரு']]),
 (48.58, 51.52, [['இன்னும்', 'நிறைய', '*ENQUIRIES'], ['*WALK-INS', 'வந்துட்டே', 'இருக்கு']]),
 (51.52, 53.80, [['அவரே', '^WHATSAPP', 'GROUP-ல'], ['UPDATE', 'பண்ணிருக்காரு']]),
 (53.80, 57.16, [['உங்க', 'WELLNESS', 'CENTRE-க்கும்'], ['*CONSISTENT', 'ENQUIRIES']]),
 (57.16, 59.60, [['வேணுமா?', 'உங்களுக்குன்னு'], ['ஒரு', '*ONLINE', '*CALENDAR']]),
 (59.60, 62.18, [['*WALK-INS', 'CONSISTENT-ஆ'], ['GENERATE', 'பண்ணணுமா?']]),
 (62.18, 64.34, [['இப்பவே', '^கீழே', 'இருக்கிற'], ['^LINK-ஐ', 'CLICK', 'பண்ணி']]),
 (64.34, 66.92, [['ஒரு', '*APPOINTMENT'], ['BOOK', 'பண்ணிக்கோங்க']]),
 (66.92, 69.80, [['என்ன', 'INVESTMENT-ல'], ['இந்த', '*ONLINE', '*SYSTEM']]),
 (69.80, 72.62, [['உங்களுக்காக', '^24/7'], ['WORK', 'ஆகும்']]),
 (72.62, 75.14, [['*DETAILED-ஆ', 'EXPLAIN'], ['பண்றேன்']]),
 (75.14, 77.60, [['ONLINE', '*MEETING-ல'], ['உங்களை', 'MEET', 'பண்ணி']]),
 (77.60, 79.46, [['*NEXT', '*LEVEL-க்கு'], ['எப்படி', 'எடுத்துட்டு', 'போறது']]),
 (79.46, 81.44, [['DETAILED-ஆ', 'DISCUSS'], ['பண்ணுவோம்']]),
 (81.44, END, [['SEE', 'YOU', 'IN', 'THE', 'MOST'], ['*IMPORTANT', '*APPOINTMENT']]),
]
PUNCH = [(5.6, 8.2, 1.10), (8.2, 12.2, 1.14), (12.2, 15.9, 1.08), (62.2, 66.9, 1.06), (72.6, 77.6, 1.08), (77.6, 79.5, 1.14), (79.5, 84.6, 1.08)]
MUSIC = [(0.0, 15.96, 'pulse'), (15.96, 53.8, 'warm'), (53.8, 62.2, 'tech'), (62.2, END + HOLD, 'uplift')]
SFX = [(0.20, 'hit'), (5.60, 'cash'), (8.16, 'cash'), (12.24, 'thud'), (13.90, 'thud'), (15.96, 'swipe'), (21.06, 'ding'), (35.26, 'ding'), (37.36, 'cash'), (61.70, 'riser'), (77.60, 'hit')]
