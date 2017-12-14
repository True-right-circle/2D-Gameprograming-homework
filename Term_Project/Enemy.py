import random
from run_in_game import*
from pico2d import*
from math import*

class enemy:
     def __init__(self):
        self.x,self.y=850,50
        self.run_frame=0
        self.run_image=load_image('flying_sheet.png')
        
     def update(self,enemyspeed):
         self.x-=enemyspeed
         self.run_frame=(self.run_frame+1)%8
         if(self.x<-100):
              self.x=850
              self.y=random.randint(6,9)*10

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
         
     def get_bb(self):
          return self.x-3,self.y-18,self.x+11,self.y+5
     def draw_bb(self):
          draw_rectangle(*self.get_bb())
    
class G_enemy:
     def __init__(self):
        self.x,self.y=1050,55
        self.run_frame=0
        self.run_image=load_image('green_sheet.png')
        
     def update(self,enemyspeed2):
         self.x-=enemyspeed2
         self.run_frame=(self.run_frame+1)%8
         if(self.x<-50):
              self.x=1050

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
         
     def get_bb(self):
          return self.x-6,self.y-26,self.x+14,self.y+1
     def draw_bb(self):
          draw_rectangle(*self.get_bb())


