import pygame


class Button:
    def __init__(
        self,
        screen: pygame.Surface,
        text,
        x1,
        y1,
        width,
        height,
        background_color=(217, 217, 217),
    ):
        self.screen = screen
        self.text = text
        self.x1 = x1
        self.width = width
        self.y1 = y1
        self.height = height
        self.hovered = False
        self.visible = False

        self.FONT = pygame.font.SysFont("Comic Sans MS", 30)
        self.TEXT = self.FONT.render(text, False, (0, 0, 0))
        self.TEXTRECT = self.TEXT.get_rect()

        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()
        self.background_color = background_color

    def setXY(self, x1: int | float, y1: int | float):
        self.x1 = x1
        self.y1 = y1

    def draw(self):
        if self.getHovered():
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (self.x1 - 2, self.y1 - 2, self.width + 4, self.height + 4),
                border_radius=40,
            )
        pygame.draw.rect(
            self.screen,
            self.background_color,
            (self.x1, self.y1, self.width, self.height),
            border_radius=40,
        )

        if self.text != "":
            self.screen.blit(
                self.TEXT,
                (
                    self.x1 + self.width / 2 - self.TEXTRECT.width / 2,
                    self.y1 + self.height / 2 - self.TEXTRECT.height / 2,
                ),
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
        return self.hovered and self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
