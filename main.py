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
greenPipe = [pygame.image.load('images/pipe-green.png')]

isJump = False
jumpCount = 10

FPS = 60 # Создаем переменную FPS
clock = pygame.time.Clock() # Создаем счетчик для FPS

def drawDisp():
    display.blit(backGround, (0, 0))
    pygame.draw.rect(display, (0, 0, 0), (x, y, width, height))
    pygame.display.update()

# Основной цикл игры
while True:
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