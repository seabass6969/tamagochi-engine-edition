import pygame, os, random
IMAGE = {
    "ENGINE": pygame.image.load(os.path.join("assets", "engine.png")),
    "INFO": pygame.image.load(os.path.join("assets/icon_button", "info.png")),
    "SHOP": pygame.image.load(os.path.join("assets/icon_button", "shop.png")),
    "WARN": pygame.image.load(os.path.join("assets/icon_button", "warn.png")),
    "ERROR": pygame.image.load(os.path.join("assets/icon_button", "error.png")),
    "GARAGE": pygame.image.load(os.path.join("assets/icon_button", "garage.png")),
    "BRAIN": pygame.image.load(os.path.join("assets/icon_button", "brain.png")),
    "STRING": pygame.image.load(os.path.join("assets/icon_button", "string.png")),
    "HAND": pygame.image.load(os.path.join("assets/icon_button", "hand.png")),
    "CAR": pygame.image.load(os.path.join("assets/icon_button", "car.png")),
    "HEART": pygame.image.load(os.path.join("assets/icon_button", "heart.png")),
    "CASH": pygame.image.load(os.path.join("assets/icon_button", "cash.png")),
    "BACK": pygame.image.load(os.path.join("assets/icon_button", "back.png")),
    "TEST": pygame.image.load(os.path.join("assets/icon_button", "test.png")),
    "HAPPY1": pygame.image.load(os.path.join("assets/icon_button", "happy1.png")),
    "HAPPY2": pygame.image.load(os.path.join("assets/icon_button", "happy2.png")),
    "HAPPY3": pygame.image.load(os.path.join("assets/icon_button", "happy3.png")),
    "ILL": pygame.image.load(os.path.join("assets/icon_button", "ill.png")),
    "MID": pygame.image.load(os.path.join("assets/icon_button", "mid.png")),
    "SAD": pygame.image.load(os.path.join("assets/icon_button", "sad.png")),
    "ANGRY": pygame.image.load(os.path.join("assets/icon_button", "angry.png")),
    "YES": pygame.image.load(os.path.join("assets/icon_button", "check.png")),
    "NO": pygame.image.load(os.path.join("assets/icon_button", "cross.png")),
    "GEAR": pygame.image.load(os.path.join("assets/icon_button", "cog.png")),
    "DRAWING": pygame.image.load(os.path.join("assets/icon_button", "drawing.png")),
}

IMAGE_MEMORY = [
    pygame.image.load(os.path.join("assets/memory_game", "front_page.png")),
    pygame.image.load(os.path.join("assets/memory_game", "cake.png")),
    pygame.image.load(os.path.join("assets/memory_game", "can.png")),
    pygame.image.load(os.path.join("assets/memory_game", "car.png")),
    pygame.image.load(os.path.join("assets/memory_game", "earth.png")),
    pygame.image.load(os.path.join("assets/memory_game", "gear.png")),
    pygame.image.load(os.path.join("assets/memory_game", "lemon.png")),
]

IMAGE_CELEBRATION = [
    pygame.image.load(os.path.join("assets/celebration", "well_done.png")),
    pygame.image.load(os.path.join("assets/celebration", "excellent.png")),
]
def get_image_celebration():
    return random.choice(IMAGE_CELEBRATION)