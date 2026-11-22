"""Become an AI SaaS marketing agency (17916567354301224.mp4, 68.0 s). SRT 18098033044964571. Banners top+bottom; source already has music: no BGM added.
CTA lines (43-46 s, 65-68 s): no B-roll, button only."""
from kit import *
SRC = '17916567354301224.mp4'; END, HOLD = 67.90, 1.5
CY, ALTZ, CROP_Y0 = 960, 1.04, 330
BROLL = [
 ('B01', 12.5, 21.8, 'reasons', 'split', dict(title='YOUR CLIENT ALREADY PAYS FOR', items=[['🎥', 'ZOOM'], ['📚', 'LMS'], ['💬', 'WHATSAPP AUTOMATION']], cues=[12.6, 14.6, 16.7]), '"client pays for Zoom, LMS, WhatsApp automation"'),
 ('B02', 26.0, 34.8, 'reframe', 'split', dict(title='TRANSFORM', A=['📢', 'MARKETING AGENCY'], B=['🤖', 'AI SAAS AGENCY'], al='ONLY', bl='+ SAAS SERVICES ✓', xc=29.5, bc=31.0), '"add SaaS services, become an AI SaaS marketing agency"'),
 ('B03', 48.9, 54.2, 'autoflow', 'split', dict(title='PERSONALISED <span class="y">ROAD MAP</span>', N=[['📞', '1:1 CALL'], ['🗺️', 'ROAD MAP'], ['🤖', 'AI SAAS<br>AGENCY'], ['🔁', 'RECURRING<br>CLIENTS']], cues=[49.0, 50.0, 51.5, 52.8], wm=''), '"personalised road map to convert your agency"'),
]
GFX = [badge(0.3, 3.0, '🤔 GETTING CLIENTS IS EASY?', y=495), slam(5.5, 10.0, 'KEEPING THEM<br><span class="r">IS THE CHALLENGE</span>', 84, 480),
 gb(37.0, 41.4, '✅ MENTEES ARE CLOSING DEALS', y=495), cta(43.1, 46.2, '📅 BOOK APPOINTMENT', '👇 LINK BELOW', y=880),
 yb(57.4, 59.2, '⚠️ SERIOUS FREELANCERS ONLY', y=495), cta(65.0, END, '📅 BOOK NOW', '👇 LINK BELOW', y=880)] + end(END, HOLD, '🤖', 'AI SAAS AGENCY', 'RECURRING CLIENTS', '📅 BOOK APPOINTMENT')
PUNCH = [(5.5, 10.0, 1.05)]
MUSIC = []
SFX = [(0.3, 'hit'), (5.5, 'thud'), (37.0, 'ding'), (42.7, 'riser'), (64.6, 'riser')]
