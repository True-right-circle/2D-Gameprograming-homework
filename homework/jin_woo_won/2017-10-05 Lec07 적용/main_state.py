import game_framework
import random
from pico2d import*
import title_state


name = 'MainState'
image = None
font = None
team = None
n = 0
class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
 
    def draw(self):
        self.image.draw(400,30)
        
 
class Boy:
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
        self.run_frames=0
        self.stand_frames=0
        self.state = random.randint(0,3)
        if Boy.image==None:
            Boy.image=load_image('animation_sheet.png')
        
    def update(self):
        self.frame=(self.frame+1)%8
        self.handle_state[self.state](self)
        
    def draw(self):
        self.image.clip_draw(self.frame*100,self.state*100,100,100,self.x,self.y)
        font.draw(580,560,'Boy Num ='+str(n))


def handle_mouseevents():
    global running,n,team
    select()
    events=get_events()
    for event in events:
        global team
        if event.type==SDL_MOUSEMOTION:
            team[n].x,team[n].y,=event.x,600-event.y


def enter():
    global team,grass,boy,n,running,image,font
    team=[Boy() for i in range(1000)] 
    grass = Grass()
    font=load_font('ENCR10B.TTF',30)
    running=True
    image=None

    
def exit():
    global team, grass
    del(team)
    del(grass)

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()

def update():
    global team
    for i in range(1000):
        team[i].update()
        
def draw():
    global team
    while running:
        global n
        update()
        clear_canvas()
        grass.draw()
        for i in range(1000):
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
            if n>=1000:
                n=0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            n-=1
            print(n)
            if n<=0:
                n=999
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
            game_framework.change_state(title_state)
            
if __name__=='__main__':
    main()
    
