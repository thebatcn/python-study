import sys
import pygame

# 定义背景图片和鼠标图片的文件名
background_image_filename = "sushiplate.jpg"
mouse_image_filename = "fugu.png"

# 初始化 Pygame
pygame.init()

# 创建窗口并设置标题
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello World")

# 加载背景图片和鼠标图片
background = pygame.image.load(background_image_filename).convert()  # 转换为与屏幕兼容的像素格式
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()  # 转换为带透明度的像素格式

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, (0, 0))  # 绘制背景图片到窗口上的指定位置 (0, 0)

    # 获取鼠标的当前位置，并将鼠标图片置于鼠标位置的中心
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))  # 绘制鼠标图片到窗口上的指定位置 (x, y)

    pygame.display.update()  # 更新窗口显示内容
