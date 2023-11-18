import pygame
import sys
from random import randint

from pygame.sprite import Group

from pygame.sprite import Sprite

SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)

pygame.display.set_caption("Rock")

rock_image = pygame.image.load("飞机1.bmp").convert_alpha()

rock_rect = rock_image.get_rect()

print(rock_rect)
screen_rect = screen.get_rect()
print((screen_rect))

rock_rect.bottom = screen_rect.bottom
rock_y = rock_rect.y

print(rock_rect)


direction = False
bullet_group = Group()

man_group = Group()


def update_rock(direction):
    global rock_y
    if direction == "Up" and rock_rect.y > 0:
        rock_y -= 0.5
        rock_rect.y = rock_y
    elif direction == "Down" and rock_rect.bottom < 480:
        rock_y += 0.5
        rock_rect.y = rock_y

    # print(rock_rect)


class Bullets(Sprite):

    """docstring for Bullets"""

    def __init__(self, screen, rock_rect):
        super(Bullets, self).__init__()

        self.image = pygame.Surface((10,3))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.y = rock_rect.centery
        self.x = rock_rect.right

        
        self.screen = screen


    def update(self):
        # print((self.x, self.y))

        # if self.x + 10 > screen_rect.right:

        #     self.x = screen_rect.right -10

        # else:

        self.x += 1
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

def update_bullets(bullets, man_group):
    bullets.update()

    for bullet in bullets.copy():
        bullet.draw()

        if bullet.rect.x > screen_rect.right:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, man_group, True, True)
    if collisions:
        print("collisions = ", collisions)
    # print(len(bullets))


class Aman(Sprite):

    """docstring for Aman"""
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((60,60)) 
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        self.screen.blit(self.image, self.rect)

# bullet = Bullets(screen,rock_rect)

aman = Aman(screen, 500, 100)

aman1 = Aman(screen, 300, 300)
man_group.add(aman)

man_group.add(aman1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "Up"

            elif event.key == pygame.K_SPACE:
                bullet = Bullets(screen, rock_rect)
                bullet_group.add(bullet)
                print("现在子弹数量是：",len(bullet_group))
            elif event.key == pygame.K_1:
                aman = Aman(screen, randint(69,640), randint(60,420))  #横坐标要大于飞机的宽和aman高度
                man_group.add(aman)
                print("现在aman数量是：",len(man_group))
                # bullet.updata()

            elif event.key == pygame.K_DOWN:
                direction = "Down"

            elif event.key == pygame.K_q:
                pygame.quit()

                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = "False"

            elif event.key == pygame.K_DOWN:
                direction = "False"

    screen.fill((255, 255, 255))

    screen.blit(rock_image, rock_rect)

    update_rock(direction)

    # group.update()

    update_bullets(bullet_group, man_group)

    man_group.draw(screen)
    # aman.draw()

    # aman1.draw()

    # group.draw()
    pygame.display.flip()

    # print(len(group))

    # print(pygame.sprite.spritecollideany(aman1, group))
