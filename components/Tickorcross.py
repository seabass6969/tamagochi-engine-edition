import pygame
from asset import IMAGE
from components import Image
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
        if YesOrNo == True:
            self.image = self.SCALED_CHECKMARK
        else:
            self.image = self.SCALED_CROSS