const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const base=process.env.REVIEW_BASE_URL||'http://127.0.0.1:8080',dir=process.env.REVIEW_OUTPUT||path.resolve(__dirname,'../../docs/review-results');
const serviceCatalog=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../data/services.json'))),serviceTotal=serviceCatalog.services.length,feedTotal=serviceCatalog.services.filter(s=>s.statusSource).length;
(async()=>{
 fs.mkdirSync(dir,{recursive:true});const b=await chromium.launch({executablePath:process.env.REVIEW_BROWSER==='bundled'?chromium.executablePath():(process.env.REVIEW_BROWSER||'/usr/bin/brave'),headless:true});const page=await b.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});const checks=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
 const check=(name,passed)=>{checks.push({name,passed});assert.ok(passed,name);};
 try{
  await page.goto(base+'/status.html');await page.locator('.service-row').first().waitFor();
  check('all documented services appear',await page.locator('.service-row').count()===serviceTotal);
  check('website connectors remain explicitly not connected',await page.locator('.service-row .service-signal:last-child [data-state="not_connected"]').count()===serviceTotal);
  check('verified provider feeds have current observations',(await page.locator('#statusFreshness').innerText()).includes('Live monitor'));
  await page.locator('#serviceSearch').fill('Meteora');check('search isolates intended provider',await page.locator('.service-row').count()===1 && await page.locator('[data-service="meteora"]').count()===1);
  check('Meteora has no invented green feed',await page.locator('[data-service="meteora"] .service-signal').first().locator('[data-state="unknown"]').count()===1);
  await page.locator('#serviceSearch').fill('');await page.locator('#statusFilter').selectOption('pending');check('pending integrations are not classified as outages',await page.locator('.service-row').count()===serviceTotal);
  await page.locator('#statusFilter').selectOption('ours');check('no fake connector failures before connection',await page.locator('.service-row').count()===0);
  await page.locator('#statusFilter').selectOption('all');await page.screenshot({path:path.join(dir,'status-1440.png'),fullPage:true});
  await page.goto(base+'/roadmap.html');await page.locator('.roadmap-stage').first().waitFor();check('seven stages render',await page.locator('.roadmap-stage').count()===7);
  check('roadmap exposes completion gates',await page.locator('.stage-gates li').count()===3);
  await page.locator('#roadmapFilter').selectOption('access');check('access focus highlights four tracks while retaining graph context',await page.locator('.flow-node:not(.flow-muted)').count()===4&&await page.locator('.flow-node').count()===7);
  await page.locator('#roadmapFilter').selectOption('all');await page.locator('[data-xpay]').click();await page.waitForURL('**/roadmap.html#phase-6');await page.locator('#phase-6').waitFor();check('X Pay leads to the conditional payments plan',(await page.locator('#phase-6').innerText()).includes('Access unconfirmed'));
  await page.goto(base+'/roadmap.html');await page.locator('.roadmap-stage').first().waitFor();await page.screenshot({path:path.join(dir,'roadmap-1440.png'),fullPage:true});
  const fixture=await (await page.request.get(base+'/api/service-status')).json();fixture.generatedAt=new Date().toISOString();
  for(const s of fixture.services){s.provider.status=s.provider.reason==='provider_report'?'operational':'unknown';s.provider.incidents=[];}
  fixture.services.find(s=>s.id==='solana').provider.status='outage';
  fixture.services.find(s=>s.id==='paymenter').connector={status:'degraded',reason:'authentication',checkedAt:new Date().toISOString()};
  await page.route('**/api/service-status',route=>route.fulfill({json:fixture}));
  await page.goto(base+'/status.html');await page.locator('.service-row').first().waitFor();
  await page.locator('#statusFilter').selectOption('issues');check('provider outage view isolates external Solana incident',await page.locator('.service-row').count()===1 && await page.locator('[data-service="solana"]').count()===1);
  await page.locator('#statusFilter').selectOption('ours');check('our failure view isolates Paymenter authentication failure',await page.locator('.service-row').count()===1 && await page.locator('[data-service="paymenter"]').count()===1);
  check('internal authentication error has explicit attribution',(await page.locator('[data-service="paymenter"] .service-signal:last-child').innerText()).includes('authentication'));
  check('internal failure does not invent Paymenter provider outage',await page.locator('[data-service="paymenter"] .service-signal:nth-child(2) [data-state="unknown"]').count()===1);
  await page.unroute('**/api/service-status');
  const snapshot=JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../data/service-status.json')));snapshot.generatedAt=new Date(Date.now()-3600_000).toISOString();
  await page.route('**/api/service-status',route=>route.fulfill({json:snapshot}));
  await page.goto(base+'/status.html');await page.locator('.service-row').first().waitFor();
  check('stale monitor exposes expired evidence warning',(await page.locator('#statusNotice').innerText()).includes('stale'));
  check('stale snapshot cannot show green provider health',await page.locator('.service-row .service-signal:nth-child(2) [data-state="operational"]').count()===0);
  check('stale monitor does not claim current website health',await page.locator('#ownHealth [data-state="operational"]').count()===0);
  check('snapshot preserves integration readiness separately',await page.locator('.service-row .service-signal:last-child [data-state="not_connected"]').count()===serviceTotal);
  await page.route('**/api/service-status',route=>route.abort());for(const service of JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../data/services.json'))).services){if(service.statusSource)await page.route(service.statusSource.url,route=>route.abort());}await page.route('**/data/service-status.json',route=>route.abort());await page.locator('#refreshStatus').click();await page.waitForFunction(total=>document.querySelector('#statusNotice').textContent.includes(`0 of ${total}`),serviceTotal);
  check('unreadable public feeds are unknown, never all operational',await page.locator('.service-row [data-state="operational"]').count()===0);
  await page.unroute('**/api/service-status');await page.unroute('**/data/service-status.json');for(const service of JSON.parse(fs.readFileSync(path.resolve(__dirname,'../../data/services.json'))).services){if(service.statusSource)await page.unroute(service.statusSource.url);}
  for(const name of ['status','roadmap']){await page.setViewportSize({width:390,height:844});await page.goto(base+'/'+name+'.html');await page.locator(name==='status'?'.service-row':'.roadmap-stage').first().waitFor();check(name+' mobile has no horizontal overflow',await page.evaluate(()=>document.documentElement.scrollWidth===innerWidth));await page.screenshot({path:path.join(dir,name+'-390.png'),fullPage:true});}
  check('no browser execution errors',errors.length===0);
 }finally{fs.writeFileSync(path.join(dir,'operations.json'),JSON.stringify({checks,errors},null,2));await b.close();}
 console.log(JSON.stringify({passed:checks.length,errors},null,2));
})().catch(e=>{console.error(e.message);process.exitCode=1});
