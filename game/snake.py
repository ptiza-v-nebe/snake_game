from enum import Enum
from .point import Point
from .path import Path
from .field import Field
from .symbol import Symbol


# body parts type enum
class BodyType(Enum):
    HEAD = 0
    TAIL = 1


# the main snake class
# this class handles the interaction with the environment
class Snake:
    def __init__(self, origin):
        self.origin = origin
        self.path = Path()

        # building initial snake
        self.path.append_tail(Point(0, 0))
        self.path.append_tail(Point(1, 0))
        self.path.append_tail(Point(1, 1))

        # set initial parts of the snake
        self.body = [BodyType.HEAD, BodyType.TAIL, BodyType.TAIL]
        self.length = len(self.body)

    # get all waypoints in global coordinates
    def get_waypoints(self):
        waypoints = []
        for waypoint in self.path.get_waypoints():
            waypoints.append(self.origin + waypoint)
        return waypoints

    # convert body repr into symbol repr
    @staticmethod
    def body2symbol(body):
        symbol = 0
        if body == BodyType.TAIL:
            symbol = Symbol.TAIL
        elif body == BodyType.HEAD:
            symbol = Symbol.HEAD
        return symbol

    # assembles the snake with their waypoints and bodyparts as Field objects
    def render(self):
        fields = []
        for idx, waypoint in enumerate(self.get_waypoints()):
            fields.append(Field(waypoint.x, waypoint.y, Snake.body2symbol(self.body[idx])))
        return fields

    # get absolute head position
    def get_head(self):
        return self.origin + self.path.peek_head()

    # get absolute phantom head position
    def get_phantom_head(self):
        return self.origin + self.path.peek_phantom_head()

    # update snake mechanism
    def update(self):
        self.path.update()

    # set move direction of snake
    def set_direction(self, direction):
        self.path.set_direction(direction)

    # check if snake has a self collision of head with body
    def check_self_collision(self):
        return self.path.check_self_collision()

    # add a new tail body part
    def grow(self):
        last_tail = self.path.get_last_tail()
        self.path.append_tail(last_tail)
        self.body.append(BodyType.TAIL)



