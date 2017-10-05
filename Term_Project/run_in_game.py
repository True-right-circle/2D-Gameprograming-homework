import game_framework
import random
from pico2d import*

name='MainState'

class Background:
    image=None
    
    def __init__(self):
        self.image=load_image('back_pink.png')
 
    def draw(self):
        self.image.draw(400,300)

class Main_Char:
    def __init__(self):
        self.x,self.y=50,90
        self.frame=0
        self.image=load_image('char_sheet.png')

    def update(self):
        self.frame=random.randint(0,7)
        
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
    del(background)
    del(boy)
    
def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
            
def update():
    boy.update()
    
def draw():
    while running:
        update()
        clear_canvas()
        drawback()
        boy.draw()
        update_canvas()
        delay(0.05)
    
def pause():
    pass

def resume():
    pass


def drawback():
    global background
    background.draw()
