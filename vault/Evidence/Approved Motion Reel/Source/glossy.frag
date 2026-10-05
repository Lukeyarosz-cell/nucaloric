#version 330
uniform vec2 resolution;
uniform float time;
uniform float pulse;
out vec4 fragColor;
mat2 rot(float a){return mat2(cos(a),-sin(a),sin(a),cos(a));}
float smin(float a,float b,float k){float h=clamp(.5+.5*(b-a)/k,0.,1.);return mix(b,a,h)-k*h*(1.-h);}
float map(vec3 p){
 vec3 world=p;
 p.xz=rot(time*.6+.4)*p.xz;p.xy=rot(time*.28)*p.xy;
 float a=length(p-vec3(-.65,.23*sin(time*1.8),0))-.92;
 float b=length(p-vec3(.7,.2,-.12))-.92;
 float c=length(p-vec3(.05,.85,.18))-.78;
 float d=smin(smin(a,b,.8),c,.7);
 float ring=length(vec2(length(p.xy)-1.05,p.z))-.43;
 float blend=.5+.5*sin(time*2.4-1.5);
 float main=mix(ring,d,blend);
 float sat1=length(world-vec3(2.65+.12*sin(time*2.),.85+.15*cos(time),-1.2))-.50;
 float sat2=length(world-vec3(2.2+.17*cos(time),-1.25,-.65))-.43;
 return min(main,min(sat1,sat2));
}
vec3 normal(vec3 p){vec2 e=vec2(.002,0);return normalize(vec3(map(p+e.xyy)-map(p-e.xyy),map(p+e.yxy)-map(p-e.yxy),map(p+e.yyx)-map(p-e.yyx)));}
vec3 studio(vec3 r){
 vec3 col=vec3(.009,.004,.007)+vec3(.055,.016,.029)*max(0.,r.y);
 float strip1=exp(-pow((r.x+.30)/.085,2.))*smoothstep(-.6,.2,r.y)*smoothstep(-.4,.1,r.z);
 float strip2=exp(-pow((r.y+.25)/.06,2.))*smoothstep(-.6,.1,r.z);
 float strip3=pow(max(0.,dot(r,normalize(vec3(-.45,.7,.4)))),38.);
 col+=vec3(3.5,3.46,3.41)*strip1+vec3(2.2,1.03,1.61)*strip2+vec3(2.2)*strip3;
 return col;
}
void main(){
 vec2 uv=(gl_FragCoord.xy-.5*resolution)/resolution.y;
 float zoom=1.+.07*pulse;vec3 ro=vec3(.2*sin(time*.7),.12,8.3/zoom);
 vec3 rd=normalize(vec3(uv,-1.8));float travel=0.;bool hit=false;vec3 pos;
 for(int i=0;i<88;i++){
  pos=ro+travel*rd;float d=map(pos);
  if(d<.001){hit=true;break;}travel+=d*.72;if(travel>12.)break;
 }
 vec3 col=vec3(.001,.001,.002);col+=vec3(.015,.003,.007)*exp(-length(uv-vec2(.5,-.35))*2.5);
 if(hit){
  vec3 n=normal(pos);vec3 refl=reflect(rd,n);float fres=pow(1.-max(0.,dot(n,-rd)),5.);
  vec3 chrome=studio(refl);vec3 pink=vec3(.79,.37,.53);
  float diffuse=max(0.,dot(n,normalize(vec3(-.4,.8,1))));
  col=chrome*mix(vec3(.72,.39,.53),vec3(.97,.92,.90),fres*.65)+pink*.09*diffuse;
  col+=vec3(.8,.62,.69)*pow(max(0.,dot(reflect(-normalize(vec3(-.6,.9,1)),n),-rd)),90.)*.8;
  col*=.85+.15*smoothstep(-1.3,1.2,pos.y);
 }
 col=col/(col+vec3(.6));col=pow(col,vec3(1./2.2));
 fragColor=vec4(col,1.);
}
