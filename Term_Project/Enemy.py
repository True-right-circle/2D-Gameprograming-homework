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
         if(self.x<-50):
              self.x=850

     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
         
     def get_bb(self):
          return self.x-5,self.y-15,self.x+5,self.y+10      
    
