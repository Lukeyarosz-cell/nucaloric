const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const base=process.env.REVIEW_BASE_URL||'http://127.0.0.1:8080',dir=process.env.REVIEW_OUTPUT||path.resolve(__dirname,'../../docs/review-results');
(async()=>{
 fs.mkdirSync(dir,{recursive:true});const browser=await chromium.launch({executablePath:process.env.REVIEW_BROWSER==='bundled'?chromium.executablePath():(process.env.REVIEW_BROWSER||'/usr/bin/brave'),headless:true});const page=await browser.newPage({viewport:{width:1440,height:1000}}),checks=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
 const check=(name,result)=>{checks.push({name,passed:Boolean(result)});assert.ok(result,name);console.log('PASS',name)};
 try{
  await page.goto(base+'/status.html');await page.locator('.service-row').first().waitFor();
  const canvas=page.locator('.signature-art > canvas[data-dot-field]');await canvas.scrollIntoViewIfNeeded();await page.waitForTimeout(250);const first=await canvas.evaluate(c=>c.toDataURL());await page.waitForTimeout(500);check('status signal artwork animates',first!==await canvas.evaluate(c=>c.toDataURL()));
  await page.locator('[data-motion-toggle]').click();await page.waitForTimeout(80);const paused=await canvas.evaluate(c=>c.toDataURL());await page.waitForTimeout(300);check('pause control freezes the canvas',paused===await canvas.evaluate(c=>c.toDataURL()));check('pause announces its state',await page.locator('[data-motion-toggle]').getAttribute('aria-pressed')==='true');
  await page.goto(base+'/registry.html');await page.waitForTimeout(150);check('motion preference survives page navigation',(await page.locator('[data-motion-toggle]').innerText()).includes('RESUME'));
  await page.locator('[data-motion-toggle]').click();await page.waitForTimeout(80);const weave=page.locator('.signature-art > canvas[data-dot-field]');const unpaused=await weave.evaluate(c=>c.toDataURL());await page.waitForTimeout(500);check('resume restarts the shared dot motion',unpaused!==await weave.evaluate(c=>c.toDataURL()));
  check('each capability family has a dot composition',await page.locator('.registry-group .family-art canvas').count()===8);
  await page.emulateMedia({reducedMotion:'reduce'});await page.goto(base+'/studio.html');await page.waitForTimeout(200);const bloom=page.locator('.signature-art > canvas[data-dot-field]');const reduced=await bloom.evaluate(c=>c.toDataURL());await page.waitForTimeout(300);check('reduced motion is static',reduced===await bloom.evaluate(c=>c.toDataURL()));check('reduced motion cannot be bypassed with the pause toggle',await page.locator('[data-motion-toggle]').isDisabled());
  check('three project chapters are directly reachable',await page.locator('.studio-chapter-nav a').count()===3);
  const initial=await page.locator('#briefDetailsCount').innerText();await page.locator('[name="name"]').fill('A working draft');check('draft detail meter reflects real entered fields',initial!==await page.locator('#briefDetailsCount').innerText());
  await page.locator('.studio-chapter-nav a').nth(1).click();check('chapter navigation reaches the evidence section',page.url().endsWith('#brief-evidence') && await page.locator('#brief-evidence').evaluate(e=>{const r=e.getBoundingClientRect();return r.top<innerHeight && r.bottom>76}));
  await page.goto(base+'/status.html');await page.locator('.service-row').first().waitFor();const evidence=page.locator('[data-service="solana"] details');await evidence.locator('summary').click();await page.locator('#refreshStatus').click();await page.waitForFunction(()=>!document.querySelector('#refreshStatus').disabled);check('refresh preserves open provider evidence',await evidence.getAttribute('open')!==null);
  for(const width of [1440,390,320]){
   await page.setViewportSize({width,height:1000});
   for(const name of ['status','studio','registry','roadmap']){
    await page.goto(base+'/'+name+'.html');await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(200);
    check(name+' fits '+width+'px',await page.evaluate(()=>document.documentElement.scrollWidth===innerWidth));
    if(width!==320){await page.screenshot({path:path.join(dir,name+'-'+width+'.png'),fullPage:true});}
   }
  }
  check('no browser runtime errors',errors.length===0);
 }finally{fs.writeFileSync(path.join(dir,'creative-workspace.json'),JSON.stringify({checks,errors},null,2));await browser.close();}
})().catch(e=>{console.error(e.stack);process.exitCode=1});
