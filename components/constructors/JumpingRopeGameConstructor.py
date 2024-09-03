"""
All constructor must have __init__(), update(), draw(), setVisibility()
"""

from dataHandler import dataHandler
import random, pygame
from components.interactables.jumpingRopeGame.platform import Platform
from components.interactables.jumpingRopeGame.DeathPit import DeathPit
from components.interactables.jumpingRopeGame.character import Character
from components.interactables.jumpingRopeGame.spike import Spike
from components.interactables.jumpingRopeGame.Tips import Tips
from components.interactables.jumpingRopeGame.crusher import Crusher
from components.interactables.jumpingRopeGame.WinPlatform import WinPlatform
from components.displays.Navbar import Navbar


class JumpingRopeGameConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.y = y1
        self.navbar = Navbar(self.screen)
        self.tips = Tips(self.screen)
        self.platforms = []
        self.platforms.append(Platform(screen, 10, self.y + 100, 30))
        self.platforms.append(Platform(screen, 100, self.y + 100, 100))
        self.deathPits = []
        self.deathPits.append(
            DeathPit(screen, 0, self.y + 200, width=screen.get_width() - 100)
        )
        self.deathPits.append(DeathPit(screen, 0, 2, height=self.screen.get_height()))
        self.spikes = []
        self.spikes.append(Spike(screen, 100, self.y + 80, 65))

        self.crushers = []
        # self.crushers.append(Crusher(screen, 150, self.y))

        self.character = Character(screen, 10, self.y + 20)
        self.winplatform = WinPlatform(screen, 170, self.y + 80)

        self.keys = []

    def checkObstacle(self,data: dataHandler.Datahandler):
        for deathpit in self.deathPits:
            if deathpit.line_mask.overlap(
                self.character.engine_mask,
                (self.character.x - deathpit.x, self.character.y - deathpit.y),
            ):
                self.reset()

        for spike in self.spikes:
            if spike.spike_mask.overlap(
                self.character.engine_mask,
                (self.character.x - spike.x, self.character.y - spike.y),
            ):
                self.reset()

        for crusher in self.crushers:
            if crusher.crushing_mask.overlap(
                self.character.engine_mask,
                (self.character.x - crusher.x, self.character.y - crusher.y),
            ):
                self.reset()

        if self.winplatform.win_mask.overlap(
            self.character.engine_mask,
            (self.character.x - self.winplatform.x, self.character.y - self.winplatform.y),
        ):

            data.increaseLevel(10)
            data.increaseGotchiPoint(10)
            self.reset()

    def update(self, x, y, data: dataHandler.Datahandler):
        for platform in self.platforms:
            platform.update(x, y, data)
        for deathpit in self.deathPits:
            deathpit.update(x, y, data)
        for spike in self.spikes:
            spike.update(x, y, data)
        for crusher in self.crushers:
            crusher.update(x, y, data)
        self.character.update(x, y, data)
        self.gravity()

        self.checkObstacle(data)

        if pygame.locals.K_w in self.keys:
            if self.checkWalls(1, 0):
                self.character.x += 1
        if pygame.locals.K_s in self.keys:
            if self.checkWalls(-1, 0):
                self.character.x -= 1
        if pygame.locals.K_SPACE in self.keys:
            if self.checkWalls(0, -1):
                self.character.y -= 1
        self.character.engine_rect.topleft = (self.character.x, self.character.y)

    def checkWalls(self, x, y) -> bool:
        for platform in self.platforms:
            if platform.platform_mask.overlap(
                self.character.engine_mask,
                (
                    (self.character.x + x) - platform.x,
                    (self.character.y + y - 0.5) - platform.y,
                ),
            ):
                return False
        return True

    def draw(self):
        for platform in self.platforms:
            platform.draw()
        for deathpit in self.deathPits:
            deathpit.draw()
        for spike in self.spikes:
            spike.draw()
        for crusher in self.crushers:
            crusher.draw()
        self.character.draw()
        self.winplatform.draw()
        # navbar

        self.navbar.draw()
        self.tips.draw()

    def setVisibility(self, vis: bool):
        pass

    def getHovered(self):
        return False

    # when there is a button
    def clickRegister(self):
        self.character.clickRegister()

    def keyRegister(self, key, down):

        if down == True:
            self.keys.append(key)
        else:
            try:
                self.keys.remove(key)
            except:
                pass

        # self.character.keyRegister(key, down)

    def gravity(self):
        # gravity check
        overlaps = []
        for platform in self.platforms:
            if platform.platform_mask.overlap(
                self.character.engine_mask,
                (self.character.x - platform.x, self.character.y - platform.y),
            ):
                overlaps.append(True)
        if True in overlaps:
            self.character.overlap = True
        else:
            self.character.overlap = False

        if self.character.overlap == False:
            self.character.y += 0.5

    def reset(self):
        self.character.x = 10

        self.character.y = self.y + 20
        self.keys = []
