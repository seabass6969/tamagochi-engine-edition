import pygame
from dataHandler import dataHandler


class MemoryGameConstructor:
    def __init__(self, screen, data: dataHandler.Datahandler):
        self.memoryGameItems = []
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass

    def draw(self):
        for component in self.memoryGameItems:
            component.draw()

    def getHovered(self) -> bool:
        return self.hovered and self.visible

    def setVisibility(self, vis: bool):
        for component in self.memoryGameItems:
            component.setVisibility(vis)
