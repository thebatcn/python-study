# 根据下面代码修改，生成并显示随机位置和数量的星星。
from random import randint
import pygame
import sys
from pygame.sprite import Group
from time import sleep

SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
star_image = pygame.image.load('star.bmp')


class Star(pygame.sprite.Sprite):
    """定义一个Star的类"""
    def __init__(self,image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
star_group = Group()
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
                
    nums_star = randint(1,5)
    # print(nums_star)
    star_group.empty()

    for i in range(nums_star):
        star_sprite = Star(star_image, randint(0,640), randint(0,480))
        star_group.add(star_sprite)
    screen.fill((0,0,0))
    # for i in range(nums_star):
    #     stars.append((randint(0,640),randint(0,480)))
    # stars = [(randint(0,640),randint(0,480)) for i in range(nums_star)]
    # print("nums_star: ",len(stars))
    # for star in stars:
    #     screen.blit(star_image,star)
    # print(len(star_group))
    star_group.draw(screen)
    pygame.display.flip()
    # sleep(2)
# 显示的星星数量多余nums_star