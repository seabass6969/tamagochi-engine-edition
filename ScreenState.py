import pygame


class State:

    def __init__(
        self, screen: pygame.Surface, background_color: pygame.Color, components: []
    ):
        self.screen = screen
        self.background_color = background_color
        self.components = components

    def draw(self):
        self.screen.fill((115, 115, 115))
        for component in self.components:
            component.draw()

    def update(self, x: int, y: int):
        for component in self.components:
            component.update(x, y)
