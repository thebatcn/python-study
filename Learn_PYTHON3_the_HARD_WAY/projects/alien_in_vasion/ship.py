import pygame

class Ship():   

    def __init__(self,ai_settings,screen) -> None:
        """初始化飞船并设置其初始位置"""

        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load("images/ship.bmp")   
        self.rect = self.image.get_rect()   
        self.screen_rect = screen.get_rect()  

        self.rect.centerx = self.screen_rect.centerx  
        self.rect.bottom = self.screen_rect.bottom      

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动方向更新飞船的位置"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 5
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 5
        if  self.moving_down and self.rect.bottom < self.screen_rect.bottom:   
            self.rect.centery += 5

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        # pygame.display.flip()
  
    