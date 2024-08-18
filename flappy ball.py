import pgzrun
#import pygame
#pygame.init()
#screen=pygame.display.set_mode((600,600))
#screen.fill("black")

GRAVITY=2000
WIDTH=800
HEIGHT=600
TITLE="Flappy Ball"

class Ball():
    def __init__(self, initial_x, initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
    
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"white")

b=Ball(50,100)

def draw():
    screen.clear()
    b.draw()

def update(dt):
    uy=b.vy
    b.vy=b.vy+GRAVITY*dt
    b.y=b.y+(uy+b.vy)*0.5*dt
    
    if b.y>HEIGHT-b.radius:
        b.y=HEIGHT-b.radius
        b.vy=-b.vy*0.9
    
    b.x=b.x+b.vx*dt 
    if b.x>WIDTH-b.radius or b.x<b.radius:
        b.vx=-b.vx
    

def on_key_down(key):
    if key==keys.SPACE:
        b.vy=-500

pgzrun.go()


