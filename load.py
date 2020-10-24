import pygame
# *this file loads all the files of the game
# * this file contains prescales all the images
# * this file hitmasks
FPS = 60
black = 0, 0, 0
clock = pygame.time.Clock()
globalh = 360*2 
globalw = 288*2
bgh=60
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
def load(): # function responsible for loading and scaling images
    global numbers
    numbers = []
    for i in range(0,10):
        numbers.append(pygame.image.load("images/{}.png".format(i)))
    
    global birdimgs
    birdimgs = [
        pygame.image.load("images/redbird-upflap.png"),
        pygame.image.load("images/redbird-downflap.png"),
        pygame.image.load("images/redbird-midflap.png")
        ]

    global bgimgs 
    bgimgs={"bg":pygame.image.load("images/background.jpg"),"gnd":pygame.image.load("images/base.png")}
    
    global pipeimgs
    pipeimgs = {"nrml":pygame.image.load("images/pipe-green.png"),"revr":pygame.image.load("images/pipe-green-reversed.png")}
    
    
load()
# global piperectrev
#     birdrect =  birdimgs[0].get_rect()
#     piperect = pipeimgs["nrml"].get_rect()
#     piperectrev = pipeimgs["revr"].get_rect()
#     gndrect = bgimgs["gnd"].get_rect()

def getRect(img,obj):
    return img.get_rect(center=(obj["x"],obj["y"]))
birdrect = getRect(birdimgs[0],{"x":50,"y":50})
