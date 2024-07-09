import pygame


class Gap:
    def __init__(self, screen, x1, y1, width, height, discoverable=False):
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.discoverable = discoverable
        self.visible = False

    def draw(self):
        if self.discoverable:
            pygame.draw.rect(
                self.screen, (0, 0, 0), (self.x1, self.y1, self.width, self.height)
            )

    def setXY(self, x1: int | float, y1: int | float):
        self.x1 = x1
        self.y1 = y1

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
