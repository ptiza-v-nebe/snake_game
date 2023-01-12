from enum import Enum
from point import Point
from path import Path
from field import Field
from symbol import Symbol


class BodyType(Enum):
    HEAD = 0
    TAIL = 1


class Snake:
    def __init__(self, origin):
        self.origin = origin
        self.path = Path()

        # initial snake
        self.path.append_tail(Point(0, 0))
        self.path.append_tail(Point(1, 0))
        self.path.append_tail(Point(1, 1))
        self.path.append_tail(Point(1, 2))
        self.path.append_tail(Point(2, 2))

        self.body = [BodyType.HEAD, BodyType.TAIL, BodyType.TAIL, BodyType.TAIL, BodyType.TAIL, BodyType.TAIL]
        self.length = len(self.body)

    def get_waypoints(self):
        waypoints = []
        for waypoint in self.path.get_waypoints():
            waypoints.append(self.origin + waypoint)
        return waypoints

    @staticmethod
    def body2symbol(body):
        symbol = 0
        if body == BodyType.TAIL:
            symbol = Symbol.TAIL
        elif body == BodyType.HEAD:
            symbol = Symbol.HEAD
        return symbol

    def render(self):
        fields = []
        for idx, waypoint in enumerate(self.get_waypoints()):
            fields.append(Field(waypoint.x, waypoint.y, Snake.body2symbol(self.body[idx])))
        return fields

    def update(self):
        self.path.update()

    def set_direction(self, direction):
        self.path.set_direction(direction)



