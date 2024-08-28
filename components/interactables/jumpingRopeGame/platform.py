import pygame
from constants.asset import IMAGE_ROPE_GAME
from dataHandler import dataHandler


class Platform:
    def __init__(self, screen: pygame.Surface, x, y, width):
        self.screen = screen
        self.y= y
        self.x = x
        self.width = width
        
        self.platform_image = pygame.Surface((self.width, 50))
        self.platform_image.blit(pygame.transform.scale_by(IMAGE_ROPE_GAME.get("PLATFORM"), 10), (0,0))
        self.platform_mask = pygame.mask.from_surface(self.platform_image)
        self.platform_rect = (0,0, self.width, 50)
        # self.platform_rect.topleft = (self.x, self.y)
        self.overlap = False

    def draw(self):
        self.screen.blit(self.platform_image,(self.x,self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass