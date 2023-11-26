import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame import time

            
class Ball(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.pos = [randint(10,620),randint(10,460)]
        self.radius = 10
        self.speed = 5
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.radius,self.radius)
    
    def draw(self):
        pygame.draw.circle(screen,(255,0,0),self.pos,self.radius)

    def update(self):
        if self.pos[1] > 470:
            self.pos[1]=0
        else:
            self.pos[1] += self.speed
            self.rect = pygame.Rect(self.pos[0],self.pos[1],self.radius,self.radius)
            

class Block(Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0],self.pos[1],10,100)
    def draw(self):
        pass
class Paddle(Sprite):
    def __init__(self):
        super().__init__()
        self.pos = [320,460]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],10,100)
    def move(self,key):
        if key[pygame.K_UP]:
            self.pos[1] -= 10
        if key[pygame.K_DOWN]:
            self.pos[1] += 10
        self.rect = pygame.Rect(self.pos[0],self.pos[1],10,100)

SCREEN_SIZE = (640,480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('13-5抓球')
clock = time.Clock()

ball = Ball(screen)
print("\n",ball.pos)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type==pygame.KEYDOWN:
    screen.fill((0,0,0))
    ball.draw()
    # print("\n",ball.pos)
    ball.update()
    clock.tick(60)
    pygame.display.update()
    
