import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    ai_settings = Settings()
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Vasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组  
    bullets = Group()
    aliens = Group()
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats,screen,ship, aliens,bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # pygame.display.flip()


run_game()
