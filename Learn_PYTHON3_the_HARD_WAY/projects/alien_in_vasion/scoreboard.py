import pygame.font

class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self,ai_settings,screen,stats) -> None:
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        #准备初始得分图像
        self.pre_score()
        
    def pre_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #将得分放在屏幕右上角
        
