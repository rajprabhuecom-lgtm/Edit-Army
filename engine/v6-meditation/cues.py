# Build subtitle cues + timeline from Whisper word timestamps. Times here are VOICE time; OFFSET added for video.
import json,re
OFFSET=8.0; TAIL=26.0
segs=json.load(open('segs.json'))
words=[w for s in segs for w in s['w']]
cues=[];cur=[]
def flush():
    global cur
    if cur: cues.append([cur[0][0],cur[-1][1],''.join(w[2] for w in cur).strip()]); cur=[]
for i,w in enumerate(words):
    cur.append(w)
    txt=w[2].strip(); nxt=words[i+1] if i+1<len(words) else None
    gap=(nxt[0]-w[1]) if nxt else 9
    n=len(cur); dur=w[1]-cur[0][0]
    if round(w[1],2) in (9.51,162.97,11.55): flush()
    elif re.search(r"[.?!]$",txt) and (n>=2 or gap>0.8): flush()
    elif re.search(r'[,]$',txt) and (n>=6 or gap>1.2) : flush()
    elif (n>=14) or gap>1.6: flush()
flush()
# manual fixes (Whisper mis-hearings / ad-lib we can't confirm)
fix={"Hello sisters, this is Naheed.":"Hello sisters, this is Naheed."}
out=[]
for s,e,t in cues:
    t=t.replace("It will be still there","It will still be there")
    if t.startswith("I recommend closing more"): continue   # unclear ad-lib, no subtitle rather than a guess
    if t.startswith("Three, two, three"): t="Two, three, four, five, six."
    t=t.replace("It is not a medical advice and","It is not a medical advice, and").replace("driving or while","driving, or while")
    if out and re.match(r"^[a-z]",t) and len(t.split())<=2: out[-1][1]=round(e+OFFSET,2); out[-1][2]+=" "+t; continue
    out.append([round(s+OFFSET,2),round(e+OFFSET,2),t])
for c in out: print(c)
voice_end=words[-1][1]
tl=dict(offset=OFFSET,total=round(OFFSET+voice_end+TAIL,2),voice_end=round(OFFSET+voice_end,2),cues=out,
  sections=[[0,'Opening'],[45.4,'Settling'],[124.2,'Breathing'],[222.8,'Body softening'],[308.6,'Letting go'],[356.3,'Ending']],
  # breath guide phases [start,end,'in'|'out'] (voice time)
  breath=[[143.9,149.2,'hold0'],[149.3,154.0,'in'],[155.3,173.3,'out'],[174.2,181.5,'in'],[183.0,193.4,'out'],[196.1,201.6,'in'],[201.8,211.2,'out'],[358.2,360.1,'in'],[360.1,362.8,'out']],
  bowls=[0.0,45.4,124.2,222.8,308.6,356.3],
  lantern=[316.5,336.0],  # "as you breathe out, imagine setting it down"
)
for k in ('sections','breath'):
    tl[k]=[[a+OFFSET if i<2 and isinstance(a,(int,float)) else a for i,a in enumerate(x)] for x in tl[k]]
tl['sections'][0][0]=0
tl['bowls']=[0.6]+[b+OFFSET for b in tl['bowls'][1:]]
tl['lantern']=[x+OFFSET for x in tl['lantern']]
json.dump(tl,open('timeline.json','w'),indent=1)
print(len(out),'cues total',tl['total'])
