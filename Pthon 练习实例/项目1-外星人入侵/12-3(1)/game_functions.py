import pygame
import sys


def check_events(rock):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_LEFT:
                rock.Moving_left = True
                # print("left")
            elif event.key == pygame.K_RIGHT:
                rock.Moving_right = True
                print("Moving_right: ", rock.Moving_right)
            elif event.key == pygame.K_UP:
                rock.Moving_up = True
            elif event.key == pygame.K_DOWN:
                rock.Moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rock.Moving_left = False
            elif event.key == pygame.K_RIGHT:
                rock.Moving_right = False
            elif event.key == pygame.K_UP:
                rock.Moving_up = False
            elif event.key == pygame.K_DOWN:
                rock.Moving_down = False
        

def update_screen(screen,rock):
    #draws the image
    bg = rock.image.get_at((0,0))
    screen.fill(bg)
    rock.blitme()
    # print(self.rect)
    pygame.display.flip()

