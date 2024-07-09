import pygame, sys
from components import (
    Button,
    StartButton,
    BackButton,
    Text,
    TutorialText,
    LogoButton,
    Grid,
    Navbar,
    TextAnimator,
    Image,
    LevelDisplay,
    Gap,
)

# from dataHandler import dataHandler
from pygame.locals import *
import ScreenState
import Alert
from Level import Level, levelUnlockCheck, REQUIREMENT
from asset import IMAGE


WIDTH = 600
HEIGHT = 700
# load assets
if __name__ == "__main__":

    def numberAdjuster(number: int, degits: int) -> str:
        num = str(number)
        return (degits - len(num)) * "0" + num

    screenState = "start"
    transition = False
    pygame.init()
    # data = dataHandler.Datahandler()

    level = Level(1, 0.1)
    gochiPoint = 0
    health = 10  # the max health is 10
    tutorial = False  # false means done

    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0, 0
    startButton = StartButton.StartButton(screen, WIDTH, HEIGHT)
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

    infoButton = LogoButton.LogoButton(
        screen, "info", IMAGE.get("INFO"), "Pet Info", 50, 50
    )
    marketButton = LogoButton.LogoButton(
        screen, "market", IMAGE.get("SHOP"), "Marketplace", 50, 50
    )
    garageButton = LogoButton.LogoButton(
        screen, "garage", IMAGE.get("GARAGE"), "Garage", 50, 50
    )
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
    mainScreenButton = [
        infoButton,
        marketButton,
        garageButton,
        memorygameButton,
        jumpinggameButton,
        catchinggameButton,
        racinggameButton,
    ]
    Grid.Grid_adjuster(
        mainScreenButton,
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
    cashImageScaled = pygame.transform.scale(
        IMAGE.get("CASH"), (healthtextHeight, healthtextHeight)
    )
    cashImage = Image.Image(screen, 0, 0, cashImageScaled)
    cashText = Text.Text(screen, ": {}".format(gochiPoint), 0, 0, fontSize=26)
    leveldisplay = LevelDisplay.LevelDisplay(
        screen, 10, 10, level.getLevel(), level.getProgression(), 150, healthtextHeight
    )
    navbarItem = [
        healthImage,
        healthText,
        cashImage,
        cashText,
        Gap.Gap(screen, 0, 0, 20, 10),
        leveldisplay,
    ]
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

    # defining screen state drawing action
    startScreen = ScreenState.State(
        screen,
        "start",
        (115, 115, 115),
        [startButton],
        [tamagotchiText, engineEditionText, byCephasText, animatedText],
    )
    introductionScreen = ScreenState.State(
        screen, "intro1", (115, 115, 115), [], [tutorialA]
    )
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
        optional_update_component=[leveldisplay],
    )
    infoScreen = ScreenState.State(
        screen,
        "info",
        (115, 115, 115),
        [],
        realNavbarItem,
        optional_update_component=[leveldisplay],
        optional_back_button=True
    )
    marketScreen = ScreenState.State(
        screen,
        "market",
        (115, 115, 115),
        [],
        realNavbarItem,
        optional_update_component=[leveldisplay],
        optional_back_button=True
    )
    # hash table that stores the key value of the name of the state to the State
    screenStateTable = {
        "start": startScreen,
        "intro1": introductionScreen,
        "main": mainScreen,
        "info": infoScreen,
        "market": marketScreen,
    }
    for component in screenStateTable.get(screenState).components:
        component.setVisibility(True)
    while True:
        mouseX, mouseY = pygame.mouse.get_pos()
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
                pass
            elif event.type == MOUSEBUTTONDOWN:
                # mouse down event with button event
                if startButton.getHovered():
                    if tutorial == False:
                        screenState = ScreenState.changeState(
                            True,
                            screenStateTable.get("main"),
                            screenStateTable.get(screenState),
                            screen,
                            fpsClock,
                        )
                    else:
                        screenState = ScreenState.changeState(
                            True,
                            screenStateTable.get("intro1"),
                            screenStateTable.get(screenState),
                            screen,
                            fpsClock,
                        )
                if screenState == "main":
                    for button in mainScreenButton:
                        if button.getHovered():
                            if button.disabled:
                                Alert.Alert(
                                    screen,
                                    screenStateTable.get(screenState),
                                    IMAGE.get("ERROR"),
                                    "Low level",
                                    "Come back when you are level {}!".format(
                                        button.level_requirement
                                    ),
                                )
                            else:
                                screenState = ScreenState.changeState(
                                    True,
                                    screenStateTable.get(button.name),
                                    screenStateTable.get(screenState),
                                    screen,
                                    fpsClock,
                                )

                # backButton listener
                if screenStateTable.get(screenState).getBackButtonHover():
                    screenState = ScreenState.changeState(
                        True,
                        screenStateTable.get("main"),
                        screenStateTable.get(screenState),
                        screen,
                        fpsClock,
                    )
                        
            elif event.type == MOUSEBUTTONUP:
                pass
            elif event.type == KEYDOWN:
                # place the key event
                if screenState == "intro1":
                    if tutorialA.awaitSkip(event.key) == True:
                        screenState = ScreenState.changeState(
                            True,
                            screenStateTable.get("main"),
                            screenStateTable.get(screenState),
                            screen,
                            fpsClock,
                        )

        # update the display and the target FPS is 30
        pygame.display.update()
        fpsClock.tick(120)
