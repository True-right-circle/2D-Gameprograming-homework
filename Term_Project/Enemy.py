import random
from run_in_game import*
from pico2d import*
enemyspeed =18.0
blockspeed=8.0

class enemy:
     def __init__(self):
        self.x,self.y=1400,(random.randint(9,13)*10)
        self.run_frame=0
        self.run_image=load_image('flying_sheet.png')
        
     def update(self):
         self.run_frame=(self.run_frame+1)%8
         self.x-=enemyspeed
         if(self.x<0):
             self.x=1400
             self.y=(random.randint(8,20)*10)
     #def enemykAI(self):    
     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
    
class breadblock:
     def __init__(self):
        self.x,self.y=1200,200
        self.image=load_image('block1.png')
        
     def update(self):
         self.x-=enemyspeed
         if(self.x<-100):
             self.x=1400
             
     def draw(self):
        self.image.draw(self.x,self.y)

     #def bloackAI(self):
          
class grayblock:
     def __init__(self):
        self.x,self.y=1200,60
        self.image=load_image('block2.png')
        
     def update(self):
         self.x-=blockspeed
         if(self.x<-100):
             self.x=1400
             
     def draw(self):
        self.image.draw(self.x,self.y)
        
     #def graybloackAI(self):
        
