import pygame
import math


def slideLeftToRight(screen: pygame.Surface, clock: pygame.time.Clock, nextDisplay):
    for i in range(math.floor(screen.get_width() / 6)):
        # x y width height
        pygame.draw.rect(screen, (125, 125, 0), (0, 0, i * 6, screen.get_height()))
        pygame.display.flip()

    nextDisplay()
