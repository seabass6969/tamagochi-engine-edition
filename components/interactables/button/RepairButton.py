import pygame
from components.interactables.button.Button import Button
from constants.asset import IMAGE
from constants.MarketPlaceItems import marketplaceItems_byID
from dataHandler import dataHandler
from Alert import Question, Alert
import math

class RepairButton(Button):
    def __init__(
        self,
        screen,
        item_id,
        x1,
        y1,
        data:dataHandler.Datahandler,
        background_color=(217, 217, 217),
    ):
        self.NAME_FONT = pygame.font.SysFont("Comic Sans MS", 20)
        self.REMAINING_FONT = pygame.font.SysFont("Comic Sans MS", 30)

        self.item_id = item_id
        self.ITEM_IMAGE = marketplaceItems_byID.get(self.item_id).image
        self.ITEM_IMAGE = pygame.transform.scale(self.ITEM_IMAGE, (96, 96))
        self.ITEM_IMAGE_RECT = self.ITEM_IMAGE.get_rect()

        self.REMAINING = data.garagePartsRemaining(self.item_id)
        self.REMAINING_TEXT = self.REMAINING_FONT.render("You got: {}".format(self.REMAINING), False, (0, 0, 0))
        self.REMAINING_TEXT_RECT = self.REMAINING_TEXT.get_rect()

        self.ITEM_NAME = marketplaceItems_byID.get(self.item_id).name
        self.ITEM_NAME_TEXT = self.NAME_FONT.render(self.ITEM_NAME, False, (0, 0, 0))
        self.ITEM_NAME_TEXT_RECT = self.ITEM_NAME_TEXT.get_rect()

        self.disabled = data.isRepaired(self.item_id)
        super().__init__(screen, "", x1, y1, 180,200, background_color)
    
    def draw(self):
        if self.getHovered() and not self.disabled:
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (self.x1 - 2, self.y1 - 2, self.width + 4, self.height + 4),
                border_radius=20,
            )
        if self.disabled:
            pygame.draw.rect(
                self.screen,
                (150, 150, 150),
                (self.x1, self.y1, self.width, self.height),
                border_radius=20,
            )
        else:
            pygame.draw.rect(
                self.screen,
                (217, 217, 217),
                (self.x1, self.y1, self.width, self.height),
                border_radius=20,
            )

        if self.disabled:
            for i in range(20, math.floor(self.width - 10), 8):
                pygame.draw.line(
                    self.screen,
                    (0, 0, 0),
                    (self.x1 + i, self.y1),
                    (self.x1, self.y1 + i),
                )
        self.screen.blit(
            self.ITEM_IMAGE, (self.x1 + self.width / 2 - self.ITEM_IMAGE_RECT.width / 2, self.y1)
        )
        self.screen.blit(
            self.ITEM_NAME_TEXT, (self.x1 + self.width / 2 - self.ITEM_NAME_TEXT_RECT.width / 2, self.y1 + 5 + self.ITEM_IMAGE_RECT.height)
        )
        self.screen.blit(
            self.REMAINING_TEXT, (self.x1 + self.width / 2 - self.REMAINING_TEXT_RECT.width / 2, self.y1 + 5 * 2 + self.ITEM_IMAGE_RECT.height + self.ITEM_NAME_TEXT_RECT.height)
        )
    
    def click(self, data: dataHandler.Datahandler, currentScreen):
        if self.hovered == True:
            if self.disabled == False:
                if data.garagePartsRemaining(self.item_id) > 0:
                    questionAnswer = Question(self.screen, currentScreen, "Question", ["Do you want to repair using {}?".format(self.ITEM_NAME)])
                    if questionAnswer == True:
                        data.garagePartsRepairer(self.item_id)
                        data.increaseLevel(10)
                else:
                    Alert(self.screen, currentScreen, "ERROR", "Lack of the Item", ["You don't have {}.".format(self.ITEM_NAME)])
            else:
                Alert(self.screen, currentScreen, "ERROR", "No need", ["You don't need to repair {}.".format(self.ITEM_NAME)])
            

    def update(self, x, y, data:dataHandler.Datahandler):
        super().update(x,y,data)
        if self.REMAINING != data.garagePartsRemaining(self.item_id):
            self.REMAINING = data.garagePartsRemaining(self.item_id)
            self.REMAINING_TEXT = self.REMAINING_FONT.render("You got: {}".format(self.REMAINING), False, (0, 0, 0))
            self.REMAINING_TEXT_RECT = self.REMAINING_TEXT.get_rect()
        self.disabled = data.isRepaired(self.item_id)
            

        
