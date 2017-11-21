import random
from run_in_game import*
from pico2d import*
from math import*

radius=700
angle=0

class enemy:
     def __init__(self):
        self.x,self.y=1000,(random.randint(9,13)*10)
        self.run_frame=0
        self.run_image=load_image('flying_sheet.png')
        
     def update(self,enemyspeed,check_time):
         global radius,angle
         angle+=0.02
         self.run_frame=(self.run_frame+1)%8
         self.x=400+(radius*cos(angle))
         self.y=-480+radius*sin(angle)
 
     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
    
