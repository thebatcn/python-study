import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    ai_settings = Settings()
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Vasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()
    aliens = Group()
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # pygame.display.flip()


run_game()
