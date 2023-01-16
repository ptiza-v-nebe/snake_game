from dataclasses import dataclass
from .symbol import Symbol


# this class represents the resulting rendering cell for Render class
@dataclass
class Field:
    x: int
    y: int
    t: Symbol
