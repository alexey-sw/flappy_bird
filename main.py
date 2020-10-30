from load import *

class Pipe:
    def __init__(self, image, x, y, scalecoeff, pipespeed):
        self.sclcoeff = scalecoeff  # newheight = height * sclcoeff
        self.x = x  # *coords of left top corner
        self.y = y  # * it it is reversed pipe it is 0, if it is normal pipe y is level of the chute
        self.image = pygame.transform.scale(
            image, (pipewidth, int(pipeheight*scalecoeff)))
        self.speed = pipespeed
        self.rect = getRect(self.image,
                            Vec(self.x+pipewthcenter, self.y+(pipehtcenter)*scalecoeff))  # *hitrect

    def update(self, speed):
        # updating coordinates
        self.speed = speed
        self.x -= self.speed
        self.rect.x -= self.speed
        scr.blit(self.image, [self.x, self.y])

    def freeze(self):
        scr.blit(self.image, [self.x, self.y])

class Bird:
    flapcount = 0 #* how many flaps have been made by bird ( to make effect of flapping wings)
    whitespace_pressed = False #* if whitespace has been pressed
    coefficient = 1 #* coefficient which is multiplied by speed
    subtractor = 0.3 # * subtracted from coefficient

    def __init__(self, images):
        self.images = images  # array
        self.coord = Vec(50, 100)  # starting position
        self.speed = Vec(0, 0)  # starting speed
        self.rect = birdrect
        self.mincoeff = 0.2 #* minimal speed coefficient

    def collide(self, another_rect):  
        if self.rect.colliderect(another_rect): #* collision detection with all other objects
            return True
        return False

    def update(self):
        self.flapcount += 0.2
        if self.flapcount > 998:
            self.flapcount = 0
        if self.whitespace_pressed: #* increase speed if whitespace is pressed
            self.subtractor += 0.03
            self.coefficient -= self.subtractor
            self.speed.add(0, 9*self.coefficient)
            self.whitespace_pressed = False
        self.speed.subtract(0, 0.4)
        if self.coefficient < 1:
            self.coefficient += 0.002
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
    def __init__(self, rect): #* rectangular hitbox
        self.rect = rect


class Ceiling:
    def __init__(self, rect): #* rectangular hitbox
        self.rect = rect


class Game:

    def __init__(self, bird, gndimg, gndobj, bgimg):
        self.frozen = False #* if bird has collided with something 
        self.pipecreated = True #* if current state needs another pipe
        self.chutegap = 200 
        self.minchutegap = 100
        self.gapchange = 0 # * random change of gaps between pipes
        self.bgimg = bgimg # * background image
        self.startime = 0 # * timer
        self.gndimg = gndimg #* ground image
        self.gndobj = gndobj #* ground object
        self.ceiling = ceiling # * ceiling object
        self.bird = bird #* bird object
        self.w = globalw # * width and height of the screen 
        self.h = globalh
        self.pipespeed = 3  # x speed of the pipes
        self.updateobjects = [self.bird]  # *objects that are updated
        self.freezeobjects = [self.bird] #* objects that are frozen if bird detects collision
        self.collideobjects = [self.gndobj, self.ceiling] # * objects that can collide with bird
        self.lastpipex = 200  #*x of the last pipe row
        self.minrowgap = 170  # * minimal gap between piperows
        self.rowgap = 450
        self.count = 0 #* counts pipes that bird has bypassed
        self.changedelay = 10 #* delay between difficulty changes

    def start(self):
        global scr
        scr = pygame.display.set_mode((self.w, self.h)) #initialising screen
        self.startime = time()
        pygame.display.set_caption("Flappy bird")
        pygame.display.set_icon(programmicon)

    def update(self):
        if not self.frozen: #* if game process hasn't been terminated yet
            for obj in self.collideobjects:
                if not self.bird.collide(obj.rect):
                    pass
                else:
                    self.frozen = True # * freezing  game
                    self.pipecreated = True #* no need to create pipes
                    break
        # * drawing background
        scr.blit(self.bgimg, (0, 0)) 
        scr.blit(self.gndimg, (gndpos.x, gndpos.y))
        
        if not self.frozen:
            # print(self.gapchange)
            if not self.pipecreated: #* if game requires another pipe
                self.createPipeRow(self.calculateNextPipe())
                self.pipecreated = True 
            self.deleteRow() #* this function deletes rows (that have negative x coordinate)
            self.lastpipex -= self.pipespeed #* updating pipe position
            self.needNextPipe() #* changes self.pipecreated value
            for obj in self.updateobjects: # updating objects
                if isinstance(obj, Pipe): #* if it is pipe
                    obj.update(self.pipespeed)
                else: #* if it is bird
                    obj.update()
            self.countUpdate(self.bird) #* updating count if necessary
        else:
            for obj in self.freezeobjects:
                obj.freeze() 
        timenow = time()

        if timenow-self.startime > self.changedelay and self.chutegap != self.minchutegap: #* changing difficulty of our game
            self.chutegap = self.chutegap-randint(1, 5) #* narrowing chutegap
            self.startime = timenow #* setting time of last change of difficulty
            if self.chutegap < self.minchutegap: #* limiting chutegap
                self.chutegap = self.minchutegap
            self.rowgap = self.rowgap-randint(10, 20) #*decreasing distance between rows
            if self.rowgap < self.minrowgap: 
                self.rowgap = self.minrowgap
                
        self.displayCount() #* drawing count
        pygame.display.flip()

    def Scalepipe(self, chutegap):  
        minpipeheight = 35 #* minimal height of the pipe
        
        avheight = nrmlpipelev-chutegap #* height available
        maxcoeff = ((avheight-35)/pipeheight) 
        mincoeff = (35/pipeheight)
        coeff1 = uniform(mincoeff, maxcoeff)  #* generating random coeff for the pipe
        secondpipeheight = avheight - pipeheight*coeff1 #* height of reversed pipe
        coeff2 = (secondpipeheight/pipeheight) 
        # calculating y of transformed pipe
        ynrml = nrmlpipelev-int(pipeheight*coeff1)  # y of top left corner of normal pipe
        return [coeff1, coeff2, ynrml] 

    def createPipeRow(self, x):

        self.lastpipex = x
        metrics = self.Scalepipe(self.chutegap)
        pipe = Pipe(pipeimgs["nrml"], x, metrics[2],
                    metrics[0], self.pipespeed)
        # y of reversed pipe equals 0(base level)
        rvrpipe = Pipe(pipeimgs["revr"], x, 0, metrics[1], self.pipespeed)
        #* adding created objects for all arrays
        self.updateobjects += [pipe, rvrpipe]
        self.collideobjects += [pipe, rvrpipe]
        self.freezeobjects += [pipe, rvrpipe]

    def countUpdate(self, bird): #* detects bypass of pipe by the bird
        if len(self.updateobjects) > 1: 
            firstpipex = self.updateobjects[1].x
            if firstpipex+pipewidth < bird.coord.x and firstpipex+pipewidth+self.pipespeed > bird.coord.x:
                self.count += 1

    def displayCount(self):
        font_size = 30
        counter_font = pygame.font.SysFont("Verdana", font_size)
        textpos = [int(globalw/2), 100] 
        antiliasing = 0
        color = (0, 0, 0)
        textsurface = counter_font.render(str(self.count), antiliasing, color)
        scr.blit(textsurface, textpos)

    def needNextPipe(self):

        if globalw-self.lastpipex-self.gapchange > self.rowgap-20:
            self.pipecreated = False
            self.gapchange = randint(-30, 30)

    def calculateNextPipe(self):  # returns x of next pipe row
        x_of_nextpiperow = globalw+18
        self.lastpipex = x_of_nextpiperow
        return x_of_nextpiperow

    def deleteRow(self):  # deletes pipes that are out of the screen

        if len(self.updateobjects) > 1 and self.updateobjects[1].x < -100:
            #* consecutive deletion of piperow in all game arrays
            for i in range(2):
                deletedobj2 = self.updateobjects.pop(1)
                deletedobj1 = self.freezeobjects.pop(1)
                deletedobj3 = self.collideobjects.pop(2)
                del deletedobj1, deletedobj2, deletedobj3

#* initialising main game objects
ceiling = Ceiling(ceilingrect)
ground = Ground(gndrect)
flappy_bird = Bird(birdimgs)
game = Game(flappy_bird, gndimgs["gnd"], ground, gndimgs["bgrnd"])
pygame.display.set_icon(programmicon)
game.start()
pygame.init()

#* main cycle
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # * if space pressed
                flappy_bird.whitespace_pressed = True
    game.update()
    clock.tick(FPS)
