REQUIREMENT = {"JUMPING_ROPE_GAME": 2, "CATCH_GAME": 5, "RACING_GAME": 10}

def levelUnlockCheck(level: int, requirement: int) -> bool:
    if level >= requirement:
        return False
    else:
        return True
            
class Level:
    def __init__(self, level: int, progression: float):
        self.level = level
        self.progression = progression
    def getLevel(self) -> int:
        return self.level
    def getProgression(self) -> float:
        return self.progression