import pygame
import pygame_shaders

import os
import uuid



        
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
background = gradientRoundedCornerRectangle(screen, [(180, 41, 249), (38,197,243)], (1000,1000),20, 10, 10)
background.preRender()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background.draw()


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
