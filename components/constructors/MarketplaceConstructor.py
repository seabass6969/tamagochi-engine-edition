from dataHandler import dataHandler
from constants.MarketPlaceItems import marketplaceItems_byID
from components.interactables.button import PurchaseButton
from components import Grid


class MarketplaceConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.components = []
        self.purchase_components = []
        self.y = y1
        for keys in marketplaceItems_byID:
            self.purchase_components.append(
                PurchaseButton.PurchaseButton(self.screen, keys, 0, 0)
            )

        self.components.extend(self.purchase_components)
        Grid.Grid_adjuster(
            self.purchase_components,
            self.screen.get_width() / 2
            - (self.purchase_components[0].width * 3 + 10 * 2) / 2,
            y1 + 10,
            10,
            3,
        )

    def update(self, x, y, data: dataHandler.Datahandler):
        for component in self.components:
            component.update(x, y, data)

    def draw(self):
        for component in self.components:
            component.draw()

    def setVisibility(self, vis: bool):
        for component in self.components:
            component.setVisibility(vis)

    def clickRegister(self,data, currentScreen):
        for component in self.components:
            component.click(data, currentScreen)

    def getHovered(self):
        return False