# ? git stash apply - num of latest stash
# ? git stash pop - applies latest stash and deletes it from the list
# ? git stash clear
# ? git stash list - outputs list of stashes


# score will be added later
import pygame
import sys
from load import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'  # to center the window

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

    def collide(self,another_rect):  # returns true if bird collides with pipes or ground or ceiling
        if self.rect.colliderect(another_rect):
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
    def __init__(self,rect):
        self.rect = rect

class Game:
    frozen = False
    def __init__(self, bird, gndimg,gndobj):
        self.gndimg = gndimg
        self.gndobj = gndobj
        self.ceiling = ceiling
        self.bird = bird
        self.state = "playing"
        self.w = globalw
        self.h = globalh
        # * size of our background
        self.objects = [self.gndobj,self.ceiling]    # for obj in self objects: i.update

    def start(self):
        global scr
        scr = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Flappy bird")

    def update(self):
        scr.blit(self.gndimg, (gndpos.x, gndpos.y))
        for obj in self.objects:
            if not self.bird.collide(obj.rect):
                pass
            else:
                self.bird.freeze()
                self.frozen = True
                break
        if not self.frozen:
            self.bird.update()
        pygame.display.flip()

        # if not self.bird.collide():
        #     self.bird.update()
        # else:
        #     self.bird.freeze()
        # pygame.display.flip()
ceiling = Ceiling(ceilingrect)
ground = Ground(gndrect)
flappy_bird = Bird(birdimgs)
game = Game(flappy_bird, gndimgs["gnd"],ground)
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
