# * this file contains game assets and makes it easier to use assets in main file
# import of all main libraries
import pygame
from random import randint, uniform
import sys
from load import *
import os
from time import time
FPS = 60
clock = pygame.time.Clock()
globalh = 360*2
globalw = 288*2
gndh = 60 #* height of our ground
os.environ['SDL_VIDEO_CENTERED'] = '1'  # * centering pygame window



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
    gndimgs = {"bgrnd": pygame.transform.scale(pygame.image.load("images/background.jpg"), (globalw, globalh)),
               "gnd": pygame.transform.scale(pygame.image.load("images/gnd.png"), (gndsize.x, gndsize.y))}

    global pipeimgs
    pipeimgs = {"nrml": pygame.image.load(
        "images/pipe-green.png"), "revr": pygame.image.load("images/pipe-green-reversed.png")}


load()


def getRect(img, obj):
    return img.get_rect(center=(obj.x, obj.y))


gndpos = Vec(0, globalh-gndsize.y)  # * ground position
gndposrect = Vec(
    0+int(gndimgs["gnd"].get_width()/2), gndpos.y+int(gndsize.y/2))
# * hitmaks
birdrect = getRect(birdimgs[0], Vec(50+int(birdimgs[0].get_width()/2), 50))
gndrect = getRect(gndimgs["gnd"], gndposrect)
ceilingrect = pygame.Rect(0, -5, globalw, 5)


#!pipes variables
pipewthcenter = int(pipeimgs["nrml"].get_width()/2)
pipehtcenter = int(pipeimgs["nrml"].get_height()/2)
nrmlpipelev = globalh-gndsize.y  # level of ground
pipewidth = int(pipeimgs["nrml"].get_width())
pipeheight = int(pipeimgs["nrml"].get_height())


#! icon
programmicon = pygame.image.load("images/redbird-midflap.png")
