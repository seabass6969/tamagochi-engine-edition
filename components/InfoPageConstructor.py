import random
import pygame
from asset import IMAGE
from components import Gap, Grid, Image, Text
from dataHandler import dataHandler


EMOTIONAL_IMAGE = {
    "happy": [
        IMAGE.get("HAPPY1"),
        IMAGE.get("HAPPY2"),
        IMAGE.get("HAPPY3"),
    ],
    "ill": [
        IMAGE.get("ILL"),
    ],
    "mid": [
        IMAGE.get("MID"),
    ],
    "sad": [
        IMAGE.get("SAD"),
    ],
    "angry": [
        IMAGE.get("ANGRY"),
    ],
}


class InfoPageConstructor:
    def __init__(self, screen, data: dataHandler.Datahandler):
        self.emotion = data.getEmotion()
        self.screen = screen
        self.hovered = False
        self.visible = False

        self.INFO_PAGE_PADDING = 10
        self.SCALED_ENGINE = pygame.transform.scale(IMAGE.get("ENGINE"), (100, 100))
        self.EngineImage = Image.Image(self.screen, 0, 0, self.SCALED_ENGINE)
        self.EmotionText = Text.Text(self.screen, "Emotion:", 0, 0, fontSize=29)
        self.EmotionTextHeight = self.EmotionText.height
        self.SCALED_EMTIONAL_IMAGE = pygame.transform.scale(
            random.choice(EMOTIONAL_IMAGE.get(self.emotion)), (self.EmotionTextHeight, self.EmotionTextHeight)
        )
        self.EmotionalImage = Image.Image(self.screen, 0, 0, self.SCALED_EMTIONAL_IMAGE)
        self.infoPageItems = [
            self.EngineImage,
            Gap.Gap(self.screen, 0, 0, 0, 0),
            self.EmotionText,
            self.EmotionalImage,
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
        if pygame.time.get_ticks() % 100 == 0 :
            self.SCALED_EMTIONAL_IMAGE = pygame.transform.scale(
                random.choice(EMOTIONAL_IMAGE.get(self.emotion)), (self.EmotionTextHeight, self.EmotionTextHeight)
            )
            self.EmotionalImage = Image.Image(self.screen, 0, 0, self.SCALED_EMTIONAL_IMAGE)
            self.infoPageItems = [
                self.EngineImage,
                Gap.Gap(self.screen, 0, 0, 0, 0),
                self.EmotionText,
                self.EmotionalImage,
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
