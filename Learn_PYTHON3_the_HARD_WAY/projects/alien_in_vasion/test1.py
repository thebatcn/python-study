import pygame

pygame.init()

# 设置窗口大小
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# 创建窗口
screen = pygame.display.set_mode(WINDOW_SIZE)

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 设置矩形的初始位置和大小
rect = pygame.Rect(0, 0, 50, 50)

# 设置矩形每帧移动的距离
dx = 5
dy = 5

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 清屏
    screen.fill(WHITE)

    # 更新矩形位置
    rect.move_ip(dx, dy)

    # 判断矩形是否超出屏幕边界，如果是，反向移动
    if rect.left < 0 or rect.right > WINDOW_WIDTH:
        dx = -dx
    if rect.top < 0 or rect.bottom > WINDOW_HEIGHT:
        dy = -dy

    # 绘制矩形
    pygame.draw.rect(screen, BLACK, rect)

    # 刷新屏幕
    pygame.display.update()

    # 控制游戏帧率
    pygame.time.Clock().tick(60)