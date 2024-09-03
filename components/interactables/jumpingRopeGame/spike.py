import pygame
from dataHandler import dataHandler
from constants.asset import IMAGE_ROPE_GAME


class Spike:
    def __init__(self, screen: pygame.Surface, x, y, width):
        self.screen = screen
        self.y= y
        self.x = x
        self.width = width
        # self.platform_rect.topleft = (self.x, self.y)
        self.spike_image = pygame.Surface((self.width, 40))
        self.spike_image.set_colorkey(pygame.color.Color(0,0,0,0))
        self.spike_image.blit(pygame.transform.scale_by(IMAGE_ROPE_GAME.get("SPIKE"), 5), (0,0))
        # 7 per block width 20 per block height
        self.spike_mask = pygame.mask.from_surface(self.spike_image)
        
        self.overlap = False

    def draw(self):
        self.screen.blit(self.spike_image,(self.x,self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass