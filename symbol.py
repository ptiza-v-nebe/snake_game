from enum import Enum


class Symbol(str, Enum):
    HEAD = "h"
    TAIL = "s"
    FOOD = "*"
    WALL = "#"
    PATH = "-"
