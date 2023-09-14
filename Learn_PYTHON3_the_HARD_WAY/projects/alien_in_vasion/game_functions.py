import sys
import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                print("right")
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                print("left")
            elif event.key == pygame.K_UP:
                ship.moving_up = True
                print("up")
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
                print("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()   
