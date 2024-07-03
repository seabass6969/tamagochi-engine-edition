import pygame, sys
from components import Button,StartButton, Text
from pygame.locals import *
if __name__ == "__main__":
    pygame.init()
    WIDTH = 600
    HEIGHT = 700
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0,0 
    # btn = Button.Button(screen, "a", WIDTH / 2 - 200 / 2,HEIGHT / 2 - 100 / 2, 200,100)
    btn = StartButton.StartButton(screen, WIDTH, HEIGHT)
    tamagotchiText = Text.Text(screen, "Tamagotchi", 0, 60, fontSize=50)
    tamagotchiText.verticallyCentered()

    engineEditionText = Text.Text(screen, "Engine Edition", 0, 130, fontSize=20)
    engineEditionText.verticallyCentered()

    introText = Text.Text(screen, "Your new pet is called", 0, 0)
    screenState = 0
    # screen state:
    # 0 - start screen 
    # 1 - 
    while True:
        # place drawing here
        if screenState == 0:
            screen.fill((115,115,115))
            tamagotchiText.draw()
            engineEditionText.draw()
            btn.draw()
        elif screenState == 1:
            screen.fill((115,115,115))
            introText.draw()

        # update for each component
        if screenState == 0:
            btn.update(mouseX, mouseY)

        # all event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # mouse event 
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                if btn.getHovered() and btn.getVisibility():
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                # mouse down event
                if btn.getHovered() and btn.getVisibility():
                    screenState = 1
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
                    btn.setVisibility(False)
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
            elif event.type == KEYDOWN:
                # place the key event
                if event.key in (K_0, K_1):
                    print(True)
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(30)