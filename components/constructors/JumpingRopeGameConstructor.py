'''
All constructor must have __init__(), update(), draw(), setVisibility()
'''

from dataHandler import dataHandler
class JumpingRopeGameConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.components = []
        self.y = y1
        pass

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
    def clickRegister(self):
        for component in self.components:
            component.click()
