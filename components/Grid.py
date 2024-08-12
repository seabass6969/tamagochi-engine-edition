import pygame
from components.displays.text import Text
from components.interactables.button import Button


def Grid_adjuster(
    items: [],
    x1: int | float,
    y1: int | float,
    gap: int | float,
    row_limit: int,
):
    item_on_row = 0
    x1_on = x1
    y1_on = y1

    highest_height = 0
    for item in items:
        item.setXY(x1_on, y1_on)
        item_on_row += 1
        if item_on_row == row_limit:
            x1_on = x1
            if highest_height < item.height:
                highest_height = item.height
            y1_on += highest_height
            y1_on += gap
            item_on_row = 0
            highest_height = 0
        else:
            x1_on += item.width
            x1_on += gap
            if highest_height < item.height:
                highest_height = item.height