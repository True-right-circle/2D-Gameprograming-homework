import game_framework
import random
from pico2d import*
from Background import*
from Enemy import*
import time

name='MainState'
image=None
jump_sound=None
jump_time=0.0
jump_check=0.0
speed=5.0
now=0
start_time = 0
check_time=0

enemyspeed =9.0
blockspeed=8.0
blockspeed2 =5.0
class Main_Char:
    def __init__(self):
        self.x,self.y=90,50
        self.run_frame=0
        self.jump_frame=0
        self.run_image=load_image('new_char_sheet.png')
        self.jump_image=load_image('jump_sheet.png')
        self.jump_sound=load_wav('pickup.wav')
        self.jump_sound.set_volume(32)

    def update(self):
        global jump,jump_time,jump_check,background ,running,check_time
        self.run_frame=(self.run_frame+1)%6
        self.jump_frame=(self.jump_frame+1)%6

        if(jump==False and jump_time<3.0):
            jump_time+=0.6
            boy.y+=40.0
            jump_check+=40.0
        if(jump_time>=3.0):
            jump=True
        if(jump_check>=0):
            boy.y-=20.0
            jump_check-=20.0
        if(jump_time==4.0):
             boy.y+=0.0
             jump_check+=0.0
        if(jump_check==0):
             jump_time=0.0
    
    def draw(self):
        global jump
        if(jump==True):
            self.run_image.clip_draw(self.run_frame*100,0,100,55,self.x,self.y)
        elif(jump==False):
            self.jump_image.clip_draw(self.jump_frame*100,0,100,55,self.x,self.y)

    def get_bb(self):
        return self.x-8,self.y-8,self.x+8,self.y+18
    
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    

            
    
def enter():
    global green,moun,font,image,background,running,boy,jump,flying,sun,moon
    font=load_font('ENCR10B.TTF',30)
    boy=Main_Char()
    moun=Mountain(800,400)
    moon=moon()
    background = Background(800,400)
    flying=enemy()
    green=G_enemy()
    sun=Sun()
    jump=True
    running=True
    image=None

    
def exit():
    global green,background,boy,flying,moun,sun,moon
    del(boy)
    del(background)
    del(moun)
    del(flying)
    del(sun)
    del(moon)
    del(green)

    
def handle_events():
    global running,jump,jump_time
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()  
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
             jump=False
             boy.jump_sound.play()
        else:  
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                running=False
                if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                    #running=False
                    game_framework.quit()

def collide(a,b):
    left_a,bottom_a,right_a,top_a=a.get_bb()
    left_b,bottom_b, right_b,top_b=b.get_bb()
    
    if left_a>right_b: return False
    if right_a<left_b: return False
    if top_a<bottom_b: return False
    if bottom_a>top_b: return False

    return True
    
    
        
def update():
    global green,running,moun,jump,jump_time,jump_check,background,flying,sun,moon,boy,enemy
    boy.update()
    sun.update()
    moon.update()
    moun.update()
    background.update()
    green.update(enemyspeed)
    flying.update(enemyspeed)
    if collide(flying,boy):
        running=False
        font.draw(300,200,"Game Over")
        font.draw(270,150,"Score : ")
        font.draw(410,150,str(check_time))
        font.draw(470,150,"Second ")
    if collide(green,boy):
        running=False
        font.draw(300,200,"Game Over")
        font.draw(270,150,"Score : ")
        font.draw(410,150,str(check_time))
        font.draw(470,150,"Second ")



def draw():
    start_time = time.time()
    global check_time
    while running:
        end_time = time.time()
        clear_canvas()
        moun.draw()
        sun.draw()
        moon.draw()
        background.draw()
        update()
        check_time=int(end_time - start_time)
        font.draw(730,350,str(check_time))
        font.draw(620,350,"Score:")
        boy.draw()
        flying.draw()
        green.draw()
        green.draw_bb()
        flying.draw_bb()
        boy.draw_bb()
        update_canvas()
        handle_events()
        delay(0.05)

    
def pause():
    pass

def resume():
    pass
