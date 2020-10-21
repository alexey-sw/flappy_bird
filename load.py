import pygame
import sys
# *this file loads all the files of the game
# * this file contains prescales all the images
# * this file hitmaks
def load(): # function responsible for loading and scaling images
    global numbers = []
    for i in range(0,10):
        numbers.append("images/{}.png".format(i))
    
    global birdimgs = []
    birdimgs.append("images/redbird-downflap.png")
    birdimgs.append("images/redbird-midflap.png")
    birdimgs.append("images/redbird-upflap.png")
    
    global bgimgs ={"bg":"images/background.jpg","gnd":"images/base.png"}
    
    global pipeimgs = {"nrml":"images/pipe-green.png","revr":"images/pipe-green-reversed.png"}
load()
