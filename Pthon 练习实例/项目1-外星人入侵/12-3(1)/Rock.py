import pygame

class Rock():

	def __init__(self,screen):

		self.image = pygame.image.load("R-C.bmp")

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.speed = 10

		self.Moveing_left = False
		self.Moveing_right = False
		self.Moveing_up = False
		self.Moveing_down = False
		

	def blitme(self,screen):

		screen.blit(self.image,self.rect)
		pygame.display.flip()




