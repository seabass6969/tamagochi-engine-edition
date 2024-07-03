import pygame, sys, os
from components import Button,StartButton, Text, TutorialText
from transition import slideLeftToRight
from pygame.locals import *
if __name__ == "__main__":
    pygame.init()
    WIDTH = 600
    HEIGHT = 700
    # load assets
    ENGINEIMAGE = pygame.image.load(os.path.join('assets', 'engine.png'))

    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0,0 
    btn = StartButton.StartButton(screen, WIDTH, HEIGHT, ENGINEIMAGE)
    tamagotchiText = Text.Text(screen, "Tamagotchi", 0, 60, fontSize=50)
    tamagotchiText.verticallyCentered()

    engineEditionText = Text.Text(screen, "Engine Edition", 0, 130, fontSize=20)
    engineEditionText.verticallyCentered()

    tutorialA = TutorialText.TutorialText(screen, WIDTH, HEIGHT, ["Test 1", "Test 2"])
    screenState = 0
    transition = False
    # screen state:
    # 0 - start screen 
    # 1 - 
    while True:
        # defining screen state drawing action
        def startScreen():
            screen.fill((115,115,115))
            tamagotchiText.draw()
            engineEditionText.draw()
            btn.draw()
        def introductionScreen():
            screen.fill((115,115,115))
            tutorialA.draw()
        # place drawing here
        if transition == False:
            if screenState == 0:
                startScreen()
            elif screenState == 1:
                introductionScreen()

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
                    transition = True
                    slideLeftToRight(screen, fpsClock, introductionScreen)
                    transition = False
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
            elif event.type == KEYDOWN:
                # place the key event
                if event.key in (K_0, K_1):
                    print(True)
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(30)