import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
sub_scr = screen.subsurface((200,100,50,50))   #设置一个子表面，等下演示。
n = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    n += 1
    rand_col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    screen.lock()
    for _ in range(100):
        rand_pos = (random.randint(0,639),random.randint(0,479))
        if n > 500:
            screen.fill((0,0,0))
            n = 0
        screen.set_at(rand_pos,rand_col)
    sub_scr.fill((255,0,0))
    screen.unlock()
    pygame.display.update()
    
