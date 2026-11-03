"""Original meditation bed for 'Tonight Wind-Down' (all procedural, no third-party audio):
evolving D-major pad, soft bell notes, ocean swell, singing bowls on section changes,
breath-synced pad swell. Mixes with the voice, gentle duck, -16 LUFS."""
import numpy as np, json, soundfile as sf
from scipy.signal import butter, sosfilt, fftconvolve
SR=48000; rng=np.random.default_rng(11)
tl=json.load(open('timeline.json')); T=tl['total']; N=int(T*SR); t=np.arange(N)/SR
def lp(x,fc,o=2): return sosfilt(butter(o,fc/(SR/2),'low',output='sos'),x)
def hp(x,fc,o=2): return sosfilt(butter(o,fc/(SR/2),'high',output='sos'),x)
def midi(m): return 440*2**((m-69)/12)
def smooth(x,sec):
    k=int(sec*SR); 
    if k<2: return x
    c=np.cumsum(np.insert(x,0,0)); y=(c[k:]-c[:-k])/k; return np.concatenate([np.full(k//2,y[0]),y,np.full(len(x)-len(y)-k//2,y[-1])])
def reverb(x,decay=5.0,mix=0.45,seed=0,bright=4000):
    r=np.random.default_rng(seed); n=int(decay*SR); tt=np.arange(n)/SR
    ir=r.standard_normal(n)*np.exp(-tt/(decay/6.9)); ir=lp(ir,bright); ir[:int(0.02*SR)]*=np.linspace(0,1,int(0.02*SR)); ir/=np.sqrt(np.sum(ir**2))
    return x*(1-mix)+fftconvolve(x,ir)[:len(x)]*mix
# --- section-based master brightness/energy: slowly darker toward the end
dark=np.interp(t,[0,60,200,330,tl['voice_end'],T],[1.0,0.95,0.85,0.75,0.65,0.5])
# --- pad
chords=[[38,50,57,62,64,66],[35,47,54,57,62,66],[43,55,59,62,66,69],[45,57,61,64,69]]  # Dadd9, Bm7(add11), Gmaj7, A(sus-ish)
CL=16.0; XF=7.0
pad=np.zeros((2,N))
k=0; start=-2.0
while start<T:
    ch=chords[k%len(chords)]; s=max(0,start); e=min(T,start+CL+XF)
    i0,i1=int(s*SR),int(e*SR); tt=t[i0:i1]
    env=np.clip(np.minimum((tt-start)/XF,(start+CL+XF-tt)/XF),0,1); env=np.sin(env*np.pi/2)**2
    for j,m in enumerate(ch):
        f=midi(m); a=(0.55 if j==0 else 0.22)/np.sqrt(len(ch))
        for ch_i,det in enumerate((-2.5,2.5)):
            ff=f*2**(det/1200); ph=rng.uniform(0,6.28)
            trem=1+0.15*np.sin(2*np.pi*(0.05+0.03*j)*tt+ph)
            sig=np.sin(2*np.pi*ff*tt+ph)+0.25*np.sin(4*np.pi*ff*tt+ph*1.3)+0.08*np.sin(6*np.pi*ff*tt)
            pad[ch_i,i0:i1]+=a*sig*trem*env
    k+=1; start+=CL
for c in range(2): pad[c]=lp(pad[c],1600)
# breath swell on pad
sw=np.ones(N)
for a,b,kind in tl['breath']:
    i0,i1=int(a*SR),int(b*SR); x=np.linspace(0,1,i1-i0)
    if kind=='in': sw[i0:i1]=1+0.35*np.sin(x*np.pi/2)**2; 
    elif kind=='out': sw[i0:i1]=1+0.35*np.cos(x*np.pi/2)**2
sw=smooth(sw,0.8)
pad*=sw*dark
# --- drone
drone=0.06*np.sin(2*np.pi*midi(26)*t)*(1+0.2*np.sin(2*np.pi*0.03*t))+0.03*np.sin(2*np.pi*midi(38)*t)
# --- bell notes (sparse, pentatonic)
bells=np.zeros((2,N)); pent=[74,76,78,81,83,86,88]
tb=6.0
while tb<tl['voice_end']+4:
    m=pent[rng.integers(len(pent))]; f=midi(m); d=6.0; n=int(d*SR); tt=np.arange(n)/SR
    x=(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*f*2.01*tt)*np.exp(-tt/0.8)+0.1*np.sin(2*np.pi*f*3.0*tt)*np.exp(-tt/0.4))
    x*=np.exp(-tt/1.8)*np.minimum(1,tt/0.01)*0.05
    pan=rng.uniform(0.25,0.75); i=int(tb*SR); j=min(N,i+n)
    bells[0,i:j]+=x[:j-i]*(1-pan); bells[1,i:j]+=x[:j-i]*pan
    # sparser during breathing counts, fewer near the end
    gap=rng.uniform(7,12) if not (tl['breath'][0][0]<tb<tl['breath'][6][1]) else rng.uniform(12,18)
    tb+=gap*(1.0 if tb<300 else 1.4)
bells*=dark
# --- singing bowls
bowls=np.zeros((2,N))
for k_,b in enumerate(tl['bowls']):
    f0=midi(50) if k_%2==0 else midi(45); d=14; n=int(d*SR); tt=np.arange(n)/SR; x=np.zeros(n)
    for r,a,dec in [(1,1,9),(2.71,.45,6),(5.15,.2,4),(8.43,.08,2.5)]:
        x+=a*np.sin(2*np.pi*f0*r*tt)*(1+0.35*np.sin(2*np.pi*0.7*r**0.3*tt))*np.exp(-tt/dec)
    x*=np.minimum(1,tt/0.004)*0.09
    i=int(b*SR); j=min(N,i+n); bowls[0,i:j]+=x[:j-i]; bowls[1,i:j]+=x[:j-i]*0.9
# --- ocean
def brown(seed):
    r=np.random.default_rng(seed); w=np.cumsum(r.standard_normal(N)); w=hp(w,20); return w/np.std(w)
ocean=np.zeros((2,N))
for c in range(2):
    nz=brown(100+c)
    s=0.5+0.3*np.sin(2*np.pi*t/11.3+c*0.6)+0.2*np.sin(2*np.pi*t/7.1+1.7+c*0.4); s=np.clip(s,0,1)**1.6
    lo=lp(nz,350); hi=lp(nz,1800)
    ocean[c]=(lo*(0.5+0.5*s)+hi*s*0.6)*0.07
ocean*=np.interp(t,[0,T],[1,0.8])
mus=pad+bells+bowls+ocean+drone
for c in range(2): mus[c]=reverb(mus[c],5.5,0.4,seed=c)
bowls_dry=0  # bowls already in reverb
# --- voice
v,_=sf.read('voice_clean.wav'); v=v.astype(np.float64)
vv=np.zeros(N); o=int(tl['offset']*SR); vv[o:o+len(v)]=v[:N-o]
vrev=reverb(vv,2.2,0.12,seed=5,bright=6000)
# duck: music down ~3.5 dB while voice active, plus louder bed in intro/outro
venv=smooth(np.abs(vv),0.05); act=(venv>0.01).astype(float); act=smooth(act,1.5)
gain=10**(-3.5*act/20)
bed=np.interp(t,[0,tl['offset']-1,tl['offset']+2,tl['voice_end'],tl['voice_end']+3,T-12,T],[1.8,1.8,1,1,2.2,2.0,0])
bed*=np.minimum(1,t/3.0)
mus*=gain*bed
# music level relative to voice
vr=np.sqrt(np.mean(vv[o:o+len(v)]**2)); mr=np.sqrt(np.mean(mus[:,o:o+len(v)]**2))
mus*= (vr*10**(-17/20))/mr
out=np.stack([vrev+mus[0],vrev+mus[1]],1)
out/=np.max(np.abs(out))*1.05
sf.write('mix_pre.wav',out.astype(np.float32),SR)
print('ok',T)
