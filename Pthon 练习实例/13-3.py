import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption("One test")


class Rain(Sprite):
    def __init__(self, screen, x=0, y=0):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("rain.bmp").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.1
        
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.y > self.screen.get_height():
            self.y = 0
rain_group = Group()

for i in range(20):
    rain = Rain(screen, x=i * 20, y=0)
    rain_group.add(rain)

# rain = Rain(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    rain_group.update()
    rain_group.draw(screen)
    # screen.blit(rain.image, rain.rect)
    # rain.update()
    pygame.display.flip()
