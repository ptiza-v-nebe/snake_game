from .point import Point
from .field import Field
from .symbol import Symbol


# this class holds all food objects on the field
class Food:
    def __init__(self):
        self.food = []

    # add new food object at specific position
    def add(self, point):
        self.food.append(point)

    # remove specific food object
    def remove(self, point):
        self.food.remove(point)

    # check if the head is touching the food
    # useful for handling the "eat" mechanic of the snakee
    def check_collision(self, head):
        for f in self.food:
            if head == f:
                return True
        return False

    # output all food objects as field objects for rendering
    def render(self):
        fields = []
        for f in self.food:
            fields.append(Field(f.x, f.y, Symbol.FOOD))
        return fields
