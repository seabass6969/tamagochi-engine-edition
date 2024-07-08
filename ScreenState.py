import pygame


class State:

    def __init__(
        self, screen: pygame.Surface, background_color: pygame.Color, components_button: [], components_text: []
    ):
        self.screen = screen
        self.background_color = background_color
        self.components = []
        self.components.extend(components_text)
        self.components.extend(components_button)
        self.components_text = components_text
        self.components_button = components_button

    def draw(self):
        self.screen.fill((115, 115, 115))
        for component in self.components:
            component.draw()

    def update(self, x: int, y: int):
        hovered_list = []
        for component in self.components_button:
            component.update(x, y)
            hovered_list.append(component.getHovered())
        if True in hovered_list:
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)