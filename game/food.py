from .point import Point
from .field import Field
from .symbol import Symbol


class Food:
    def __init__(self):
        self.food = []

    def add(self, point):
        self.food.append(point)

    def remove(self, point):
        self.food.remove(point)

    def check_collision(self, head):
        for f in self.food:
            if head == f:
                return True
        return False

    def render(self):
        fields = []
        for f in self.food:
            fields.append(Field(f.x, f.y, Symbol.FOOD))
        return fields
