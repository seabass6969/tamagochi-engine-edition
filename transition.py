import pygame
import math


def slideLeftToRight(screen: pygame.Surface, clock: pygame.time.Clock, nextDisplay):
    for i in range(math.floor(screen.get_width() / 6)):
        # x y width height
        pygame.draw.rect(screen, (255,163,165), (0, 0, i * 3, screen.get_height()))
        pygame.draw.rect(screen, (255,163,165), (screen.get_width() - (i * 3), 0 , i * 3, screen.get_height()))
        pygame.display.flip()
        clock.tick(1000)

    for i in range(math.floor(screen.get_width() / 12), 0, -1):
        # x y width height
        nextDisplay()
        pygame.draw.rect(screen, (255,163,165), (0, 0, i * 6, screen.get_height()))
        pygame.draw.rect(screen, (255,163,165), (screen.get_width() - (i * 6), 0 , i * 6, screen.get_height()))
        pygame.display.flip()
        clock.tick(1000)

