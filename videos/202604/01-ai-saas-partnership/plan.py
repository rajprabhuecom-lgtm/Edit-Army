"""AI SaaS partnership program for marketing agencies (17916820782141642.mp4, 67.3 s). Banners top+bottom. CTA lines: button only."""
from kit import *
SRC = '17916820782141642.mp4'; END, HOLD = 67.10, 1.5
CY, ALTZ, CROP_Y0 = 960, 1.04, 330
BROLL = [
 ('B01', 4.8, 14.8, 'reframe', 'split', dict(title='STOP SELLING', A=['🧾', 'ONE-TIME SERVICE'], B=['🔁', 'MONTHLY SUBSCRIPTION'], al='❌', bl='LIKE CLAUDE • GPT • GEMINI', xc=7.0, bc=9.6), '"not one-time service - monthly subscriptions like Claude, ChatGPT, Gemini"'),
 ('B02', 14.8, 21.5, 'growth', 'split', dict(title='BUILD YOUR OWN <span class="g">AI TOOLS</span>', chip='🤖 AUTOMATE MARKETING TASKS'), '"automate marketing tasks, create your own tools"'),
 ('B03', 29.9, 39.8, 'autoflow', 'split', dict(title='I DO IT <span class="y">WITH YOU</span>', N=[['📢', 'EXACT ADS'], ['🧲', 'FILTER<br>LEADS'], ['📞', 'SALES<br>CALL'], ['🤝', 'FIRST<br>CLIENT']], cues=[30.2, 32.4, 35.6, 37.6], wm='🎯 DONE WITH YOU'), '"create ads, filter leads, close your sales call and first client"'),
]
GFX = [badge(0.3, 4.8, '🤖 AI SAAS MARKETING AGENCY', y=495), slam(21.5, 27.7, 'HOW TO GET THE<br><span class="y">FIRST CLIENT?</span> 🤔', 86, 480),
 cta(27.7, 29.9, '📅 BOOK APPOINTMENT', '👇 LINK BELOW', y=880), gb(39.8, 42.2, '🤝 PERSONAL PARTNERSHIP PROGRAM', 46, 495),
 stat(42.2, 45.8, 2, 'AGENCIES PER MONTH ONLY', y=480, size=170, col='var(--rd)'), slam(45.8, 51.0, 'NEXT LEVEL<br><span class="g">AGENCY</span> 🚀', 100, 480),
 cta(51.0, 53.4, '📅 BOOK APPOINTMENT', '👇 LINK BELOW', y=880), yb(53.4, 56.2, '⚠️ SERIOUS AGENCIES ONLY', y=495),
 slam(56.2, 62.3, '₹2–5 LAKH<br><span class="g">RECURRING / MONTH</span>', 84, 480), cta(63.8, END, '📅 BOOK NOW', '👇 LINK BELOW', y=880)] + end(END, HOLD, '🤝', 'PARTNERSHIP', 'AI SAAS AGENCY', '📅 BOOK APPOINTMENT')
PUNCH = [(21.5, 27.7, 1.05), (45.8, 51.0, 1.06), (56.2, 62.3, 1.05)]
MUSIC = [(0, 21.5, 'pulse'), (21.5, 51.0, 'tech'), (51.0, END + HOLD, 'uplift')]
SFX = [(0.3, 'hit'), (21.5, 'thud'), (42.2, 'hit'), (56.2, 'cash')]
