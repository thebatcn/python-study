import pygame
import sys

SCREEN_SIZE = (640, 480)
sprite_image_filename = "fugu.png"
ball_filename = "pydroball.png"

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption('One test')

sprite = pygame.image.load(sprite_image_filename)
ball = pygame.image.load(ball_filename)

clock = pygame.time.Clock()

x, y = 100.0, 100.0
speed_x, speed_y = 240., 170.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))        
    screen.blit(ball,(x,y))

    time_passed = clock.tick(1200)
    time_passed_second = time_passed / 1000.0

    x += time_passed_second * speed_x
    y += time_passed_second * speed_y

    if x > 640 - ball.get_width():
        x = 640 - ball.get_width()
        speed_x = -speed_x
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > 480 - ball.get_height():
        speed_y = -speed_y
        y = 480 - ball.get_height()
    elif y < 0 :
        speed_y = -speed_y
        y = 0

    pygame.display.update()

    
