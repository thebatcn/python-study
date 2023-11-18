import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings,screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        print('self.rect：',self.rect)

        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        print('rect.x = {}, rect.y ={}'.format(self.rect.x,self.rect.y))

        self.x = float(self.rect.x)
        print('float(self.x:)',self.x)
    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.x += (self.settings.alien_speed_factor * 
                   self.settings.fleet_direction)
        self.rect.x = self.x    

    def center_alien(self):
        """Center the alien on the screen"""
        self.rect.y = self.rect.height
        self.rect.x = self.screen.get_rect().centerx
        
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True