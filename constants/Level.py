import math

REQUIREMENT = {"JUMPING_ROPE_GAME": 2, "CATCH_GAME": 3, "RACING_GAME": 5, "CIRCLE_GAME": 4}


def levelUnlockCheck(level: int, requirement: int) -> bool:
    if level >= requirement:
        return False
    else:
        return True


XP_PROGRESSION = [
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    1024,
    2048,
    4096,
    5000,
    6000,
    7000,
    8000,
    9000,
    10000,
    11000,
    12000,
    13000,
    14000,
    15000,
    16000,
    17000,
    18000,
    19000,
    20000,
    21000,
    22000,
    23000,
    24000,
    25000,
    26000,
    27000,
    28000,
    29000,
    30000,
]


class Level:
    def __init__(self, level: int, progression: int):
        self.level = level
        self.progression = progression

    def getLevel(self) -> int:
        return self.level

    def getProgression(self) -> int:
        return self.progression
    def getLevelProgressionMax(self) -> int:
        return XP_PROGRESSION[self.getLevel()]

