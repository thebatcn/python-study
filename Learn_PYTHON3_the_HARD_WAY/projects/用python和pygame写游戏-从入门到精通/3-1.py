from pygame.locals import *
from sys import exit
import pygame

# 设置背景图片文件名
background_file_name = "sushiplate.jpg"

# 设置屏幕尺寸
SCREEN_SIZE = (640, 480)

# 初始化pygame
pygame.init()

# 创建屏幕对象
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

# 加载背景图片并转换为适合屏幕的格式
background = pygame.image.load(background_file_name).convert()

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == VIDEORESIZE:
            # 处理窗口大小改变事件
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption('window resized to ' + str(event.size))

    # 获取屏幕的宽度和高度
    screen_width, screen_height = SCREEN_SIZE

    # 循环绘制背景图像,填满窗口
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    
    # 更新屏幕显示
    pygame.display.flip()
