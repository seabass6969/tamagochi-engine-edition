import pygame
from components.Button import Button
from asset import IMAGE


class StartButton(Button):
    def __init__(self, screen: pygame.Surface, WIDTH, HEIGHT):
        super().__init__(screen, "START", WIDTH / 2 - 300 / 2, HEIGHT / 2 - 80 / 2, 300, 80)
        self.ENGINEIMAGE = IMAGE.get("ENGINE")
        self.ENGINEIMAGE = pygame.transform.scale(self.ENGINEIMAGE, (80, 80))
        self.ENGINEIMAGERECT = self.ENGINEIMAGE.get_rect()

    def draw(self):
        super().draw()
        self.screen.blit(
            self.ENGINEIMAGE,
            (self.ENGINEIMAGERECT.x + self.x1, self.ENGINEIMAGERECT.y + self.y1),
        )
        self.screen.blit(
            self.ENGINEIMAGE,
            (
                self.WIDTH / 2 + 300 / 2 - self.ENGINEIMAGERECT.width,
                self.ENGINEIMAGERECT.y + self.y1,
            ),
        )
        
        pygame.display.flip()
