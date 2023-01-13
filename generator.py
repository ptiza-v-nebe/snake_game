import random
from point import Point


class Generator:
    def __init__(self, food, move_space):
        self.move_space = move_space
        self.food = food

    def update(self):
        rpoint = self.move_space[random.randint(0, len(self.move_space)-1)]
        self.food.add(rpoint)
