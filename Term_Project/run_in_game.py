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

class Main_Char:
    def __init__(self):
        self.x,self.y=50,90
        self.run_frame=0
        self.jump_frame=0
        self.run_image=load_image('new_char_sheet.png')
        self.jump_image=load_image('jump_sheet.png')
        self.jump_sound=load_wav('pickup.wav')
        self.jump_sound.set_volume(32)

    def update(self):
        global jump,jump_time,jump_check,background ,running,check_time
        self.run_frame=(self.run_frame+1)%8
        self.jump_frame=(self.jump_frame+1)%2
        if flying.y<=90 and flying.x == boy.x and boy.y<=90:
            running=False
            font.draw(300,400,"Game Over")
            font.draw(270,350,"Score : ")
            font.draw(410,350,str(check_time))
            font.draw(470,350,"Second ")
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
            self.jump_sound.play()
            
            
    
def enter():
    global font,image,background,running,boy,jump,nextbackground,flying,block1,block2
    font=load_font('ENCR10B.TTF',30)
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
    global jump,jump_time,jump_check,background,flying,block1,block2,now
    boy.update()
    background.update()
    nextbackground.update()
    flying.update()
    block1.update()
    block2.update()



   
def draw():
    start_time = time.time()
    global check_time
    while running:
        end_time = time.time()
        clear_canvas()
        background.draw()
        nextbackground.draw()
        update()
        check_time=int(end_time - start_time)
        font.draw(730,560,str(check_time))
        font.draw(620,560,"Score:")
        boy.draw()
        flying.draw()
        block1.draw()
        block2.draw()
        update_canvas()
        handle_events()
        delay(0.04)
    
def pause():
    pass

def resume():
    pass
