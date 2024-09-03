import pygame
from dataHandler import dataHandler


class DeathPit:
    def __init__(self, screen: pygame.Surface, x, y, width = 0, height = 0):
        self.screen = screen
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        # self.platform_rect.topleft = (self.x, self.y)
        if self.width != 0:
            self.line_surface = pygame.Surface((self.width, 2))
        elif self.height != 0:
            self.line_surface = pygame.Surface((2, self.height))
            
        self.line_mask = pygame.mask.from_surface(self.line_surface)
        pygame.draw.line(
            self.line_surface, (200, 100, 100), (0, 0), (self.height, self.width), width=2
        )

        self.overlap = False

    def draw(self):
        self.screen.blit(self.line_surface, (self.x, self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass
