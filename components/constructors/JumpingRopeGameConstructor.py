"""
All constructor must have __init__(), update(), draw(), setVisibility()
"""

from dataHandler import dataHandler
import random
from components.interactables.jumpingRopeGame.platform import Platform
from components.interactables.jumpingRopeGame.DeathPit import DeathPit 
from components.interactables.jumpingRopeGame.character import Character 


class JumpingRopeGameConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.y = y1
        self.platforms = []
        self.platforms.append(Platform(screen, 10, self.y + 100, 30))
        self.platforms.append(Platform(screen, 150, self.y + 100, 100))
        self.deathPits = []
        self.deathPits.append(DeathPit(screen, 0,self.y + 200, screen.get_width() - 100))
        self.character = Character(screen, 10, self.y + 20)

    def update(self, x, y, data: dataHandler.Datahandler):
        for platform in self.platforms:
            platform.update(x, y, data)
        for deathpit in self.deathPits:
            deathpit.update(x, y, data)
        self.character.update(x,y,data)
        self.gravity()

        for deathpit in self.deathPits:
            if deathpit.line_mask.overlap(self.character.engine_mask, (self.character.x - deathpit.x, self.character.y - deathpit.y)):
                print("deattpit")

    def draw(self):
        for platform in self.platforms:
            platform.draw()
        for deathpit in self.deathPits:
            deathpit.draw()
        self.character.draw()

    def setVisibility(self, vis: bool):
        pass

    def getHovered(self):
        return False

    # when there is a button
    def clickRegister(self):
        self.character.clickRegister()

    def keyRegister(self, key, down):
        self.character.keyRegister(key, down)

    def gravity(self):
        # gravity check
        overlaps = []
        for platform in self.platforms:
            if platform.platform_mask.overlap(self.character.engine_mask, (self.character.x - platform.x, self.character.y - platform.y)):
                overlaps.append(True)
        if True in overlaps:
            self.character.overlap = True
        else:
            self.character.overlap = False
        
        if self.character.overlap == False:
            self.character.y += 0.5