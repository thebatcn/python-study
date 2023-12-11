import pygame
import random

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("Shooting Practice")

# 设置字体
font = pygame.font.SysFont(None, 30)

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)

# 定义矩形目标
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width - 100
        self.rect.y = random.randint(0, screen_height - 50)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0 or self.rect.y > screen_height - 50:
            self.speed *= -1

# 定义飞船
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = screen_height / 2
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > screen_height - 50:
            self.rect.y = screen_height - 50

# 定义子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 5])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

# 创建精灵组
all_sprites = pygame.sprite.Group()
targets = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 创建目标
def create_target():
    target = Target()
    all_sprites.add(target)
    targets.add(target)

# 创建飞船
spaceship = Spaceship()
all_sprites.add(spaceship)

# 创建目标
target = Target()
all_sprites.add(target)
targets.add(target)

# 创建Play按钮
play_button = pygame.Rect(screen_width / 2 - 50, screen_height / 2 - 25, 100, 50)

# 初始化游戏状态
score = 0
game_over = True
nums_bullet = 0

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and play_button.collidepoint(event.pos):
                # 重新开始游戏
                all_sprites.empty()
                targets.empty()
                bullets.empty()
                spaceship = Spaceship()
                all_sprites.add(spaceship)
                create_target()
                score = 0
                game_over = False
                nums_bullet = 0
            elif not game_over and event.button == 1 :
                # 发射子弹
                bullet = Bullet(spaceship.rect.x + 50, (spaceship.rect.centery-5/2))
                all_sprites.add(bullet)
                bullets.add(bullet)
                print("Spaceship.center = {},bullet.center = {}".format(spaceship.rect.center,bullet.rect.center))

    # 更新游戏状态
    if not game_over:
        all_sprites.update()
        # targets.update()

        # 检测子弹和目标的碰撞
        hits = pygame.sprite.groupcollide(bullets, targets, True, True)
        for hit in hits:
            score += 1
            create_target()
            nums_bullet = 0
            bullets.empty()

        # 检测目标是否到达屏幕左侧
        for target in targets:
            if target.rect.x < 0:
                game_over = True

       # 检测子弹是否超出屏幕宽度
        for bullet in bullets:
            if bullet.rect.x > screen_width:
                bullets.remove(bullet)
                nums_bullet += 1
              
            if  nums_bullet >=3:
                game_over = True
        print("nums_bullet = {}".format(nums_bullet))
    # 渲染屏幕
    screen.fill(black)
    all_sprites.draw(screen)
    # targets.draw(screen)

    # 显示得分
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    # 显示Play按钮
    if game_over:
        pygame.draw.rect(screen, white, play_button)
        play_text = font.render("Play", True, black)
        screen.blit(play_text, (screen_width / 2 - 20, screen_height / 2 - 10))

    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)
# 这个示例使用了pygame库来实现游戏开发，通过创建精灵对象和精灵组来管理游戏中的对象。游戏循环中处理事件、更新游戏状态、渲染屏幕和控制帧率。玩家可以通过键盘控制飞船的上下移动，按下空格键发射子弹，击中目标得分，未能击中目标三次游戏结束。重新开始游戏需要单击Play按钮。

# "
#  chrome-extension://dhoenijjpgpeimemopealfcbiecgceod/chat/index.html?reason=newTab#:~:text=%E7%A0%81%E7%A4%BA%E4%BE%8B%EF%BC%9A-,import,-py