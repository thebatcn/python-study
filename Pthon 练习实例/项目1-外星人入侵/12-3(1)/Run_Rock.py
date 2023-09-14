from Rock import Rock
import pygame
import sys


def run_rock():

	pygame.init()
	screen = pygame.display.set_mode((800,600),0,depth=32)

	rock = Rock(screen)

	print((rock.rect))
	print(rock.screen_rect)
	print(rock.Moveing_down)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		rock.blitme(screen)

run_rock()

