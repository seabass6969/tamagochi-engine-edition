import traceback
import pygame
import Alert
from transition import slideLeftToRight
from asset import IMAGE
from components import BackButton


class State:

    def __init__(
        self,
        screen: pygame.Surface,
        name: str,
        background_color: pygame.Color,
        components_button: [],
        components_text: [],
        optional_update_component=[],
        optional_back_button=False
    ):
        self.screen = screen
        self.background_color = background_color
        self.optional_update_component = optional_update_component
        self.components = []
        self.components.extend(components_text)
        self.components.extend(components_button)
        self.components.extend(optional_update_component)
        self.components_text = components_text
        self.components_button = components_button
        self.name = name

        self.optional_back_button = optional_back_button
        
        if self.optional_back_button:
            self.backbutton = BackButton.BackButton(screen, 10, 10)
            self.components.append(self.backbutton)
            self.components_button.append(self.backbutton)

    def draw(self):
        self.screen.fill((115, 115, 115))
        for component in self.components:
            component.draw()

    def update(self, x: int, y: int):
        hovered_list = []
        for component in self.components_button:
            component.update(x, y)
            hovered_list.append(component.getHovered())
        for component in self.optional_update_component:
            component.update(x, y)
        if True in hovered_list:
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)
    def getBackButtonHover(self) -> bool:
        if self.optional_back_button:
            return self.backbutton.getHovered()
        else:
            return False



def changeState(
    withAnimation: bool,
    nextState: State,
    previousState: State,
    screen: pygame.Surface,
    fpsClock,
    # nextStateName: str,
    componentDisable: [] = [],
    componentEnable: [] = [],
) -> str:
    try:
        name = nextState.name
        pygame.mouse.set_cursor(pygame.cursors.arrow)
        componentDisable.extend(previousState.components_button)
        componentDisable.extend(previousState.components_text)

        componentEnable.extend(nextState.components_button)
        componentEnable.extend(nextState.components_text)
        for component in componentDisable:
            component.setVisibility(False)
            component.hovered = False
        for component in componentEnable:
            component.setVisibility(True)
            component.hovered = False
        if withAnimation:
            slideLeftToRight(screen, fpsClock, nextState.draw)

        return name
    except AttributeError:
        Alert.Alert(screen, previousState, IMAGE.get("ERROR"), "In Construction", "The Page is in construction!")
        return previousState.name
    except Exception as e:
        Alert.Alert(screen, previousState, IMAGE.get("ERROR"), "Danger Zone", "The Page is broken!")
        print(traceback.format_exc())
        return previousState.name
        
