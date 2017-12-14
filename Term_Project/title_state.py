import game_framework
import run_in_game
from pico2d import*

name ='TitleState'
image=None

def enter():
    global state,title_sound,image,arrow,arrow2
    image = load_image('title.png')
    state=1
    arrow= load_image('arrowRight.png')
    arrow2= load_image('arrowRight.png')
    title_sound=load_wav('title.wav')
    if state ==1:
        title_sound.repeat_play()
    title_sound.set_volume(35)
    arrow.x=415
    arrow.y=145
    arrow2.x=415
    arrow2.y=70
    

def exit():
    global title_sound,image
    del(image)
    del(title_sound)

def handle_events():
    global state
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(run_in_game)

def update():
    global title_sound,arrow,arrow2
    if arrow.x<430:
        arrow.x+=0.025
    if arrow.x>=430:
        arrow.x=415
    if arrow2.x<430:
        arrow2.x+=0.025
    if arrow2.x>=430:
        arrow2.x=415
    
def draw():
    clear_canvas()
    update()
    image.draw(400,300)
    arrow.draw(arrow.x,arrow.y)
    arrow2.draw(arrow2.x,arrow2.y)
    update_canvas()

def pause():
    pass
def resume():
    pass
