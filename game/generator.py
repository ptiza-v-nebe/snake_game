import random
from .point import Point


class Generator:
    def __init__(self):
        self.width_begin = 0
        self.width_end = 0
        self.height_begin = 0
        self.height_end = 0

    def calculate_nonwall_field(self, width_total, height_total):
        self.width_begin = 1
        self.width_end = width_total - self.width_begin - 1
        self.height_begin = 1
        self.height_end = height_total - self.height_begin - 1

    def set_dim(self, width, height):
        self.calculate_nonwall_field(width, height)

    def get_random_position(self):
        x = random.randint(self.width_begin, self.width_end)
        y = random.randint(self.height_begin, self.height_end)
        return Point(x, y)
