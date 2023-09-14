import sys
import pygame


# def moving():

# 	if rock_moving_up and rock_rect.top > 0:
# 		rock_rect.centery -= 5
# 	if rock_moving_down and rock_rect.bottom < screen_rect.bottom:
# 		rock_rect.centery += 5
# 	if rock_moving_left and rock_rect.left >0:
# 		rock_rect.centerx -=5
# 	if rock_moving_right and rock_rect.right < screen_rect.right:
# 		rock_rect.centerx += 5

def run_game():
	pygame.init()

	screen = pygame.display.set_mode((1280,720),depth=32)
	pygame.display.set_caption("Rock")

	rock_image = pygame.image.load("R-C.bmp").convert_alpha()
	rock_rect = rock_image.get_rect()
	screen_rect = screen.get_rect()
	rock_rect.centerx = screen_rect.centerx
	rock_rect.bottom = screen_rect.bottom

	
	rock_moving_left = False
	rock_moving_right = False
	rock_moving_up = False
	rock_moving_down = False

	blackground_color = rock_image.get_at((0,0))
	
	screen.fill(blackground_color)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rock_moving_left = True
					print("LEFT")
				if event.key == pygame.K_RIGHT:
					rock_moving_right = True
					print("RIGHT")

				if event.key == pygame.K_DOWN:
					rock_moving_down =True
					print("DOWN")
				if event.key == pygame.K_UP:
					rock_moving_up = True
					print(("UP"))
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_DOWN:
					rock_moving_down = False
				if event.key == pygame.K_UP:
					rock_moving_up = False
				if event.key == pygame.K_LEFT:
					rock_moving_left = False
				if event.key == pygame.K_RIGHT:
					rock_moving_right = False
		# moving()
		if rock_moving_up and rock_rect.top > 0:
			rock_rect.centery -= 5
		if rock_moving_down and rock_rect.bottom < screen_rect.bottom:
			rock_rect.centery += 5
		if rock_moving_left and rock_rect.left >0:
			rock_rect.centerx -=5
		if rock_moving_right and rock_rect.right < screen_rect.right:
			rock_rect.centerx += 5
		screen.blit(rock_image,rock_rect)
		pygame.display.update()




run_game()