from dataclasses import dataclass
from symbol import Symbol


@dataclass
class Field:
    x: int
    y: int
    t: Symbol
