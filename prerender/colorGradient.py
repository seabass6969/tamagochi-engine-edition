import os
import pygame
import uuid
from constants.asset import IMAGE_ERROR 
from prerender.preRenderErase import newCacheReporting


class GradientColorBackground:
    def __init__(self, screen: pygame.Surface, colors: [tuple]):
        self.screen = screen
        self.colors = colors
        self.length = len(colors)
        self.UNIQUE_ID = uuid.uuid1()

        self.colour_rect = pygame.Surface((2,self.length))
        self.image = IMAGE_ERROR
        self.screen_rect = self.screen.get_rect()
        
    def preRender(self):
        for index, color in enumerate(self.colors):
            pygame.draw.line(self.colour_rect, color, (index, 0), (index, 1))
        self.colour_rect = pygame.transform.smoothscale(
            self.colour_rect, (self.screen_rect.width, self.screen_rect.height)
        )  # stretch!

        pygame.image.save(
            self.colour_rect, os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID))
        )

        newCacheReporting(os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID)))
        self.image = pygame.image.load(os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID)))

    def draw(self):
        self.screen.blit(self.image, self.screen.get_rect())
        
