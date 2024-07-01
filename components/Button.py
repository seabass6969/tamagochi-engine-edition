import pygame
class Button:
    def __init__(self, screen: pygame.Surface ,text, x1, y1, width, height):
        self.screen = screen
        self.text = text
        self.x1 = x1
        self.width = width 
        self.y1 = y1
        self.height = height 
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), (self.x1 , self.y1, self.width , self.height))