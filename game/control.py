from enum import Enum


class Control(int, Enum):
    UP: int = 0
    DOWN: int = 1
    RIGHT: int = 2
    LEFT: int = 3
