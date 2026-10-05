const fs = require('node:fs');
const path = require('node:path');
const catalog = JSON.parse(fs.readFileSync(path.resolve(__dirname, '../../data/services.json')));
const TTL = 60_000, STALE_AFTER = 180_000;
const ownConnectors=[{id:'project-api',name:'Project API & identity'},{id:'workspace-provisioner',name:'Workspace provisioner'},{id:'terminal-gateway',name:'Terminal gateway'},{id:'ai-gateway',name:'AI gateway'},{id:'machine-bridge',name:'Own-hardware bridge'}];
const {parseProvider}=require('../../provider-status.js');
async function getJSON(url, options={}) {
  const response = await fetch(url, { ...options, redirect:'error', signal:AbortSignal.timeout(10_000), headers:{ Accept:'application/json', ...options.headers } });
  if (!response.ok) throw new Error('fetch');
  if (!response.headers.get('content-type')?.includes('json')) throw new Error('format');
  const text = await response.text();
  if (text.length > 2_000_000) throw new Error('size');
  return JSON.parse(text);
}
async function providerObservation(service) {
  const source = service.statusSource;
  if (!source) return {status:'unknown',checkedAt:null,reason:'no_verified_feed',source:null,components:[],incidents:[]};
  try {
    const result = parseProvider(await getJSON(source.url), source);
    return {...result, checkedAt:new Date().toISOString(), reason:'provider_report', source:source.page};
  } catch {
    // A collector error is NOT evidence that the provider is down.
    return {status:'unknown',checkedAt:new Date().toISOString(),reason:'feed_unavailable',source:source.page,components:[],incidents:[]};
  }
}
const reasons = new Set(['healthy','authentication','quota','timeout','backend_error','provider_error','maintenance','unknown']);
function normalizeConnector(report, observedAt) {
  if (!report || !['operational','degraded','outage','maintenance','unknown'].includes(report.status)) return { status:'unknown',reason:'invalid_health_report',checkedAt:observedAt };
  const ts = Date.parse(report.checkedAt);
  if (!Number.isFinite(ts) || Date.now()-ts > STALE_AFTER || ts > Date.now()+30_000) return {status:'unknown',reason:'stale_health_report',checkedAt:report.checkedAt || null};
  return {status:report.status,reason:reasons.has(report.reason)?report.reason:'unknown',checkedAt:report.checkedAt};
}
function internalURL(value) {
  const url = new URL(value);
  if (url.username || url.password || url.search || url.hash || (url.protocol !== 'https:' && !(url.protocol==='http:' && ['localhost','127.0.0.1','[::1]'].includes(url.hostname)))) throw new Error('invalid internal health URL');
  return url.href;
}
async function connectors() {
  const url = process.env.NUC_INTERNAL_HEALTH_URL;
  const targets=[...catalog.services,...ownConnectors];
  if (!url) return Object.fromEntries(targets.map(s=>[s.id,{status:'not_connected',reason:'not_configured',checkedAt:null}]));
  let body;
  try { body = await getJSON(internalURL(url),{headers:process.env.NUC_INTERNAL_HEALTH_TOKEN ? {Authorization:'Bearer '+process.env.NUC_INTERNAL_HEALTH_TOKEN} : {}}); if(!body.services || typeof body.services !== 'object') throw new Error('schema'); }
  catch { return Object.fromEntries(targets.map(s=>[s.id,{status:'unknown',reason:'internal_feed_unavailable',checkedAt:new Date().toISOString()}])); }
  return Object.fromEntries(targets.map(s=>[s.id,body.services[s.id] ? normalizeConnector(body.services[s.id],new Date().toISOString()) : {status:'not_connected',reason:'not_configured',checkedAt:null}]));
}
let cached, pending;
async function collect() {
  const [providers, own] = await Promise.all([Promise.all(catalog.services.map(providerObservation)), connectors()]);
  const at=new Date().toISOString();
  const failures=providers.filter(p=>p.reason==='feed_unavailable').length;
  const covered=providers.filter(p=>p.reason==='provider_report').length;
  return {schemaVersion:1,generatedAt:at,staleAfterSeconds:STALE_AFTER/1000,environment:process.env.NUC_STATUS_ENVIRONMENT === 'production' ? 'Production monitor' : 'Local preview monitor',mode:'live',coverage:{monitored:covered,total:catalog.services.length},ownServices:[{id:'web',name:'Website / monitor server',status:'operational',reason:'This request reached the server.',checkedAt:at},{id:'collector',name:'Provider status collector',status:failures?'degraded':'operational',reason:failures?`${failures} configured feed(s) could not be read.`:`${covered} configured feeds checked; unconfigured feeds remain unknown.`,checkedAt:at},...ownConnectors.map(s=>({...s,...own[s.id],reason:own[s.id].status==='not_connected'?'Backend component is not deployed or monitored.':`Internal observation: ${own[s.id].reason}.`}))],services:catalog.services.map((s,i)=>({id:s.id,name:s.name,category:s.category,provider:providers[i],connector:own[s.id]}))};
}
async function status() {
  if (cached && Date.now()-Date.parse(cached.generatedAt) < TTL) return cached;
  if (!pending) pending=collect().then(result=>{cached=result;return result}).finally(()=>pending=null);
  return pending;
}
module.exports={catalog,parseProvider,providerObservation,normalizeConnector,internalURL,status,collect,STALE_AFTER};
