import sys
import pygame
import pygame.font

def init_pygame():

    SCREEN_SIZE = (640,480)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
    pygame.display.set_caption('play_button')

class Button():
    def __init__(self,screen,msg):
        self.screen = screen
        self.button_width,self.button_height = 200,50

        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.font = pygame.font.SysFont(None, 48)

        self.pre_msg(msg)

    def pre_msg(self,msg):
        self.msg_image = self.font.render(msg,True,(255,255,255),(255,0,255))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill((255,0,255),self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


def main():
 
    SCREEN_SIZE = (640,480)

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,0,depth=32)
    pygame.display.set_caption('play_button')
    play_button = Button(screen, "Play")

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        play_button.draw_button()
        pygame.display.flip()
if __name__ == "__main__":
    main()