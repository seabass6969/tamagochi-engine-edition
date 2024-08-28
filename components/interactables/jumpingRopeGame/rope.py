import pygame, random, time, math
from constants.asset import IMAGE_ROPE_GAME
from dataHandler import dataHandler
from pygame.locals import *


class Rope:
    def __init__(self, screen: pygame.Surface, x, y, random_swing_motion):
        self.screen = screen
        self.rope_image = pygame.transform.chop(
            IMAGE_ROPE_GAME.get("ROPE"), (1, 12, 3, 0)
        )
        self.y = y + self.rope_image.get_width() / 2
        self.x = x + self.rope_image.get_height() / 2

        # self.rope_image = pygame.transform.scale_by(self.rope_image, 10)
        # self.rope_image_original = self.rope_image
        self.rope_image = pygame.Surface((100,300))
        self.rope_image.fill(pygame.Color(0,0,0,0))
        self.rope_image.set_colorkey(pygame.Color(0,0,0,0))
        pygame.draw.arc(self.rope_image, (255,255,255), (-54, -150, 100, 300), 0, 10, 2)
        self.rope_mask = pygame.mask.from_surface(self.rope_image)
        self.rope_rect = self.rope_mask.get_rect()
        self.rope_rect.topleft= (self.x, self.y)
        self.overlap = False
        self.random_swing_motion = random_swing_motion
        self.swing_angle = 0
        if self.random_swing_motion == True:
            self.swingDirection = random.choice(["forward", "backward"])

    def draw(self):
        self.screen.blit(self.rope_image, self.rope_rect)

    def clickRegister(self):
        pass

    def keyRegister(self, key, down):
        # if down == True:
        #     if key == K_LEFT:
        #         self.rope_image = pygame.transform.rotate(self.rope_image_original, 10)
        #     if key == K_RIGHT:
        #         self.rope_image = pygame.transform.rotate(self.rope_image_original, )
        # elif down == False:
        #     if key == K_LEFT:
        #         self.rope_image = pygame.transform.rotate(self.rope_image_original, 0)
        #     if key == K_RIGHT:
        #         self.rope_image = pygame.transform.rotate(self.rope_image_original, 0)
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        # if self.rope_mask.overlap_area(self.mouse_mask, (x - self.rope_rect.x,y - self.rope_rect.y)):
        #     self.overlap = True
        # else:
        #     self.overlap = False
        
        if self.random_swing_motion == True:
            if self.swingDirection == "forward":
                if self.swing_angle >= 90:
                    self.swingDirection = "backward"
                else:
                    self.swing_angle += 0.1
            elif self.swingDirection == "backward":
                if self.swing_angle <= 30:
                    self.swingDirection = "forward"
                else:
                    self.swing_angle -= 0.1
        
        self.rope_image.fill(pygame.Color(0,0,0,0))
        pygame.draw.arc(self.rope_image, (255,255,255), (-54, -150+ abs(self.swing_angle) / 2, 100, 300 + abs(self.swing_angle)), 0, abs(self.swing_angle), 2)
        
        print(self.swing_angle)

        pass