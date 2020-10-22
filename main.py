import pygame
from sys import exit

pygame.init()

dispWidht = 288*2
dispHeight = 360*2
x = 50
y = 50
width = 40
height = 60
speed = 5

display = pygame.display.set_mode( (dispWidht, dispHeight) )

pygame.display.set_caption("Flappy Bird")

backGround = pygame.transform.scale(pygame.image.load("images/bg1.png"),(dispWidht,dispHeight))
greenPipe = pygame.transform.scale(pygame.image.load('images/pipe-green.png'), (52, 320)) #52 320
greenPipeReversed = pygame.transform.scale(pygame.image.load('images/pipe-green-reversed.png'), (52, 320)) #52 320



isJump = False
jumpCount = 10

FPS = 60 # Создаем переменную FPS
clock = pygame.time.Clock() # Создаем счетчик для FPS

def drawDisp():
    display.blit(backGround, (0, 0))
    for i in range(10):
        display.blit(greenPipe, (pipesX[i], 420)) 
        display.blit(greenPipeReversed, (pipesX[i], -20))
    pygame.draw.rect(display, (0, 0, 0), (x, y, width, height))
    pygame.display.update()

pipesX = []
pipesY = []

pipeX = 350
pipeY = 420
for i in range(10):
    pipesX.append(pipeX)
    pipesY.append(pipeX)
    #pipesY.append()
    pipeX += 100

# Основной цикл игры
while True:
    for i in range(len(pipesX)):
        if pipesX[i] < 0:
            pipesX= pipesX[1::]
            pipesX.append(pipeX)
            pipeX += 100
        pipesX[i] -= 2
    # Ждем события (действия пользователя)
    for event in pygame.event.get():
        # Если нажали на крестик,
        # то закрываем окно
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x-=speed
    if keys[pygame.K_RIGHT] and x < dispWidht-width:
        x+=speed
    if keys[pygame.K_DOWN] and y < dispHeight-height:
        y+=speed
    if keys[pygame.K_UP] and y > 0:
        y-=speed

    drawDisp()
    clock.tick(FPS) # Замедляем цикл до 60 выполнений в секунду