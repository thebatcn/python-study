import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE =(640,480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

font = pygame.font.SysFont('arial',16)
font_height = font.get_linesize()

event_txt=[]
while True:
    event = pygame.event.wait()
    event_txt.append(str(event))
    event_txt = event_txt[-int(SCREEN_SIZE[1]/font_height):]

    if event.type == QUIT:
        exit()

    screen.fill((255,255,255))

    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_txt):
        screen.blit(font.render(text,True,(0,0,0)),(0,y))
        y -=font_height

    pygame.display.update()
