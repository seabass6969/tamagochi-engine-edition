import pygame
from components import Button
import math


class LogoButton(Button.Button):
    def __init__(self, screen: pygame.Surface, image: pygame.image, text: str, x1, y1, disabled: bool = False):
        super().__init__(screen, "", x1, y1, 150, 150)
        self.image = image
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.imagerect = self.image.get_rect()
        self.FONT = pygame.font.SysFont("Comic Sans MS", 20)
        self.TEXT = self.FONT.render(text, False, (0, 0, 0))
        self.TEXTRECT = self.TEXT.get_rect()

        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()
        self.disabled = disabled

    def draw(self):
        if self.getHovered() and not self.disabled:
            pygame.draw.rect(
                self.screen,
                (0,0,0),
                (self.x1 - 2, self.y1 - 2, self.width + 4, self.height + 4),
                border_radius=10,
            )
        pygame.draw.rect(
            self.screen,
            (217, 217, 217),
            (self.x1, self.y1, self.width, self.height),
            border_radius=10,
        )
        self.screen.blit(
            self.image, (self.x1 + self.width / 2 - self.imagerect.width / 2, self.y1)
        )
        self.screen.blit(
            self.TEXT,
            (
                self.x1 + self.width / 2 - self.TEXTRECT.width / 2,
                self.y1 + self.imagerect.height,
            ),
        )

        if self.disabled:
            for i in range(0, math.floor(self.width), 8):
                pygame.draw.line(self.screen, (0,0,0), (self.x1 + i, self.y1), (self.x1, self.y1 + i))
