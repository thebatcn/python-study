import pygame
import sys

SCREEN_SIZE = (640,480)

star = pygame.image.load('star.bmp')
star_rect = star.get_rect()

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
number_star_col = int(screen.get_width()/(2 * star_rect.width))
number_star_row = int(screen.get_height()/(2 * star_rect.height))
print(number_star_col,number_star_row)


pygame.display.set_caption('13-1 stars')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()  
    for i in range(number_star_row):
        for j in range(number_star_col):
            screen.blit(star,(j*2*star_rect.width,i*2*star_rect.height))
    pygame.display.update()