import pygame
# *this file loads all the files of the game
# * this file contains prescales all the images
# * this file hitmasks
FPS = 60
black = 0, 0, 0
clock = pygame.time.Clock()
globalh = 600
globalw = 800
bgh=60
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
