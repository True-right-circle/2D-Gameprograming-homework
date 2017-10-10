import game_framework
import random
from pico2d import*

name='MainState'
image=None
jump_time=0.0
jump_check=0.0

class Background:
    def __init__(self):
        self.image=load_image('back_pink.png')
 
    def draw(self):
        self.image.draw(400,300)

class Main_Char:
    def __init__(self):
        self.x,self.y=50,90
        self.run_frame=0
        self.jump_frame=0
        self.run_image=load_image('new_char_sheet.png')
        self.jump_image=load_image('jump_sheet.png')

    def update(self):
        self.run_frame=(self.run_frame+1)%8
        self.jump_frame=(self.jump_frame+1)%2
        
    def draw(self):
        global jump
        if(jump==True):
            self.run_image.clip_draw(self.run_frame*100,0,100,100,self.x,self.y)
        elif(jump==False):
            self.jump_image.clip_draw(self.jump_frame*100,0,100,100,self.x,self.y)
            
    
def enter():
    global image,background,running,boy,jump
    boy=Main_Char()
    background = Background()
    jump=True
    running=True
    image=None

    
def exit():
    global background,boy
    del(boy)
    del(background)
    
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
    global jump,jump_time,jump_check
    boy.update()
    if(jump==False and jump_time<=2.0):
        jump_time+=1.0
        boy.y+=75.0
        jump_check+=75.0
    if(jump_time>=3.0):
        jump=True
        jump_time=0.0
    if(jump_check>=0):
        boy.y-=25.0
        jump_check-=25.0
         
def draw():
    while running:
        update()
        clear_canvas()
        background.draw()
        boy.draw()
        update_canvas()
        handle_events()
        delay(0.05)
    
def pause():
    pass

def resume():
    pass


