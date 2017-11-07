import random
from run_in_game import*
from pico2d import*
speed=5.0
class nBackground:
    def __init__(self):
        self.image=load_image('back_pink.png')
        self.x,self.y=1600,300
        
    def draw(self):
        self.image.draw(self.x,self.y)
        
    def update(self):
        if(self.x>-600):
            self.x-=speed
        elif(self.x<=-600):
            self.x=1400

class Background:
    def __init__(self):
        self.image=load_image('back_pink.png')
        self.x,self.y=400,300
        
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        if(self.x>-600):
            self.x-=speed
        elif(self.x<=-600):
            self.x=1400
