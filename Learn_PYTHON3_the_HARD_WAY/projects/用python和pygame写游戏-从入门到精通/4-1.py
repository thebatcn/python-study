my_name = "Will McGugan"
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((648,480),0,32)
my_font = pygame.font.SysFont("arial",64)
name_surface = my_font.render(my_name,True,(0,0,0),(255,0,255))
pygame.image.save(name_surface,"my_name.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(name_surface,((screen.get_width()-name_surface.get_width())/2,screen.get_height()//2-name_surface.get_height()))
    pygame.display.flip()



