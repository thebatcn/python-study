import pygame
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    ai_settings = Settings()
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Vasion")
    ship = Ship(screen)

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.K_RIGHT:
        #         pass
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        # screen.fill((230,230,230))
        gf.check_events(ship)
        ship.update()
        # screen.fill((ai_settings.bg_color))
        # ship.blitme()
        gf.update_screen(ai_settings, screen, ship)

        # pygame.display.flip()
    
run_game()
