from enum import Enum


# represents the global game state
class GameState(Enum):
    IDLE = 0
    RUNNING = 1
    STOPPED = 2