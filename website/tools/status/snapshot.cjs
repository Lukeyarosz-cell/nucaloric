const fs=require('node:fs'),path=require('node:path');
const {collect}=require('./monitor.cjs');
(async()=>{const result=await collect();result.mode='snapshot';result.ownServices=result.ownServices.map(s=>s.status==='not_connected'?s:{...s,status:'unknown',reason:'Saved observation; current server health requires the live API.'});fs.writeFileSync(path.resolve(__dirname,'../../data/service-status.json'),JSON.stringify(result,null,2)+'\n');console.log('Saved dated provider observation:',result.generatedAt);})();
