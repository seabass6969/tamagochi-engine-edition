import pygame, sys, os
from components import (
    Button,
    StartButton,
    Text,
    TutorialText,
    LogoButton,
    Grid,
    Navbar,
    TextAnimator,
    Image,
    LevelDisplay
)
from transition import slideLeftToRight

# from dataHandler import dataHandler
from pygame.locals import *
import ScreenState
import Alert
from Level import Level, levelUnlockCheck, REQUIREMENT

if __name__ == "__main__":

    def numberAdjuster(number: int, degits: int) -> str:
        num = str(number)
        return (degits - len(num)) * "0" + num

    def changeState(
        withAnimation: bool,
        nextState: ScreenState.State,
        previousState: ScreenState.State,
        # nextStateName: str,
        componentDisable: [] = [],
        componentEnable: [] = [],
    ):
        global screenState
        screenState = nextState.name
        pygame.mouse.set_cursor(pygame.cursors.arrow)
        componentDisable.extend(previousState.components)
        componentEnable.extend(nextState.components)

        for component in componentDisable:
            component.setVisibility(False)
        for component in componentEnable:
            component.setVisibility(True)
        if withAnimation:
            global transition
            transition = True
            slideLeftToRight(screen, fpsClock, nextState.draw)
            transition = False

    pygame.init()
    WIDTH = 600
    HEIGHT = 700
    # load assets
    IMAGE = {
        "ENGINE": pygame.image.load(os.path.join("assets", "engine.png")),
        "INFO": pygame.image.load(os.path.join("assets/icon_button", "info.png")),
        "SHOP": pygame.image.load(os.path.join("assets/icon_button", "shop.png")),
        "WARN": pygame.image.load(os.path.join("assets/icon_button", "warn.png")),
        "ERROR": pygame.image.load(os.path.join("assets/icon_button", "error.png")),
        "GARAGE": pygame.image.load(os.path.join("assets/icon_button", "garage.png")),
        "BRAIN": pygame.image.load(os.path.join("assets/icon_button", "brain.png")),
        "STRING": pygame.image.load(os.path.join("assets/icon_button", "string.png")),
        "HAND": pygame.image.load(os.path.join("assets/icon_button", "hand.png")),
        "CAR": pygame.image.load(os.path.join("assets/icon_button", "car.png")),
        "HEART": pygame.image.load(os.path.join("assets/icon_button", "heart.png")),
    }
    # data = dataHandler.Datahandler()

    level = Level(1, 0.1)
    gochiPoint = 0
    health = 10  # the max health is 10
    tutorial = False  # false means done

    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0, 0
    startButton = StartButton.StartButton(screen, WIDTH, HEIGHT, IMAGE.get("ENGINE"))
    tamagotchiText = Text.Text(screen, "Tamagotchi", 0, 60, fontSize=50)
    tamagotchiText.verticallyCentered()
    animatedText = TextAnimator.TextAnimator(
        screen, tamagotchiText.x + tamagotchiText.TEXTRECT.width, tamagotchiText.y
    )

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
    infoButton = LogoButton.LogoButton(screen, "info" ,IMAGE.get("INFO"), "Pet Info", 50, 50)
    marketButton = LogoButton.LogoButton(
        screen, "market", IMAGE.get("SHOP"), "Marketplace", 50, 50
    )
    garageButton = LogoButton.LogoButton(screen, "garage", IMAGE.get("GARAGE"), "Garage", 50, 50)
    memorygameButton = LogoButton.LogoButton(
        screen, "memory", IMAGE.get("BRAIN"), "Memory Game", 50, 50
    )
    jumpinggameButton = LogoButton.LogoButton(
        screen,
        "jumping",
        IMAGE.get("STRING"),
        "Jumping Rope",
        50,
        50,
        levelUnlockCheck(level.getLevel(), REQUIREMENT.get("JUMPING_ROPE_GAME")),
        REQUIREMENT.get("JUMPING_ROPE_GAME"),
    )
    catchinggameButton = LogoButton.LogoButton(
        screen,
        "catching",
        IMAGE.get("HAND"),
        "Catch",
        50,
        50,
        levelUnlockCheck(level.getLevel(), REQUIREMENT.get("CATCH_GAME")),
        REQUIREMENT.get("CATCH_GAME"),
    )
    racinggameButton = LogoButton.LogoButton(
        screen,
        "racing",
        IMAGE.get("CAR"),
        "Racing",
        50,
        50,
        levelUnlockCheck(level.getLevel(), REQUIREMENT.get("RACING_GAME")),
        REQUIREMENT.get("RACING_GAME"),
    )
    nav = Navbar.Navbar(screen, WIDTH, HEIGHT)
    Grid.Grid_adjuster(
        [
            infoButton,
            marketButton,
            garageButton,
            memorygameButton,
            jumpinggameButton,
            catchinggameButton,
            racinggameButton,
        ],
        WIDTH / 2 - (infoButton.width * 3 + 10 * 2) / 2,
        nav.height + 20,
        10,
        3,
    )

    healthText = Text.Text(
        screen, ": {} / 10 ".format(numberAdjuster(health, 2)), 0, 0, fontSize=26
    )
    healthtextHeight = healthText.TEXTRECT.height
    healthImageScaled = pygame.transform.scale(
        IMAGE.get("HEART"), (healthtextHeight, healthtextHeight)
    )
    healthImage = Image.Image(screen, 10, 10, healthImageScaled)
    leveldisplay = LevelDisplay.LevelDisplay(screen, 10,10, level.getLevel(), level.getProgression(), 150, healthtextHeight)
    navbarItem = [healthImage, healthText, leveldisplay]
    combined_width = 0
    for i in navbarItem:
        combined_width += i.width
    Grid.Grid_adjuster(
        navbarItem,
        WIDTH / 2 - (combined_width + 8 * len(navbarItem)) / 2,
        30,
        8,
        999999,
    )
    screenState = "start"
    transition = False

    # defining screen state drawing action
    startScreen = ScreenState.State(
        screen,
        "start",
        (115, 115, 115),
        [startButton],
        [tamagotchiText, engineEditionText, byCephasText, animatedText],
    )
    introductionScreen = ScreenState.State(screen, "intro1", (115, 115, 115), [], [tutorialA])
    realNavbarItem = [nav]
    realNavbarItem.extend(navbarItem)
    mainScreen = ScreenState.State(
        screen,
        "main",
        (115, 115, 115),
        [
            # all menu button
            infoButton,
            marketButton,
            garageButton,
            memorygameButton,
            jumpinggameButton,
            catchinggameButton,
            racinggameButton,
        ],
        realNavbarItem,
        optional_update_component=[leveldisplay]
    )
    infoScreen = ScreenState.State(screen,"info" , (115,115,115), [], realNavbarItem, optional_update_component=[leveldisplay])
    marketScreen = ScreenState.State(screen,"market", (115,115,115), [], realNavbarItem, optional_update_component=[leveldisplay])
    # hash table that stores the key value of the name of the state to the State
    screenStateTable = {
        "start": startScreen,
        "intro1": introductionScreen,
        "main": mainScreen,
        "info": infoScreen,
        "market": marketScreen,
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
                    if tutorial == False:
                        changeState(
                            True,
                            screenStateTable.get("main"),
                            screenStateTable.get(screenState),
                        )
                    else:
                        changeState(
                            True,
                            screenStateTable.get("intro1"),
                            screenStateTable.get(screenState),
                        )
                if screenState == "main":
                    for button in mainScreen.components_button:
                        if (
                            button.disabled
                            and button.getHovered()
                            and button.__class__.__name__ == "LogoButton"
                        ):

                            Alert.Alert(
                                screen,
                                screenStateTable.get(screenState).draw,
                                IMAGE.get("ERROR"),
                                "Low level",
                                "Come back when you are level {}!".format(
                                    button.level_requirement
                                ),
                            )
                        if (button.getHovered() and button.__class__.__name__ == "LogoButton"):
                            changeState(
                                True,
                                screenStateTable.get("intro1"),
                                screenStateTable.get(screenState),
                            )
                            
            elif event.type == MOUSEBUTTONUP:
                pass
            elif event.type == KEYDOWN:
                # place the key event
                if screenState == "intro1":
                    if tutorialA.awaitSkip(event.key) == True:
                            changeState(
                                True,
                                screenStateTable.get("main"),
                                screenStateTable.get(screenState),
                            )
        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(120)
