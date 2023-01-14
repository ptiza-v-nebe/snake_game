import random
from .point import Point


class Generator:
    def __init__(self, food, move_space):
        self.move_space = move_space
        self.food = food

    def random_add(self):
        rpoint = self.move_space[random.randint(0, len(self.move_space)-1)]
        self.food.add(rpoint)

    def add(self, point):
        self.food.add(point)
