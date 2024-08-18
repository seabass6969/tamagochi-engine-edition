import pygame
import ScreenState
from components.displays.text.TutorialText import TutorialText
from pygame.locals import *

footerText = "(Skip this by pressing space)"
tutorial_text = [
    [
        "You have a pet of a engine unit.",
        "You have to keep it alive in different ways",
        "Click on the (Infomation) Icon",
    ],
    [
        "You have to feed it with:",
        "Oil, power (battery)",
        "You can buy them in the marketplace",
    ],
    [
        "Also the engine might malfunction",
        "such as missing gears,",
        "fuel filters and spark plugs",
        "You can buy them in the marketplace",
    ],
    ["You have to repair them in the Garage"],
    [
        "You can earn money by playing mini-games",
    ],
    [
        "The level system also unlocks new mini-games",
        "to play",
    ],
    ["Have fun!"],
]


class TutorialScreen:
    def __init__(self, screen: pygame.Surface, footer_text: str, list_text: [[str]]):
        self.screen = screen
        self.footer_text = footer_text
        self.list_text = list_text
        self.generatedDict = {}
        self.tutorial_text = []
        self.introIncrement = 0

        for index, text in enumerate(self.list_text):
            adding_text = text
            adding_text.append(footerText)
            tutorialA = TutorialText(self.screen, adding_text)
            self.tutorial_text.append(tutorialA)
            introductionScreen = ScreenState.State(
                screen, "intro{}".format(index), (115, 115, 115), [], [tutorialA]
            )
            self.generatedDict["intro{}".format(index)] = introductionScreen

    def awaitSkip(self, key):
        if key == K_SPACE:
            return True
        else:
            return False
    def reachedEnds(self):
        if len(self.list_text) == (self.introIncrement + 1):
            return True
        else:
            return False