import pygame, sys, random, math, os 
from prerender.preRenderErase import (
    cleanCache
)
from components.displays.text import (
    Text,
    TutorialText,
    TextAnimator,
)
from components.displays import (
    Navbar,
    Image,
    LevelDisplay,
)
from components import (
    Grid,
    Gap,
)
from components.interactables.button import (
    Button,
    StartButton,
    BackButton,
    LogoButton,
)
from components.constructors import (
    InfoPageConstructor,
    MemoryGameConstructor,
    MarketplaceConstructor,
    GaragePageConstructor,
    JumpingRopeGameConstructor
)
from constants.tutorial import TutorialScreen, footerText, tutorial_text

# from dataHandler import dataHandler
from pygame.locals import *
import ScreenState
import Alert
from constants.Level import Level, levelUnlockCheck, REQUIREMENT
from constants.asset import IMAGE, IMAGE_LOADING
from dataHandler import dataHandler


WIDTH = 600
HEIGHT = 700
# load assets
if __name__ == "__main__":

    if not os.path.exists("../prerender"):
        os.makedirs("../prerender")
    screenState = "start"
    transition = False
    pygame.init()

    
    data = dataHandler.Datahandler()
    data.setLastLogin()

    # gotchiPoint = data.getGotchiPoint()

    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tamagotchi Engine edition")
    mouseX, mouseY = 0, 0

    screen.blit(IMAGE_LOADING, (0,0))

    # home screen
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

    # tutorial screen 
    tutorialScreen = TutorialScreen(screen, footerText, tutorial_text)

    # menu screen 
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
    perfectcircleGameButton = LogoButton.LogoButton(
        screen,
        "circle",
        IMAGE.get("DRAWING"),
        "Perfect Circle",
        50,
        50,
        levelUnlockCheck(data.getLevel().getLevel(), REQUIREMENT.get("CIRCLE_GAME")),
        REQUIREMENT.get("CIRCLE_GAME"),
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
        perfectcircleGameButton,
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
    memoryGameConstructor = MemoryGameConstructor.MemoryGameConstructor(
        screen, nav.height + 10
    )
    # Marketplace Page
    marketplaceConstructor = MarketplaceConstructor.MarketplaceConstructor(screen, nav.height + 10)
    # Garage Page:
    garagePageConstructor = GaragePageConstructor.GaragePageConstructor(screen, nav.height + 10, data)
    # JumpingRope Game Page:
    jumpingRopeGameConstructor = JumpingRopeGameConstructor.JumpingRopeGameConstructor(screen, nav.height + 10)
    # Bug page:
    hurtButton = Button.Button(screen, "hurt", 20, nav.height + 10, 100, 100)
    gotchiButton = Button.Button(screen, "gotchi", 20, nav.height + 20 + 100, 100, 100)
    emotionButton = Button.Button(
        screen, "emotion", 20, nav.height + 30 + 200, 100, 100
    )
    batteryButton = Button.Button(
        screen, "battery", 20, nav.height + 40 + 300, 100, 100
    )
    increaserButton = Button.Button(
        screen, "level increase", 20, nav.height + 50 + 400, 300, 100
    )
    # batteryButton = Button.Button(screen, "battery", 20, nav.height + 40 + 300, 100, 100)
    # defining screen state drawing action
    startScreen = ScreenState.State(
        screen,
        "start",
        [(180, 41, 249), (38,197,243)],
        [startButton],
        [tamagotchiText, engineEditionText, byCephasText, animatedText],
    )
    # introductionScreen = ScreenState.State(
    #     screen, "intro1", (115, 115, 115), [], [tutorialA]
    # )
    mainScreen = ScreenState.State(
        screen,
        "main",
        [(165, 194, 193), (30, 108, 142)],
        mainScreenButton,  # all menu button
        [],
        optional_navbar=True,
        optional_navbar_options=data,
    )
    infoScreen = ScreenState.State(
        screen,
        "info",
        [(255, 202, 166), (248, 101, 148)],
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
        [(243, 245, 32), (89, 209, 2)],
        [marketplaceConstructor],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    garageScreen = ScreenState.State(
        screen,
        "garage",
        [(94, 55, 25), (178, 164, 150)],
        [garagePageConstructor],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    memoryScreen = ScreenState.State(
        screen,
        "memory",
        [(94, 55, 25), (178, 164, 150)],
        [memoryGameConstructor],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    jumpinggameScreen = ScreenState.State(
        screen,
        "jumping",
        [(94, 55, 25), (178, 164, 150)],
        [jumpingRopeGameConstructor],
        [],
        optional_update_component=[jumpingRopeGameConstructor],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    catchinggameScreen = ScreenState.State(
        screen,
        "catching",
        [(94, 55, 25), (178, 164, 150)],
        [],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    perfectcircleGameScreen = ScreenState.State(
        screen,
        "circle",
        [(94, 55, 25), (178, 164, 150)],
        [],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    racinggameScreen = ScreenState.State(
        screen,
        "racing",
        [(94, 55, 25), (178, 164, 150)],
        [],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    testScreen = ScreenState.State(
        screen,
        "test",
        (115, 115, 115),
        [hurtButton, gotchiButton, emotionButton, batteryButton, increaserButton],
        [],
        optional_navbar=True,
        optional_navbar_options=data,
        optional_back_button=True,
    )
    # hash table that stores the key value of the name of the state to the State
    screenStateTable = {
        "start": startScreen,
        "main": mainScreen,
        "info": infoScreen,
        "market": marketScreen,
        "garage": garageScreen,
        "memory": memoryScreen,
        "jumping": jumpinggameScreen,
        "catching": catchinggameScreen,
        "circle": perfectcircleGameScreen,
        "racing": racinggameScreen,
        "test": testScreen,
    }
    screenStateTable.update(tutorialScreen.generatedDict)
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
                data.end()
                cleanCache()
                sys.exit()

                if data.isDead():
                    data.wipeData()
                    pygame.quit()
                    cleanCache()
                    sys.exit()
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
                            screenStateTable.get("intro0"),
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
                                    "ERROR",
                                    "Low level",
                                    [
                                        "Your level is {}.".format(
                                            data.getLevel().getLevel()
                                        ),
                                        "You haven't met the level requirement",
                                        "Come back when you are level {}!".format(
                                            button.level_requirement
                                        ),
                                    ],
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
                    if increaserButton.getHovered():
                        data.increaseLevel(10)
                elif screenState == "memory":
                    memoryGameConstructor.clickRegister()
                elif screenState == "market":
                    marketplaceConstructor.clickRegister(data, screenStateTable.get(screenState))
                elif screenState == "garage":
                    garagePageConstructor.clickRegister(data, screenStateTable.get(screenState))
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
                if screenState[:5] == "intro":
                    if tutorialScreen.awaitSkip(event.key) == True:
                        if tutorialScreen.reachedEnds() == False:
                            tutorialScreen.introIncrement += 1
                            screenState = ScreenState.changeState(
                                True,
                                screenStateTable.get("intro{}".format(tutorialScreen.introIncrement)),
                                screenStateTable.get(screenState),
                                screen,
                                fpsClock,
                            )
                        else:
                            screenState = ScreenState.changeState(
                                True,
                                screenStateTable.get("main"),
                                screenStateTable.get(screenState),
                                screen,
                                fpsClock,
                            )
                            data.setDoneTutorial(True)
                elif screenState == "jumping":
                    jumpingRopeGameConstructor.keyRegister(event.key, True)
            elif event.type == KEYUP:
                if screenState == "jumping":
                    jumpingRopeGameConstructor.keyRegister(event.key, False)
                    
                
        if screenState == "memory" and memoryGameConstructor.switchAfterWon:
            screenState = ScreenState.changeState(
                True,
                screenStateTable.get("main"),
                screenStateTable.get(screenState),
                screen,
                fpsClock,
            )
            memoryGameConstructor.switchAfterWon = False
        if screenState == "main":
            for button in mainScreenButton:
                if button.level_requirement != 0:
                    button.disabled = levelUnlockCheck(data.getLevel().getLevel(), button.level_requirement)
        if data.isDead():

            Alert.Alert(
                screen,
                screenStateTable.get(screenState),
                "SKULL",
                "RIP",
                [
                    "Your pet is dead and",
                    "the age of death is: ",
                    "{}".format(data.petAge()),
                ],
            )
            data.wipeData()

            pygame.quit()
            cleanCache()
            sys.exit()

        
        # update the display and the target FPS is infinity
        FPS_DISPLAY = True
        if FPS_DISPLAY:
            FONT = pygame.font.SysFont("Comic Sans MS", 20)
            TEXT = FONT.render(str(math.floor(fpsClock.get_fps())), False, (0, 0, 0))
            screen.blit(TEXT, (10, 10))
        pygame.display.update()
        # print(data.getTimeTillLastLogin("s"))
        data.randomDeduction()
        fpsClock.tick(120)
