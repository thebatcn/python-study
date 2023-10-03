import pygame
import sys
import settings
import bullet
SCREEN_SIZE = (640,480)

bullets = bullet.Bullet()
st = settings.Settings()
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
pygame.display.set_caption('One test')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill((255,255,255))
        pygame.draw.rect(screen,st.bullet_color,(100,100,st.bullet_width,st.bullet_height))
        pygame.display.flip()



            
            