import moderngl,numpy as np,pathlib
from PIL import Image
class Glossy:
 def __init__(self,w=1920,h=1080):
  self.w=w;self.h=h;self.ctx=moderngl.create_standalone_context(backend='egl')
  vert='#version 330\nin vec2 in_pos;void main(){gl_Position=vec4(in_pos,0.,1.);}'
  self.prog=self.ctx.program(vertex_shader=vert,fragment_shader=(pathlib.Path(__file__).parent/'glossy.frag').read_text())
  buf=self.ctx.buffer(np.array([-1,-1,1,-1,-1,1,1,1],dtype='f4').tobytes());self.vao=self.ctx.simple_vertex_array(self.prog,buf,'in_pos')
  self.fbo=self.ctx.simple_framebuffer((w,h),components=3);self.prog['resolution'].value=(w,h)
 def render(self,time,pulse=0):
  self.fbo.use();self.prog['time'].value=time;self.prog['pulse'].value=pulse;self.vao.render(moderngl.TRIANGLE_STRIP)
  return Image.frombytes('RGB',(self.w,self.h),self.fbo.read(components=3,alignment=1)).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
if __name__=='__main__':
 g=Glossy();g.render(.8,.2).save(pathlib.Path(__file__).parents[1]/'output/glossy-test.jpg',quality=95)
 print(g.ctx.info['GL_RENDERER'])
