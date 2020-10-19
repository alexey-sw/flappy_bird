# will help us manage our coordinates for bird
# where will be 3 classes in our game: bird vec and game
# bird class has pictures of the bird, x,y as properties
# bird contains methods for its update(x,y update),collision detection
# game class contains methods for pipe generation(randomised, redrawal of all objects) and game start and game end

# score will be added later
import load
# import keyboard from pynput
import pygame
pygame.init()
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,addx,addy):
        self.x = self.x+addx
        self.y = self.y+addy
class Bird:
    def __init__(self,images,coord):
        self.images = images
        self.coord = coord
    
class Game:
    def __init__(self):
        pass
        # self.bg = bg
        # self.bird = bird
        # self.state = lost
        # self.w = w
        # self.h = h
    def start(self):
        global scr
        scr = pygame.display.set_mode((400,400))


game = Game()
game.start()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if game.state == "lost":
        continue
