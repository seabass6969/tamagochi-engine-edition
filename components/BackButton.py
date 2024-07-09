import pygame
from components.Button import Button
from asset import IMAGE


class BackButton(Button):
    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, "", x, y, 40, 40)
        self.BACKIMAGE = IMAGE.get("BACK")
        self.BACKIMAGE = pygame.transform.scale(self.BACKIMAGE, (40, 40))
        self.BACKIMAGERECT = self.BACKIMAGE.get_rect()

    def draw(self):
        super().draw()
        self.screen.blit(self.BACKIMAGE, (self.x1, self.y1))
