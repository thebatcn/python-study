import pygame

class Rock():

	def __init__(self,screen):

		self.screen = screen
		self.image = pygame.image.load("R-C.bmp")

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.speed = 10

		self.Moving_left = False
		self.Moving_right = False
		self.Moving_up = False
		self.Moving_down = False
		
	def update(self):
		if self.Moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.speed
			# print(self.rect)
		if self.Moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.speed
			# print(self.rect)
		if self.Moving_up and self.rect.top > self.screen_rect.top:
			self.rect.centery -= self.speed
			# print(self.rect)
		if self.Moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.speed
			# print(self.rect)
		# print(self.rect)
	def blitme(self):
		#draws the image
		self.screen.blit(self.image,self.rect)
	



