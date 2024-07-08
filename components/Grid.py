import pygame
from components import Button, Text


def Grid_adjuster(
    items: [Button.Button],
    x1: int | float,
    y1: int | float,
    gap: int | float,
    row_limit: int,
):
    item_on_row = 0
    x1_on = x1
    y1_on = y1
    for item in items:
        item.setXY(x1_on, y1_on)
        item_on_row += 1
        if item_on_row == row_limit:
            x1_on = x1
            y1_on += item.height
            y1_on += gap
            item_on_row = 0
        else:
            x1_on += item.width
            x1_on += gap
