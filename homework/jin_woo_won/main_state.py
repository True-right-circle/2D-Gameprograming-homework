from boy_ai import*
import game_framework
import random
from pico2d import*
import title_state
import json


name = 'MainState'

def get_frame_time():
    global current_time

    frame_time=get_time()-current_time
    current_time+=frame_time
    return frame_time
  
def handle_events():
    global running
    global team
    events = get_events()
    for event in events:
        global team
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False
        else:
            team[n].handle_event(event)
            
def create_team():

    team_data_json= '{"Tiffany":{"StartState":"LEFT_RUN","x":100,"y":100},"Yuna":{"StartState":"RIGHT_RUN","x":100,"y":100},"Sunny":{"StartState":"LEFT_STAND","x":100,"y":100},"Yuri":{"StartState":"RIGHT_STAND","x":100,"y":100},"Jessica":{"StartState":"LEFT_RUN","x":100,"y":100}}'
    
    player_state_table={
        "LEFT_RUN":Boy.LEFT_RUN,
        "RIGHT_RUN":Boy.RIGHT_RUN,
        "LEFT_STAND":Boy.LEFT_STAND,
        "RIGHT_STAND":Boy.RIGHT_STAND
        }
    team_data=json.loads(team_data_json)

    team=[]
    for name in team_data:
        player=Boy()
        player.name=name
        player.x=team_data[name]['x']
        player.y=team_data[name]['y']
        player.state=player_state_table[team_data[name]['StartState']]
        team.append(player)

    return team            

def handle_mouseevents():
    global running,n,team
    select()
    events=get_events()
    global team
    for event in events:
        if event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y,=event.x,600-event.y  

current_time = 0.0
frame_time=0.0



def enter():
    global team,grass,boy,n,running,image,font,char_font
    #team=[Boy() for i in range(member)]
    team=create_team()
    grass = Grass()
    font=load_font('ENCR10B.TTF',50)
    char_font=load_font('ENCR10B.TTF',25)
    running=True
    image=None

    

def exit():
    global team, grass
    del(team)
    del(grass)

def get_frame_time():

    global current_time,frame_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
    global team
    for i in range(member):
        team[i].update(frame_time)
        
def draw():
    global team,current_time,n
    current_time=get_time()  
    frame_time=get_time()-current_time

    while running:
        update()
        clear_canvas()
        grass.draw()
        font.draw(730,560,str(n))
        char_font.draw(team[n].x-50,team[n].y+50,'This Boy')
        char_font.draw(team[n].x-50,team[n].y-15,str(n))
        for i in range(member):
            team[i].draw()
        frmae_time=get_frame_time()    
        update_canvas()
        handle_mouseevents()
        delay(0.01)
        delay(0.03)

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
        else:
            team[n].handle_event(event)  
            
