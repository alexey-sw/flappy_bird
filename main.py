import pygame
from sys import exit

pygame.init()

display = pygame.display.set_mode( (288, 360) )

pygame.display.set_caption("Flappy Bird")


dispWidht = 288
dispHeight = 360
x = 50
y = 50
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

FPS = 60 # Создаем переменную FPS
clock = pygame.time.Clock() # Создаем счетчик для FPS

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

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 0), (x, y, width, height))


    # Обновляем поверхность игры
    # на каждом шаге основного цикла игры
    pygame.display.update()
    clock.tick(FPS) # Замедляем цикл до 60 выполнений в секунду