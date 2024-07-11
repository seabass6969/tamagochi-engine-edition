import pygame, sys, random, math
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
    InfoPageConstructor,
    MemoryGameConstructor
)

# from dataHandler import dataHandler
from pygame.locals import *
import ScreenState
import Alert
from Level import Level, levelUnlockCheck, REQUIREMENT
from asset import IMAGE
from dataHandler import dataHandler


WIDTH = 600
HEIGHT = 700
# load assets
if __name__ == "__main__":

    screenState = "start"
    transition = False
    pygame.init()
    data = dataHandler.Datahandler()

    # gotchiPoint = data.getGotchiPoint()

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
        levelUnlockCheck(
            data.getLevel().getLevel(), REQUIREMENT.get("JUMPING_ROPE_GAME")
        ),
        REQUIREMENT.get("JUMPING_ROPE_GAME"),
    )
    catchinggameButton = LogoButton.LogoButton(
        screen,
        "catching",
        IMAGE.get("HAND"),
        "Catch",
        50,
        50,
        levelUnlockCheck(data.getLevel().getLevel(), REQUIREMENT.get("CATCH_GAME")),
        REQUIREMENT.get("CATCH_GAME"),
    )
    racinggameButton = LogoButton.LogoButton(
        screen,
        "racing",
        IMAGE.get("CAR"),
        "Racing",
        50,
        50,
        levelUnlockCheck(data.getLevel().getLevel(), REQUIREMENT.get("RACING_GAME")),
        REQUIREMENT.get("RACING_GAME"),
    )

    testButton = LogoButton.LogoButton(
        screen,
        "test",
        IMAGE.get("TEST"),
        "TEST ONLY",
        50,
        50,
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
        testButton,
    ]
    Grid.Grid_adjuster(
        mainScreenButton,
        WIDTH / 2 - (infoButton.width * 3 + 10 * 2) / 2,
        nav.height + 20,
        10,
        3,
    )
    # Info Page:
    infopageConstructor = InfoPageConstructor.InfoPageConstructor(screen, data)
    # memory Page:
    memoryGameConstructor = MemoryGameConstructor.MemoryGameConstructor(screen, data)
    # Bug page:
    hurtButton = Button.Button(screen, "hurt", 20, nav.height + 10, 100, 100)
    gotchiButton = Button.Button(screen, "gotchi", 20, nav.height + 20 + 100, 100, 100)
    emotionButton = Button.Button(screen, "emotion", 20, nav.height + 30 + 200, 100, 100)
    batteryButton = Button.Button(screen, "battery", 20, nav.height + 40 + 300, 100, 100)
    # batteryButton = Button.Button(screen, "battery", 20, nav.height + 40 + 300, 100, 100)
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
    mainScreen = ScreenState.State(
        screen,
        "main",
        (115, 115, 115),
        mainScreenButton,  # all menu button
        [],
        optional_navbar=True,
        optional_navbar_options=data,
    )
    infoScreen = ScreenState.State(
        screen,
        "info",
        (115, 115, 115),
        [],
        [infopageConstructor],
        optional_update_component=[infopageConstructor],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    marketScreen = ScreenState.State(
        screen,
        "market",
        (115, 115, 115),
        [],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    memoryScreen = ScreenState.State(
        screen,
        "memory",
        (115, 115, 115),
        [memoryGameConstructor],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    testScreen = ScreenState.State(
        screen,
        "test",
        (115, 115, 115),
        [hurtButton, gotchiButton, emotionButton, batteryButton],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    # hash table that stores the key value of the name of the state to the State
    screenStateTable = {
        "start": startScreen,
        "intro1": introductionScreen,
        "main": mainScreen,
        "info": infoScreen,
        "market": marketScreen,
        "memory": memoryScreen,
        "test": testScreen,
    }
    for component in screenStateTable.get(screenState).components:
        component.setVisibility(True)

    while True:
        mouseX, mouseY = pygame.mouse.get_pos()
        # place drawing here
        if transition == False:
            screenStateTable.get(screenState).draw()
            screenStateTable.get(screenState).update(mouseX, mouseY, data)

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
                    if data.getDoneTutorial():
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
                elif screenState == "test":
                    if gotchiButton.getHovered():
                        data.increaseGotchiPoint(10)
                    if hurtButton.getHovered():
                        data.decreaseHealth(1)
                    if emotionButton.getHovered():
                        listEmotion = ["happy", "sad", "ill", "mid", "angry"]
                        data.setEmotion(random.choice(listEmotion))
                        print(data.getEmotion())
                    if batteryButton.getHovered():
                        data.setBatteryLevel(0.5)
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
                        data.setDoneTutorial(True)

        # update the display and the target FPS is infinity
        FPS_DISPLAY = True
        if FPS_DISPLAY:
            FONT = pygame.font.SysFont("Comic Sans MS", 20)
            TEXT = FONT.render(str(math.floor(fpsClock.get_fps())), False, (0,0,0))
            screen.blit(TEXT, (10,10))
        pygame.display.update()
        fpsClock.tick(0)

