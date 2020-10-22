# will help us manage our coordinates for bird
# where will be 3 classes in our game: bird vec and game
# bird class has pictures of the bird, x,y as properties
# bird contains methods for its update(x,y update),collision detection
# game class contains methods for pipe generation(randomised, redrawal of all objects) and game start and game end

# score will be added later
import pygame
import sys
from load import *

bgimg = pygame.transform.scale(pygame.image.load("images/base.png"),(globalw,bgh))# changing size of our image
#!scale (xsize,ysize)
pygame.init()

# would be great to implement clock.get_fps()
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,addx,addy):
        self.x = self.x+addx
        self.y = self.y+addy
    def subtract(self,subtrx,subtry):
        self.x-=subtrx
        self.y-=subtry
    def __repr__(self):
        return "{} {}".format(self.x,self.y)
class Bird:
    flapcount = 0
    whitespace_pressed = False
    def __init__(self,images):
        self.images = images # array
        self.coord = Vec(50,50) # starting position
        self.speed = Vec(0,0) # starting speed
    def collide(self): # returns true if bird collides with pipes or ground
        if self.coord.y>=globalh-bgh: # only checks the ground
            return True
        return False
        # collision detection of bird with pipes and ground
    def update(self):
        self.flapcount+=0.2
        if self.flapcount>998:
            self.flapcount = 0
        if self.whitespace_pressed:
            self.speed.add(0,9)   
            self.whitespace_pressed=False
        self.speed.subtract(0,0.4)
        self.coord.y-=self.speed.y
        scr.blit(self.images[int(self.flapcount%3)],[self.coord.x,self.coord.y]) # we don't add any speed to x as long as 
    def freeze(self):
        scr.blit(self.images[1],[self.coord.x,self.coord.y])
#
class Game:
    def __init__(self,bird,bg):
        self.bg = bgimg
        self.bird = bird
        self.state = "playing"
        self.w = globalw
        self.h = globalh
        self.bgsize = Vec(self.bg.get_width(),self.bg.get_height()) #* size of our background
        self.objects = [self.bird]    # for obj in self objects: i.update
    def start(self):
        global scr
        print(self.bgsize.y)
        print(self.h-self.bgsize.y)
        scr = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Flappy bird")
    def update(self):
        scr.blit(self.bg,(self.w-self.bgsize.x,self.h-self.bgsize.y))
        if not self.bird.collide():
            self.bird.update()
        else:
            self.bird.freeze()
        pygame.display.flip()
        
flappy_bird = Bird(birdimgs)
game = Game(flappy_bird,"path/to/background")
game.start()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                flappy_bird.whitespace_pressed=True
    scr.fill(black)
    game.update()
    clock.tick(FPS)
    

