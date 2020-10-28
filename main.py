# ? git stash apply - num of latest stash
# ? git stash pop - applies latest stash and deletes it from the list
# ? git stash clear
# ? git stash list - outputs list of stashes


# score will be added later
from random import uniform
import pygame
import sys
from load import *
import os
from time import time
os.environ['SDL_VIDEO_CENTERED'] = '1'  # to center the window


# would be great to implement clock.get_fps()


class Pipe:
    def __init__(self, image, x, y, scalecoeff):
        self.sclcoeff = scalecoeff
        self.x = x  # *coords of left top corner
        self.y = y
        self.image = pygame.transform.scale(
            image, (pipewidth, int(pipeheight*scalecoeff)))
        self.speed = 1
        self.rect = getRect(self.image,
                            Vec(self.x+pipewthcenter, self.y+(pipehtcenter)*scalecoeff))  # * x,y of pipe cente

    def update(self, speed):
        self.speed = speed
        self.x -= self.speed
        self.rect.x -= self.speed
        scr.blit(self.image, [self.x, self.y])
        pygame.draw.rect(scr, (255, 0, 0), self.rect, 4)

    def freeze(self):
        scr.blit(self.image, [self.x, self.y])


class Bird:
    flapcount = 0
    whitespace_pressed = False
    coefficient = 1
    subtractor = 0.3

    def __init__(self, images):
        self.images = images  # array
        self.coord = Vec(50, 50)  # starting position
        self.speed = Vec(0, 0)  # starting speed
        self.rect = birdrect

    def collide(self, another_rect):  # returns true if bird collides with pipes or ground or ceiling
        if self.rect.colliderect(another_rect):
            return True
        return False
        # collision detection of bird with pipes and ground

    def update(self):

        self.flapcount += 0.2
        if self.flapcount > 998:
            self.flapcount = 0
        if self.whitespace_pressed:
            self.speed.add(0, 8*self.coefficient)
            self.coefficient -= self.subtractor
            self.subtractor += 0.1
            self.whitespace_pressed = False
        self.speed.subtract(0, 0.4)
        if self.coefficient < 1:
            self.coefficient += 0.03
        if self.subtractor > 0:
            self.subtractor -= 0.01

        self.coord.y -= self.speed.y
        self.rect.y = self.coord.y

        # we don't add any speed to x as long as
        scr.blit(self.images[int(self.flapcount % 3)],
                 [self.coord.x, self.coord.y])

    def freeze(self):
        scr.blit(self.images[1], [self.rect.x, self.rect.y])
#


class Ground:
    def __init__(self, rect):
        self.rect = rect


class Ceiling:
    def __init__(self, rect):
        self.rect = rect


class Game:
    frozen = False
    pipecreated = False
    chutegap = 200

    def __init__(self, bird, gndimg, gndobj):
        self.startime = 0
        self.gndimg = gndimg
        self.gndobj = gndobj
        self.ceiling = ceiling
        self.bird = bird
        self.state = "playing"
        self.w = globalw
        self.h = globalh
        self.pipespeed = 1  # x speed of the pipes
        self.updateobjects = [self.bird]  # * objects that i need to update
        self.freezeobjects = [self.bird]
        self.collideobjects = [self.gndobj, self.ceiling]
        self.lastpipex = 400  # x of the last pipe row
        self.maxrowgap = 200  # chutegap between pipe rows

    def start(self):
        global scr
        scr = pygame.display.set_mode((self.w, self.h))
        self.startime = time()
        print(self.startime)
        pygame.display.set_caption("Flappy bird")

    def update(self):
        currenttime = time()
        if currenttime-self.startime > 20:  # 20 seconds elapsed
            self.startime = currenttime
            self.pipespeed += 1

        self.lastpipex -= self.pipespeed
        self.needNextPipe()
        if not self.pipecreated:

            # 400 is x of the very first piperow
            self.createPipeRow(self.calculateNextPipe())
            self.pipecreated = True

        scr.blit(self.gndimg, (gndpos.x, gndpos.y))
        for obj in self.collideobjects:
            if not self.bird.collide(obj.rect):
                pass
            else:
                self.frozen = True
                break
        if not self.frozen:
            for obj in self.updateobjects:
                if isinstance(obj, Pipe):
                    obj.update(self.pipespeed)
                else:
                    obj.update()
        else:
            for obj in self.freezeobjects:
                obj.freeze()
        pygame.display.flip()

    def Scalepipe(self, chutegap):  # generates rows with pipes of random size
        # outputs scale of the firstpipe,second pipe
        # calculates chutegap between pipes

        avheight = nrmlpipelev-chutegap
        # 20 px is minimal height of the pipe
        maxcoeff = ((avheight-35)/pipeheight)

        mincoeff = (35/pipeheight)
        coeff1 = uniform(mincoeff, maxcoeff)  # coeff of the normal pipe
        secondpipeheight = avheight - pipeheight*coeff1
        coeff2 = (secondpipeheight/pipeheight)
        # calculating y of transformed pipe
        ynrml = nrmlpipelev-int(pipeheight*coeff1)  # y of normal pipe
        return [coeff1, coeff2, ynrml]

    def createPipeRow(self, x):
        self.lastpipex = x
        metrics = self.Scalepipe(self.chutegap)
        pipe = Pipe(pipeimgs["nrml"], x, metrics[2], metrics[0])
        # y of reversed pipe equals 0(base level)
        rvrpipe = Pipe(pipeimgs["revr"], x, 0, metrics[1])
        self.updateobjects += [pipe, rvrpipe]
        self.collideobjects += [pipe, rvrpipe]
        self.freezeobjects += [pipe, rvrpipe]

    def needNextPipe(self):
        if globalw-self.lastpipex > self.maxrowgap-20:
            self.pipecreated = False

    def calculateNextPipe(self):  # returns x of next pipe row
        print(list(self.updateobjects))
        x_of_nextpiperow = globalw+18
        self.lastpipex = x_of_nextpiperow
        return x_of_nextpiperow


ceiling = Ceiling(ceilingrect)
ground = Ground(gndrect)
flappy_bird = Bird(birdimgs)
game = Game(flappy_bird, gndimgs["gnd"], ground)
game.start()
pygame.init()
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
