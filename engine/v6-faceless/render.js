// Render overlay/scene frames: node render.js <workdir> <worker> <nworkers> [framelist.json]
const {chromium}=require('playwright');const fs=require('fs');
const [W,w,n,only]=[process.argv[2],+process.argv[3],+process.argv[4],process.argv[5]];const FPS=30;
(async()=>{const tl=JSON.parse(fs.readFileSync(W+'/timeline.json'));const nfr=Math.round(tl.total*FPS);
 let idx=only?JSON.parse(fs.readFileSync(only)):[];if(!only)for(let i=w;i<nfr;i+=n)idx.push(i);
 fs.mkdirSync(W+'/ov',{recursive:true});
 const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file://'+W+'/engine.html');await pg.evaluate(tl=>init(tl),tl);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(800);
 for(let k=0;k<idx.length;k++){const i=idx[k];const vis=await pg.evaluate(t=>setT(t),i/FPS);
  if(vis)await pg.screenshot({path:`${W}/ov/${String(i).padStart(5,'0')}.png`,omitBackground:true});
  if(k%200==0)console.log(w,k,idx.length)}
 if(errs.length)console.log('ERR',errs.slice(0,3));await b.close()})();
