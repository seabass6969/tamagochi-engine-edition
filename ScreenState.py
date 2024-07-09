import traceback
import pygame
import Alert
from components import BackButton
from transition import slideLeftToRight
from asset import IMAGE


class State:

    def __init__(
        self,
        screen: pygame.Surface,
        name: str,
        background_color: pygame.Color,
        components_button: [],
        components_text: [],
        optional_update_component=[],
        optional_back_button=False,
    ):
        self.screen = screen
        self.background_color = background_color
        self.components = []
        self.components.extend(components_text)
        self.components.extend(components_button)
        self.components.extend(optional_update_component)
        self.components_text = components_text
        self.components_button = components_button
        self.optional_update_component = optional_update_component
        self.name = name
        self.optional_back_button = optional_back_button
        self.backButton = BackButton.BackButton(self.screen, 10, 10)
        if self.optional_back_button:
            self.components_button.append(self.backButton)
            self.components.append(self.backButton)

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

    def getBackButtonhover(self) -> bool:
        return self.backButton.getHovered()


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
        componentDisable.extend(previousState.components)
        componentEnable.extend(nextState.components)

        for component in componentDisable:
            component.setVisibility(False)
        for component in componentEnable:
            component.setVisibility(True)
        if withAnimation:
            slideLeftToRight(screen, fpsClock, nextState.draw)

        print(previousState.name,nextState.name)
        return name
    except AttributeError:
        Alert.Alert(screen, previousState, IMAGE.get("ERROR"), "In Construction", "The Page is in construction!")
        return previousState.name
    except Exception as e:
        Alert.Alert(screen, previousState, IMAGE.get("ERROR"), "Danger Zone", "The Page is broken!")
        print(traceback.format_exc())
        return previousState.name
        
