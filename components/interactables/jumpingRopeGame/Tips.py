import pygame
from components.displays.text.Text import Text
from components.displays.text.Keys import Keys
from components.Grid import Grid_adjuster


class Tips:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.WIDTH = self.screen.get_width()
        self.height = 100
        self.TEXT_W = Keys(self.screen, "w", 0, 0)
        self.TEXT_Forward = Text(self.screen, "Forward", 0, 0)
        self.TEXT_S = Keys(self.screen, "s", 0, 0)
        self.TEXT_Backward = Text(self.screen, "Backward", 0, 0)
        self.TEXT_SPACE = Keys(self.screen, "", 0, 0)
        self.TEXT_JUMP = Text(self.screen, "Jump", 0, 0)
        self.TEXT_GOAL = Text(self.screen, "Goal: reached the green pad", 0, 0)
        self.items = [
            self.TEXT_W,
            self.TEXT_Forward,
            self.TEXT_S,
            self.TEXT_Backward,
            self.TEXT_SPACE,
            self.TEXT_JUMP,
            self.TEXT_GOAL
        ]
        Grid_adjuster(self.items, 50, 10, 5, len(self.items) - 1)

    def draw(self):
        for item in self.items:
            item.draw()
        # 60 high box

    def update(self, x, y, data):
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
