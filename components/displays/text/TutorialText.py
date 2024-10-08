import pygame
from pygame.locals import *


def multiplication(a: float | int, b: float | int) -> float | int:
    return a * b


class TutorialText:
    def __init__(self, screen: pygame.Surface, text: [str]):
        self.SKIPBUTTON = K_SPACE
        self.screen = screen
        self.WIDTH = screen.get_width() 
        self.HEIGHT = screen.get_height()
        self.text = text

        self.visible = False
        self.FONT = pygame.font.SysFont("Comic Sans MS", 30)
        self.text = []
        for i in text:
            self.text.append(self.FONT.render(i, False, (0, 0, 0)))
        self.TEXTRECT = self.text[0].get_rect()

    def draw(self):
        # draw a speech bubble
        pygame.draw.rect(
            self.screen,
            (217, 217, 217),
            (10, self.HEIGHT / 2 - 10, self.WIDTH - 80, self.HEIGHT / 2 - 80),
            border_radius=40,
        )
        pygame.draw.circle(
            self.screen, (217, 217, 217), (self.WIDTH - 10, self.HEIGHT - 10), 10
        )
        pygame.draw.circle(
            self.screen, (217, 217, 217), (self.WIDTH - 33, self.HEIGHT - 33), 20
        )
        pygame.draw.circle(
            self.screen, (217, 217, 217), (self.WIDTH - 70, self.HEIGHT - 70), 30
        )

        for index, i in enumerate(self.text):
            self.screen.blit(
                i,
                (
                    10 + 45,
                    self.HEIGHT / 2
                    - 10
                    + 45
                    + multiplication(self.TEXTRECT.height, index),
                ),
            )

    def update(self, mouseX, mouseY, data):
        pass

    def getVisibility(self) -> bool:
        return self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False

    def awaitSkip(self, keypress) -> bool:
        if keypress == self.SKIPBUTTON:
            return True
        else:
            return False
