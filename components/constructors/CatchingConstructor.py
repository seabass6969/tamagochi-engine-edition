from dataHandler import dataHandler
from components.interactables.catchingGame.bag import Bag
from components.interactables.catchingGame.randomDrops import RandomDrops


class CatchingConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.components = []
        self.y = y1
        self.visible = False
        self.bag = Bag(screen)
        for _ in range(4):
            self.components.append(RandomDrops(screen, y1, self.bag))

    def update(self, x, y, data: dataHandler.Datahandler):
        self.bag.update(x,y,data)
        for component in self.components:
            component.update(x, y, data)
            if component.circles_mask.overlap(
                self.bag.bag_mask,
                (self.bag.x - component.x, self.bag.y - component.y),
            ):
                data.increaseLevel(10)
                data.increaseGotchiPoint(10)
                component.touched_update()



    def draw(self):
        for component in self.components:
            component.draw()
        self.bag.draw()

    def setVisibility(self, vis: bool):
        print(vis)
    # when there is a button
    def clickRegister(self):
        for component in self.components:
            component.click()

    def getHovered(self):
        pass