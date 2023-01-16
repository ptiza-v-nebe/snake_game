from enum import Enum


# global symbol enum
# this structure is important for rendering
class Symbol(str, Enum):
    HEAD = "h"
    TAIL = "s"
    FOOD = "*"
    WALL = "#"
    PATH = "-"
