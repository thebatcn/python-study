from rock import Rock
import game_functions as gf
import pygame
import sys


def run_rock():

	pygame.init()
	screen = pygame.display.set_mode((800,600),0,depth=32)

	rock = Rock(screen)

	# print((rock.rect))
	# print(rock.screen_rect)
	print(rock.Moving_right)

	while True:
		gf.check_events(rock)
		rock.update()
		# print(rock.Moveing_down)
		gf.update_screen(screen,rock)
		pygame.display.flip()


run_rock()

