import pygame
import sys
import math

SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('One test')
screen.fill((255,255,255))

pygame.draw.rect(screen,(255,255,0),(50,50,100,80))
pygame.draw.rect(screen,(255,0,0),(135,155,30,30),2)

pygame.draw.polygon(screen,(0,0,255),[(300,300),(350,310),(400,380),(420,250)],2)

pygame.draw.circle(screen,(0,0,0),(320,240),40)
pygame.draw.ellipse(screen,(255,0,255),(180,80,100,70))
pygame.draw.arc(screen,(125,0,0),(350,100,80,40),math.radians(00),math.radians(260),3) #不用math.radians，画出的是椭圆或者圆

pygame.draw.line(screen,(0,0,255),(650,100),(600,300),3)
pygame.draw.aaline(screen,(0,0,255),(650,50),(600,250),3)
pygame.draw.lines(screen,(0,0,255),0,[(100,400),(180,370),(130,400),(300,450)],4)
pygame.draw.aalines(screen,(0,255,255),0,[(500,300),(400,200),(500,400),(450,480)],5)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        