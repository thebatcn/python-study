import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rand_col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    screen.lock()
    for _ in range(100):
        rand_pos = (random.randint(0,639),random.randint(0,479))
        screen.set_at(rand_pos,rand_col)
    screen.unlock()
    pygame.display.update()
    
