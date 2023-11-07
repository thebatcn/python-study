import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('One test')

class Rain(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('rain.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 1
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.screen.get_height():
            self.rect.y = 0

rain = Rain(screen)
rain_group = Group()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    rain.update()
    screen.blit(rain.image,rain.rect)
    pygame.display.update()