import random
from run_in_game import*
from pico2d import*
import time
from math import*

g_speed=5.0
m_speed=3.0
m_angle=360.0

radius=800
angle=0


class Background:
    def __init__(self,w,h):
        self.image=load_image('ground.png')

        self.frame=0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        
    def update(self):
        global speed
        self.left=(self.left+g_speed)%self.image.w
        
    def draw(self):
        x=int(self.left)
        w=min(self.image.w-x,self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,0)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,0)


class Mountain:
    def __init__(self,w,h):
        self.image=load_image('mountain.png')

        self.frame=0
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        
    def update(self):
        global speed
        self.left=(self.left+m_speed)%self.image.w
        
    def draw(self):
        x=int(self.left)
        w=min(self.image.w-x,self.screen_width)
        self.image.clip_draw_to_origin(x,0,w,self.screen_height,0,100)
        self.image.clip_draw_to_origin(0,0,self.screen_width-w,self.screen_height,w,100)

class Sun:
    def __init__(self):
        self.x,self.y=-100,-100
        self.run_frame=0
        self.image=load_image('sun.png')

    def update(self):
        global radius,angle
        angle+=0.02
        self.x=200+(radius*cos(angle))
        self.y=-480+radius*sin(angle)

        
    def draw(self):
        self.image.draw(self.x,self.y)
        
class moon:
    def __init__(self):
        self.x,self.y=-100,-100
        self.run_frame=0
        self.image=load_image('moon.png')
        
    def update(self):
        global radius,m_angle,check_suny

        m_angle-=0.02
        self.x=200+(radius*cos(m_angle))
        self.y=-480-(radius*sin(m_angle))
        
    def draw(self):
        self.image.draw(self.x,self.y)
