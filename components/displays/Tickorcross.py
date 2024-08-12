import pygame
from constants.asset import IMAGE
from components.displays import Image
class TickCross(Image.Image):
    def __init__(self, screen, YesOrNo, x, y, width, height):
        self.YesOrNo = YesOrNo
        self.width = width
        self.height = height 
        self.SCALED_CHECKMARK = pygame.transform.scale(IMAGE.get("YES"), (self.width, self.height))
        self.SCALED_CROSS = pygame.transform.scale(IMAGE.get("NO"), (self.width, self.height))
        if self.YesOrNo == True:
            super().__init__(screen, x, y, self.SCALED_CHECKMARK)
        else:
            super().__init__(screen, x, y, self.SCALED_CROSS)
        self.width = width
        self.height = height 
    def update(self,x,y, data):
        super().update(x,y, data)

    def draw(self):
        if self.YesOrNo == True:
            self.screen.blit(self.SCALED_CHECKMARK, (self.x1, self.y1))
        else:
            self.screen.blit(self.SCALED_CROSS, (self.x1, self.y1))