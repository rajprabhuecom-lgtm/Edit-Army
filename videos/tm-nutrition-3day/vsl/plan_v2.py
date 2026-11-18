"""TM Nutrition VSL v2: coach-only cut (face-tracked), full-frame face with alternating punch-ins, Google Flow B-roll slots.
Inputs : /home/user/w/vsl2/{takes.json, src48.wav, broll/}  (SELECTS=selects_v2 WD=/home/user/w/vsl2/ build_src.py)
Flow clips: drop each generated clip into /home/user/w/vsl2/broll/F01.mp4 ... and re-run (missing clips fall back to the animated scene).
Outputs: gfx/timeline.json, frames.json, audio/cues.json, comp_cfg.json, broll_plan_v2.csv, flow_shotlist.md (timecodes)."""
import json, re, subprocess, os, csv
HERE = os.path.dirname(os.path.abspath(__file__)); W = '/home/user/w/vsl2/'; FPS = 30
TAKES = json.load(open(W + 'takes.json')); TK = {t['id']: t for t in TAKES}

# ---------- 1. jump cuts: coach speaking (mouth) AND voice present ----------
def islands(a, b, noise=-34, d=0.20):
    log = subprocess.run(['ffmpeg', '-nostdin', '-ss', f'{a}', '-t', f'{b - a}', '-i', W + 'src48.wav', '-af', f'silencedetect=noise={noise}dB:d={d}', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ss = [float(x) + a for x in re.findall(r'silence_start: (-?[\d.]+)', log)]; se = [float(x) + a for x in re.findall(r'silence_end: ([\d.]+)', log)]
    se += [b] * (len(ss) - len(se)); out = []; t = a
    for s, e in zip(ss, se):
        if s - t > 0.06: out.append([t, s])
        t = e
    if b - t > 0.06: out.append([t, b])
    return out
def inter(A, B):
    out = []
    for a0, a1 in A:
        for b0, b1 in B:
            s, e = max(a0, b0), min(a1, b1)
            if e - s > 0.08: out.append([s, e])
    return out
PRE, POST, MERGE = 0.06, 0.12, 0.14
pieces = []
for t in TAKES:
    if t['kind'] == 'bite': pieces.append(dict(k='bite', id=t['id'], dur=t['dur'], clip=t['clip'])); continue
    a = t['off']; b = a + t['dur']
    coach = [[a + x, a + y] for x, y in (t.get('client') or [[0, t['dur']]])]
    keep = inter(islands(a, b), coach); segs = []
    for s, e in keep:
        s, e = max(a, s - PRE), min(b, e + POST)
        if segs and s - segs[-1][1] < MERGE: segs[-1][1] = e
        else: segs.append([s, e])
    for s, e in (segs or [[a, b]]): pieces.append(dict(k='seg', id=t['id'], s0=s, s1=e))
o = 0.0
for p in pieces: p['o0'] = o; o += (p['s1'] - p['s0']) if p['k'] == 'seg' else p['dur']; p['o1'] = o
TAIL = 3.2; TOTAL = o + TAIL
def s2o(ts):
    for p in pieces:
        if p['k'] != 'seg': continue
        if ts < p['s0']: return p['o0']
        if ts <= p['s1']: return p['o0'] + ts - p['s0']
    return o
def O(tid, rel=0.0): return s2o(TK[tid]['off'] + rel) if TK[tid]['kind'] == 'take' else [p for p in pieces if p['id'] == tid][0]['o0'] + rel
def span(a_id, b_id=None):
    b_id = b_id or a_id
    return min(p['o0'] for p in pieces if p['id'] == a_id), max(p['o1'] for p in pieces if p['id'] == b_id)

# ---------- 2. Google Flow slots (fallback = animated scene until the clip exists) ----------
# (id, start, end, layout when the clip exists, fallback (scene, layout, extra) or None, spoken line, Flow prompt)
STYLE = ('Photorealistic cinematic footage, 16:9, natural warm light, shallow depth of field, 35mm lens, slow subtle camera movement, '
         'South Indian Tamil middle-class family in a modern Trichy home, realistic skin, no text, no logos, no subtitles, no one looking at the camera, no talking to camera.')
FLOW = []
def F(fid, a, b, lay, fb, line, prompt): FLOW.append((fid, a, b, lay, fb, line, prompt))
a, b = span('V01'); F('F01', a + 1.6, b, 'side', ('tally', 'side', {}), 'உங்க வீட்டுல ரெண்டு பேரும் weight குறைக்கணும்னு எத்தனை தடவை...',
  'A Tamil husband and wife in their late 30s in their bedroom in the morning. The husband steps onto a bathroom weighing scale, looks down, sighs; the wife stands beside him holding a printed diet chart, shakes her head with a tired smile. Medium shot, slow push-in.')
a, b = span('V04'); F('F02', a + .3, b, 'side', None, '18 வருஷமா நூற்றுக்கணக்கான families...',
  'USE REAL FOOTAGE, NOT FLOW: TM Nutrition Centre Trichy signboard, interior, Coach Pradheesh with real client families and group photos from past programmes.')
a, b = span('V05'); F('F03', a + .2, b, 'side', None, 'இப்போ புது batch, couples-க்கு மட்டும்',
  'A smiling Tamil couple in their 30s sitting close together on a sofa in a bright living room, the wife shows the husband something on her phone, he nods and they high-five. Medium shot, gentle dolly in.')
a, b = span('V06'); F('F04', a, b, 'full', ('pain', 'side', dict(v='diet', cues=[1.0])), 'மூணு நாள் diet... அப்புறம் biryani',
  'Close-up on a dining table: a bowl of plain salad is pushed aside and a steaming plate of chicken biryani is placed down; a Tamil couple happily digs in with their hands. Overhead to 45-degree angle, steam rising, warm tungsten light.')
a, b = span('V07'); F('F05', a, b, 'full', ('pain', 'side', dict(v='gym', cues=[1.4])), 'Gym membership கட்டி, ரெண்டு வாரம் கூட போறது இல்ல',
  'A new gym bag with a membership card on top sits untouched by the front door of an Indian apartment, gathering dust; time-lapse feel, morning light changes; a man walks past it in office clothes without looking. Static wide shot.')
a, b = span('V08'); F('F06', a, b, 'full', ('pain', 'side', dict(v='midnight', cues=[1.2])), 'ராத்திரி 12 மணி வரைக்கும் கையில mobile',
  'Night, dark bedroom: a Tamil husband and wife lie in bed side by side, both faces lit blue by their phone screens, scrolling silently; a wall clock above shows midnight. Slow push-in, moody low light.')
a, b = span('V09'); F('F07', a, b, 'side', ('pain', 'side', dict(v='tomorrow', cues=[1.6])), '"நாளைக்கு ஆரம்பிச்சுக்கலாம்"',
  'A Tamil couple on a sofa with a bowl of fried snacks; the wife points at a wall calendar, the husband waves his hand casually as if saying "tomorrow", both laugh and keep eating. Medium shot, warm evening light.')
a, b = span('V10'); F('F08', a, b, 'full', ('pattern', 'full', dict(cues=[1.0, 2.0])), 'Problem will power-ல இல்ல, வீட்டோட pattern-ல',
  'Top-down slow dolly over an Indian family dinner table at night: father, mother and two children each looking at their own phone, TV glowing in the background, fried snacks and soft drinks on the table, nobody talking.')
a, b = span('V15'); F('F09', O('V15', 0.2), b, 'side', None, 'ஆனா அந்த மாற்றம் ஆரம்பிச்சது வெறும் மூணே நாள்ல',
  'Sunrise in a Trichy home: a Tamil couple opens the balcony curtains together, morning light floods in, they stretch, drink a glass of water each and smile at each other. Slow push-in, golden light.')
a, b = span('V20', 'V21'); F('F10', a, b, 'side', ('habits', 'side', dict(cues=[0.1, O('V21') - a, O('V22') - a])), 'mobile-ஐ continuous-ஆ பாக்காம, habit pattern tune',
  'A Tamil husband places his phone face-down on a table and slides it away; he and his wife put on walking shoes and step out of the front door into the morning. Medium shot, handheld feel.')
a, b = span('V22'); F('F11', a, b, 'side', None, 'hand-hold guidance-ல சொல்லித்தர மாதிரி',
  'Over-the-shoulder shot of a Tamil couple at home watching a live online wellness class on a laptop (video-call grid of many participants, faces blurred), the wife takes notes in a notebook, the husband nods. No readable text on screen.')
a, b = span('V23'); F('F12', a + 1.2, b, 'side', ('famhealth', 'side', dict(cues=[0.2, 2.6])), 'உங்க மொத்த family-யும் healthy-ஆ',
  'A Tamil family (husband, wife, two school-age kids and a grandmother) cooking a colourful healthy breakfast together in a bright kitchen - cutting fruits, sprouts and vegetables, kids helping, everyone smiling. Medium wide, slow dolly.')
a, b = span('V25', 'V26'); F('F13', a, O('V26'), 'side', ('happy', 'side', dict(cues=[1.8, O('V26') - a])), 'அந்த happiness உங்க வீட்டுக்குள்ள வரணும்னா... என்ன routine',
  'Evening in a Tamil home: the whole family plays carrom on the living-room floor, laughing loudly, the grandmother claps; warm lamp light, the kids hug their parents. Medium shot, slow push-in.')
a, b = span('V26'); F('F15', a, b, 'side', None, 'எப்படி அந்த happiness-ஐ வீட்டுக்குள்ள கொண்டு வரணும்',
  'Golden-hour on a house terrace in Trichy: a Tamil couple, their two kids and the grandparents share tea and snacks, the kids hug their father, everyone laughing together. Wide to medium shot, slow dolly sideways.')
a, b = span('V27'); F('F14', a + .3, b, 'side', ('money', 'side', dict(cues=[0.8, 2.6])), 'financial independence-க்கான first step',
  'A Tamil couple at the dining table at night with a notebook, a calculator and a glass jar of coins; the wife writes a monthly plan, the husband drops a coin into the jar and they smile. Close-up to medium, warm light.')

# testimonials (real) + proof bites
TCLIP = {'V11': ('T_vid_0606.mp4', 0.3), 'V12': ('T_vid_0608.mp4', 11.5), 'V13': ('T_vid_0610.mp4', 0.0)}
BROLL = []
for tid, nm, res in [('V11', 'RAVEENDRAN • 58', None), ('V12', 'SIVAKARTHIK • 32 • ERODE', '<span class="y">26 KG</span><br>EXCESS WEIGHT'), ('V13', 'KRISHNA PRIYA • 48', None)]:
    a, b = span(tid); BROLL.append(('T' + tid[1:], a, b, 'testi', 'tside', dict(clip=TCLIP[tid], name=nm, res=res, x=40, y=40, rx=60, ry=760, rt=1.2), 'client named on camera', 'P2 real testimonial'))
a, b = span('V14'); BROLL.append(('T14', a, b, 'vid', 'tside', dict(clip=('T_vid_0613.mp4', 34.0), chips=[['🤔 "இது எனக்கு WORK ஆகாது"', 'var(--ob)', '#fff', 'var(--rd)']], ct=[0.3], cy=60), 'everyone thought it would not work', 'P2 real testimonial'))
# T14b audio (Joseph: "my family and I are healthy and happy") originally showed a handshake at the centre; use his solo shot instead
BITE_VIS = {'T14b': ('T_vid_0615.mp4', 4.2)}
BITE_NAMES = {'T11': 'RAVEENDRAN • 58 • TRICHY', 'T12': 'SIVAKARTHIK • 32 • ERODE', 'T13': 'KRISHNA PRIYA • 48', 'T13b': 'KRISHNA PRIYA • 48',
              'T14': 'JOSEPH RAJ • 62', 'T14b': 'JOSEPH RAJ • 62', 'B01': 'SIVAKARTHIK • ERODE', 'B02': 'KRISHNA PRIYA • 48'}
for bid, nm in [(t['id'], BITE_NAMES.get(t['id'], 'REAL CLIENT')) for t in TAKES if t['kind'] == 'bite']:
    a, b = span(bid); BROLL.append(('P' + bid[1:], a, b, 'testi', 'full', dict(clip=(TK[bid]['clip'], 0.0), name=nm, x=60, y=60, note='Individual results vary'), 'client proof bite (own audio)', 'P2 real testimonial'))
a, b = span('V18'); BROLL.append(('G01', a, b, 'q3days', 'full', dict(cues=[0.0, 0.2, 0.5]), 'Yes - change can start in 3 days', 'P5 motion graphics'))
a, b = span('V19'); BROLL.append(('G02', a, b + .4, 'agenda', 'full', dict(focus=0, cues=[0, .08, .16, .24]), 'Day 1: Habits', 'P5 motion graphics'))
a, _ = span('V23'); BROLL.append(('G03', a, a + 1.2, 'agenda', 'full', dict(focus=1, cues=[0, .06, .12, .18], title='<span class="y">DAY 2</span> • FAMILY HEALTH'), 'Day 2 (title card)', 'P5 motion graphics'))
a, b = span('V24'); BROLL.append(('G04', a, b, 'agenda', 'full', dict(focus=2, cues=[0, .08, .16, .24], title='<span class="y">DAY 3</span> • ரொம்ப IMPORTANT ★'), 'Day 3 very important: family happiness', 'P5 motion graphics'))
for fid, a0, b0, lay, fb, line, prompt in FLOW:
    if os.path.exists(W + f'broll/{fid}.mp4'):
        BROLL.append((fid, a0, b0, 'vid', lay, dict(clip=(f'{fid}.mp4', 0.3)), line, 'P3 AI (Google Flow) - disclose in Meta'))
    elif fb:
        BROLL.append((fid + '*', a0, b0, fb[0], fb[1], fb[2], line, 'P5 motion graphics (placeholder until Flow clip)'))

GFX = []
def G(ty, o0, o1, **ex): GFX.append((ty, o0, o1, ex))
a, b = span('V02'); G('badge', a + .2, b, html='▶ முழுசா பாருங்க', x=60, w=760, y=140, bg='var(--yl)', fg='#000', size=54)
a, b = span('V03'); G('lower', a + .3, b + 1.0, name='COACH PRADHEESH MUTHARASU', title='TM NUTRITION CENTRE • TRICHY', x=80, y=700)
if not os.path.exists(W + 'broll/F02.mp4'): a, b = span('V04'); G('text', a + .2, b, html='<span class="y">18 YEARS</span><br>100s OF FAMILIES', x=40, w=800, y=170, size=96)
if not os.path.exists(W + 'broll/F03.mp4'): a, b = span('V05'); G('badge', a + .2, b, html='👫 NEW BATCH • COUPLES ONLY', x=40, w=820, y=180, bg='var(--em)', fg='#04110c', size=52)
if not os.path.exists(W + 'broll/F09.mp4'): G('text', O('V15', 2.6), span('V15')[1], html='வெறும்<br><span class="g">3 நாள்ல</span>', x=40, w=800, y=170, size=120, nocap=True)
a, b = span('V16', 'V17'); G('badge', a + .1, b, html='🤔 3 நாள்ல CHANGE? அது எப்படி?', x=40, w=840, y=180, size=50, bg='var(--rd)')
a, b = span('V28'); G('price', O('V28', 1.9), b + .3, value=555, pre='JUST', sub='3 DAYS + BONUS', x=90, y=170)
a, b = span('V29', 'V30'); G('stamp', a + .3, b, x=110, y=170, sub='3 நாள் LIVE • VALUE இல்லைன்னா', badge='🛡️ RISK முழுசா என் பக்கம்', bt=O('V30') - a - .3)
a, b = span('V31', 'V32'); G('badge', a + .2, b, html='🔥 ONLY 5 COUPLES • TRICHY', x=40, w=840, y=150, size=56)
a, b = span('V32'); G('text', a + .2, b, html='நானே <span class="y">PERSONAL-ஆ</span><br>TRAIN', x=40, w=840, y=300, size=78, nocap=True)
a, b = span('V33'); G('flash', a - .05, a + .1); G('cta', a + .15, b + .2, label='👇 START YOUR FAMILY JOURNEY', badge='₹555 • 100% MONEY BACK', x=0, w=1000, y=520)
G('endcard', o, TOTAL, price=555, btn='BOOK NOW', seats='ONLY 5 COUPLES • THIS BATCH', loc='TM NUTRITION CENTRE • COACH PRADHEESH MUTHARASU • TRICHY')

# ---------- 3. captions ----------
CAP = {
 'V01': [['உங்க', 'வீட்டுல'], ['^ரெண்டு பேரும்'], ['*WEIGHT', 'குறைக்கணும்னு'], ['!எத்தனை தடவை'], ['முடிவு', 'பண்ணியிருப்பீங்க?']],
 'V02': [['இந்த', 'VIDEO-வ', '^முழுசா', 'பாருங்க'], ['உங்க', '*FAMILY-க்கான', '*ANSWER'], ['இந்த', 'VIDEO-ல', 'இருக்கு']],
 'V03': [['HI,', 'நான்', '*COACH PRADHEESH'], ['^TM NUTRITION', 'CENTRE,', 'TRICHY']],
 'V04': [['^18 வருஷமா'], ['நூற்றுக்கணக்கான', '*FAMILIES'], ['*HEALTHY-ஆ', 'மாத்தியிருக்கோம்']],
 'V05': [['இப்போ', '^புது BATCH'], ['*COUPLES-க்கு', 'மட்டும்']],
 'V06': [['மூணு நாள்', '*DIET...'], ['அப்புறம்', '!BIRYANI']],
 'V07': [['GYM', 'MEMBERSHIP', 'கட்டி'], ['முழுசா', '!ரெண்டு வாரம்'], ['கூட', 'போறது இல்ல']],
 'V08': [['ராத்திரி', '^12 மணி', 'வரைக்கும்'], ['கையில', '!MOBILE']],
 'V09': [['^"நாளைக்கு', 'ஆரம்பிச்சுக்கலாம்"'], ['ரெண்டு பேரும்'], ['சமாதானப்படுத்திப்பீங்க']],
 'V10': [['PROBLEM', '!WILL POWER-ல', 'இல்ல'], ['உங்க', '*வீட்டோட PATTERN-ல'], ['இருக்கு']],
 'V11': [['இவரு', '^58 வயசு']],
 'V12': [['இவரு', 'ERODE-லருந்து'], ['^32 வயசு'], ['!26 KG', 'EXCESS WEIGHT']],
 'V13': [['இவங்க', '^48 வயசு']],
 'V14': [['எல்லாருமே'], ['!"இது எனக்கு', '!WORK ஆகாது"'], ['னு நினைச்சாங்க']],
 'V15': [['ஆனா', 'அந்த', '*மாற்றம்'], ['ஆரம்பிச்சது'], ['வெறும்', '*மூணே நாள்ல']],
 'B01': [['இங்க', '*DAY 1', 'வந்து'], ['எனக்கு', 'நெஞ்செரிச்சல்'], ['^குறைய', 'ஆரம்பிச்சது']],
 'T11': [['^HbA1c', 'LEVEL', '!9.6'], ['இருந்தது'], ['தொடர்ந்து', '^4 மாசம்', 'FOLLOW', 'பண்ணதுல'], ['*5.4-ஆ', 'குறைஞ்சிருச்சு'], ['என்னுடைய', '!12 KG', 'EXCESS WEIGHT'], ['குறைச்சு', '*IDEAL WEIGHT', 'REACH', 'ஆயிட்டேன்']],
 'T12': [['^ஆறு மாசத்துல'], ['*26 KG', 'குறைச்சு'], ['இப்போ', '*IDEAL WEIGHT-ல'], ['FIT-ஆ,', '*HAPPY-ஆ', 'இருக்கேன்']],
 'T13': [['!SUGAR,', '!PRESSURE'], ['BORDER-ல', 'இருந்தது'], ['!OVER WEIGHT-ல', 'இருந்தேன்']],
 'T13b': [['THYROID,', 'SUGAR,', 'PRESSURE'], ['எல்லாம்', '*CONTROL-க்கு', 'வந்தது']],
 'T14': [['வணக்கம்,', 'என் பெயர்'], ['^ஜோசப் ராஜ்'], ['வயசு', '^62', 'ஆகுது']],
 'T14b': [['இப்ப', 'நானும்', 'என்', '*FAMILY-யும்'], ['*HEALTHY-ஆ,', '*HAPPY-ஆ', 'இருக்கோம்']],
 'B02': [['ரொம்ப', '*ACTIVE-ஆ,', '*FRESH-ஆ'], ['FEEL', 'பண்ண', 'ஆரம்பிச்சேன்']],
 'V16': [['^மூணு நாள்ல', 'எல்லாம்'], ['CHANGE', 'ஆயிடுமா?']],
 'V17': [['!அது எப்படி?']],
 'V18': [['*YES.', 'CHANGE', 'START'], ['ஆகுறது', '*POSSIBLE']],
 'V19': [['^DAY 1:', '*HABITS']],
 'V20': [['நீங்க', 'உங்க', '!MOBILE-ஐ'], ['CONTINUOUS-ஆ'], ['பாத்துக்கிட்டு', 'இல்லாம']],
 'V21': [['உங்களோட', '*HABIT PATTERN-ஐ'], ['எப்படி', '^TUNE', 'பண்றது']],
 'V22': [['*HAND-HOLD', '*GUIDANCE-ல'], ['சொல்லித்தர', 'மாதிரி'], ['^DAY 1', 'இருக்கப்போகுது']],
 'V23': [['உங்க', 'HEALTH'], ['^உங்களுக்கு மட்டும்', 'இல்லாம'], ['உங்க', '*மொத்த FAMILY-யும்'], ['எப்படி', '*HEALTHY-ஆ', 'இருக்கலாம்ங்கிறத'], ['நாங்க', 'சொல்லித்தரப்போறோம்']],
 'V24': [['^DAY 3,', 'இது', 'ரொம்ப', '!IMPORTANT'], ['*FAMILY HAPPINESS']],
 'V25': [['அந்த', '*HAPPINESS'], ['உங்க', 'வீட்டுக்குள்ள', 'வரணும்னா'], ['நீங்களும்', 'உங்க', 'FAMILY-யும்'], ['என்ன', '^ROUTINE', 'FOLLOW', 'பண்ணணும்']],
 'V26': [['எப்படி', 'அந்த', '*HAPPINESS-ஐ'], ['வீட்டுக்குள்ள', 'கொண்டு', 'வரணும்'], ['சொல்லித்தரப்போறோம்']],
 'V27': [['இதோட', '*FINANCIAL'], ['*INDEPENDENCE-க்கான'], ['^FIRST STEP'], ['நீங்க', 'எடுக்கப்போறீங்க']],
 'V28': [['இத்தனை', '*SECRETS-உம்'], ['நாங்க', '^JUST ₹555-க்கு'], ['கொடுக்கப்போறோம்']],
 'V29': [['3 நாள்', 'LIVE-ஆ'], ['ATTEND', 'பண்ணிட்டு'], ['VALUE-வே', 'கிடைக்கலைன்னா'], ['*100%', '*MONEY BACK']],
 'V30': [['RISK', 'முழுசா', '^என் பக்கம்']],
 'V31': [['ஆனா', 'இந்த', 'BATCH-க்கு'], ['TRICHY-ல', 'இருந்து'], ['வெறும்', '!5 COUPLES', 'மட்டும்தான்']],
 'V32': [['நானே', '^PERSONAL-ஆ'], ['TRAIN', 'பண்ணப்போறேன்']],
 'V33': [['கீழே', 'இருக்கிற', '^BUTTON-ஐ'], ['CLICK', 'பண்ணி'], ['FAMILY-ஓட', 'இந்த', '*JOURNEY-ஐ'], ['START', 'பண்ணுங்க']],
}
def layout_at(t):
    for bid, a0, b0, sc, lay, ex, kw, src in BROLL:
        if a0 <= t < b0: return lay
    return 'face'
EMPH = {'V01': 1.08, 'V10': 1.06, 'V15': 1.08, 'V16': 1.10, 'V17': 1.18, 'V28': 1.10, 'V30': 1.14, 'V31': 1.08, 'V32': 1.12, 'V33': 1.05}
DESAT = [span('V09'), span('V14')]
MUSIC = [(0.0, span('V10')[1], 'dark'), (span('V10')[1], span('V18')[0], 'warm'), (span('V18')[0], span('V28')[0], 'tech'), (span('V28')[0], TOTAL, 'uplift')]

def build():
    items, captions, sfx = [], [], []
    for bid, a0, b0, sc, lay, ex, kw, src in BROLL:
        d = dict(type=sc, t0=round(a0, 3), t1=round(b0, 3), layout='side' if lay == 'tside' else lay, id=bid); ex = dict(ex); ex.pop('clip', None); d.update(ex)
        items.append(d); sfx.append((a0 - 0.1, 'whoosh'))
    for ty, a0, b0, ex in GFX:
        d = dict(type=ty, t0=round(a0, 3), t1=round(b0, 3)); d.update(ex); items.append(d)
        sfx.append((a0, {'text': 'hit', 'badge': 'pop', 'price': 'cash', 'stamp': 'thud', 'cta': 'ding', 'lower': 'swipe', 'flash': 'whoosh', 'endcard': 'hit'}[ty]))
    for tid, chunks in CAP.items():
        ps = [p for p in pieces if p['id'] == tid]
        if not ps: continue          # line not in this cut
        a0, b0 = ps[0]['o0'], ps[-1]['o1']
        wts = [sum(len(w.lstrip('*^!')) for w in c) + 3 for c in chunks]; tot = sum(wts); t = a0
        for c, wt in zip(chunks, wts):
            d = (b0 - a0) * wt / tot; col = {'*': '#00C896', '^': '#FFD60A', '!': '#FF3B30'}
            cap = dict(t0=round(t, 3), t1=round(t + d, 3), words=[w.lstrip('*^!') for w in c], hl=[i for i, w in enumerate(c) if w[0] in '*^!'])
            cc = next((col[w[0]] for w in c if w[0] in col), None)
            if cc: cap['col'] = cc
            if layout_at(t + d / 2) in ('side', 'tside'): cap['pos'] = 'side'
            captions.append(cap); t += d
    for s, e in DESAT: sfx.append((s, 'thud'))
    sfx.append((span('V33')[0] - 1.4, 'riser'))
    sfx = sorted([(max(0, round(t, 3)), n) for t, n in sfx])
    os.makedirs(W + 'gfx', exist_ok=True); os.makedirs(W + 'audio', exist_ok=True)
    json.dump(dict(total=round(TOTAL, 3), items=items, captions=captions), open(W + 'gfx/timeline.json', 'w'), ensure_ascii=False)
    # per-frame: every jump cut alternates the framing (wide 1.0 / close 1.12) so cuts read as deliberate
    segz = {}; k = 0; prev_id = None
    for p in pieces:
        if p['k'] != 'seg': continue
        k += 1; base = 1.0 if k % 2 else 1.12
        segz[id(p)] = base * (EMPH.get(p['id'], 1.0) if base == 1.0 else 1.0)
    frames = []; n = int(round(TOTAL * FPS)); last_ts = 0
    for i in range(n):
        t = i / FPS; p = next((q for q in pieces if q['o0'] <= t < q['o1']), None); fr = dict(L='face', z=1.0)
        if p and p['k'] == 'seg':
            last_ts = p['s0'] + (t - p['o0']); prog = (t - p['o0']) / max(.01, p['o1'] - p['o0'])
            fr['z'] = round(segz[id(p)] * (1 + 0.02 * prog), 4)      # slow creep inside each shot
        fr['ts'] = round(last_ts, 4)
        if p and p['k'] == 'bite':
            vis = BITE_VIS.get(p['id'])     # some bites play the client's words over a cleaner shot of the same client
            fr['L'] = 'full'; fr['V'] = [vis[0], round(vis[1] + t - p['o0'], 4), round((t - p['o0']) / p['dur'], 3)] if vis else [p['clip'], round(t - p['o0'], 4), round((t - p['o0']) / p['dur'], 3)]
        for bid, a0, b0, sc, lay, ex, kw, src in BROLL:
            if a0 <= t < b0 and not (p and p['k'] == 'bite'):
                fr['L'] = lay
                if 'clip' in ex: fr['V'] = [ex['clip'][0], round(ex['clip'][1] + t - a0, 4), round((t - a0) / (b0 - a0), 3)]
        if any(a0 <= t < b0 for a0, b0 in DESAT): fr['des'] = True
        if t >= o: fr['L'] = 'face'; fr['z'] = 1.0
        frames.append(fr)
    json.dump(frames, open(W + 'frames.json', 'w'))
    json.dump(dict(total=TOTAL, pieces=pieces, sfx=sfx, music=MUSIC), open(W + 'audio/cues.json', 'w'))
    json.dump(dict(face=[910, 330], skin_glow=True, facebox=[830, 320, 985, 535]), open(W + 'comp_cfg.json', 'w'))
    with open(os.path.join(HERE, 'broll_plan_v2.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['ID', 'Final time (s)', 'Line', 'Visual now', 'Source', 'Layout', 'On-screen (s)', 'Licence'])
        for bid, a0, b0, sc, lay, ex, kw, src in sorted(BROLL, key=lambda r: r[1]):
            vis = f'clip {ex["clip"][0]}' if 'clip' in ex else f'animated "{sc}"' + (f' ({ex["v"]})' if 'v' in ex else '')
            w.writerow([bid, f'{a0 / 1.2:.1f}-{b0 / 1.2:.1f}', kw, vis, src, lay, f'{(b0 - a0) / 1.2:.1f}', 'client consent needed' if 'P2' in src else ('AI - disclose' if 'P3' in src else 'original')])
    with open(os.path.join(HERE, 'flow_shotlist.md'), 'w') as f:
        f.write('# Google Flow shot list: TM Nutrition VSL v2\n\n')
        f.write('Generate each clip in Google Flow (Veo 3.1), **16:9, 8 s, no audio needed**. Name the file with its ID (F01.mp4 ...) and upload them to Drive; '
                'they drop straight into the edit at the timecodes below (we use the best 2-5 s).\n\n')
        f.write(f'**Paste this style line at the end of every prompt:** _{STYLE}_\n\n')
        f.write('Rules: these are scene-setting shots only. Never generate anything that looks like a client result, a testimonial, a weighing-scale "after" number, or Coach Pradheesh himself. Mark the ad as containing AI content in Meta.\n\n')
        f.write('| ID | Plays at (final video) | Length used | Line it covers | Prompt |\n|---|---|---|---|---|\n')
        for fid, a0, b0, lay, fb, line, prompt in FLOW:
            mm = lambda x: f'{int(x // 60)}:{x % 60:04.1f}'
            f.write(f'| **{fid}** | {mm(a0 / 1.2)}–{mm(b0 / 1.2)} | {(b0 - a0) / 1.2:.1f} s | {line} | {prompt} |\n')
    cov = sum(b0 - a0 for _, a0, b0, *_ in BROLL)
    print(f'{len([p for p in pieces if p["k"] == "seg"])} shots | output {TOTAL:.1f}s pre-speed = {TOTAL / 1.2:.1f}s final | B-roll {cov / TOTAL * 100:.0f}% | flow clips present: '
          f'{[x[0] for x in FLOW if os.path.exists(W + "broll/" + x[0] + ".mp4")]}')

if __name__ == '__main__':
    build()
