/* v6.1 motion scene library (loaded after engine.html's main script).
   Full-screen animated cutaways (comp draws the neon stage under them; layout mode 'gfx'),
   zone graphics that live around the presenter (never on the face), swipe transitions,
   kinetic titles, odometer counters. All pure functions of time. */
const R01=i=>{let x=Math.sin(i*99.13+7.7)*43758.5453;return x-Math.floor(x)};
const ST=`position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden`;
// ---------- kinetic letters ----------
function KL(txt,cls='',style=''){ // letter-split title; Tamil stays as one run
  const parts=/[஀-௿]/.test(txt)?[txt]:[...txt];
  return `<div class="kl ${cls}" style="${style}">${parts.map(c=>`<span class="kc" style="display:inline-block;white-space:pre">${c==' '?'&nbsp;':MK(c)}</span>`).join('')}</div>`}
function klUpd(el,t0,t,{st=.035,d=.4,mode='flip'}={}){qa(el,'.kc').forEach((c,i)=>{const p=(t-t0-i*st)/d;const e=ease(p),b=back(p);
  c.style.opacity=clamp(p*3);
  if(mode=='flip')c.style.transform=`perspective(600px) translateY(${(1-e)*80}px) rotateX(${(1-e)*-90}deg) scale(${p<0?.6:lerp(.6,1,b)})`;
  else if(mode=='drop')c.style.transform=`translateY(${(1-b)*-160}px) rotate(${(1-e)*(i%2?-25:25)}deg)`;
  else c.style.transform=`scale(${p<0?0:b})`})}
// ---------- odometer ----------
function ODO(v,fs,color='#FFD60A'){return `<div class="odo" style="display:inline-flex;font-family:A;font-size:${fs}px;line-height:1;color:${color};text-shadow:0 0 50px rgba(255,214,10,.35)">${[...v].map(ch=>/\d/.test(ch)?`<span style="display:inline-block;height:${fs}px;overflow:hidden"><span class="oc" data-d="${ch}" style="display:block">${Array.from({length:30},(_,k)=>`<div style="height:${fs}px">${k%10}</div>`).join('')}</span></span>`:`<span>${ch}</span>`).join('')}</div>`}
function odoUpd(el,t0,t,fs,d=1.1){const cs=qa(el,'.oc');cs.forEach((c,i)=>{const target=20+ +c.dataset.d;const p=easeIO((t-t0-(cs.length-1-i)*.08)/d);c.style.transform=`translateY(${-lerp(0,target,p)*fs}px)`;
  c.parentNode.style.filter=`blur(${(p>0&&p<1)?Math.sin(p*Math.PI)*3:0}px)`})}
// ---------- particles ----------
function PARTS(n,cx,cy,col='#2EE59D'){return Array.from({length:n},(_,i)=>`<div class="pt" style="position:absolute;left:${cx}px;top:${cy}px;width:${6+R01(i)*10}px;height:${6+R01(i)*10}px;border-radius:50%;background:${i%5==0?'#FFD60A':col};box-shadow:0 0 12px ${col}"></div>`).join('')}
function partUpd(el,dt,{sp=420,life=1.6,burst=false}={}){qa(el,'.pt').forEach((p,i)=>{const a=R01(i+3)*6.283,s=sp*(.5+R01(i+9));const tt=burst?dt:((dt+R01(i+5)*life)%life);
  const k=burst?ease(tt/1.2):tt/life;p.style.transform=`translate(${Math.cos(a)*s*k}px,${Math.sin(a)*s*k}px) scale(${burst?1-k*.6:1-k})`;p.style.opacity=burst?(1-k)*clamp(dt/.05):Math.sin(k*Math.PI)})}
const sceneOut=(el,dt,dur)=>{const po=ease((dt-(dur-.18))/.18);el.style.opacity=1-po};

/* ===== 1. 18 YEARS: ring + odometer + zero hospital ===== {k:'sc_years',a,b,v,l,x}*/
S.sc_years=it=>{const el=mk(`<div style="${ST}">
 <div class="eb0" style="position:absolute;top:250px;left:0;right:0;text-align:center;font-weight:900;font-size:44px;letter-spacing:6px" class="mint">${KL('ME + MY FAMILY','','color:#2EE59D')}</div>
 <svg width="1080" height="1920" style="position:absolute;left:0;top:0"><circle class="rg" cx="540" cy="860" r="330" fill="none" stroke="#2EE59D" stroke-width="16" stroke-linecap="round" stroke-dasharray="2073" stroke-dashoffset="2073" transform="rotate(-90 540 860)" style="filter:drop-shadow(0 0 18px #2EE59D)"/>
 <circle class="rd" cx="540" cy="860" r="380" fill="none" stroke="rgba(46,229,157,.35)" stroke-width="4" stroke-dasharray="6 22"/></svg>
 ${PARTS(26,540,860)}
 <div class="od" style="position:absolute;left:0;right:0;top:${860-230}px;text-align:center">${ODO(it.v||'18',330)}</div>
 <div style="position:absolute;left:0;right:0;top:1000px;text-align:center;font-weight:900;font-size:64px;letter-spacing:10px">${KL(it.l||'YEARS')}</div>
 <div class="zb" style="position:absolute;left:150px;width:780px;top:1330px;display:flex;align-items:center;gap:30px;padding:28px 40px;border-radius:999px;background:rgba(8,20,17,.9);border:3px solid rgba(255,92,92,.6)">
  <div style="position:relative;font-size:84px">🏥<svg width="110" height="110" style="position:absolute;left:-6px;top:-6px"><circle cx="55" cy="55" r="48" fill="none" stroke="#FF5C5C" stroke-width="9"/><line class="sl" x1="22" y1="88" x2="88" y2="22" stroke="#FF5C5C" stroke-width="9" stroke-dasharray="94" stroke-dashoffset="94"/></svg></div>
  <div style="font-weight:900;font-size:46px;line-height:1.1">${MK(it.x||'*ZERO* HOSPITAL VISITS')}</div></div></div>`);
 return {el,upd(t,dt,dur){q(el,'.rg').setAttribute('stroke-dashoffset',2073*(1-easeIO(dt/1.3)));q(el,'.rd').setAttribute('transform',`rotate(${dt*30} 540 860)`);
  odoUpd(el,it.a+.05,t,330,1.0);klUpd(q(el,'.eb0'),it.a,t,{mode:'pop',st:.03});klUpd(qa(el,'.kl')[1],it.a+.5,t,{st:.06});partUpd(el,dt);
  const z=q(el,'.zb');z.style.opacity=clamp((dt-.7)/.15);z.style.transform=`translateY(${(1-back((dt-.7)/.4))*200}px)`;q(el,'.sl').setAttribute('stroke-dashoffset',94*(1-ease((dt-1.0)/.3)));
  sceneOut(el,dt,dur);return []}}};

/* ===== 2. 6 MONTHS: calendar tiles flip + ticks ===== {k:'sc_months',a,b,ticks:[t..6]} */
S.sc_months=it=>{const el=mk(`<div style="${ST}">
 <div style="position:absolute;left:0;right:0;top:170px;text-align:center;font-family:A;font-size:210px;color:#FFD60A;paint-order:stroke fill;-webkit-text-stroke:12px #000">${KL('6 MONTHS')}</div>
 ${Array.from({length:6},(_,i)=>`<div class="tl" style="position:absolute;left:${105+(i%3)*300}px;top:${560+Math.floor(i/3)*380}px;width:270px;height:340px;border-radius:30px;overflow:hidden;background:#f4f7f6;box-shadow:0 30px 60px rgba(0,0,0,.55);transform-origin:50% 0">
  <div style="height:80px;background:linear-gradient(#ff5c5c,#e03b30);color:#fff;font-weight:900;font-size:34px;display:flex;align-items:center;justify-content:center;letter-spacing:3px">MONTH</div>
  <div style="height:260px;display:flex;align-items:center;justify-content:center;font-family:A;font-size:170px;color:#111">${i+1}</div>
  <div class="ck" style="position:absolute;right:16px;bottom:16px;width:84px;height:84px;border-radius:50%;background:#2EE59D;color:#063;font-size:52px;font-weight:900;display:flex;align-items:center;justify-content:center">✓</div></div>`).join('')}
 <div style="position:absolute;left:120px;width:840px;top:1360px;height:34px;border-radius:17px;background:rgba(255,255,255,.12);overflow:hidden"><div class="pb" style="height:100%;width:0;background:linear-gradient(90deg,#0fbf83,#36f0aa);box-shadow:0 0 30px #2EE59D"></div></div>
 <div class="ez" style="position:absolute;left:0;right:0;top:1440px;text-align:center"><span style="display:inline-block;padding:20px 50px;border-radius:999px;background:#2EE59D;color:#063;font-weight:900;font-size:60px">${MK(it.e||'EASY-ஆ ✓')}</span></div></div>`);
 return {el,upd(t,dt,dur){klUpd(q(el,'.kl'),it.a,t,{mode:'drop',st:.05});
  qa(el,'.tl').forEach((c,i)=>{const p=(dt-.25-i*.17)/.4;c.style.opacity=clamp(p*4);c.style.transform=`perspective(900px) rotateX(${(1-ease(p))*-100}deg) translateY(${Math.sin(t*2+i)*6}px)`;
   const k=q(c,'.ck');const kp=(dt-.6-i*.17)/.25;k.style.transform=`scale(${kp<0?0:back(kp)})`});
  q(el,'.pb').style.width=(easeIO((dt-.3)/1.6)*100)+'%';const e=q(el,'.ez');e.style.transform=`scale(${back((dt-1.7)/.35)})`;e.style.opacity=clamp((dt-1.7)/.1);
  sceneOut(el,dt,dur);return []}}};

/* ===== 3. BLUEPRINT: drafting lines draw + title ===== {k:'sc_blue',a,b} */
S.sc_blue=it=>{const L=[[90,500,990,500],[90,1400,990,1400],[140,420,140,1480],[940,420,940,1480],[90,560,990,1340],[90,1340,990,560]];
 const el=mk(`<div style="${ST}"><div class="bg" style="position:absolute;inset:0;background-image:linear-gradient(rgba(120,200,255,.13) 2px,transparent 2px),linear-gradient(90deg,rgba(120,200,255,.13) 2px,transparent 2px);background-size:60px 60px;background-color:rgba(6,30,60,.55)"></div>
 <svg width="1080" height="1920" style="position:absolute;left:0;top:0">${L.map(l=>`<line class="dl" x1="${l[0]}" y1="${l[1]}" x2="${l[2]}" y2="${l[3]}" stroke="#9fd8ff" stroke-width="3" stroke-dasharray="1400" stroke-dashoffset="1400" opacity=".7"/>`).join('')}
 <circle class="dc" cx="540" cy="950" r="300" fill="none" stroke="#9fd8ff" stroke-width="3" stroke-dasharray="1885" stroke-dashoffset="1885" opacity=".8"/><circle class="dc2" cx="540" cy="950" r="200" fill="none" stroke="#2EE59D" stroke-width="5" stroke-dasharray="10 14" opacity=".7"/></svg>
 <div class="ttl" style="position:absolute;left:0;right:0;top:760px;text-align:center;font-family:A;font-size:190px;line-height:1">${KL('BLUEPRINT','', 'color:#fff;text-shadow:0 0 40px rgba(159,216,255,.6)')}</div>
 <div class="t2" style="position:absolute;left:0;right:0;top:960px;text-align:center;font-family:A;font-size:120px;color:#FFD60A">${KL('FOR SUCCESS')}</div>
 <div class="ty" style="position:absolute;left:0;right:0;top:1130px;text-align:center;font-weight:900;font-size:40px;letter-spacing:6px;color:#9fd8ff"></div>
 <div class="rk" style="position:absolute;left:0;top:0;font-size:110px">🚀</div>${PARTS(18,540,950,'#9fd8ff')}</div>`);
 const typ='TRANSFORMATION PROGRAM';
 return {el,upd(t,dt,dur){qa(el,'.dl').forEach((l,i)=>l.setAttribute('stroke-dashoffset',1400*(1-ease((dt-i*.06)/.6))));q(el,'.dc').setAttribute('stroke-dashoffset',1885*(1-ease((dt-.1)/.8)));
  q(el,'.dc2').setAttribute('transform',`rotate(${dt*-40} 540 950)`);q(el,'.bg').style.opacity=clamp(dt/.25);q(el,'.bg').style.backgroundPosition=`0 ${dt*30}px`;
  klUpd(q(el,'.ttl .kl'),it.a+.12,t,{st:.045});klUpd(q(el,'.t2 .kl'),it.a+.45,t,{mode:'pop',st:.04});
  q(el,'.ty').textContent=typ.slice(0,Math.max(0,Math.floor((dt-.7)*30)))+((dt*4|0)%2?'▍':'');
  const rp=ease(dt/1.4);const rk=q(el,'.rk');rk.style.transform=`translate(${lerp(-150,1000,rp)}px,${lerp(1500,250,rp)}px) rotate(0deg)`;partUpd(el,dt,{burst:true,sp:600});
  sceneOut(el,dt,dur);return []}}};

/* ===== 4. TRIAD: health wealth happiness orbs connect ===== {k:'sc_triad',a,b,at:[3],c} */
S.sc_triad=it=>{const P=[[540,560],[250,1120],[830,1120]],E=[['💪','HEALTH'],['💰','WEALTH'],['😊','HAPPINESS']];
 const el=mk(`<div style="${ST}"><svg width="1080" height="1920" style="position:absolute;left:0;top:0">${[[0,1],[1,2],[2,0]].map(([a,b])=>`<line class="tl" x1="${P[a][0]}" y1="${P[a][1]}" x2="${P[b][0]}" y2="${P[b][1]}" stroke="#2EE59D" stroke-width="8" stroke-dasharray="14 16" style="filter:drop-shadow(0 0 10px #2EE59D)"/>`).join('')}</svg>
 ${P.map((p,i)=>`<div class="ob" style="position:absolute;left:${p[0]-150}px;top:${p[1]-150}px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#1f6b54,#0a241d);border:6px solid #2EE59D;box-shadow:0 0 60px rgba(46,229,157,.5);display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:110px">${E[i][0]}</div><div style="font-weight:900;font-size:38px">${E[i][1]}</div></div>`).join('')}
 <div class="cn" style="position:absolute;left:0;right:0;top:880px;text-align:center"><span style="display:inline-block;padding:18px 40px;border-radius:999px;background:#FFD60A;color:#111;font-weight:900;font-size:50px">${MK(it.c||'மூணும் CONNECTED')}</span></div>
 <div class="tt0" style="position:absolute;left:0;right:0;top:1400px;text-align:center;font-family:A;font-size:120px">${KL('ALL CONNECTED')}</div></div>`);
 return {el,upd(t,dt,dur){const at=it.at||[it.a,it.a+.3,it.a+.6];qa(el,'.ob').forEach((o,i)=>{const p=(t-at[i])/.35;o.style.opacity=clamp(p*4);o.style.transform=`scale(${p<0?0:back(p)}) translateY(${Math.sin(t*2.2+i*2)*10}px)`});
  const lp=t-at[2];qa(el,'.tl').forEach((l,i)=>{l.style.opacity=clamp((lp-i*.12)/.2);l.setAttribute('stroke-dashoffset',-dt*90)});
  const c=q(el,'.cn');c.style.transform=`scale(${back((lp-.3)/.35)}) rotate(${Math.sin(t*3)*2}deg)`;c.style.opacity=clamp((lp-.3)/.1);klUpd(q(el,'.tt0 .kl'),at[2]+.4,t,{mode:'drop'});
  sceneOut(el,dt,dur);return []}}};

/* ===== 5. 75 LAKH families: dot wave + counter + my family ===== {k:'sc_fam',a,b,at2} */
S.sc_fam=it=>{const C=14,Rw=13,dots=[];for(let r=0;r<Rw;r++)for(let c=0;c<C;c++)dots.push([90+c*69,700+r*58]);
 const el=mk(`<div style="${ST}"><div style="position:absolute;left:0;right:0;top:150px;text-align:center">${ODO('75',300)}<div class="lk" style="font-family:A;font-size:150px;color:#fff;margin-top:-10px">${KL('LAKH FAMILIES')}</div></div>
 ${dots.map(([x,y],i)=>`<div class="fd" style="position:absolute;left:${x}px;top:${y}px;width:40px;height:40px;border-radius:50%;background:#2EE59D"></div>`).join('')}
 <div class="me" style="position:absolute;left:${dots[6*C+7][0]-30}px;top:${dots[6*C+7][1]-30}px;width:100px;height:100px;border-radius:50%;background:#FFD60A;display:flex;align-items:center;justify-content:center;font-size:56px;box-shadow:0 0 50px #FFD60A">❤️</div>
 <div class="mel" style="position:absolute;left:${dots[6*C+7][0]-150}px;top:${dots[6*C+7][1]-150}px;padding:12px 26px;border-radius:999px;background:#fff;color:#111;font-weight:900;font-size:34px">MY FAMILY TOO</div>
 <div class="xp" style="position:absolute;left:0;right:0;top:1520px;text-align:center"><span style="display:inline-block;padding:22px 50px;border-radius:999px;background:rgba(8,20,17,.92);border:3px solid #2EE59D;font-weight:900;font-size:56px">${MK('*EXTRAORDINARY* PERSON ⭐')}</span></div></div>`);
 return {el,upd(t,dt,dur){const pre=q(el,'.lk').parentNode;odoUpd(pre,it.a,t,300,1.1);klUpd(q(el,'.lk .kl'),it.a+.3,t,{st:.03});
  qa(el,'.fd').forEach((d,i)=>{const [x,y]=dots[i];const dist=Math.hypot(x-540,y-1050)/600;const p=(dt-.2-dist*.9)/.3;d.style.transform=`scale(${p<0?0:back(p)*(1+.15*Math.sin(t*4+i))})`;d.style.opacity=p<0?0:.35+.65*R01(i)});
  const me=q(el,'.me');const mp=(dt-1.3)/.35;me.style.transform=`scale(${mp<0?0:back(mp)*(1+.08*Math.sin(t*6))})`;const ml=q(el,'.mel');ml.style.opacity=clamp((dt-1.5)/.15);ml.style.transform=`translateY(${(1-ease((dt-1.5)/.3))*30}px)`;
  const xp=q(el,'.xp');const xa=(it.at2||it.a+2)-it.a;xp.style.transform=`scale(${back((dt-xa)/.35)})`;xp.style.opacity=clamp((dt-xa)/.1);
  sceneOut(el,dt,dur);return []}}};

/* ===== 6. RINGS: goals fill automatically ===== {k:'sc_rings',a,b,at:[3]} */
S.sc_rings=it=>{const N=[['💪','HEALTH'],['💰','WEALTH'],['😊','HAPPINESS']];
 const el=mk(`<div style="${ST}"><div style="position:absolute;left:0;right:0;top:220px;text-align:center;font-family:A;font-size:170px;color:#FFD60A">${KL('AUTOMATIC ⚡')}</div>
 <div class="sb" style="position:absolute;left:0;right:0;top:420px;text-align:center;font-weight:900;font-size:48px;letter-spacing:4px">${MK('IT JUST *HAPPENED*')}</div>
 ${N.map((n,i)=>`<div class="rr" style="position:absolute;left:90px;width:900px;top:${640+i*360}px;height:310px;border-radius:40px;background:rgba(8,20,17,.85);border:3px solid rgba(46,229,157,.3);display:flex;align-items:center;gap:40px;padding:0 50px">
  <svg width="230" height="230"><circle cx="115" cy="115" r="95" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="22"/><circle class="rc" cx="115" cy="115" r="95" fill="none" stroke="#2EE59D" stroke-width="22" stroke-linecap="round" stroke-dasharray="597" stroke-dashoffset="597" transform="rotate(-90 115 115)" style="filter:drop-shadow(0 0 12px #2EE59D)"/><text x="115" y="140" text-anchor="middle" font-size="80">${n[0]}</text></svg>
  <div style="flex:1"><div style="font-weight:900;font-size:60px">${n[1]}</div><div class="pc" style="font-family:A;font-size:80px;color:#2EE59D">0%</div></div><div class="ck" style="font-size:90px">✅</div></div>`).join('')}</div>`);
 return {el,upd(t,dt,dur){klUpd(q(el,'.kl'),it.a,t,{mode:'drop',st:.05});q(el,'.sb').style.opacity=clamp((dt-.3)/.2);
  const at=it.at||[it.a+.3,it.a+.5,it.a+.7];qa(el,'.rr').forEach((r,i)=>{const ap=(dt-.1-i*.12)/.35;r.style.opacity=clamp(ap*4);r.style.transform=`translateX(${(1-ease(ap))*(i%2?-500:500)}px)`;
   const p=easeIO((t-at[i])/.9);q(r,'.rc').setAttribute('stroke-dashoffset',597*(1-p));q(r,'.pc').textContent=Math.round(p*100)+'%';const c=q(r,'.ck');c.style.transform=`scale(${t<at[i]+.9?0:back((t-at[i]-.9)/.3)})`;
   r.style.borderColor=p>=1?'rgba(46,229,157,.9)':'rgba(46,229,157,.3)'});sceneOut(el,dt,dur);return []}}};

/* ===== 7. CHASE: runner chases goal that runs away ===== {k:'sc_chase',a,b} */
S.sc_chase=it=>{const el=mk(`<div style="${ST}"><div style="position:absolute;left:0;right:0;top:260px;text-align:center;font-family:A;font-size:150px;line-height:1.05">${KL("DON'T CHASE",'','color:#FF5C5C')}${KL('THE GOAL')}</div>
 <div class="gr" style="position:absolute;left:0;right:0;top:1230px;height:8px;background:repeating-linear-gradient(90deg,#2EE59D 0 60px,transparent 60px 100px);opacity:.6"></div>
 <div class="rn" style="position:absolute;top:930px;font-size:300px;transform-origin:50% 100%">🏃</div><div class="gl" style="position:absolute;top:990px;font-size:220px">🎯</div>
 <div class="tr" style="position:absolute;top:1120px;height:10px;border-radius:5px;background:linear-gradient(90deg,transparent,#FF5C5C)"></div>
 <div class="nx" style="position:absolute;left:0;right:0;top:1400px;text-align:center"><span style="display:inline-block;padding:20px 50px;border-radius:999px;background:#FF5C5C;font-weight:900;font-size:58px">✕ STILL OUT OF REACH</span></div></div>`);
 return {el,upd(t,dt,dur){qa(el,'.kl').forEach((k,i)=>klUpd(k,it.a+i*.25,t,{st:.04}));q(el,'.gr').style.backgroundPosition=`${-dt*600}px 0`;
  const rx=lerp(-200,330,ease(dt/.8))+Math.sin(dt*14)*6;const gx=lerp(560,840,ease(dt/2))+Math.sin(dt*3)*20;const rn=q(el,'.rn');
  rn.style.left=rx+'px';rn.style.transform=`scaleX(-1) translateY(${-Math.abs(Math.sin(dt*14))*30}px) rotate(${Math.sin(dt*14)*4}deg)`;
  const g=q(el,'.gl');g.style.left=gx+'px';g.style.transform=`translateY(${-Math.abs(Math.sin(dt*9))*40}px) rotate(${dt*80}deg)`;
  const tr=q(el,'.tr');tr.style.left=(rx+180)+'px';tr.style.width=Math.max(0,gx-rx-180)+'px';
  const nx=q(el,'.nx');nx.style.opacity=clamp((dt-1.1)/.15);nx.style.transform=`scale(${back((dt-1.1)/.35)})`;sceneOut(el,dt,dur);return []}}};

/* ===== 8. MAGNET: everything comes to ME ===== {k:'sc_magnet',a,b,t1} */
S.sc_magnet=it=>{const I=['💪','💰','😊','🎯','🏆','❤️','🌟','📈'];
 const el=mk(`<div style="${ST}"><div style="position:absolute;left:0;right:0;top:200px;text-align:center;font-weight:900;font-size:66px;line-height:1.2">${MK(it.t1||'எல்லாமே என்னை<br>*தேடி வந்துச்சு*')}</div>
 ${[0,1,2].map(i=>`<div class="rp" style="position:absolute;left:340px;top:820px;width:400px;height:400px;border-radius:50%;border:5px solid #2EE59D"></div>`).join('')}
 <div class="me" style="position:absolute;left:390px;top:870px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#36f0aa,#0b8f62);display:flex;align-items:center;justify-content:center;font-family:A;font-size:120px;color:#063;box-shadow:0 0 90px rgba(46,229,157,.7)">ME</div>
 ${I.map(e=>`<div class="ic" style="position:absolute;left:0;top:0;font-size:110px">${e}</div>`).join('')}</div>`);
 return {el,upd(t,dt,dur){const tt=q(el,'div');tt.style.opacity=clamp(dt/.2);tt.style.transform=`translateY(${(1-ease(dt/.4))*-60}px)`;
  const me=q(el,'.me');me.style.transform=`scale(${back(dt/.4)*(1+.05*Math.sin(t*5))})`;
  qa(el,'.rp').forEach((r,i)=>{const k=((dt+i*.4)%1.2)/1.2;r.style.transform=`scale(${.7+k*1.4})`;r.style.opacity=(1-k)*.8});
  qa(el,'.ic').forEach((c,i)=>{const a0=i/I.length*6.283;const p=ease((dt-.2-i*.09)/.8);const rad=lerp(900,250,p);const a=a0+p*1.2+dt*.6*p;
   c.style.transform=`translate(${540-55+Math.cos(a)*rad}px,${1020-60+Math.sin(a)*rad}px) scale(${lerp(.6,1,p)})`;c.style.opacity=clamp((dt-.2-i*.09)/.1)});sceneOut(el,dt,dur);return []}}};

/* ===== 9. CTA end scene ===== {k:'sc_cta',a,b} */
S.sc_cta=it=>{const el=mk(`<div style="${ST}">
 <div class="e1" style="position:absolute;left:0;right:0;top:170px;text-align:center;font-weight:800;font-size:38px;letter-spacing:8px;color:#2EE59D">TRANSFORMATION PROGRAM</div>
 <div style="position:absolute;left:0;right:0;top:240px;text-align:center;font-family:A;font-size:180px;line-height:1">${KL('BLUEPRINT')}</div>
 <div style="position:absolute;left:0;right:0;top:420px;text-align:center;font-family:A;font-size:130px;line-height:1;color:#FFD60A">${KL('FOR SUCCESS')}</div>
 <div class="by" style="position:absolute;left:0;right:0;top:580px;text-align:center;font-weight:800;font-size:40px;color:rgba(255,255,255,.85)">by Mr. Ravi Sundaram</div>
 <div class="yr" style="position:absolute;left:0;right:0;top:690px;text-align:center"><span style="display:inline-block;padding:16px 40px;border-radius:999px;border:3px solid #FFD60A;font-weight:900;font-size:44px">${MK('*2027* · YOUR _BEST VERSION_')}</span></div>
 ${[0,1,2].map(i=>`<div class="rp" style="position:absolute;left:140px;top:960px;width:800px;height:200px;border-radius:999px;border:5px solid #2EE59D"></div>`).join('')}
 <div class="bt" style="position:absolute;left:140px;top:960px;width:800px;height:200px;border-radius:999px;background:linear-gradient(#36f0aa,#0fbf83);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:84px;color:#04140f;box-shadow:0 0 80px rgba(46,229,157,.6),inset 0 4px 0 rgba(255,255,255,.5)">REGISTER NOW</div>
 <div class="hd" style="position:absolute;left:760px;top:1080px;font-size:150px">👆</div>
 ${[0,1,2].map(i=>`<div class="cv" style="position:absolute;left:0;right:0;top:${1330+i*90}px;text-align:center;font-size:90px;color:#FFD60A;line-height:1">⌄</div>`).join('')}
 <div class="lb" style="position:absolute;left:0;right:0;top:1640px;text-align:center"><span style="display:inline-block;padding:20px 50px;border-radius:999px;background:#FFD60A;color:#111;font-weight:900;font-size:56px">👇 LINK BELOW</span></div>${PARTS(40,540,1060)}</div>`);
 return {el,upd(t,dt,dur){const k=qa(el,'.kl');klUpd(k[0],it.a+.1,t,{st:.04});klUpd(k[1],it.a+.35,t,{mode:'pop',st:.04});
  [['.e1',0],['.by',.7],['.yr',.9],['.lb',1.2]].forEach(([s,d])=>{const e=q(el,s);e.style.opacity=clamp((dt-d)/.15);e.style.transform=`translateY(${(1-ease((dt-d)/.4))*40}px) scale(${s=='.lb'?1+.04*Math.sin(t*6):1})`});
  const bt=q(el,'.bt');const bp=dt-.5;bt.style.transform=`scale(${bp<0?0:back(bp/.4)*(1+.035*Math.max(0,Math.sin(t*6.3)))})`;
  qa(el,'.rp').forEach((r,i)=>{const kk=((dt+i*.45)%1.35)/1.35;r.style.opacity=bp<0?0:(1-kk)*.7;r.style.transform=`scale(${1+kk*.35},${1+kk*.9})`});
  const h=q(el,'.hd');h.style.opacity=clamp((dt-.9)/.2);const tap=Math.max(0,Math.sin((t)*6.3));h.style.transform=`translate(${-tap*12}px,${(1-ease((dt-.9)/.4))*300-tap*30}px)`;
  qa(el,'.cv').forEach((c,i)=>{const kk=((dt*1.6)+i*.33)%1;c.style.opacity=Math.sin(kk*Math.PI)*clamp((dt-1)/.2);c.style.transform=`translateY(${kk*40}px)`});
  partUpd(el,dt-.5,{burst:true,sp:700});return []}}};

/* ===== swipe transition (covers a hard cut) ===== {k:'wipe',a,b,dir} a..b ~0.36s, cut at the middle */
S.wipe=it=>{const el=mk(`<div class="wp" style="position:absolute;top:-200px;left:0;width:1500px;height:2320px;transform-origin:50% 50%">
 <div style="position:absolute;inset:0;background:linear-gradient(90deg,#2EE59D 0,#2EE59D 40px,#0a2a22 40px,#061512 85%,#2EE59D 85%,#2EE59D calc(85% + 18px),transparent calc(85% + 18px));box-shadow:0 0 80px #2EE59D"></div></div>`);
 const w=q(el,'.wp');return {el,upd(t,dt,dur){const p=easeIO(dt/dur);const d=it.dir||1;w.style.transform=`translateX(${d*lerp(1200,-1700,p)}px) skewX(${-12*d}deg)`;return []}}};

/* ===== kinetic title for the zones ===== {k:'kin',a,b,v,y,fs,c,mode} */
S.kin=it=>{const el=mk(`<div style="position:absolute;left:0;right:0;top:${it.y||120}px;text-align:center;font-family:A;font-size:${it.fs||150}px;line-height:1.05;color:${it.c||'#fff'};paint-order:stroke fill;-webkit-text-stroke:12px #000;text-shadow:0 12px 40px rgba(0,0,0,.5)">${(it.v.split('|')).map(l=>KL(l)).join('')}</div>`);
 return {el,upd(t,dt,dur){qa(el,'.kl').forEach((k,i)=>klUpd(k,it.a+i*.2,t,{mode:it.mode||'flip',st:.035}));const o=el.firstChild;o.style.opacity=1-ease((dt-(dur-.15))/.15);const wmax=Math.max(...qa(el,'.kl').map(k=>k.scrollWidth));const fit=Math.min(1,1010/Math.max(1,wmax));o.style.transformOrigin='50% 0';o.style.transform=`translateY(${Math.sin(t*2)*6}px) scale(${fit})`;return []}}};

/* ===== flow: A -> B pills with drawing arrow ===== {k:'flow',a,b,y,v:[['📚','LEARN',t],['⚙️','APPLY',t]]} */
S.flow=it=>{const el=mk(`${it.v.map((v,i)=>`<div class="fp" style="position:absolute;left:${i?600:80}px;top:${it.y||1400}px;width:400px;height:300px;border-radius:40px;background:rgba(10,30,25,.92);border:4px solid #2EE59D;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;box-shadow:0 0 40px rgba(46,229,157,.3)"><div style="font-size:120px">${v[0]}</div><div style="font-weight:900;font-size:50px">${MK(v[1])}</div></div>`).join('')}
 <svg width="1080" height="1920" style="position:absolute;left:0;top:0"><path class="ar" d="M490 ${(it.y||1400)+150} L590 ${(it.y||1400)+150}" stroke="#FFD60A" stroke-width="14" stroke-linecap="round" stroke-dasharray="100" stroke-dashoffset="100"/><path class="ah" d="M560 ${(it.y||1400)+120} L595 ${(it.y||1400)+150} L560 ${(it.y||1400)+180}" fill="none" stroke="#FFD60A" stroke-width="14" stroke-linecap="round" opacity="0"/></svg>`);
 return {el,upd(t,dt,dur){const po=1-ease((dt-(dur-.2))/.2);qa(el,'.fp').forEach((p,i)=>{const a=it.v[i][2]!=null?it.v[i][2]:it.a+i*.5;const k=(t-a)/.4;p.style.opacity=clamp(k*4)*po;p.style.transform=`scale(${k<0?0:back(k)}) translateY(${Math.sin(t*2+i)*8}px)`});
  const a1=it.v[1][2]!=null?it.v[1][2]:it.a+.5;q(el,'.ar').setAttribute('stroke-dashoffset',100*(1-ease((t-a1+.25)/.25)));q(el,'.ah').setAttribute('opacity',clamp((t-a1)/.1)*po);q(el,'.ar').style.opacity=po;return []}}};

/* ===== stairs: rising steps with labels ===== {k:'stairs',a,b,y,v:[[label,t]]} */
S.stairs=it=>{const n=it.v.length,W=290,y0=(it.y||1300);const el=mk(it.v.map((v,i)=>`<div class="sp" style="position:absolute;left:${75+i*(W+20)}px;width:${W}px;bottom:${1920-(y0+560)}px;height:0;border-radius:24px 24px 0 0;background:linear-gradient(#36f0aa,#0b8f62);box-shadow:0 0 40px rgba(46,229,157,.35);overflow:visible">
 <div class="sl" style="position:absolute;left:-10px;right:-10px;top:-120px;text-align:center;font-weight:900;font-size:40px;line-height:1.1">${MK(v[0])}</div></div>`).join('')+`<div class="up" style="position:absolute;left:0;top:${y0-30}px;font-size:120px">🚀</div>`);
 return {el,upd(t,dt,dur){const po=1-ease((dt-(dur-.2))/.2);qa(el,'.sp').forEach((s,i)=>{const p=(t-it.v[i][1])/.5;s.style.height=(ease(p)*(180+i*170))+'px';s.style.opacity=po*clamp(p*5);q(s,'.sl').style.opacity=clamp((p-.4)*3)});
  const last=it.v[n-1][1];const u=q(el,'.up');const k=ease((t-last-.3)/.6);u.style.opacity=clamp((t-last-.3)/.1)*po;u.style.transform=`translate(${lerp(60,900,k)}px,${lerp(500,-40,k)}px) rotate(-10deg)`;return []}}};

/* ===== idle float + periodic shine for glass cards ===== */
(function(){const g=S.glass;S.glass=it=>{const o=g(it);const u=o.upd;o.upd=(t,dt,dur)=>{const r=u(t,dt,dur);const gc=q(o.el,'.gc');if(dt>.35&&dt<dur-.25)gc.style.transform=`translateY(${Math.sin(t*1.8+it.a)*7}px) rotate(${Math.sin(t*1.1+it.a)*.4}deg)`;
  const sh=q(o.el,'.sh');const cyc=(dt-.8)%2.6;if(dt>.8)sh.style.left=lerp(-300,1200,ease(cyc/.8))+'px';return r};return o}})();
/* ===== word-by-word pill: each word pops in across the line ===== */
(function(){const splitMK=v=>{let st={'*':0,'_':0,'~':0};return v.split(' ').map(w=>{let pre=Object.keys(st).filter(k=>st[k]).join('');let raw=w;for(const ch of w)if(ch in st)st[ch]^=1;raw=raw.replace(/[*_~]/g,'');const cls=(pre+w).match(/[*_~]/)?(((pre.includes('*')||/^\*|\*/.test(w))?'mint':(pre.includes('_')||/_/.test(w))?'y':'r')):'';return cls?`<span class="${cls}">${TX(raw)}</span>`:TX(raw)})};
S.pill=it=>{const words=splitMK(it.v);const el=mk(`<div class="pill" style="top:${it.y||1590}px">${words.map(w=>`<span class="pw" style="display:inline-block;margin:0 9px">${w}</span>`).join('')}</div>`);const p=q(el,'.pill'),ws=qa(el,'.pw');
 return {el,upd(t,dt,dur){const pi=back(dt/.22),po=ease((dt-(dur-.12))/.12);p.style.opacity=clamp(dt/.06)*(1-po);const fit=Math.min(1,1000/Math.max(1,p.offsetWidth));p.style.transform=`translateX(-50%) scale(${fit*lerp(.75,1,pi)*(1-po*.1)})`;
  const span=Math.min(dur*.6,ws.length*.28);ws.forEach((w,i)=>{const a=i/Math.max(1,ws.length)*span;const k=(dt-a)/.2;w.style.opacity=clamp(k*4);w.style.transform=`translateY(${(1-back(k))*26}px) scale(${k<0?.5:lerp(1.25,1,ease(k))})`});return []}}}})();
