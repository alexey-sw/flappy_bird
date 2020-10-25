# will help us manage our coordinates for bird
# where will be 3 classes in our game: bird vec and game
# bird class has pictures of the bird, x,y as properties
# bird contains methods for its update(x,y update),collision detection
# game class contains methods for pipe generation(randomised, redrawal of all objects) and game start and game end
# ? git stash apply - num of latest stash
# ? git stash pop - applies latest stash and deletes it from the list
# ? git stash clear
# ? git stash list - outputs list of stashes


# score will be added later
import pygame
import sys
from load import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

baseimg = pygame.transform.scale(pygame.image.load(
    "images/base.png"), (globalw, baseh))  # changing size of our image
#!scale (xsize,ysize)
pygame.init()

# would be great to implement clock.get_fps()


class Bird:
    flapcount = 0
    whitespace_pressed = False

    def __init__(self, images):
        self.images = images  # array
        self.coord = Vec(50, 50)  # starting position
        self.speed = Vec(0, 0)  # starting speed
        self.rect = birdrect

    def collide(self):  # returns true if bird collides with pipes or ground or ceiling
        if self.rect.colliderect(baserect):
            return True
        return False
        # collision detection of bird with pipes and ground

    def update(self):
        self.flapcount += 0.2
        if self.flapcount > 998:
            self.flapcount = 0
        if self.whitespace_pressed:
            self.speed.add(0, 9)
            self.whitespace_pressed = False
        self.speed.subtract(0, 0.4)
        self.coord.y -= self.speed.y
        self.rect.y=self.coord.y
        # we don't add any speed to x as long as
        scr.blit(self.images[int(self.flapcount % 3)],
                 [self.coord.x, self.coord.y])

    def freeze(self):
        scr.blit(self.images[1], [self.coord.x, self.coord.y])
#


class Game:
    def __init__(self, bird, base):
        self.base = base
        self.bird = bird
        self.state = "playing"
        self.w = globalw
        self.h = globalh
        # * size of our background
        self.objects = [self.bird]    # for obj in self objects: i.update

    def start(self):
        global scr
        scr = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Flappy bird")

    def update(self):
        scr.blit(self.base, (basepos.x, basepos.y))
        pygame.draw.rect(scr,(255,0,0),baserect,4)
        pygame.draw.rect(scr,(255,0,0),birdrect,4)

        if not self.bird.collide():
            self.bird.update()
        else:
            self.bird.freeze()
        pygame.display.flip()


flappy_bird = Bird(birdimgs)
game = Game(flappy_bird, baseimgs["gnd"])
game.start()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappy_bird.whitespace_pressed = True
    scr.fill(black)
    game.update()
    clock.tick(FPS)
