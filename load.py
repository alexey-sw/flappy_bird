import pygame
# *this file loads all the files of the game
# * this file contains prescales all the images
# * this file hitmasks
FPS = 60
black = 0, 0, 0
clock = pygame.time.Clock()
globalh = 360*2
globalw = 288*2
gndh = 60


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, addx, addy):
        self.x = self.x+addx
        self.y = self.y+addy

    def subtract(self, subtrx, subtry):
        self.x -= subtrx
        self.y -= subtry

    def __repr__(self):
        return "{} {}".format(self.x, self.y)


gndsize = Vec(globalw, int(0.05*globalh))


def load():  # function responsible for loading and scaling images
    global numbers
    numbers = []
    for i in range(0, 10):
        numbers.append(pygame.image.load("images/{}.png".format(i)))

    global birdimgs
    birdimgs = [
        pygame.image.load("images/redbird-upflap.png"),
        pygame.image.load("images/redbird-downflap.png"),
        pygame.image.load("images/redbird-midflap.png")
    ]

    global gndimgs
    gndimgs = {"bgrnd": pygame.image.load("images/background.jpg"),
               "gnd": pygame.transform.scale(pygame.image.load("images/gnd.png"), (gndsize.x, gndsize.y))}

    global pipeimgs
    pipeimgs = {"nrml": pygame.image.load(
        "images/pipe-green.png"), "revr": pygame.image.load("images/pipe-green-reversed.png")}


load()
# global piperectrev
#     birdrect =  birdimgs[0].get_rect()
#     piperect = pipeimgs["nrml"].get_rect()
#     piperectrev = pipeimgs["revr"].get_rect()
#     gndrect = gndimgs["gnd"].get_rect()


def getRect(img, obj):
    return img.get_rect(center=(obj.x, obj.y))
def scaleImg(img,coeffs):
    pass

birdrect = getRect(birdimgs[0], Vec(50+int(birdimgs[0].get_width()/2), 50))
gndpos = Vec(0, globalh-gndsize.y)
gndposrect = Vec(
    0+int(gndimgs["gnd"].get_width()/2), gndpos.y+int(gndsize.y/2))
gndrect = getRect(gndimgs["gnd"], gndposrect)
ceilingrect = pygame.Rect(0,-5,globalw,5)



#!pipes
pipewthcenter = int(pipeimgs["nrml"].get_width()/2)
pipehtcenter = int(pipeimgs["nrml"].get_height()/2)
nrmlpipelev = globalh-gndsize.y # level of ground
chutelev = nrmlpipelev-int(pipeimgs["nrml"].get_height())
pipewidth = int(pipeimgs["nrml"].get_width())
pipeheight = int(pipeimgs["nrml"].get_height())

