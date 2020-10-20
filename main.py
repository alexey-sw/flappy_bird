# will help us manage our coordinates for bird
# where will be 3 classes in our game: bird vec and game
# bird class has pictures of the bird, x,y as properties
# bird contains methods for its update(x,y update),collision detection
# game class contains methods for pipe generation(randomised, redrawal of all objects) and game start and game end

# score will be added later
import load
import pygame,sys
pygame.init()
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,addx,addy):
        self.x = self.x+addx
        self.y = self.y+addy
class Bird:
    stPos = {"x":50,"y":100}
    def __init__(self,images):
        self.images = images # array
        self.coord = self.stPos
    def collide(self,crd=stPos):
        return False
        # collision detection of bird with pipes and ground
    def update(self):
        pass
    
class Game:
    def __init__(self,bird,bg):
        self.bg = bg
        self.bird = bird
        self.state = "playing"
        self.w = 400
        self.h = 400
    def start(self):
        global scr
        scr = pygame.display.set_mode((self.h,self.w))
        pygame.display.set_caption("Flappy bird")
    def update(self):
        if not self.bird.collide():
            self.bird.update()

flappy_bird = Bird([1,2,4])
game = Game(flappy_bird,"path/to/background")
game.start()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if game.state == "lost":
        continue
    game.update()
    

