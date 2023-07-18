import pygame
import sys
from random import randint
import math

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption('One test')
font = pygame.font.SysFont("arialblac",40)
myfont = font.render("Game Over",True,(255,0,0))
clock = pygame.time.Clock()
SNAKE = [(100, 100), (100, 110), (100, 120)]
FOOD = (randint(0, 639), randint(0, 479))
SNAKE_SIZE = len(SNAKE)
directions = [10, 0]
directions_old = [0, 0]
snake_head = SNAKE[0]
ACTION = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and ACTION and directions !=[0,-10]:
                directions = [0, 10]
            elif event.key == pygame.K_RIGHT and ACTION and directions !=[-10,0]:
                directions = [10, 0]
            elif event.key == pygame.K_UP and ACTION and directions !=[0,10]:
                directions = [0, -10]
            elif event.key == pygame.K_LEFT and ACTION and directions !=[10,0]:
                directions = [-10, 0]
            elif event.key == pygame.K_SPACE and ACTION:
                directions_old = directions
                ACTION = not ACTION
                directions = [0, 0]
            elif event.key == pygame.K_SPACE and not ACTION:
                directions = directions_old
                ACTION = not ACTION

    screen.fill((0, 0, 0))

    for dot in SNAKE:
        if dot == SNAKE[0]:
            pygame.draw.circle(screen,(255,165,0),dot,5)
        else:
            pygame.draw.circle(screen, (255, 0, 255), dot, 5)

    pygame.draw.circle(screen, (0, 255, 0), FOOD, 5)
    clock.tick(10)

    snake_head = (snake_head[0]+directions[0], snake_head[1]+directions[1])
    SNAKE_SIZE = len(SNAKE)

    if ACTION:
        if math.sqrt((snake_head[0]-FOOD[0])**2+(snake_head[1]-FOOD[1])**2) <= 10:
            FOOD = (randint(5, 634), randint(5, 474))
        else:
            SNAKE.pop()
        SNAKE.insert(0, snake_head)

    if snake_head in SNAKE[1::]:
        screen.blit(myfont,((screen.get_width()-myfont.get_width())/2,(screen.get_height()-myfont.get_height())/2))
        ACTION = False
        # break
    if snake_head[0] <= 0 or snake_head[0] >= 639:
        screen.blit(myfont,((screen.get_width()-myfont.get_width())/2,(screen.get_height()-myfont.get_height())/2))
        ACTION = False
        # break
    if snake_head[1] <= 0 or snake_head[1] >= 479:
        screen.blit(myfont,((screen.get_width()-myfont.get_width())/2,(screen.get_height()-myfont.get_height())/2))
        ACTION = False
        # break
    pygame.display.flip()
