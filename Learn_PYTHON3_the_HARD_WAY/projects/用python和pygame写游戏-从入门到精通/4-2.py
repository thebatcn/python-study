import sys
import pygame

SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)  # 初始化屏幕大小
background = pygame.image.load("sushiplate.jpg").convert()  # 加载背景图片
pygame.display.set_caption("显示中文字体")  # 设置窗口标题以显示中文字符

font = pygame.font.SysFont('方正粗黑宋简体', 40)  # 创建一个具有指定中文字体和大小的字体对象
text_surface = font.render(u'你好', True, (0, 0, 255))  # 创建一个渲染文本的表面

x = 0  # 文本的初始 x 坐标
y = 480 - text_surface.get_height()  # 文本的初始 y 坐标（屏幕底部）

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # 如果用户关闭窗口，则退出程序

    screen.blit(background, (0, 0))  # 将背景图片绘制到屏幕上

    x -= 0.25  # 将文本的 x 坐标向左移动
    if x < -text_surface.get_width():   
        x = 640 - text_surface.get_width()  # 当文本超出屏幕左边缘时，将其移到屏幕右侧

    screen.blit(text_surface, (x, y))  # 在当前 (x, y) 位置绘制文本

    pygame.display.flip()  # 更新整个显示屏的内容

