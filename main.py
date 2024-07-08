import pygame, sys, os
from components import Button, StartButton, Text, TutorialText, LogoButton, Grid, Navbar
from transition import slideLeftToRight

# from dataHandler import dataHandler
from pygame.locals import *
import ScreenState
import alert

if __name__ == "__main__":

    def changeState(
        withAnimation: bool,
        nextState,
        nextStateName: str,
        componentDisable: [],
        componentEnable: [],
    ):
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
    ENGINE_IMAGE = pygame.image.load(os.path.join("assets", "engine.png"))
    INFO_IMAGE = pygame.image.load(os.path.join("assets/icon_button", "info.png"))
    WARN_IMAGE = pygame.image.load(os.path.join("assets/icon_button", "warn.png"))
    ERROR_IMAGE = pygame.image.load(os.path.join("assets/icon_button", "error.png"))
    # data = dataHandler.Datahandler()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0, 0
    startButton = StartButton.StartButton(screen, WIDTH, HEIGHT, ENGINE_IMAGE)
    tamagotchiText = Text.Text(screen, "Tamagotchi", 0, 60, fontSize=50)
    tamagotchiText.verticallyCentered()

    engineEditionText = Text.Text(screen, "Engine Edition", 0, 130, fontSize=20)
    engineEditionText.verticallyCentered()

    byCephasText = Text.Text(screen, "by Cephas", 0, 600, fontSize=20)
    byCephasText.verticallyCentered()

    tutorialA = TutorialText.TutorialText(
        screen,
        WIDTH,
        HEIGHT,
        [
            "You have a starter pet of",
            "a basic engine unit.",
            "Click on the (Infomation) Icon",
            "(Skip this by pressing space)",
        ],
    )

    infoButton = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50)
    infoButton1 = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50)
    infoButton2 = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50)
    infoButton3 = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50)
    infoButton4 = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50)
    infoButton5 = LogoButton.LogoButton(screen, INFO_IMAGE, "pet info", 50, 50, True)
    Grid.Grid_adjuster(
        [infoButton, infoButton1, infoButton2, infoButton3, infoButton4, infoButton5],
        WIDTH / 2 - (infoButton.width * 3 + 10 * 2) / 2,
        50,
        10,
        3,
    )
    nav = Navbar.Navbar(screen, WIDTH, HEIGHT)

    screenState = "start"
    transition = False

    # defining screen state drawing action
    startScreen = ScreenState.State(
        screen,
        (115, 115, 115),
        [startButton],
        [tamagotchiText, engineEditionText, byCephasText],
    )
    introductionScreen = ScreenState.State(screen, (115, 115, 115), [], [tutorialA])
    mainScreen = ScreenState.State(
        screen,
        (115, 115, 115),
        [infoButton, infoButton1, infoButton2, infoButton3, infoButton4, infoButton5],
        [nav],
    )
    # hash table that stores the key value of the name of the state to the State
    screenStateTable = {
        "start": startScreen,
        "intro1": introductionScreen,
        "main": mainScreen,
    }
    while True:
        mouseX, mouseY = pygame.mouse.get_pos()
        # place drawing here
        if transition == False:
            screenStateTable.get(screenState).draw()

        # all event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                data.end()
            # mouse event
            elif event.type == MOUSEMOTION:
                screenStateTable.get(screenState).update(mouseX, mouseY)
                pass
            elif event.type == MOUSEBUTTONDOWN:
                # mouse down event with button event
                if startButton.getHovered():
                    changeState(
                        True,
                        introductionScreen.draw,
                        "intro1",
                        screenStateTable.get(screenState).components,
                        screenStateTable.get("intro1").components,
                    )
                elif infoButton5.getHovered():
                    alert.Alert(
                        screen,
                        screenStateTable.get(screenState).draw,
                        ERROR_IMAGE,
                        "Error",
                        "You haven't reached the level yet",
                    )
            elif event.type == MOUSEBUTTONUP:
                pass
            elif event.type == KEYDOWN:
                # place the key event
                if screenState == "intro1":
                    if tutorialA.awaitSkip(event.key) == True:
                        changeState(
                            True,
                            mainScreen.draw,
                            "main",
                            screenStateTable.get(screenState).components,
                            screenStateTable.get("main").components,
                        )
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(120)
