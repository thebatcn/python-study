import pygame
import sys

SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('One test')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()  
        elif event.type==pygame.KEYDOWN:
            print(event.key)