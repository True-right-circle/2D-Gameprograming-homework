import game_framework
import main_state
import random
from pico2d import*

name='AI'
member =5
image = None
font = None
char_font = None
n = 0

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
 
    def draw(self):
        self.image.draw(400,30)
        
class Boy:
    PIXEL_PER_METER=(10.0/3.0)
    RUN_SPEED_KMPH=20.0
    RUN_SPEED_MPM=(RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS*PIXEL_PER_METER)

    TIME_PER_ACTION=0.5
    ACTION_PER_TIME=1.0/TIME_PER_ACTION
    FRAMES_PER_ACTION=8
    
    image = None
    global n,team
    LEFT_RUN,RIGHT_RUN,LEFT_STAND,RIGHT_STAND =0,1,2,3

    def handle_left_run(self):
        self.x-=5
        self.run_frames+=1
        if self.x<0:
            self.state=self.RIGHT_RUN
            self.x=0
        if self.run_frames == 100:
            self.state=self.LEFT_STAND
            self.stand_frames=0
            
    def handle_left_stand(self):
        self.stand_frames+=1
        if self.stand_frames==50:
            self.state=self.LEFT_RUN
            self.run_frames=0
            
    def handle_right_run(self):
        self.x+=5
        self.run_frames+=1
        if self.x>800:
            self.state=self.LEFT_RUN
            self.x=800
        if self.run_frames == 100:
            self.state=self.RIGHT_STAND
            self.stand_frames=0
            
    def handle_right_stand(self):
        self.stand_frames+=1
        if self.stand_frames==50:
            self.state=self.RIGHT_RUN
            self.run_frames=0

    handle_state={
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND:handle_left_stand,
        RIGHT_STAND: handle_right_stand
        }        
    def __init__(self):
        self.x,self.y=random.randint(100,700),random.randint(90,500)
        self.frame= random.randint(0,7)
        self.dir=1
        self.total_frames = 0.0
        self.run_frames=0
        self.total_frames = 0.0
        self.stand_frames=0
        self.state = random.randint(0,3)
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')

    def handle_event(self,event):
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND):
                self.state=self.LEFT_RUN
                self.dir=-1
        elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND):
                self.state=self.RIGHT_RUN
                self.dir=1
        elif(event.type,event.key)==(SDL_KEYUP,SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state=self.LEFT_STAND
                self.dir=0

        elif(event.type,event.key)==(SDL_KEYUP,SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state=self.RIGHT_STAND
                self.dir=0
                
    def update(self,frame_time):
        distance=Boy.RUN_SPEED_PPS*frame_time
        self.total_frames+=Boy.FRAMES_PER_ACTION*Boy.ACTION_PER_TIME*frame_time
        self.frame=int(self.total_frames)%8
        self.handle_state[self.state](self)

        if self.x>800:
            self.dir=-1
            self.x=800
            self.state=self.LEFT_RUN
        elif self.x<=0:
            self.dir=1
            self.x=0
            self.state=self.RIGHT_RUN
            
        if self.state==self.RIGHT_RUN:
            self.x+=(self.dir*distance)
        elif self.state==self.LEFT_RUN:
            self.x-=(self.dir*distance)    
        #self.frame=(self.frame+1)%8
        #self.handle_state[self.state](self)
        #if self.state==self.RIGHT_RUN:
         #  self.x=min(800,self.x+5)
        #elif self.state==self.LEFT_RUN:
        #   self.x=max(0,self.x-5)
            
    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
