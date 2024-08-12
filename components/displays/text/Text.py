import pygame


class Text:
    def __init__(
        self,
        screen: pygame.Surface,
        text: str,
        x: float,
        y: float,
        color=(0, 0, 0),
        fontSize=30,
    ):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.visible = False

        self.FONT = pygame.font.SysFont("Comic Sans MS", fontSize)
        self.TEXT = self.FONT.render(self.text, False, color)
        self.TEXTRECT = self.TEXT.get_rect()
        self.width = self.TEXTRECT.width
        self.height = self.TEXTRECT.height

    def verticallyCentered(self):
        self.x = self.screen.get_width() / 2 - self.TEXTRECT.width / 2

    def draw(self):
        self.screen.blit(self.TEXT, (self.x, self.y))

    def update(self, x, y, data):
        pass

    def setXY(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def getVisibility(self) -> bool:
        return self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
