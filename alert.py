import pygame
from pygame.locals import *


def Alert(
    screen: pygame.Surface, currentScreen, logoImage: pygame.image, title, message
):
    
    pygame.mouse.set_cursor(pygame.cursors.arrow)
    global transition
    transition = True
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    backdrop = pygame.Surface((WIDTH, HEIGHT))
    alpha = 0
    backdrop.set_alpha(alpha)
    backdrop.fill((100, 100, 100))
    logoImage = pygame.transform.scale(logoImage, (50, 50))
    logoImageRect = logoImage.get_rect()
    FONT = pygame.font.SysFont("Comic Sans MS", 20)
    TITLE_TEXT = FONT.render(title, False, (0, 0, 0))
    TITLE_TEXTRECT = TITLE_TEXT.get_rect()
    MESSAGE_TEXT = FONT.render(message, False, (0, 0, 0))
    MESSAGE_TEXTRECT = MESSAGE_TEXT.get_rect()
    while transition == True:
        currentScreen()
        screen.blit(backdrop, (0, 0))
        pygame.draw.rect(
            screen,
            (230, 230, 230),
            (WIDTH / 2 - 500 / 2, HEIGHT / 2 - 300 / 2, 500, 300),
            border_radius=40,
        )
        screen.blit(logoImage, (WIDTH / 2 - 500 / 2 + 50, HEIGHT / 2 - 300 / 2 + 50))
        screen.blit(
            TITLE_TEXT,
            (
                WIDTH / 2 - 500 / 2 + 50 + logoImageRect.width,
                HEIGHT / 2
                - 300 / 2
                + 50
                + logoImageRect.height / 2
                - TITLE_TEXTRECT.height / 2,
            ),
        )
        screen.blit(
            MESSAGE_TEXT,
            (
                WIDTH / 2 - 500 / 2 + 50,
                HEIGHT / 2 - 300 / 2 + 50 + logoImageRect.height + 10,
            ),
        )
        for event in pygame.event.get():
            if event.type == QUIT:
                transition = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    transition = False
        if alpha < 180:
            alpha += 1
            backdrop.set_alpha(alpha)
        pygame.display.update()
    transition = False
