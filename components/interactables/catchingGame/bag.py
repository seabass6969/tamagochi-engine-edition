import pygame
from dataHandler import dataHandler


class Bag:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = 0
        self.y = self.screen.get_height() - 40
        self.bag_platform = pygame.Surface((80, 10))
        pygame.draw.rect(self.bag_platform, (65,61,62), (0, 0, 80, 10))
        self.bag_mask = pygame.mask.from_surface(self.bag_platform)
        # self.platform_rect.topleft = (self.x, self.y)
        self.overlap = False

    def draw(self):
        self.screen.blit(self.bag_platform, (self.x, self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        self.x = x - 40
        pass
