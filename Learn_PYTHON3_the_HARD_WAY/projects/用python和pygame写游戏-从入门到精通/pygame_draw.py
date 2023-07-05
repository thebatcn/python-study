import pygame
import sys

SCREEN_SIZE = (640, 480)

# 初始化Pygame
pygame.init()

# 创建屏幕对象
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption('一个测试')

while True:
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 绘制矩形
    pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 200), 2)
    
    # 绘制椭圆
    pygame.draw.ellipse(screen, (255, 0, 0), (100, 370, 70, 110))
    
    # 绘制圆形
    pygame.draw.circle(screen, (0, 255, 0), (320, 240), 100)
    
    # 绘制抗锯齿线段
    pygame.draw.aaline(screen, (255, 255, 255), (0, 0), (640, 480))
    
    # 绘制线段
    pygame.draw.line(screen, (0, 255, 255), (640, 0), (0, 480))
    
    # 绘制折线
    pygame.draw.lines(screen, (200, 50, 128), True, [
                      [100, 100], [190, 230], [320, 200]])
    
    # 绘制折线
    pygame.draw.lines(screen, (200, 50, 128), False, [
                      [640, 100], [480, 320], [200, 320]])
    
    # 更新屏幕显示
    pygame.display.update()

# 结束游戏循环后退出Pygame
pygame.quit()