import pygame, random
from dataHandler import dataHandler


class RandomDrops:
    def __init__(self, screen: pygame.Surface, topLimit, bag):
        self.screen = screen
        self.x = random.randrange(10, self.screen.get_width() - 10)
        self.topLimit = topLimit
        self.bottomLimit = self.screen.get_height()
        self.y = topLimit
        self.circles_surface = pygame.Surface((40, 40))
        self.circles_surface.fill((0, 0, 0, 0))
        self.circles_surface.set_colorkey((0, 0, 0, 0))
        pygame.draw.circle(self.circles_surface, (252, 186, 3), (20, 20), 20)
        self.circles_mask = pygame.mask.from_surface(self.circles_surface)
        # self.platform_rect.topleft = (self.x, self.y)
        self.overlap = False
        self.bag = bag

    def draw(self):
        self.screen.blit(self.circles_surface, (self.x, self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        self.y += 2
        if self.y >= self.bottomLimit:
            self.x = random.randrange(10, self.screen.get_width() - 10)
            self.y = self.topLimit
        pass

    def touched_update(self):
        self.x = random.randrange(10, self.screen.get_width() - 10)
        self.y = self.topLimit
