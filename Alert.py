import pygame
from pygame.locals import *
from components.displays.text import Text
from components.interactables.button import Button
from components import Grid
from constants.asset import IMAGE
import math


def Alert(
    screen: pygame.Surface,
    currentScreen,
    logoImageName: str,
    title: str,
    messages: [str],
):
    fpsClock = pygame.time.Clock()

    pygame.mouse.set_cursor(pygame.cursors.arrow)
    transition = True
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    backdrop = pygame.Surface((WIDTH, HEIGHT))
    alpha = 0
    backdrop.set_alpha(alpha)
    if logoImageName == "SKULL":
        backdrop.fill((255, 131, 122))
        
    else:
        backdrop.fill((100, 100, 100))

    logoImage = pygame.transform.scale(IMAGE.get(logoImageName), (50, 50))
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
    message_text_height = 0
    message_text = []
    message_original_x = []
    message_original_y = []
    for message in messages:
        message_text_temp = Text.Text(
            screen,
            message,
            WIDTH / 2 - 500 / 2 + 20,
            HEIGHT / 2 - 300 / 2 + 20 + logoImageRect.height + 10 + message_text_height,
            fontSize=20,
        )
        message_text_height += message_text_temp.TEXTRECT.height 
        message_original_x.append(message_text_temp.x)
        message_original_y.append(message_text_temp.y)
        message_text.append(message_text_temp)
    # missing feature of passing in [str] for multi-line text builder 

    ok_button = Button.Button(
        screen,
        "OK",
        WIDTH / 2 - 100 / 2,
        HEIGHT / 2
        - 300 / 2
        + 20
        + logoImageRect.height
        + message_text_height
        + 20,
        100,
        100,
        background_color=(117, 251, 76),
    )
    # <-> left right
    sinCurveShake = 0
    sinCurveModifier = 0  # tan(sinCurveShake) = sinCurveModifier 1800 max
    # /\ \/
    quadraticShake = 100
    quadraticModifier = 0  # 2 root(quadraticShake) = quadraticModifier 20 max

    title_original_x = title.x
    # message_original_x = message_text.x
    ok_button_original_x = ok_button.x1

    title_original_y = title.y
    # message_original_y = message_text.y
    ok_button_original_y = ok_button.y1
    components = [title]
    components.extend(message_text)
    components.append(ok_button)
    for component in components:
        component.setVisibility(True)
    while transition == True:
        currentScreen.draw()
        screen.blit(backdrop, (0, 0))
        if logoImageName == "ERROR" or logoImageName == "WARN" :
            pygame.draw.rect(
                screen,
                (230, 230, 230),
                (
                    WIDTH / 2 - 500 / 2 + sinCurveModifier,
                    HEIGHT / 2 - 300 / 2,
                    500,
                    300,
                ),
                border_radius=40,
            )
            screen.blit(
                logoImage,
                (
                    WIDTH / 2 - 500 / 2 + 20 + sinCurveModifier,
                    HEIGHT / 2 - 300 / 2 + 20,
                ),
            )
            title.x = title_original_x + sinCurveModifier
            for index,component in enumerate(message_text):
                component.x = message_original_x[index] + sinCurveModifier
            # message_text.x = message_original_x + sinCurveModifier
            ok_button.x1 = ok_button_original_x + sinCurveModifier
            if sinCurveShake < 1800:
                sinCurveShake += 20
                sinCurveModifier = math.sin(sinCurveShake) * 30
        else:
            pygame.draw.rect(
                screen,
                (230, 230, 230),
                (
                    WIDTH / 2 - 500 / 2,
                    HEIGHT / 2 - 300 / 2 + quadraticModifier,
                    500,
                    300,
                ),
                border_radius=40,
            )
            screen.blit(
                logoImage,
                (
                    WIDTH / 2 - 500 / 2 + 20,
                    HEIGHT / 2 - 300 / 2 + 20 + quadraticModifier,
                ),
            )
            title.y = title_original_y + quadraticModifier
            for index,component in enumerate(message_text):
                component.y = message_original_y[index] + quadraticModifier
            # message_text.y = message_original_y - quadraticModifier
            ok_button.y1 = ok_button_original_y + quadraticModifier
            if quadraticShake > 0:
                quadraticShake -= 1
                quadraticModifier = math.sqrt(quadraticShake) * 8

        title.draw()

        for component in message_text:
            component.draw()

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
        pygame.display.update()
        fpsClock.tick(120)

def Question(
    screen: pygame.Surface,
    currentScreen, 
    title: str,
    messages: [str],
):
    logoImageName = "QUESTION"
    fpsClock = pygame.time.Clock()

    pygame.mouse.set_cursor(pygame.cursors.arrow)
    transition = True
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    backdrop = pygame.Surface((WIDTH, HEIGHT))
    alpha = 0
    backdrop.set_alpha(alpha)
    backdrop.fill((100, 100, 100))

    logoImage = pygame.transform.scale(IMAGE.get(logoImageName), (50, 50))
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
    message_text_height = 0
    message_text = []
    message_original_x = []
    message_original_y = []
    for message in messages:
        message_text_temp = Text.Text(
            screen,
            message,
            WIDTH / 2 - 500 / 2 + 20,
            HEIGHT / 2 - 300 / 2 + 20 + logoImageRect.height + 10 + message_text_height,
            fontSize=20,
        )
        message_text_height += message_text_temp.TEXTRECT.height 
        message_original_x.append(message_text_temp.x)
        message_original_y.append(message_text_temp.y)
        message_text.append(message_text_temp)
    # missing feature of passing in [str] for multi-line text builder 

    yes_button = Button.Button(
        screen,
        "yes",
        WIDTH / 2 - 100,
        HEIGHT / 2
        - 300 / 2
        + 20
        + logoImageRect.height
        + message_text_height
        + 20,
        100,
        80,
        background_color=(117, 251, 76),
    )
    no_button = Button.Button(
        screen,
        "no",
        WIDTH / 2 + 100,
        HEIGHT / 2
        - 300 / 2
        + 20
        + logoImageRect.height
        + message_text_height
        + 20,
        100,
        80,
        background_color=(235, 64, 52),
    )
    
    Grid.Grid_adjuster([yes_button, no_button], WIDTH / 2 - (100 * 2 + 20) / 2, 
        HEIGHT / 2
        - 300 / 2
        + 20
        + logoImageRect.height
        + message_text_height
        + 20, 20, 2
                       )
    # /\ \/
    quadraticShake = 100
    quadraticModifier = 0  # 2 root(quadraticShake) = quadraticModifier 20 max

    title_original_x = title.x

    title_original_y = title.y
    yes_button_original_y = yes_button.y1
    no_button_original_y = no_button.y1
    components = [title]
    components.extend(message_text)
    components.append(no_button)
    components.append(yes_button)
    for component in components:
        component.setVisibility(True)
    while transition == True:
        currentScreen.draw()
        screen.blit(backdrop, (0, 0))
        pygame.draw.rect(
            screen,
            (230, 230, 230),
            (
                WIDTH / 2 - 500 / 2,
                HEIGHT / 2 - 300 / 2 - quadraticModifier,
                500,
                300,
            ),
            border_radius=40,
        )
        screen.blit(
            logoImage,
            (
                WIDTH / 2 - 500 / 2 + 20,
                HEIGHT / 2 - 300 / 2 + 20 - quadraticModifier,
            ),
        )
        title.y = title_original_y - quadraticModifier
        for index,component in enumerate(message_text):
            component.y = message_original_y[index] - quadraticModifier
        # message_text.y = message_original_y - quadraticModifier
        no_button.y1 = no_button_original_y - quadraticModifier
        yes_button.y1 = yes_button_original_y - quadraticModifier
        if quadraticShake > 0:
            quadraticShake -= 1
            quadraticModifier = math.sqrt(quadraticShake) * 8

        title.draw()

        for component in components:
            component.draw()

        # ok_button.draw()
        mouseX, mouseY = pygame.mouse.get_pos()
        no_button.update(mouseX, mouseY, data="")
        yes_button.update(mouseX, mouseY, data="")

        for event in pygame.event.get():
            if event.type == QUIT:
                transition = False
                return False
            if event.type == MOUSEBUTTONDOWN:
                if no_button.getHovered():
                    transition = False
                    return False
                elif yes_button.getHovered():
                    transition = False
                    return True
                    

        if alpha < 180:
            alpha += 5
            backdrop.set_alpha(alpha)

        pygame.display.update()
        fpsClock.tick(120)