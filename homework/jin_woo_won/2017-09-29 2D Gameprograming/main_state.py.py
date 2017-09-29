import random
from pico2d import*
 
class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
 
    def draw(self):
        self.image.draw(400,30)
        
 
class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame=0
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame=random.randint(0,7)
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
 
 
open_canvas()
boy=Boy()
grass=Grass()
running=True
n=0
team=[Boy() for i in range(11)] 
            
def handle_mouseevents():
    global running
    global n
    select()
    events=get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
        elif event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y,=event.x,600-event.y
 
def enter():
    global team,grass
    team=Boy()
    grass = Grass()

def exit():
    gobal team, grass
    del(team)
    del(grass)

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

def update():
    team.update()
def draw():
    clear_canvas()
    grass.draw()
    team.draw()
    update_canvas()
    
def select():
    global running
    global n
    events=get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_1:
            n=1        
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            n=2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            n=3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            n=4    
        elif event.type == SDL_KEYDOWN and event.key == SDLK_5:
            n=5
        elif event.type == SDL_KEYDOWN and event.key == SDLK_6:
            n=6
        elif event.type == SDL_KEYDOWN and event.key == SDLK_7:
            n=7
        elif event.type == SDL_KEYDOWN and event.key == SDLK_8:
            n=8
        elif event.type == SDL_KEYDOWN and event.key == SDLK_9:
            n=9
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            n=10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            n=0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
            
while running:
    for i in range(11):
        team[i].update()
    clear_canvas()
    grass.draw()
    for i in range(11):
        team[i].draw()
    update_canvas()
    delay(0.05)
    handle_mouseevents()
 
close_canvas()
