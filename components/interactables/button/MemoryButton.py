import random
import pygame
from constants.asset import IMAGE, IMAGE_MEMORY


class MemoryButton:
    def __init__(
        self,
        screen,
        image,
        x1,
        y1,
        flipSide,
        background_color=(217, 217, 217),
    ):
        self.ID = random.randrange(1, 100000)
        self.TEMP_HOVER_REDUCTION_LIMIT = 10
        self.flipSide = flipSide
        self.flip_limiter = 0
        self.screen = screen
        self.x1 = x1
        self.width = 100 * 1.3
        self.y1 = y1
        self.height = 130 * 1.3
        self.hovered = False
        self.visible = False
        self.background_color = background_color
        self.imageID = image
        self.IMAGE = pygame.transform.scale(
            IMAGE_MEMORY[self.imageID], (self.width, self.height)
        )
        self.changing_image = self.IMAGE
        self.IMAGE_BACK = pygame.transform.scale(
            IMAGE_MEMORY[0], (self.width, self.height)
        )
        self.changing_image_back = self.IMAGE_BACK
        self.switching_motion = False
        self.true_flip_limiter = self.width

        self.peakCount = 0
        self.PEAK_TIMER_LIMIT = 120
        self.peakTimer = self.PEAK_TIMER_LIMIT
        self.user_linked = False

        self.fliped_times = 0

    def setXY(self, x1: int | float, y1: int | float):
        self.x1 = x1
        self.y1 = y1

    def draw(self):
        if self.user_linked:
            pygame.draw.rect(
                self.screen,
                (85, 235, 52),
                (self.x1 - 3, self.y1 - 3, self.width + 6, self.height + 6),
                border_radius=20,
            )
            self.screen.blit(
                self.changing_image,
                (self.x1 , self.y1),
            )
        else:
            if self.switching_motion == False:
                if self.flipSide == "front":
                    self.screen.blit(
                        self.changing_image,
                        (self.x1 + self.flip_limiter / 2 - self.flip_limiter / 5, self.y1),
                    )
                elif self.flipSide == "back":
                    self.screen.blit(
                        self.changing_image_back,
                        (self.x1 + self.flip_limiter / 2 - self.flip_limiter / 5, self.y1),
                    )
            else:
                if self.flipSide == "front":
                    self.screen.blit(
                        self.changing_image,
                        (self.x1 + (self.width - self.true_flip_limiter) / 2 + 1, self.y1),
                    )
                elif self.flipSide == "back":
                    self.screen.blit(
                        self.changing_image_back,
                        (self.x1 + (self.width - self.true_flip_limiter) / 2 + 1, self.y1),
                    )

    def update(self, x, y, data, peakCount: int, peaking: []):
        self.peakCount = peakCount
        if self.flipSide == "front" and self.user_linked == False and peakCount <= 2:
            self.peakTimer -= 1
        if peakCount == 2:
            if self.imageID in peaking and peaking[0] == peaking[1]:
                self.user_linked = True
        if self.peakTimer <= 0 and self.user_linked == False:
            self.peakTimer = self.PEAK_TIMER_LIMIT
            self.switching_motion = True
        if (
            x >= self.x1
            and x <= (self.x1 + self.width)
            and y >= self.y1
            and y <= (self.y1 + self.height)
            and self.user_linked == False
        ):
            self.hovered = True
        else:
            self.hovered = False

        if self.switching_motion == False:
            if self.flipSide == "front":
                if self.hovered and self.flip_limiter < self.TEMP_HOVER_REDUCTION_LIMIT:
                    self.flip_limiter += 1
                elif not self.hovered and self.flip_limiter > 0:
                    self.flip_limiter -= 1
            elif self.flipSide == "back":
                if self.hovered and self.flip_limiter < self.TEMP_HOVER_REDUCTION_LIMIT:
                    self.flip_limiter += 1
                elif not self.hovered and self.flip_limiter > 0:
                    self.flip_limiter -= 1
            if self.flipSide == "back":
                self.changing_image_back = pygame.transform.scale(
                    self.IMAGE_BACK, (self.width - self.flip_limiter, self.height)
                )
            elif self.flipSide == "front":
                self.changing_image = pygame.transform.scale(
                    self.IMAGE, (self.width - self.flip_limiter, self.height)
                )
        else:
            if self.true_flip_limiter > 4:
                self.true_flip_limiter -= 4
            else:
                self.true_flip_limiter = self.width
                self.switching_motion = False
                self.swapSide()
            if self.flipSide == "back":
                self.changing_image_back = pygame.transform.scale(
                    self.IMAGE_BACK, (self.true_flip_limiter, self.height)
                )
            elif self.flipSide == "front":
                self.changing_image = pygame.transform.scale(
                    self.IMAGE, (self.true_flip_limiter, self.height)
                )

    def getHovered(self) -> bool:
        return self.hovered and self.visible

    def setVisibility(self, vis: bool):
        self.visible = vis

    def toggleVisibility(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False

    def click(self):
        if self.getHovered() and self.peakCount < 2:
            self.switching_motion = True
            self.fliped_times += 1

    def swapSide(self):
        if self.flipSide == "front":
            self.flipSide = "back"
        elif self.flipSide == "back":
            self.flipSide = "front"

    def userLinkedUp(self):
        self.user_linked = True
