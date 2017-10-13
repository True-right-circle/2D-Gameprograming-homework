from boy_ai import*
import game_framework
import random
from pico2d import*
import title_state



name = 'MainState'

font = None
char_font = None
  


def handle_mouseevents():
    global running,n,team
    select()
    events=get_events()
    for event in events:
        global team
        if event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y,=event.x,600-event.y


def enter():
    global team,grass,boy,n,running,image,font,char_font
    team=[Boy() for i in range(member)] 
    grass = Grass()
    font=load_font('ENCR10B.TTF',50)
    char_font=load_font('ENCR10B.TTF',25)
    running=True
    image=None

    
def exit():
    global team, grass
    del(team)
    del(grass)

def handle_events():
    global team
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()

def update():
    global team
    for i in range(member):
        team[i].update()
        
def draw():
    global team
    while running:
        global n
        update()
        clear_canvas()
        grass.draw()
        font.draw(730,560,str(n))
        char_font.draw(team[n].x-50,team[n].y+50,'This Boy')
        char_font.draw(team[n].x-50,team[n].y-15,str(n))
        for i in range(member):
            team[i].draw()   
        update_canvas()
        delay(0.05)
        handle_mouseevents()
        
def pause():
    pass

def resume():
    pass

def select():
    global running,n,team
    events=get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            n+=1
            print(n)
            if n>member-1:
                n=0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            n-=1
            print(n)
            if n<=-1:
                n=member-1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
            game_framework.change_state(title_state)
            
if __name__=='__main__':
    main()
    
