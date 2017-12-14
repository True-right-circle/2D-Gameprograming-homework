import random
from run_in_game import*
from pico2d import*
import time
from math import*

class Background:
    def __init__(self,w,h):
        self.image=load_image('ground.png')
        self.frame=0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.g_speed=5.0
        self.checktime=0
        
    def update(self):
        self.checktime+=0.0001
        self.left=(self.left+self.g_speed)%self.image.w
        self.g_speed+=self.checktime/10
        
    def draw(self):
        x=int(self.left)
        w=min(self.image.w-x,self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,0)


class Mountain:
    def __init__(self,w,h):
        self.moring_image=load_image('mountain.png')
        self.noon_image=load_image('mountain_noon.png')
        self.night_image=load_image('mountain_night.png')
        self.noon_frame=0
        self.night_frame=0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.m_speed=3.0
        self.checktime=0
        
    def update(self):
        self.checktime+=0.0001
        self.left=(self.left+self.m_speed)%self.moring_image.w
        self.m_speed+=self.checktime/10
        
    def draw(self):
        if self.noon_frame<=1 and self.night_frame<=0:
            self.noon_frame+=0.005
        if self.noon_frame>=1 and self.night_frame<=1:
            self.night_frame+=0.005
        if self.night_frame>=1:
            self.noon_frame=0
        if self.noon_frame<=0 and self.night_frame>0:
            self.night_frame-=0.005
            
        x=int(self.left)
        w=min(self.moring_image.w-x,self.screen_width)
        
        self.moring_image.clip_draw_to_origin(x,0,w,self.screen_height,0,100)
        self.moring_image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,100)

        self.noon_image.clip_draw_to_origin(x,0,w,self.screen_height,0,100)
        self.noon_image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,100)

        self.night_image.clip_draw_to_origin(x,0,w,self.screen_height,0,100)
        self.night_image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,100)

        #self.moring_image.clip_draw_to_origin(x,0,w,self.screen_height,0,100)
        #self.moring_image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,100)

        self.noon_image.opacify(self.noon_frame)
        self.night_image.opacify(self.night_frame)

        
class Sun:
    def __init__(self):
        self.x,self.y=200,100
        self.run_frame=0
        self.radius =800
        self.angle=0
        self.check_sun=1
        self.check_moon=1
        self.image=load_image('sun.png')

    def update(self):
        self.angle+=0.01
        self.x=300+(self.radius*cos(self.angle))
        self.y=-480+(self.radius*sin(self.angle))
        #if(self.x<-70):
         #   self.angle=0
          #  self.x=300+(self.radius*cos(self.angle))
        
    def draw(self):
        self.image.draw(self.x,self.y)
        
class Moon:
    def __init__(self):
        self.x,self.y=-100,-100
        self.run_frame=0
        self.radius =800
        self.m_angle=360.0
        self.image=load_image('moon.png')
        
    def update(self):
        self.m_angle-=0.01  
        self.x=300+(self.radius*cos(self.m_angle))
        self.y=-480-(self.radius*sin(self.m_angle))
        
    def draw(self):
        self.image.draw(self.x,self.y)

