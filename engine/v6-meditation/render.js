// node render.js <outdir> <fps> <worker> <nworkers> [t1,t2,...]  -> chunk mp4 (or preview jpgs when times given)
const {chromium}=require('playwright');const fs=require('fs');const {spawn}=require('child_process');
const [out,FPS,w,n,list]=[process.argv[2],+process.argv[3],+process.argv[4],+process.argv[5],process.argv[6]];
(async()=>{const tl=JSON.parse(fs.readFileSync(__dirname+'/timeline.json'));
 const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
 const errs=[];pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file://'+__dirname+'/winddown.html');await pg.evaluate(()=>document.fonts.ready);
 await pg.evaluate(async()=>{for(const f of ['500 20px Corm','italic 500 20px Corm','300 20px Mont','500 20px Mont'])await document.fonts.load(f)});
 await pg.evaluate(tl=>init(tl),tl);await pg.waitForFunction(()=>document.getElementById('face').complete);
 const grab=t=>pg.evaluate(t=>{draw(t);return document.getElementById('c').toDataURL('image/jpeg',0.94).slice(23)},t);
 if(list){for(const t of list.split(',').map(Number)){fs.writeFileSync(`${out}/p_${String(t).padStart(6,'0')}.jpg`,Buffer.from(await grab(t),'base64'))}}
 else{const nfr=Math.round(tl.total*FPS), per=Math.ceil(nfr/n), a=w*per, e=Math.min(nfr,a+per);
  const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','17','-tune','grain','-pix_fmt','yuv420p',`${out}/chunk_${w}.mp4`],{stdio:['pipe','inherit','inherit']});
  const t0=Date.now();
  for(let i=a;i<e;i++){const buf=Buffer.from(await grab(i/FPS),'base64'); if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
   if((i-a)%600==0)console.log(`w${w} ${i-a}/${e-a} ${((Date.now()-t0)/1000).toFixed(0)}s`)}
  ff.stdin.end(); await new Promise(r=>ff.on('close',r));}
 if(errs.length)console.log('ERR',errs.slice(0,3));await b.close()})();
