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
            
class Paddle(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.pos = [320,460]
        self.rect = pygame.Rect(self.pos[0],self.pos[1],100,10)
    def draw(self):
        pygame.draw.rect(screen,(0,255,0),self.rect)
    
    def update(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],100,10)
SCREEN_SIZE = (640,480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('13-5抓球')
clock = time.Clock()

ball = Ball(screen)
paddle = Paddle(screen)
print("\n",paddle.pos)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                paddle.pos[0]-=10
                paddle.rect = pygame.Rect(paddle.pos[0],paddle.pos[1],100,10)

            if event.key==pygame.K_RIGHT:
                paddle.pos[0]+=10
                paddle.rect = pygame.Rect(paddle.pos[0],paddle.pos[1],100,10)
    
    screen.fill((0,0,0))
    ball.draw()
    paddle.draw()
    print("\n",paddle.pos)
    ball.update()
    clock.tick(60)
    pygame.display.update()
    
