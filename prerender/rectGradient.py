import os
import pygame
import uuid
from constants.asset import IMAGE_ERROR
from prerender.preRenderErase import newCacheReporting


class GradientRoundedCornerRectangle:
    def __init__(
        self,
        screen: pygame.Surface,
        colors: [tuple],
        size: tuple,
        border_radius: int,
        x,
        y,
    ):
        self.screen = screen
        self.colors = colors
        self.length = len(colors)
        self.UNIQUE_ID = uuid.uuid1()

        self.colour_rect = pygame.Surface((2, self.length))
        self.screen_rect = self.screen.get_rect()
        self.size = size
        self.x = x
        self.y = y
        self.border_radius = border_radius

        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)

    def preRender(self):
        for index, color in enumerate(self.colors):
            pygame.draw.line(self.colour_rect, color, (index, 0), (index, 1))
        self.colour_rect = pygame.transform.rotate(self.colour_rect, 45)
        self.colour_rect = pygame.transform.smoothscale(
            self.colour_rect, self.size
        )  # stretch!


        pygame.image.save(
            self.colour_rect,
            os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID)),
        )
        newCacheReporting(os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID)))
        self.original_image = pygame.image.load(
            os.path.join("../prerender", "{}.png".format(self.UNIQUE_ID))
        )
        pygame.draw.rect(
            self.rect_image,
            (255, 255, 255),
            (0, 0, *self.size),
            border_radius=self.border_radius,
        )
        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def draw(self):
        # self.screen.blit(self.image, self.screen.get_rect())
        self.screen.blit(self.image, (self.x, self.y))
