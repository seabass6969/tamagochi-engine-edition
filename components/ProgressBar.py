import pygame, math
from components.Text import Text
from dataHandler import dataHandler
from numberAdjuster import numberAdjuster


class ProgressBar(Text):
    def __init__(
        self,
        screen: pygame.Surface,
        x1: int,
        y1: int,
        progression: float,
        width: int,
        height: int,
    ):
        super().__init__(screen, "{}%".format(numberAdjuster(progression * 100, 3)), x1, y1, fontSize=20)
        self.x_text = 0
        self.y_text = 0
        self.width = width
        self.height = height
        self.progression = progression
        self.updated = True
        self.hovered = False

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
        if self.progression == 1:
            pygame.draw.rect(
                self.screen,
                (177, 206, 250),
                (
                    self.x,
                    self.y,
                    self.width * self.progression,
                    self.height,
                ),
                border_radius=40,
            )
        else:
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
        self.x_text = self.x + (self.width/ 2) - (self.TEXTRECT.width / 2)
        self.y_text = self.y + self.height / 2 - self.TEXTRECT.height/ 2
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

    def getHovered(self) -> bool:
        return self.hovered and self.visible
