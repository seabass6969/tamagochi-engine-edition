import pygame


class Navbar:
    def __init__(self, screen: pygame.Surface, WIDTH, HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.height = 100
        

    def draw(self):
        
        pygame.draw.rect(
            self.screen,
            (217, 217, 217),
            (0, 0, self.WIDTH, 100),
            border_bottom_left_radius=20,
            border_bottom_right_radius=20,
        )
        

    def update(self, x, y, data):
        pass
    
    def getVisibility(self) -> bool:
        return self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
