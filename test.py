import pygame
from sys import exit
from random import randint
# Функция, возвращающая случайный оттенок зеленого цвета
def randomGreen():
    return randint(0, 100), randint(100, 255), randint(0,100)
# Функция, возвращающая случайный оттенок красного цвета
def randomRed():
    return randint(100, 255), randint(0, 100), randint(0,100)

pygame.init()
display = pygame.display.set_mode( (600, 600) )
display.fill((255,255,255))
x = 100 # начальная позиция по оси X
y = 100 # начальная позиция по оси Y
while y < 500: # Пока мы не достигли точки с координатой y == 500
    # Вложенный цикл для рисования линии из квадратиков
    while x < 500: # Пока мы не достигли точки с координатой x == 500
        # Рисуем квадратик с координатами x, y
        pygame.draw.rect(display, randomGreen(), (x, y, 25, 25))
        x += 25 # Смещаем позицию квадратика по оси X
    # По завершению вложенного цикла увеличиваем переменную y
    # для перехода на новую строчку
    y += 25
    x = 100 # Возвращаем позицию по оси X в начало строчки
# Рисуем "мордочку" крипера
pygame.draw.rect(display, (0,0,0), (150, 200, 100, 100))
pygame.draw.rect(display, (0,0,0), (350, 200, 100, 100))
pygame.draw.rect(display, (0,0,0), (250, 300, 100, 100))
pygame.draw.rect(display, (0,0,0), (200, 350, 50, 100))
pygame.draw.rect(display, (0,0,0), (350, 350, 50, 100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()