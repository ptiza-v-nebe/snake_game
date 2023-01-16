from enum import Enum


class GameState(Enum):
    IDLE = 0
    RUNNING = 1
    STOPPED = 2