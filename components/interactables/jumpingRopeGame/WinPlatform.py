import pygame
from dataHandler import dataHandler


class WinPlatform:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.y = y
        self.x = x
        self.win_platform = pygame.Surface((40, 10))
        pygame.draw.rect(self.win_platform, (0, 255, 0), (0, 0, 40, 10))
        self.win_mask = pygame.mask.from_surface(self.win_platform)
        # self.platform_rect.topleft = (self.x, self.y)
        self.overlap = False

    def draw(self):
        self.screen.blit(self.win_platform, (self.x, self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass
