import game_framework
import random
from pico2d import*

name='MainState'
image=None

class Background:
    
    def __init__(self):
        self.image=load_image('back_pink.png')
 
    def draw(self):
        self.image.draw(400,300)

class Main_Char:
    def __init__(self):
        self.x,self.y=50,80
        self.frame=0
        self.image=load_image('new_char_sheet.png')

    def update(self):
        self.frame=(self.frame+1)%8
        
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
    
def enter():
    global image,background,running,boy
    boy=Main_Char()
    background = Background()
    running=True
    image=None

    
def exit():
    global background,boy
    del(boy)
    del(background)
    
def handle_events():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                running=False
                if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                    game_framework.quit()

            
def update():
    boy.update()
    
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


