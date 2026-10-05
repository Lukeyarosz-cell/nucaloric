const http=require('node:http'), fs=require('node:fs'), path=require('node:path');
const {status}=require('./monitor.cjs');
const root=path.resolve(__dirname,'../..');
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.ico':'image/x-icon','.mp4':'video/mp4','.ttf':'font/ttf'};
function json(res,code,body){res.writeHead(code,{'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(JSON.stringify(body));}
const server=http.createServer(async(req,res)=>{
  if (!['GET','HEAD'].includes(req.method)) {json(res,405,{error:'Method not allowed'});return;}
  let pathname;
  try {pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);} catch {json(res,400,{error:'Bad path'});return;}
  if(pathname==='/api/service-status'){try{const result=await status();json(res,200,result);}catch{json(res,503,{error:'Status collector unavailable'});}return;}
  if(pathname==='/api/health'){json(res,200,{status:'operational',checkedAt:new Date().toISOString(),scope:'website-monitor-process'});return;}
  if(pathname.split('/').some(p=>p.startsWith('.')) || /^\/(tools|docs)\//.test(pathname)){json(res,404,{error:'Not found'});return;}
  const filename=path.resolve(root,'.'+(pathname==='/'?'/index.html':pathname));
  try{
    const real=await fs.promises.realpath(filename);
    if(!real.startsWith(root+path.sep) || !(await fs.promises.stat(real)).isFile() || !types[path.extname(real)]) throw new Error('path');
    res.writeHead(200,{'Content-Type':types[path.extname(real)],'Cache-Control':'no-cache','X-Content-Type-Options':'nosniff','Referrer-Policy':'strict-origin-when-cross-origin'});
    if(req.method==='HEAD'){res.end();return;}
    fs.createReadStream(real).on('error',()=>res.destroy()).pipe(res);
  }catch{json(res,404,{error:'Not found'});}
});
server.listen(Number(process.env.PORT||8080),process.env.HOST||'127.0.0.1',()=>console.log('NUCALORIC website and service monitor ready'));
// Warm the fixed, verified provider feeds; never accept a probe URL from a browser.
status().catch(()=>{});
