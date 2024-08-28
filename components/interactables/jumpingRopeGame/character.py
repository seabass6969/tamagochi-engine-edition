import pygame
from constants.asset import IMAGE 
from dataHandler import dataHandler


class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.y= y
        self.x = x
        self.engine_image = IMAGE.get("ENGINE")
        
        self.engine_image= pygame.transform.scale(self.engine_image, (80, 80))
        self.engine_rect = self.engine_image.get_rect()
        self.engine_rect.topleft = (self.x, self.y)
        self.engine_mask = pygame.mask.from_surface(self.engine_image)
        self.overlap = False
        self.keys = []

    def draw(self):
        self.screen.blit(self.engine_image, self.engine_rect)

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        if down == True :
            self.keys.append(key)
        else:
            self.keys.remove(key)
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        if pygame.locals.K_w in self.keys:
            self.x += 1
        if pygame.locals.K_s in self.keys:
            self.x -= 1
        if pygame.locals.K_SPACE in self.keys:
            self.y -= 1
        self.engine_rect.topleft = (self.x, self.y)

        self.engine_mask = pygame.mask.from_surface(self.engine_image)
        pass