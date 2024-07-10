import pygame
from dataHandler import dataHandler


class Image:
    def __init__(self, screen: pygame.Surface, x1, y1, image):
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.image = image
        self.IMAGERECT = self.image.get_rect()

        self.visible = False
        self.width = self.IMAGERECT.width
        self.height = self.IMAGERECT.height

    def draw(self):
        self.screen.blit(self.image, (self.x1, self.y1))

    def update(self, x, y, data: dataHandler.Datahandler):
        pass

    def setXY(self, x1: int | float, y1: int | float):
        self.x1 = x1
        self.y1 = y1

    def getVisibility(self) -> bool:
        return self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
