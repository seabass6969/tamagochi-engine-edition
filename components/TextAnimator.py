import pygame
import math
from components import Text
class TextAnimator(Text.Text):
    def __init__(
        self,
        screen: pygame.Surface,
        x_original: float,
        y_original: float
    ):
        self.memetext = "engine drinks oil"
        super().__init__(screen, self.memetext, x_original, y_original, (255, 215, 0), 18)
        self.TEXT = pygame.transform.rotate(self.TEXT, -45)
        self.TEXTRECT = self.TEXT.get_rect()
        self.MAX_MODIFIER = 1.9
        self.modifier = 1
        self.enlarge = True
        self.x_original = x_original
        self.y_original = y_original
        
    def draw(self):
        if self.modifier >= self.MAX_MODIFIER:
            self.enlarge = False
        if self.modifier <= 1:
            self.enlarge = True
        if self.enlarge == False:
            self.modifier -= 0.02
        else:
            self.modifier += 0.02
        enlarging = pygame.transform.scale_by(self.TEXT, self.modifier)
        enlarging_rect = enlarging.get_rect()

        self.x = self.x_original - enlarging_rect.width / 2
        self.y = self.y_original - enlarging_rect.height / 2
        self.screen.blit(enlarging, (self.x, self.y))
