// Read-only access checks. Never log response bodies, tokens, endpoint URLs, or accounts.
const action=process.argv[2] || 'help';
async function probe(url,options={}){
  const r=await fetch(url,{...options,redirect:'error',signal:AbortSignal.timeout(10_000)});
  console.log(JSON.stringify({check:action,reachable:true,httpStatus:r.status,authorized:r.ok}));
  if(!r.ok)process.exitCode=1;
  return r;
}
(async()=>{
  if(action==='sdk'){
    const solana=require('@solana/web3.js');const meteora=await import('@meteora-ag/dynamic-bonding-curve-sdk');const x=await import('@xdevplatform/xdk');
    console.log(JSON.stringify({solanaSDK:typeof solana.Connection==='function',meteoraSDKExports:Object.keys(meteora).length,xSDK:typeof x.Client==='function',transactionSubmitted:false}));
  }else if(action==='solana'){
    const endpoint=process.env.SOLANA_RPC_URL || 'https://api.devnet.solana.com';
    const url=new URL(endpoint);if(url.protocol!=='https:')throw new Error('config');
    const r=await probe(url,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jsonrpc:'2.0',id:1,method:'getHealth'})});
    const d=await r.json();console.log(JSON.stringify({rpcHealthy:d.result==='ok',rpcErrorCode:d.error?.code || null}));
    if(d.result!=='ok')process.exitCode=1;
  }else if(action==='x'){
    if(!process.env.X_BEARER_TOKEN){console.log('Not configured. X developer-app access and a server-side bearer token are required.');process.exitCode=2;return;}
    const {Client}=await import('@xdevplatform/xdk');
    const client=new Client({bearerToken:process.env.X_BEARER_TOKEN});
    const result=await client.users.getByUsername('XDevelopers');
    console.log(JSON.stringify({check:'x',authorized:!!result.data,accountDataLogged:false}));
    if(!result.data)process.exitCode=1;
  }else if(action==='paymenter'){
    if(!process.env.PAYMENTER_URL || !process.env.PAYMENTER_API_TOKEN){console.log('Not configured. Provide a deployed portal URL and server-side API token through environment variables.');process.exitCode=2;return;}
    const base=new URL(process.env.PAYMENTER_URL);if(base.protocol!=='https:' || base.username || base.password || base.search)throw new Error('config');
    await probe(new URL('/api/v1/admin/services',base),{headers:{Authorization:'Bearer '+process.env.PAYMENTER_API_TOKEN,Accept:'application/json'}});
  }else{
    console.log('Usage: node access-check.cjs sdk|solana|x|paymenter\nX social: developer app access and OAuth setup required; see docs/API_ACCESS.md.\nX Money: official merchant API access remains unconfirmed.');
  }
})().catch(()=>{console.error('Check failed. Verify network, configuration and account access. Details withheld to protect credentials.');process.exitCode=1;});
