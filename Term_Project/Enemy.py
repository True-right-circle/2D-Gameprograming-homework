import random
from run_in_game import*
from pico2d import*
from math import*



class enemy:
     def __init__(self):
        self.x,self.y=850,60#(random.randint(5,10)*10)
        self.run_frame=0
        self.run_image=load_image('flying_sheet.png')
        
     def update(self,enemyspeed):
         self.x-=enemyspeed
         self.run_frame=(self.run_frame+1)%8
         if(self.x<-100):
              self.x=850

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
         
     def get_bb(self):
          return self.x-6,self.y-18,self.x+14,self.y+5
     def draw_bb(self):
          draw_rectangle(*self.get_bb())
    
class G_enemy:
     def __init__(self):
        self.x,self.y=1050,55#(random.randint(5,10)*10)
        self.run_frame=0
        self.run_image=load_image('green_sheet.png')
        
     def update(self,enemyspeed):
         self.x-=enemyspeed
         self.run_frame=(self.run_frame+1)%8
         if(self.x<-50):
              self.x=1050

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
         
     def get_bb(self):
          return self.x-6,self.y-26,self.x+14,self.y+1
     def draw_bb(self):
          draw_rectangle(*self.get_bb())

class Block:
     def __init__(self):
        self.x,self.y=1080,(random.randint(12,15)*10)
        self.run_frame=0
        self.run_image=load_image('block.png')
        
     def update(self,enemyspeed):
         self.x-=enemyspeed-3
         self.run_frame=(self.run_frame+1)%1
         if(self.x<-50):
              self.x=1050

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,32,32,self.x,self.y)
         
     def get_bb(self):
          return self.x-14,self.y-15,self.x+14,self.y+12
     def draw_bb(self):
          draw_rectangle(*self.get_bb())
