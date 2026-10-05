/* Refresh the dated primary-source catalog. No credentials or blockchain writes. */
const fs=require('node:fs/promises'),path=require('node:path');
const mint=/^[1-9A-HJ-NP-Za-km-z]{32,44}$/;
async function read(url){const r=await fetch(url,{signal:AbortSignal.timeout(15000)});if(!r.ok)throw Error(`${new URL(url).host} returned ${r.status}`);return r;}
(async()=>{
 const [paidResponse,otcResponse]=await Promise.all([read('https://usepaid.app/'),read('https://otcdesks.cash/api/coins')]);
 const paidHtml=await paidResponse.text(),otc=await otcResponse.json();
 // Match actual listing anchors, not addresses mentioned in scripts or unrelated data.
 const paid=[...new Set([...paidHtml.matchAll(/<a\b[^>]*\bhref="\/token\/([1-9A-HJ-NP-Za-km-z]{32,44})"/g)].map(m=>m[1]))];
 if(!paid.length||!Array.isArray(otc.coins)||!otc.coins.length)throw Error('Primary-source listings were unavailable. Existing catalog retained.');
 const catalog={schemaVersion:1,checkedAt:new Date().toISOString(),sources:[{id:'otc',name:'OTC Desks',url:'https://otcdesks.cash/explore',endpoint:'https://otcdesks.cash/api/coins',mode:'live-with-snapshot'},{id:'paid',name:'PAID',url:'https://usepaid.app/',mode:'verified-snapshot'}],coins:[...otc.coins.filter(c=>mint.test(c.mint)).map(c=>({mint:c.mint,name:String(c.name||'').slice(0,100),symbol:String(c.symbol||'').slice(0,30),launchpad:'otc',sourceUrl:'https://otcdesks.cash/coin/'+c.mint})),...paid.map(mint=>({mint,launchpad:'paid',sourceUrl:'https://usepaid.app/token/'+mint}))]};
 const file=path.resolve(__dirname,'../../data/launchpads.json');await fs.writeFile(file+'.tmp',JSON.stringify(catalog,null,2)+'\n');await fs.rename(file+'.tmp',file);console.log(JSON.stringify({checkedAt:catalog.checkedAt,otc:catalog.coins.filter(c=>c.launchpad==='otc').length,paid:paid.length}));
})().catch(e=>{console.error(e.message);process.exitCode=1;});
