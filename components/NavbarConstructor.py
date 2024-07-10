import pygame
from asset import IMAGE
from components import Text, Image, Gap, LevelDisplay, Grid, Navbar
import Level
from dataHandler import dataHandler


def numberAdjuster(number: int, degits: int) -> str:
    num = str(number)
    return (degits - len(num)) * "0" + num


class NavbarConstructor:
    def __init__(self, screen, health, gotchiPoint, level):
        self.screen = screen
        self.health = health
        self.gotchiPoint = gotchiPoint
        self.level = level

        self.nav = Navbar.Navbar(
            self.screen, self.screen.get_width(), self.screen.get_height()
        )
        self.healthText = Text.Text(
            screen,
            ": {} / 10 ".format(numberAdjuster(self.health, 2)),
            0,
            0,
            fontSize=26,
        )
        self.healthtextHeight = self.healthText.TEXTRECT.height
        self.healthImageScaled = pygame.transform.scale(
            IMAGE.get("HEART"), (self.healthtextHeight, self.healthtextHeight)
        )
        self.healthImage = Image.Image(self.screen, 10, 10, self.healthImageScaled)
        self.cashImageScaled = pygame.transform.scale(
            IMAGE.get("CASH"), (self.healthtextHeight, self.healthtextHeight)
        )
        self.cashImage = Image.Image(self.screen, 0, 0, self.cashImageScaled)
        self.cashText = Text.Text(
            self.screen, ": {}".format(self.gotchiPoint), 0, 0, fontSize=26
        )
        self.leveldisplay = LevelDisplay.LevelDisplay(
            self.screen,
            10,
            10,
            self.level.getLevel(),
            self.level.getProgression(),
            150,
            self.healthtextHeight,
        )
        self.navbarItem = [
            self.healthImage,
            self.healthText,
            self.cashImage,
            self.cashText,
            Gap.Gap(self.screen, 0, 0, 20, 10),
            self.leveldisplay,
        ]
        self.combined_width = 0
        for i in self.navbarItem:
            self.combined_width += i.width
        Grid.Grid_adjuster(
            self.navbarItem,
            self.screen.get_width() / 2
            - (self.combined_width + 8 * len(self.navbarItem)) / 2,
            30,
            8,
            999999,
        )
        self.components = [self.leveldisplay]

    def draw(self):
        self.nav.draw()
        for item in self.navbarItem:
            item.draw()

    def update(self, x, y, data: dataHandler.Datahandler):
        self.health = data.getHealth()
        self.gotchiPoint = data.getGotchiPoint()
        self.level = data.getLevel()

        self.healthText = Text.Text(
            self.screen,
            ": {} / 10 ".format(numberAdjuster(self.health, 2)),
            0,
            0,
            fontSize=26,
        )
        self.healthtextHeight = self.healthText.TEXTRECT.height
        self.healthImageScaled = pygame.transform.scale(
            IMAGE.get("HEART"), (self.healthtextHeight, self.healthtextHeight)
        )
        self.healthImage = Image.Image(self.screen, 10, 10, self.healthImageScaled)
        self.cashImageScaled = pygame.transform.scale(
            IMAGE.get("CASH"), (self.healthtextHeight, self.healthtextHeight)
        )
        self.cashImage = Image.Image(self.screen, 0, 0, self.cashImageScaled)
        self.cashText = Text.Text(
            self.screen, ": {}".format(self.gotchiPoint), 0, 0, fontSize=26
        )
        self.leveldisplay = LevelDisplay.LevelDisplay(
            self.screen,
            10,
            10,
            self.level.getLevel(),
            self.level.getProgression(),
            150,
            self.healthtextHeight,
        )

        self.navbarItem = [
            self.healthImage,
            self.healthText,
            self.cashImage,
            self.cashText,
            Gap.Gap(self.screen, 0, 0, 20, 10),
            self.leveldisplay,
        ]
        self.combined_width = 0
        for i in self.navbarItem:
            self.combined_width += i.width
        Grid.Grid_adjuster(
            self.navbarItem,
            self.screen.get_width() / 2
            - (self.combined_width + 8 * len(self.navbarItem)) / 2,
            30,
            8,
            999999,
        )