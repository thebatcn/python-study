# 通过这个方法更新位置来生成动画
# rect = pygame.Rect(100, 100, 50, 50)
# rect.move_ip(100, 100) 
# 或者下面这个方法来更新
# rect =rect.move(10,10)


import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

#background = pygame.image.load(background_image_filename).convert()
sprite = pygame.Surface((50,50),0,depth=32)
sprite.fill((255,0,0))

clock = pygame.time.Clock()

# sprite的起始x坐标
x = 0.

myrect_x = 100
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    clock.tick(60)

 #   screen.blit(background, (0,0))
    screen.fill((0,0,0))
    screen.blit(sprite, (x, 100))
    x+= 4.     #如果你的机器性能太好以至于看不清，可以把这个数字改小一些
    myrect = pygame.draw.rect(screen,(255,0,255),(myrect_x,100,50,50))
    myrect_x +=2


    # 如果移动出屏幕了，就搬到开始位置继续
    if x > 640.:
        x = 0.  
    if myrect_x > 640:
        myrect_x = 0  


    pygame.display.update()
    
