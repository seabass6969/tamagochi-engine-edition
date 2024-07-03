import pygame
from components.Button import Button
class StartButton(Button):
    def __init__(self, screen:pygame.Surface, WIDTH, HEIGHT, ENGINEIMAGE):
        super().__init__(screen, "", WIDTH / 2 - 300 / 2,HEIGHT / 2 - 80 / 2, 300,80)
        self.ENGINEIMAGE = ENGINEIMAGE
        self.ENGINEIMAGE = pygame.transform.scale(self.ENGINEIMAGE, (80,80))
        self.ENGINEIMAGERECT = self.ENGINEIMAGE.get_rect()
        self.FONT = pygame.font.SysFont('Comic Sans MS', 30)
        self.TEXT = self.FONT.render("START", False, (0,0,0))
        self.TEXTRECT = self.TEXT.get_rect()
    def draw(self):
        super().draw()
        self.screen.blit(self.ENGINEIMAGE, (self.ENGINEIMAGERECT.x + self.x1, self.ENGINEIMAGERECT.y + self.y1))
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        self.screen.blit(self.TEXT, (WIDTH / 2 - self.TEXTRECT.width / 2, HEIGHT / 2 - self.TEXTRECT.height/ 2))
        self.screen.blit(self.ENGINEIMAGE, (WIDTH / 2 + 300 / 2 - self.ENGINEIMAGERECT.width, self.ENGINEIMAGERECT.y + self.y1))
        pygame.display.flip()