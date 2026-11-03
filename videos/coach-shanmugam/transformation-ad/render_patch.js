const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const tl=JSON.parse(fs.readFileSync('/home/user/w/gfx/timeline.json'));const js=JSON.parse(fs.readFileSync('/home/user/w/jobs.json'));
 const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1920}});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file:///home/user/w/gfx/engine.html');await pg.evaluate(tl=>init(tl),tl);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(500);
 for(const [n,t] of js){await pg.evaluate(t=>setT(t),t);await pg.screenshot({path:`/home/user/w/patch/${n}.png`,omitBackground:true})}
 if(errs.length)console.log('ERR',errs.slice(0,3));await b.close();console.log('done',js.length)})();
