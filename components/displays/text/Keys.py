import pygame
from components.displays.text.Text import Text


class Keys(Text):
    def __init__(
        self,
        screen: pygame.Surface,
        keys: str,
        x: float,
        y: float,
        color=(0, 0, 0),
    ):
        super().__init__(screen, keys, x, y, fontSize=15)
        self.width = 20
        self.height = 20

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 20,20), 2)
        self.screen.blit(self.TEXT, (self.x + self.height / 2 - self.TEXT.get_width() / 2, self.y + self.height / 2- self.TEXT.get_height() / 2))
