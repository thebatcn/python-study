import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame import time


class Ball(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.pos = [randint(10, 620), randint(10, 460)]
        self.radius = 10
        self.speed = 5
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.radius, self.radius)
        self.loss = 3

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), self.pos, self.radius)

    def update(self):
        if self.pos[1] > 470:
            self.pos[1] = 0
            self.loss -= 1
        elif self.speed < 0 and self.pos[1] < 10:
            self.speed = abs(self.speed)
        else:
            self.pos[1] += self.speed
            self.rect = pygame.Rect(self.pos[0], self.pos[1], self.radius, self.radius)


class Paddle(Sprite):
    def __init__(self, screen, direction):
        super().__init__()
        self.screen = screen
        self.pos = [320, 460]
        self.x = self.pos[0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 10)
        self.direction = direction

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

    def update(self):
        if self.direction:
            if self.direction == "Left" and self.x > 0:
                self.x -= 5
                self.pos[0] = self.x
            elif self.direction == "Right" and self.rect.right < 640:
                self.x += 5
                self.pos[0] = self.x
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 10)


def is_collsion(ball, paddle):
    if ball.rect.colliderect(paddle.rect):
        ball.speed = -ball.speed
        return True


def isloss(ball):
    if ball.rect.bottom > 470:
        return True


def check_gameactive(ball):
    global game_active
    if ball.loss == 0:
        game_active = False
        return False
    elif ball.loss > 0:
        game_active = True
        return True


# 游戏主循环
SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, depth=32)
pygame.display.set_caption("13-5抓球")
clock = time.Clock()
direction = False
game_active = True

ball = Ball(screen)
ballsprint = pygame.sprite.Group()

paddle = Paddle(screen, direction)
# print("\n",paddle.pos)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.direction = "Left"
            if event.key == pygame.K_RIGHT:
                paddle.direction = "Right"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle.direction = False
            if event.key == pygame.K_RIGHT:
                paddle.direction = False
            # if event.key == pygame.K_SPACE:
            #     ballsprint.add(Ball(screen))
    if game_active:

        screen.fill((0, 0, 0))
        ball.draw()
        paddle.update()
        paddle.draw()
        ball.update()
        is_collsion(ball, paddle)
        # print("\n",paddle.pos)
        if isloss(ball):
            game_active = check_gameactive(ball)
        clock.tick(60)
        pygame.display.update()

        print("ball.loss: {}".format(ball.loss))
        print("game_active: {}".format(game_active))
