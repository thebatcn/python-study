import pygame
import sys
SCREEN_SIZE = (640,480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('Rock')
rock_image = pygame.image.load("飞机1.bmp").convert_alpha()
rock_rect = rock_image.get_rect()
print(rock_rect)
screen_rect = screen.get_rect()
print((screen_rect))
rock_rect.bottom = screen_rect.bottom
print(rock_rect)

direction = "False"

def update_rock(direction):
    if direction == 'Up' and rock_rect.y > 0:
        rock_rect.y -= 2
    elif direction == 'Down' and rock_rect.bottom < 480:
        rock_rect.y += 2
    # print(rock_rect)

class Bullets(object):
    """docstring for Bullets"""
    def __init__(self, screen,rock_rect):
        super(Bullets, self).__init__()
        self.y = rock_rect.y + rock_rect.width / 2
        self.x = rock_rect.width
            
    def updata(self):
        self.x += 0.2
        # print((self.x, self.y))

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 10, 3))
bullet = Bullets(screen,rock_rect)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction ='Up'
            if event.key == pygame.K_SPACE:
                bullet = Bullets(screen,rock_rect)
                # bullet.updata()
            elif event.key == pygame.K_DOWN:
                direction ="Down"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = "False"
            elif event.key == pygame.K_DOWN:
                direction = "False"
    screen.fill((255,255,255))
    screen.blit(rock_image,rock_rect)
    update_rock(direction)
    bullet.updata()
    bullet.draw()
    pygame.display.flip()

