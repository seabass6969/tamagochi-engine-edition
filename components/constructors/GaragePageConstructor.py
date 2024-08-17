from dataHandler import dataHandler
from constants.MarketPlaceItems import marketplaceItems_byID
from components.interactables.button import RepairButton
from components.Grid import Grid_adjuster


class GaragePageConstructor:
    def __init__(self, screen, y1, data: dataHandler.Datahandler):
        self.screen = screen
        self.components = []
        for item in marketplaceItems_byID:
            self.components.append(
                RepairButton.RepairButton(self.screen, item, 0, 0, data)
            )
        Grid_adjuster(
            self.components,
            self.screen.get_width() / 2 - (self.components[0].width * 3 + 10 * 2) / 2,
            y1 + 10,
            10,
            3,
        )

        self.y = y1

    def update(self, x, y, data: dataHandler.Datahandler):
        for component in self.components:
            component.update(x, y, data)

    def draw(self):
        for component in self.components:
            component.draw()

    def setVisibility(self, vis: bool):
        for component in self.components:
            component.setVisibility(vis)

    # when there is a button
    def clickRegister(self, data, currentScreen):
        for component in self.components:
            component.click(data, currentScreen)

    def getHovered(self):
        return False
