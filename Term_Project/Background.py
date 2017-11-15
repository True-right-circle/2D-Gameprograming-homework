import random
from run_in_game import*
from pico2d import*
speed=8.0
cloudspeed=5.0
class nBackground:
    def __init__(self):
        self.image=load_image('back_tree.png')
        self.x,self.y=1950,430
        
    def draw(self):
        self.image.draw(self.x,self.y)
        
    def update(self):
        if(self.x>-1000):
            self.x-=speed
        elif(self.x<=-600):
            self.x=1950


class Background:
    def __init__(self):
        self.image=load_image('back_tree.png')
        self.x,self.y=400,430
        
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        if(self.x>-1000):
            self.x-=speed
        elif(self.x<=-600):
            self.x=1950
            
class SkyBackground:
    def __init__(self):
        self.image=load_image('sky.png')
        self.x,self.y=400,430
    def draw(self):
        self.image.draw(self.x,self.y)

class Cloudground:
    def __init__(self):
        self.image=load_image('cloud.png')
        self.x,self.y=400,230
    def draw(self):
        self.image.draw(self.x,self.y)
        
    def update(self):
        if(self.x>-650):
            self.x-=cloudspeed
        elif(self.x<=-650):
            self.x=1950    

