import pygame, sys, os
from components import Button ,StartButton, Text, TutorialText
from transition import slideLeftToRight
from dataHandler import dataHandler
from pygame.locals import *
import ScreenState

if __name__ == "__main__":
    def changeState(withAnimation: bool, nextState, nextStateName: str, componentDisable: [], componentEnable: []):
        global screenState
        screenState = nextStateName 
        pygame.mouse.set_cursor(pygame.cursors.arrow)
        for component in componentDisable:
            component.setVisibility(False)
        for component in componentEnable:
            component.setVisibility(True)
        if withAnimation:
            global transition
            transition = True
            slideLeftToRight(screen, fpsClock, nextState)
            transition = False
        
    pygame.init()
    WIDTH = 600
    HEIGHT = 700
    # load assets
    ENGINEIMAGE = pygame.image.load(os.path.join('assets', 'engine.png'))
    data = dataHandler.Datahandler()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0,0 
    startButton = StartButton.StartButton(screen, WIDTH, HEIGHT, ENGINEIMAGE)
    tamagotchiText = Text.Text(screen, "Tamagotchi", 0, 60, fontSize=50)
    tamagotchiText.verticallyCentered()

    engineEditionText = Text.Text(screen, "Engine Edition", 0, 130, fontSize=20)
    engineEditionText.verticallyCentered()

    byCephasText = Text.Text(screen, "by Cephas", 0, 600, fontSize=20)
    byCephasText.verticallyCentered()

    tutorialA = TutorialText.TutorialText(screen, WIDTH, HEIGHT, ["You have a starter pet of", "a basic engine unit.", "Click on the (Infomation) Icon", "(Skip this by pressing space)"])
    screenState = "start"
    transition = False

    # defining screen state drawing action
    startScreen = ScreenState.State(screen, (115,115,115), [tamagotchiText, engineEditionText, byCephasText, startButton])
    introductionScreen = ScreenState.State(screen, (115,115,115), [tutorialA])
    mainScreen = ScreenState.State(screen, (115,115,115), [])
    screenStateTable = {"start": startScreen, "intro1": introductionScreen, "main": mainScreen}
    while True:
            
        # place drawing here
        if transition == False:
            screenStateTable.get(screenState).draw()
            screenStateTable.get(screenState).update(mouseX, mouseY)


        # all event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                data.end()
            # mouse event 
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                if startButton.getHovered() and startButton.getVisibility():
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                # mouse down event with button event
                if startButton.getHovered() and startButton.getVisibility():
                    changeState(True, introductionScreen.draw, "intro1", [startButton, byCephasText, engineEditionText, tamagotchiText], [])
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
            elif event.type == KEYDOWN:
                # place the key event
                if screenState == "intro1":
                    if tutorialA.awaitSkip(event.key) == True:
                        changeState(True)
                        transition = True
                        slideLeftToRight(screen, fpsClock, mainScreen)
                        transition = False
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(30)