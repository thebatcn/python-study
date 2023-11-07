# 根据下面代码修改，生成并显示随机位置和数量的星星。
from random import randint
import pygame
import sys
from pygame.sprite import Group
SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
star_image = pygame.image.load('star.bmp')
nums_star = randint(1,2)
print(nums_star)
stars = []

pygame.display.set_caption('One test')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                pygame.quit()
                sys.exit()

    screen.fill((0,0,0))
    
    # for i in range(nums_star):
    #     stars.append((randint(0,640),randint(0,480)))
    stars = [(randint(0,640),randint(0,480)) for i in range(nums_star)]
    print("nums_star: ",len(stars))
    for star in stars:
        screen.blit(star_image,star)
    
       
    pygame.display.update()
