import pygame
from components.interactables.button.Button import Button
from constants.asset import IMAGE
from constants.MarketPlaceItems import marketplaceItems_byID
from dataHandler import dataHandler
from Alert import Question, Alert


def itemPurchasing(item_id):
    pass
    
class PurchaseButton(Button):
    def __init__(
        self,
        screen,
        item_id,
        x1,
        y1,
        background_color=(217, 217, 217),
    ):

        self.NAME_FONT = pygame.font.SysFont("Comic Sans MS", 20)
        self.PRICE_FONT = pygame.font.SysFont("Comic Sans MS", 30)

        self.item_id = item_id
        self.ITEM_IMAGE = marketplaceItems_byID.get(self.item_id).image
        self.ITEM_IMAGE = pygame.transform.scale(self.ITEM_IMAGE, (96, 96))
        self.ITEM_IMAGE_RECT = self.ITEM_IMAGE.get_rect()

        self.PRICE = marketplaceItems_byID.get(self.item_id).price
        self.ITEM_PRICE = "G$ {}".format(self.PRICE)
        self.ITEM_PRICE_TEXT = self.PRICE_FONT.render(self.ITEM_PRICE, False, (0, 0, 0))
        self.ITEM_PRICE_TEXT_RECT = self.ITEM_PRICE_TEXT.get_rect()

        self.ITEM_NAME = marketplaceItems_byID.get(self.item_id).name
        self.ITEM_NAME_TEXT = self.NAME_FONT.render(self.ITEM_NAME, False, (0, 0, 0))
        self.ITEM_NAME_TEXT_RECT = self.ITEM_NAME_TEXT.get_rect()

        super().__init__(screen, "", x1, y1, 180,200, background_color)
    
    def draw(self):
        super().draw()
        self.screen.blit(
            self.ITEM_IMAGE, (self.x1 + self.width / 2 - self.ITEM_IMAGE_RECT.width / 2, self.y1)
        )
        self.screen.blit(
            self.ITEM_NAME_TEXT, (self.x1 + self.width / 2 - self.ITEM_NAME_TEXT_RECT.width / 2, self.y1 + 5 + self.ITEM_IMAGE_RECT.height)
        )
        self.screen.blit(
            self.ITEM_PRICE_TEXT, (self.x1 + self.width / 2 - self.ITEM_PRICE_TEXT_RECT.width / 2, self.y1 + 5 * 2 + self.ITEM_IMAGE_RECT.height + self.ITEM_NAME_TEXT_RECT.height)
        )
    
    def click(self, data: dataHandler.Datahandler, currentScreen):
        if self.hovered == True:
            if data.getGotchiPointRequirementMet(self.PRICE):
                questionAnswer = Question(self.screen, currentScreen, "Question", ["Do you want to purchase", self.ITEM_NAME, "for {}?".format(self.ITEM_PRICE)])
                if questionAnswer == True:
                    data.decreaseGotchiPoint(self.PRICE)
                    data.purchaseItem(self.item_id)
            else:
                Alert(self.screen, currentScreen, "ERROR", "Insufficient fund", ["You don't have {}.".format(self.ITEM_PRICE)])
