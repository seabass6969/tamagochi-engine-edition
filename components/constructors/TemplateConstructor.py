'''
All constructor must have __init__(), update(), draw(), setVisibility()
'''

from dataHandler import dataHandler
class TemplateConstructor:
    def __init__(self, screen, y1):
        self.components = []
        self.y = y1
        pass

    def update(self, x, y, data: dataHandler.Datahandler):
        pass
    
    def draw(self):
        pass

    def setVisibility(self, vis: bool):
        for component in self.compoents:
            component.setVisibility(vis)

    # when there is a button
    def clickRegister(self):
        for component in self.components:
            component.click()
