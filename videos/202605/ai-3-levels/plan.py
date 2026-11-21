"""ai-3-levels: "AI has only 3 levels" (970146912533185.mp4, 68.1 s). Times = SOURCE seconds (SRT 18321070603257751 is in sync)."""
SRC = '970146912533185.mp4'
END, HOLD = 67.50, 1.6
BLUR = [1255, 1350]; CAPY, CAPH = 1215, 180     # cover the burned-in caption strip
# (id, s0, s1, scene, layout, extras, keyword spoken)
BROLL = [
 ('B01', 2.60, 5.00, 'levels', 'split', dict(lv=1, cues=[2.75, 2.95, 3.15]), '"Level one, chatting"'),
 ('B02', 5.00, 9.20, 'aichat', 'split', dict(), '"ChatGPT, Claude, Perplexity - you chat with these?"'),
 ('B03', 12.90, 24.96, 'autoflow', 'split', dict(cues=[13.60, 15.80, 20.30, 23.20], wc=16.90), '"enquiry -> AI agent welcome message -> answers questions -> qualified appointment"'),
 ('B04', 31.00, 42.20, 'agentmail', 'split', dict(ty=5.5, mc=36.60), '"go to my mailbox, analyse yesterday\'s mails, draft replies to clients"'),
 ('B05', 46.12, 49.50, 'levels', 'split', dict(cues=[46.40, 46.90, 47.40]), '"AI evolved in 3 different levels"'),
 ('B06', 55.06, 58.06, 'levels', 'split', dict(title='நீங்க எந்த <span class="y">LEVEL?</span>', cues=[55.2, 55.5, 55.8]), '"which level are we at?"'),
]
GFX = [
 ('badge', 0.56, 2.60, {'html': '🤖 AI = 3 LEVELS', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 66}),
 ('badge', 9.70, 12.80, {'html': '⚙️ LEVEL 2 ?', 'y': 230, 'size': 70}),
 ('badge', 25.10, 28.90, {'html': '✅ LEVEL 2 = AUTOMATION', 'y': 230, 'bg': 'var(--em)', 'fg': '#04110c', 'size': 58}),
 ('badge', 28.90, 31.00, {'html': '🤖 LEVEL 3', 'y': 230, 'bg': 'var(--yl)', 'fg': '#000', 'size': 70}),
 ('text', 43.30, 46.10, {'html': 'AI = YOUR<br><span class="g">EMPLOYEE</span> 🧑‍💼', 'y': 200, 'size': 100}),
 ('badge', 51.70, 55.00, {'html': '📈 CLAUDE PEAK', 'y': 230, 'size': 66}),
 ('text', 61.04, 64.70, {'html': 'NOBODY CAN<br><span class="y">STOP</span> YOU 🚀', 'y': 200, 'size': 104}),
 ('text', 64.70, END, {'html': '⏰ <span class="r">WAKE-UP</span><br>CALL', 'y': 200, 'size': 120}),
 ('flash', END, END + 0.12, {}),
 ('endcard2', END, END + HOLD, {'emo': '🤖', 'l1': 'AI FOR BUSINESS', 'l2': 'WHICH LEVEL ARE YOU?', 'btn': '➕ FOLLOW FOR MORE', 'l3': 'PROFITSOUL'}),
]
CAP = [
 (0.56, 2.70, [['மொத்தம்', '*மூணே', '*LEVEL', 'தான்'], ['LEARN', 'பண்ணலாமா?']]),
 (2.70, 5.00, [['^LEVEL 1'], ['*CHATTING']]),
 (5.00, 7.30, [['CHATGPT,', 'CLAUDE,'], ['PERPLEXITY']]),
 (7.30, 9.66, [['நிறைய', 'AI-கிட்ட', '*CHAT', 'பண்றீங்களா?'], ['இதுதான்', '^LEVEL 1']]),
 (9.66, 11.50, [['^LEVEL 2', 'என்ன', 'தெரியுமா?']]),
 (11.50, 12.72, [['*AUTOMATION']]),
 (12.72, 14.64, [['CLIENT-கிட்ட', 'ஒரு', '*ENQUIRY']]),
 (14.64, 17.64, [['ஒரு', '*AI AGENT', 'மூலமா'], ['*WELCOME', 'MESSAGE']]),
 (17.64, 20.16, [['உங்க', 'CLIENT'], ['நிறைய', '^கேள்வி', 'கேட்பாங்க']]),
 (20.16, 22.38, [['அதுவே', '*பதில்', 'சொல்லி']]),
 (22.38, 24.96, [['*QUALIFIED', '*APPOINTMENT'], ['BOOK', 'பண்ண', 'வைக்குது']]),
 (24.96, 28.40, [['இதுதான்', '^LEVEL 2'], ['*AUTOMATION']]),
 (28.40, 32.68, [['^LEVEL 3-ல'], ['ஒரு', '*INSTRUCTION', 'மட்டும்']]),
 (32.68, 35.14, [['"என்', '*MAILBOX-க்கு', 'போ'], ['நேத்து', 'MAIL']]),
 (35.14, 38.74, [['எல்லாத்தையும்', '*ANALYSE'], ['பண்ணு"']]),
 (38.74, 41.14, [['*REPLY', 'MESSAGE'], ['*DRAFT', 'பண்ணு"']]),
 (41.14, 43.30, [['ஒரு', '*COMMAND', 'மட்டும்', 'போதும்']]),
 (43.30, 46.12, [['ஒரு', '*EMPLOYEE', 'மாதிரி'], ['AI', 'WORK', 'பண்ணும்']]),
 (46.12, 49.54, [['^மூணு', '^LEVELS-ல'], ['AI', '*EVOLVE', 'ஆயிருக்கு']]),
 (49.54, 51.70, [['*CLAUDE', 'USE', 'பண்ணி'], ['நிறைய', 'AGENCY', 'WORK']]),
 (51.70, 55.06, [['அதனால', 'தான்'], ['*CLAUDE', 'இப்போ', '^PEAK']]),
 (55.06, 58.06, [['நம்ம', 'எந்த', '^LEVEL-ல'], ['இருக்கோம்?']]),
 (58.06, 61.04, [['BUSINESS-க்குள்ள', 'கொண்டு', 'வாங்க'], ['*DEEP-ஆ', 'THINK', 'பண்ணுங்க']]),
 (61.04, 64.70, [['*AI', 'ADOPT', 'பண்றவங்க'], ['GROWTH-ஐ', '!யாராலயும்'], ['தடுக்க', 'முடியாது']]),
 (64.70, END, [['IT', 'IS', 'A'], ['!WAKE-UP', '!CALL']]),
]
PUNCH = [(0.5, 2.6, 1.12), (9.7, 12.8, 1.14), (25.1, 28.9, 1.10), (43.3, 46.1, 1.15), (61.0, 64.7, 1.10), (64.7, 67.5, 1.18)]
MUSIC = [(0.0, 12.7, 'pulse'), (12.7, 46.1, 'tech'), (46.1, END + HOLD, 'uplift')]
SFX = [(0.56, 'hit'), (9.70, 'thud'), (25.10, 'ding'), (28.90, 'hit'), (43.30, 'thud'), (61.04, 'riser'), (64.70, 'hit')]
