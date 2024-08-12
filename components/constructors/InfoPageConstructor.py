import random
import pygame
from constants.asset import IMAGE
from components import Gap, Grid
from components.displays import Image, Tickorcross, ProgressBar
from components.displays.text import Text
from dataHandler import dataHandler
from constants.emotionConstant import EMOTIONAL_IMAGE


class InfoPageConstructor:
    def __init__(self, screen, data: dataHandler.Datahandler):
        self.emotion = data.getEmotion()
        self.sparkPlug = data.getSparkPlug()
        self.fuelFilter = data.getFilter()
        self.batteryLevel = data.getBatteryLevel()
        self.OilLevel = data.getOilLevel()
        self.gearMissing = data.getGearMissing()

        self.screen = screen
        self.hovered = False
        self.visible = False

        self.INFO_PAGE_PADDING = 10
        self.SCALED_ENGINE = pygame.transform.scale(IMAGE.get("ENGINE"), (100, 100))
        self.EngineImage = Image.Image(self.screen, 0, 0, self.SCALED_ENGINE)
        self.EmotionText = Text.Text(self.screen, "Emotion:", 0, 0, fontSize=29)
        self.EmotionTextHeight = self.EmotionText.height
        self.SCALED_EMTIONAL_IMAGE = pygame.transform.scale(
            random.choice(EMOTIONAL_IMAGE.get(self.emotion)),
            (self.EmotionTextHeight, self.EmotionTextHeight),
        )
        self.EmotionalImage = Image.Image(self.screen, 0, 0, self.SCALED_EMTIONAL_IMAGE)
        self.sparkPlugStatus = Text.Text(
            self.screen, "Spark Plug condition:", 0, 0, fontSize=29
        )
        self.sparkPlugStatusImage = Tickorcross.TickCross(
            self.screen,
            self.sparkPlug,
            0,
            0,
            self.EmotionTextHeight,
            self.EmotionTextHeight,
        )

        self.FilterStatus = Text.Text(
            self.screen, "Fuel Filter condition:", 0, 0, fontSize=29
        )
        self.FilterStatusImage = Tickorcross.TickCross(
            self.screen,
            self.fuelFilter,
            0,
            0,
            self.EmotionTextHeight,
            self.EmotionTextHeight,
        )

        self.GearMissingStatus = Text.Text(
            self.screen, "Gear Missing: {}".format(self.gearMissing), 0, 0, fontSize=29
        )
        self.BatteryLevelStatus = Text.Text(
            self.screen, "Battery Level:", 0, 0, fontSize=29
        )
        self.BatteryLevelProgressbar = ProgressBar.ProgressBar(
            self.screen, 0, 0, self.batteryLevel, 200, self.EmotionTextHeight
        )

        self.OilLevelStatus = Text.Text(self.screen, "Oil Level:", 0, 0, fontSize=29)
        self.OilLevelStatusProgressbar = ProgressBar.ProgressBar(
            self.screen, 0, 0, self.OilLevel, 200, self.EmotionTextHeight
        )

        self.infoPageItems = [
            self.EngineImage,
            Gap.Gap(self.screen, 0, 0, 0, 0),
            self.EmotionText,
            self.EmotionalImage,
            self.sparkPlugStatus,
            self.sparkPlugStatusImage,
            self.FilterStatus,
            self.FilterStatusImage,
            self.GearMissingStatus,
            Gap.Gap(self.screen, 0, 0, 0, 0),
            self.BatteryLevelStatus,
            self.BatteryLevelProgressbar,
            self.OilLevelStatus,
            self.OilLevelStatusProgressbar,
        ]
        Grid.Grid_adjuster(
            self.infoPageItems,
            self.INFO_PAGE_PADDING,
            100 + self.INFO_PAGE_PADDING,
            self.INFO_PAGE_PADDING,
            2,
        )

    def update(self, x, y, data: dataHandler.Datahandler):
        self.emotion = data.getEmotion()
        self.sparkPlug = data.getSparkPlug()
        self.fuelFilter = data.getFilter()
        self.batteryLevel = data.getBatteryLevel()
        self.OilLevel = data.getOilLevel()
        self.gearMissing = data.getGearMissing()

        if pygame.time.get_ticks() % 100 == 0:
            self.SCALED_EMTIONAL_IMAGE = pygame.transform.scale(
                random.choice(EMOTIONAL_IMAGE.get(self.emotion)),
                (self.EmotionTextHeight, self.EmotionTextHeight),
            )
            self.EmotionalImage = Image.Image(
                self.screen, 0, 0, self.SCALED_EMTIONAL_IMAGE
            )

            self.GearMissingStatus = Text.Text(
                self.screen,
                "Gear Missing: {}".format(self.gearMissing),
                0,
                0,
                fontSize=29,
            )
            self.sparkPlugStatusImage.YesOrNo = self.sparkPlug
            self.FilterStatusImage.YesOrNo = self.fuelFilter
            self.BatteryLevelProgressbar.progression = self.batteryLevel
            self.OilLevelStatusProgressbar.progression = self.OilLevel

            self.BatteryLevelProgressbar.optional_update()
            self.OilLevelStatusProgressbar.optional_update()

            self.infoPageItems = [
                self.EngineImage,
                Gap.Gap(self.screen, 0, 0, 0, 0),
                self.EmotionText,
                self.EmotionalImage,
                self.sparkPlugStatus,
                self.sparkPlugStatusImage,
                self.FilterStatus,
                self.FilterStatusImage,
                self.GearMissingStatus,
                Gap.Gap(self.screen, 0, 0, 0, 0),
                self.BatteryLevelStatus,
                self.BatteryLevelProgressbar,
                self.OilLevelStatus,
                self.OilLevelStatusProgressbar,
            ]
            Grid.Grid_adjuster(
                self.infoPageItems,
                self.INFO_PAGE_PADDING,
                100 + self.INFO_PAGE_PADDING,
                self.INFO_PAGE_PADDING,
                2,
            )

    def draw(self):
        for component in self.infoPageItems:
            component.draw()

    def getHovered(self) -> bool:
        return self.hovered and self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
