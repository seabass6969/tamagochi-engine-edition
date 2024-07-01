import pygame, sys
from components import Button
from pygame.locals import *
if __name__ == "__main__":
    pygame.init()
    WIDTH = 600
    HEIGHT = 700
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi")
    mouseX, mouseY = 0,0 
    btn = Button.Button(screen, "a", WIDTH / 2 - 200 / 2,HEIGHT / 2 - 100 / 2, 200,100)
    while True:
        # place drawing here
        screen.fill((115,115,115))
        btn.draw()

        # all event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse event 
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
            elif event.type == KEYDOWN:
                # place the key event
                if event.key in (K_0, K_1):
                    print(0)
        
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(30)