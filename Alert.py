import pygame
from pygame.locals import *
from components import Button, Text
import math


def Alert(
    screen: pygame.Surface,
    currentScreen,
    logoImage: pygame.image,
    title: str,
    message: str,
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
    title = Text.Text(
        screen,
        title,
        WIDTH / 2 - 500 / 2 + 20 + logoImageRect.width + 5,
        HEIGHT / 2 - 300 / 2 + 20 + logoImageRect.height / 2,
        fontSize=25,
    )
    title.y = (
        HEIGHT / 2 - 300 / 2 + 20 + logoImageRect.height / 2 - title.TEXTRECT.height / 2
    )
    message_text = Text.Text(
        screen,
        message,
        WIDTH / 2 - 500 / 2 + 20,
        HEIGHT / 2 - 300 / 2 + 20 + logoImageRect.height + 10,
        fontSize=20,
    )

    ok_button = Button.Button(
        screen,
        "OK",
        WIDTH / 2 - 100 / 2,
        HEIGHT / 2
        - 300 / 2
        + 20
        + logoImageRect.height
        + message_text.TEXTRECT.height
        + 20,
        100,
        100,
        background_color=(117, 251, 76),
    )
    sinCurveShake = 0
    sinCurveModifier = 0
    title_original_x = title.x
    message_original_x = message_text.x
    ok_button_original_x = ok_button.x1
    components = [title,message_text,ok_button]
    for component in components:
        component.setVisibility(True)
    while transition == True:
        currentScreen.draw()
        screen.blit(backdrop, (0, 0))
        pygame.draw.rect(
            screen,
            (230, 230, 230),
            (WIDTH / 2 - 500 / 2 + sinCurveModifier, HEIGHT / 2 - 300 / 2, 500, 300),
            border_radius=40,
        )
        screen.blit(logoImage, (WIDTH / 2 - 500 / 2 + 20 + sinCurveModifier, HEIGHT / 2 - 300 / 2 + 20))
        title.x = title_original_x + sinCurveModifier
        message_text.x = message_original_x+ sinCurveModifier
        ok_button.x1 = ok_button_original_x + sinCurveModifier
        title.draw()
        message_text.draw()
        ok_button.draw()
        mouseX, mouseY = pygame.mouse.get_pos()
        ok_button.update(mouseX, mouseY, data="")
        for event in pygame.event.get():
            if event.type == QUIT:
                transition = False
            if event.type == MOUSEBUTTONDOWN:
                if ok_button.getHovered():
                    transition = False
        if alpha < 180:
            alpha += 5
            backdrop.set_alpha(alpha)
        if sinCurveShake < 1800:
            sinCurveShake += 20
            sinCurveModifier = math.sin(sinCurveShake) * 30
        pygame.display.update()

