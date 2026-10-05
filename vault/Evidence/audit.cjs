const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
const browser=await chromium.launch({executablePath:'/usr/bin/brave',headless:true});
const result={date:new Date().toISOString(),pages:[],interactions:[]};
const pages=['index','explorer','coin','launchpad','optimizer','rewards','ecosystem','registry','dashboard'];
fs.mkdirSync('/tmp/nucaloric-inspection/screenshots',{recursive:true});
for(const size of [{width:1440,height:1000},{width:390,height:844}]){
const ctx=await browser.newContext({viewport:size});
for(const name of pages){const page=await ctx.newPage();const errors=[];const failures=[];page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>failures.push({url:r.url(),error:r.failure()?.errorText}));
await page.goto(`http://127.0.0.1:3000/${name}.html`,{waitUntil:'domcontentloaded'});await page.waitForTimeout(1200);
const info=await page.evaluate(()=>({title:document.title,documentWidth:document.documentElement.scrollWidth,viewportWidth:innerWidth,canvases:document.querySelectorAll('canvas').length,h1:document.querySelectorAll('h1').length,description:!!document.querySelector('meta[name="description"]'),missingAlt:[...document.images].filter(i=>!i.hasAttribute('alt')).length,brokenImages:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src),unlabelledInputs:[...document.querySelectorAll('input,select,textarea')].filter(i=>!i.getAttribute('aria-label')&&!i.getAttribute('aria-labelledby')&&!i.labels?.length).map(i=>i.id),overflow:[...document.querySelectorAll('body *')].filter(e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();return s.position!=='fixed'&&s.display!=='none'&&r.width>0&&r.right>innerWidth+5}).slice(0,12).map(e=>e.tagName+'.'+e.className)}));
await page.screenshot({path:`/tmp/nucaloric-inspection/screenshots/${name}-${size.width}.png`,fullPage:true});result.pages.push({page:name,size:size.width,...info,errors,failures});await page.close();}
await ctx.close();}
const ctx=await browser.newContext({viewport:{width:1440,height:1000}});const p=await ctx.newPage();p.setDefaultTimeout(4000);
async function test(name,fn){try{await fn();result.interactions.push({name,pass:true})}catch(e){result.interactions.push({name,pass:false,error:e.message.slice(0,300)})}}
await p.goto('http://127.0.0.1:3000/explorer.html');
await test('Explore search filters coins',async()=>{await p.locator('#coinSearch').fill('vortex');if(await p.locator('.coin-card:visible').count()!==1)throw Error('Expected one coin');await p.locator('#coinSearch').fill('')});
await test('Quick View opens',async()=>{await p.locator('.coin-card').first().click();if(!await p.locator('.quick-drawer.open').count())throw Error('Drawer absent');await p.keyboard.press('Escape')});
await test('Watchlist persists across reload',async()=>{await p.locator('[data-watch-key]').first().click();const before=await p.evaluate(()=>localStorage.getItem('nucWatchlist'));await p.reload();const after=await p.evaluate(()=>localStorage.getItem('nucWatchlist'));if(!before||before!==after)throw Error('Persistence failed')});
await test('Compare modal opens with two coins',async()=>{await p.locator('[data-compare-key]').nth(0).click();await p.locator('[data-compare-key]').nth(1).click();await p.locator('#compareRun').click();if(!await p.locator('.compare-modal.open').count())throw Error('Compare absent');await p.keyboard.press('Escape')});
await test('Command palette filters and navigates',async()=>{await p.keyboard.press('Control+k');await p.locator('#commandSearch').fill('dashboard');await p.locator('[data-command-href="dashboard.html"]').click();await p.waitForURL('**/dashboard.html')});
await test('Dashboard shows persisted watchlist',async()=>{if(!await p.locator('#dashboardWatchlist .dash-watch-item').count())throw Error('Watchlist absent')});
await p.goto('http://127.0.0.1:3000/launchpad.html');
await test('Launch builder traverses eight stages',async()=>{await p.locator('#launchName').fill('Test Launch');await p.locator('#launchTicker').fill('TST');for(let i=0;i<7;i++)await p.locator('#builderNext').click();if((await p.locator('#builderNext').innerText())!=='DONE')throw Error('Final stage absent');});
await p.goto('http://127.0.0.1:3000/optimizer.html');
await test('Optimizer updates score and outputs',async()=>{await p.locator('#liq').evaluate(e=>{e.value='400';e.dispatchEvent(new Event('input',{bubbles:true}))});if(!(await p.locator('#liqOut').innerText()).includes('400'))throw Error('Output unchanged')});
await p.goto('http://127.0.0.1:3000/registry.html');
await test('Registry offline filter',async()=>{await p.locator('[data-reg-filter="offline"]').click();if(!await p.locator('.cap-card:visible').count())throw Error('No offline cards');if(await p.locator('.cap-card[data-cap-status="live"]:visible').count())throw Error('Live cards still visible')});
await test('Registry capability detail opens',async()=>{await p.locator('.cap-card:visible').first().click();if(!await p.locator('.capability-drawer.open').count())throw Error('Capability drawer absent');await p.keyboard.press('Escape')});
await p.goto('http://127.0.0.1:3000/coin.html?coin=vortex');
await test('Coin query selects Vortex',async()=>{if(!(await p.locator('h1').innerText()).includes('VORTEX'))throw Error('Wrong coin')});
await test('Coin tabs switch panels',async()=>{await p.locator('[data-coin-tab="holders"]').click();if(!await p.locator('[data-coin-panel="holders"].active').count())throw Error('Holders absent')});
await test('Wallet choice stores demo wallet',async()=>{await p.locator('[data-wallet]').first().click();await p.locator('.wallet-choice').first().click();if(!await p.evaluate(()=>localStorage.getItem('nucWallet')))throw Error('Wallet absent')});
fs.writeFileSync('/tmp/nucaloric-inspection/runtime-audit.json',JSON.stringify(result,null,2));console.log(JSON.stringify({pages:result.pages.map(x=>({page:x.page,size:x.size,errors:x.errors,overflow:x.documentWidth>x.viewportWidth,brokenImages:x.brokenImages.length})),interactions:result.interactions},null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
