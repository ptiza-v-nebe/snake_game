from enum import Enum


# this enum represents actual control of the snake in the game
class Control(int, Enum):
    UP: int = 0
    DOWN: int = 1
    RIGHT: int = 2
    LEFT: int = 3
