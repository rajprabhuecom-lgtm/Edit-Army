// node render.js <worker> <nworkers> [frames.json]  -> /home/user/w/ov/NNNNN.png + ov/blur_<w>.json
const {chromium}=require('playwright');const fs=require('fs');const W='/home/user/w';
const [w,n,only]=[+process.argv[2],+process.argv[3],process.argv[4]];
(async()=>{const tl=JSON.parse(fs.readFileSync(`${W}/gfx/timeline.json`));const FPS=tl.fps;const nfr=tl.lay.length;
 let idx=only?JSON.parse(fs.readFileSync(only)):[];if(!only)for(let i=w;i<nfr;i+=n)idx.push(i);
 const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto(`file://${W}/gfx/engine.html`);await pg.evaluate(tl=>init(tl),tl);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(500);
 const blur={};
 for(let k=0;k<idx.length;k++){const i=idx[k];const r=await pg.evaluate(t=>setT(t),i/FPS);
  if(r.v)await pg.screenshot({path:`${W}/ov/${String(i).padStart(5,'0')}.png`,omitBackground:true});if(r.blur.length)blur[i]=r.blur;
  if(k%500==0)console.log(w,k,idx.length)}
 fs.writeFileSync(`${W}/ov/blur_${w}${only?'_p':''}.json`,JSON.stringify(blur));if(errs.length)console.log('ERR',errs.slice(0,5));await b.close()})();
