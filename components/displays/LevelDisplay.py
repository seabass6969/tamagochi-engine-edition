import pygame, math
from components.displays.text.Text import Text
from dataHandler import dataHandler


class LevelDisplay(Text):
    def __init__(
        self,
        screen: pygame.Surface,
        x1: int,
        y1: int,
        level: int,
        progression: float,
        width: int,
        height: int,
    ):
        # super().__init__(screen, , x1, y1, fontSize=20)

        self.screen = screen
        self.text = "lvl: {}".format(str(level))
        self.x = x1
        self.y = y1
        self.color = (0, 0, 0)
        self.visible = False

        self.FONT = pygame.font.SysFont("Comic Sans MS", 20)
        self.TEXT = self.FONT.render(self.text, False, self.color)
        self.TEXTRECT = self.TEXT.get_rect()
        self.x_text = 0
        self.y_text = 0
        self.width = width
        self.height = height
        self.level = level
        self.progression = progression
        self.updated = True
        self.hovered = False

        self.ALTERNATIVE_TEXT = self.FONT.render(
            "{}:{}%".format(str(level), math.floor(progression * 100)), False, (0, 0, 0)
        )
        self.ALTERNATIVE_TEXTRECT = self.ALTERNATIVE_TEXT.get_rect()

    def draw(self):
        pygame.draw.rect(
            self.screen,
            (149, 255, 0),
            (
                self.x,
                self.y,
                self.width,
                self.height,
            ),
            border_radius=40,
        )
        pygame.draw.rect(
            self.screen,
            (177, 206, 250),
            (
                self.x,
                self.y,
                self.width * self.progression,
                self.height,
            ),
            border_top_left_radius=40,
            border_bottom_left_radius=40,
        )
        if self.getHovered():
            self.x_text = (
                self.x + (self.width / 2) - (self.ALTERNATIVE_TEXTRECT.width / 2)
            )
            self.y_text = (
                self.y + self.height / 2 - self.ALTERNATIVE_TEXTRECT.height / 2
            )
            self.screen.blit(self.ALTERNATIVE_TEXT, (self.x_text, self.y_text))
        else:
            self.x_text = self.x + (self.width / 2) - (self.TEXTRECT.width / 2)
            self.y_text = self.y + self.height / 2 - self.TEXTRECT.height / 2
            self.screen.blit(self.TEXT, (self.x_text, self.y_text))

    def setXY(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def update(self, x, y, data: dataHandler.Datahandler):
        if (
            x >= self.x
            and x <= (self.x + self.width)
            and y >= self.y
            and y <= (self.y + self.height)
        ):
            self.hovered = True
        else:
            self.hovered = False

        self.level = data.getLevel().getLevel()
        self.progression = data.getLevel().getProgression() / data.getLevel().getLevelProgressionMax()
        self.text = "lvl: {}".format(str(self.level))
        self.TEXT = self.FONT.render(self.text, False, self.color)
        self.TEXTRECT = self.TEXT.get_rect()

        self.ALTERNATIVE_TEXT = self.FONT.render(
            "{}:{}%".format(str(self.level), math.floor(self.progression * 100)),
            False,
            (0, 0, 0),
        )
        self.ALTERNATIVE_TEXTRECT = self.ALTERNATIVE_TEXT.get_rect()

    def getHovered(self) -> bool:
        return self.hovered and self.visible
