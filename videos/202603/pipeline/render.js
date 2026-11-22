// Render overlay frames: node render.js <vid> <worker> <nworkers> [frame list json]
const {chromium}=require('playwright');const fs=require('fs');
const [vid,w,n,only]=[process.argv[2],+process.argv[3],+process.argv[4],process.argv[5]];const FPS=30;const D=`/home/user/w/${vid}/`;
(async()=>{const tl=JSON.parse(fs.readFileSync(D+'gfx/timeline.json'));const nfr=Math.round(tl.total*FPS);
 let idx=only?JSON.parse(fs.readFileSync(only)):[];if(!only)for(let i=w;i<nfr;i+=n)idx.push(i);
 const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file:///home/user/w/engine.html');await pg.evaluate(tl=>init(tl),tl);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(400);
 for(let k=0;k<idx.length;k++){const i=idx[k];const vis=await pg.evaluate(t=>setT(t),i/FPS);
  const p=`${D}ov/${String(i).padStart(5,'0')}.png`;if(vis)await pg.screenshot({path:p,omitBackground:true});else if(fs.existsSync(p))fs.unlinkSync(p);
  if(k%400==0)console.log(vid,w,k,idx.length)}
 if(errs.length)console.log('ERR',errs.slice(0,3));await b.close()})();
