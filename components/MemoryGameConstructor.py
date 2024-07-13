import pygame, math, random
import Alert
from dataHandler import dataHandler
from components import MemoryButton, Grid
from asset import IMAGE, IMAGE_MEMORY, get_image_celebration


class MemoryGameConstructor:
    def __init__(self, screen, y1):
        self.screen = screen
        self.won = False
        self.won_image = pygame.transform.rotate(get_image_celebration(), 45)
        self.WON_DELAY_LIMIT = 120
        self.won_delay = self.WON_DELAY_LIMIT
        self.won_background = pygame.Surface(
            (self.screen.get_width(), self.screen.get_height())
        )
        self.won_background.set_alpha(180)
        self.y = y1
        self.memoryGameItems = []
        self.total_peaks = 0
        for i in range(1, len(IMAGE_MEMORY)):
            self.memoryGameItems.append(
                MemoryButton.MemoryButton(self.screen, i, 10, self.y, "back")
            )
            self.memoryGameItems.append(
                MemoryButton.MemoryButton(self.screen, i, 10, self.y, "back")
            )
        random.shuffle(self.memoryGameItems)
        Grid.Grid_adjuster(
            self.memoryGameItems,
            self.screen.get_width() / 2 - ((100 * 1.3) * 4 + 10 * 3) / 2,
            self.y,
            10,
            4,
        )

    def update(self, x, y, data: dataHandler.Datahandler):
        self.total_peaks = 0
        peak = 0
        peaking = []
        for component in self.memoryGameItems:
            if (
                component.flipSide == "front" or component.switching_motion == True
            ) and component.user_linked == False:
                peak += 1
                peaking.append(component.imageID)
        for component in self.memoryGameItems:
            component.update(x, y, data, peak, peaking)
            self.total_peaks += component.fliped_times
        if self.won == False:
            total = 0
            for component in self.memoryGameItems:
                if component.flipSide == "front":
                    total += 1
            if total == len(self.memoryGameItems):
                self.won = True
        if self.won:
            if self.won_delay > 0:
                self.won_delay -= 1
            else:
                increasedBy = max(math.floor((200 - self.total_peaks) / 4), 20)
                increasedByLvl = max(math.floor((200 - self.total_peaks) / 8), 10)
                data.increaseGotchiPoint(increasedBy)
                data.increaseLevel(increasedByLvl)
                Alert.Alert(
                    self.screen,
                    self,
                    "HAPPY1",
                    "You Won",
                    "It takes you {} peaks. earning {} points / {} xp".format(
                        self.total_peaks, increasedBy, increasedByLvl
                    ),
                )
                self.reset()
        # for component in self.memoryGameItems:

    def draw(self):
        for component in self.memoryGameItems:
            component.draw()
        if self.won:
            self.screen.blit(self.won_background, (0, 0))
            self.screen.blit(
                self.won_image,
                (
                    self.screen.get_width() / 2 - self.won_image.get_width() / 2,
                    self.screen.get_height() / 2 - self.won_image.get_height() / 2,
                ),
            )

    def getHovered(self) -> bool:
        return self.hovered and self.visible

    def setVisibility(self, vis: bool):
        for component in self.memoryGameItems:
            component.setVisibility(vis)

    def clickRegister(self):
        for component in self.memoryGameItems:
            component.click()

    def reset(self):
        self.__init__(self.screen, self.y)