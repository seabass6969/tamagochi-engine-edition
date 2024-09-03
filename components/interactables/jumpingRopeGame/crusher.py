import pygame
from constants.asset import IMAGE_ROPE_GAME
from dataHandler import dataHandler


class Crusher:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.y = y
        self.x = x
        self.crushing_height = 1
        self.crushing_direction = "down"

        self.crushing_image = pygame.Surface((50, 50))
        self.crushing_image.set_colorkey((0,0,0,0))
        self.crushing_mask = pygame.mask.from_surface(self.crushing_image)
        # self.platform_rect.topleft = (self.x, self.y)
        self.overlap = False

    def draw(self):
        self.screen.blit(self.crushing_image, (self.x, self.y))

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        
        if self.crushing_height >= 50:
            self.crushing_direction = "up"
        elif self.crushing_height <= 0:
            self.crushing_direction = "down"
            
        if self.crushing_direction == "down":
            self.crushing_height += 0.1
        else:
            self.crushing_height -= 0.1
        self.crushing_image.fill((0,0,0))
        pygame.draw.rect(self.crushing_image, (235, 64, 52) , (0,0, 50, self.crushing_height))
        self.crushing_mask = pygame.mask.from_surface(self.crushing_image)
        pass
