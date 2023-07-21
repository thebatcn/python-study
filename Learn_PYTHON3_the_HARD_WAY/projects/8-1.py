import pygame
import sys

background_image_filename = "sushiplate.jpg"
sprite_image_filename = "fugu.png"
ball_filename = 'ball1.png'


SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption('One test')

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
ball = pygame.image.load(ball_filename)


clock = pygame.time.Clock()


x = 0.
y = 0.
speed = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000.0
    distance_moved = time_passed_seconds*speed


    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    screen.blit(ball, (y, 300))
    x += 1
    if x > 640:
        x -= 640

    y += distance_moved
    if y > 640:
        y -= 640

    pygame.display.flip()
   
