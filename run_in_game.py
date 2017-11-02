import game_framework
import random
from pico2d import*


name='MainState'
image=None
jump_time=0.0
jump_check=0.0
speed=5.0
enemyspeed =18.0
blockspeed=8.0

class enemy:
     def __init__(self):
        self.x,self.y=1400,90
        self.run_frame=0
        self.run_image=load_image('flying_sheet.png')
        
     def update(self):
         global flying
         self.run_frame=(self.run_frame+1)%8
         flying.x-=enemyspeed
         if(flying.x<0):
             flying.x=1400
     #def ebemykAI(self):    
     def draw(self):
         self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
    
class breadblock:
     def __init__(self):
        self.x,self.y=1200,200
        self.image=load_image('block1.png')
        
     def update(self):
         block1.x-=enemyspeed
         if(block1.x<-100):
             block1.x=1400
             
     def draw(self):
        self.image.draw(self.x,self.y)

     #def bloackAI(self):
          
class grayblock:
     def __init__(self):
        self.x,self.y=1200,60
        self.image=load_image('block2.png')
        
     def update(self):
         block2.x-=blockspeed
         if(block2.x<-100):
             block2.x=1400
             
     def draw(self):
        self.image.draw(self.x,self.y)
        
     #def graybloackAI(self):
        
class nBackground:
    def __init__(self):
        self.image=load_image('back_pink.png')
        self.x,self.y=1600,300
        
    def draw(self):
        self.image.draw(self.x,self.y)
        
    def update(self):
        if(nextbackground.x>-600):
            nextbackground.x-=speed
        elif(nextbackground.x<=-600):
            nextbackground.x=1400

class Background:
    def __init__(self):
        self.image=load_image('back_pink.png')
        self.x,self.y=400,300
        
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        if(background.x>-600):
            background.x-=speed
        elif(background.x<=-600):
            background.x=1400


class Main_Char:
    def __init__(self):
        self.x,self.y=50,90
        self.run_frame=0
        self.jump_frame=0
        self.run_image=load_image('new_char_sheet.png')
        self.jump_image=load_image('jump_sheet.png')

    def update(self):
        global jump,jump_time,jump_check,background
        self.run_frame=(self.run_frame+1)%8
        self.jump_frame=(self.jump_frame+1)%2
        #if(jump==False and jump_time<2.0):
        #    jump_time+=1.0
        #    boy.y+=105.0
        #    jump_check+=105.0
        #if(jump_time>=2.0):
        #    jump=True
        #    jump_time=0.0
        if(jump==False and jump_time<3.0):
            jump_time+=0.5
            boy.y+=50.0
            jump_check+=50.0
        if(jump_time>=3.0):
            jump=True
        if(jump_check>=0):
            boy.y-=25.0
            jump_check-=25.0
        if(jump_time==4.0):
             boy.y+=0.0
             jump_check+=0.0
        if(jump_check==0):
             jump_time=0.0
    def draw(self):
        global jump
        if(jump==True):
            self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
        elif(jump==False):
            self.jump_image.clip_draw(self.jump_frame*100,0,100,100,self.x,self.y)
            
    
def enter():
    global image,background,running,boy,jump,nextbackground,flying,block1,block2
    boy=Main_Char()
    background = Background()
    nextbackground=nBackground()
    flying=enemy()
    block1=breadblock()
    block2=grayblock()
    jump=True
    running=True
    image=None

    
def exit():
    global background,boy,nextbackground,flying,block1,block2
    del(boy)
    del(background)
    del(nextbackground)
    del(flying)
    del(block1)
    del(block2)
    
def handle_events():
    global running,jump,jump_time
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
             jump=False
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                running=False
                if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                    game_framework.quit()
                    
        
def update():
    global jump,jump_time,jump_check,background,flying,block1,block2
    boy.update()
    background.update()
    nextbackground.update()
    flying.update()
    block1.update()
    block2.update()
         
def draw():
    while running:
        update()
        clear_canvas()
        background.draw()
        nextbackground.draw()
        boy.draw()
        flying.draw()
        block1.draw()
        block2.draw()
        update_canvas()
        handle_events()
        delay(0.05)
    
def pause():
    pass

def resume():
    pass


