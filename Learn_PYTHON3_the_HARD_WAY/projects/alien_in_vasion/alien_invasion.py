import pygame
import sys
from settings import Settings

ai_settings = Settings()

def run_game():
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Vasion")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # screen.fill((230,230,230))
        screen.fill((ai_settings.bg_color))
        pygame.display.flip()
    
run_game()
