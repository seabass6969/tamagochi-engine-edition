import pygame


class Button:
    def __init__(self, screen: pygame.Surface, text, x1, y1, width, height):
        self.screen = screen
        self.text = text
        self.x1 = x1
        self.width = width
        self.y1 = y1
        self.height = height
        self.hovered = False
        self.visible = True

    def draw(self):
        pygame.draw.rect(
            self.screen,
            (217, 217, 217),
            (self.x1, self.y1, self.width, self.height),
            border_radius=40,
        )

    def update(self, x, y):
        if (
            x >= self.x1
            and x <= (self.x1 + self.width)
            and y >= self.y1
            and y <= (self.y1 + self.height)
        ):
            self.hovered = True
        else:
            self.hovered = False

    def getHovered(self) -> bool:
        return self.hovered

    def getVisibility(self) -> bool:
        return self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
