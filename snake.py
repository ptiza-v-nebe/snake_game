from enum import Enum
from point import Point
from path import Path


class SnakePartType(Enum):
    HEAD = 0
    TAIL = 1


class SnakePart:
    def __init__(self):
        self.type = SnakePartType.HEAD


class Snake:
    def __init__(self, origin):
        self.origin = origin
        # self.parts = list()  # SnakePart
        self.path = Path()

        # initial snake
        self.path.append_tail(Point(0, 0))
        self.path.append_tail(Point(1, 0))
        self.path.append_tail(Point(1, 1))
        self.path.append_tail(Point(1, 2))
        self.path.append_tail(Point(2, 2))

    def get_waypoints(self):
        waypoints = []
        for waypoint in self.path.get_waypoints():
            waypoints.append(self.origin + waypoint)
        return waypoints

    def update(self):
        self.path.update()

    def set_direction(self, direction):
        self.path.set_direction(direction)



