import pygame
import sys
from pygame.sprite import Group
from pygame.sprite import Sprite
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



direction = False
group = Group()
man_group = Group()

def update_rock(direction):
    if direction == 'Up' and rock_rect.y > 0:
        rock_rect.y -= 1
    elif direction == 'Down' and rock_rect.bottom < 480:
        rock_rect.y += 1
    # print(rock_rect)

class Bullets(Sprite):
    """docstring for Bullets"""
    def __init__(self, screen,rock_rect):
        super(Bullets, self).__init__()
        self.y =  rock_rect.centery
        self.x = rock_rect.right
        self.screen = screen
            
    def update(self):
        # print((self.x, self.y))
        # if self.x + 10 > screen_rect.right:
        #     self.x = screen_rect.right -10
        # else:
        self.x += 0.2

    def draw(self):
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, 10, 3))
        
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        bullet.draw()
        if bullet.x > screen_rect.right:
            bullets.remove(bullet)
    # print(len(bullets))
class Aman(Sprite):
    """docstring for Aman"""
    def __init__(self, screen,x,y):
        super(Aman, self).__init__()
        self.x = x
        self.y = y
        self.screen = screen
    def draw(self):
        pygame.draw.rect(self.screen, (0,255,0), (self.x, self.y, 60, 60)) 
        
        
# bullet = Bullets(screen,rock_rect)
aman = Aman(screen,500,100)
aman1 = Aman(screen, 300,300)
man_group.add(aman)
man_group.add(aman1)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction ='Up'
            elif event.key == pygame.K_SPACE:
                bullet = Bullets(screen,rock_rect)
                group.add(bullet)
                # bullet.updata()
            elif event.key == pygame.K_DOWN:
                direction ="Down"
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = "False"
            elif event.key == pygame.K_DOWN:
                direction = "False"
    screen.fill((255,255,255))
    screen.blit(rock_image,rock_rect)
    update_rock(direction)
    # group.update()
    update_bullets(group)
    aman.draw()
    aman1.draw()
    # group.draw()
    pygame.display.flip()
    # print(len(group))
    # print(pygame.sprite.spritecollideany(aman1, group))


