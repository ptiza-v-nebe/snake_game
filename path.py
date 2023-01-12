from point import Point
from collections import deque
from direction import Direction
from copy import deepcopy


class Path:
    def __init__(self):
        self.waypoints = deque()
        self.direction = Direction.NORTH

    def append_head(self, point):
        return self.waypoints.appendleft(point)

    def append_tail(self, point):
        return self.waypoints.append(point)

    def pop_head(self):
        return self.waypoints.popleft()

    def pop_tail(self):
        return self.waypoints.pop()

    def peek_head(self):
        return self.waypoints[0]

    def peek_tail(self):
        return self.waypoints[-1]

    def set_direction(self, direction):
        # TODO: checking if direction is allowed
        self.direction = direction

    @staticmethod
    def calc_head(actual_head, direction):
        if direction == Direction.NORTH:
            new_head = actual_head + Point(0, 1)

        elif direction == Direction.EAST:
            new_head = actual_head + Point(1, 0)

        elif direction == Direction.SOUTH:
            new_head = actual_head + Point(0, -1)

        elif direction == Direction.WEST:
            new_head = actual_head + Point(-1, 0)

        return new_head

    # @staticmethod
    # def correct_zero(waypoints):
    #     head = deepcopy(waypoints[0])
    #     for idx in range(0, len(waypoints)):
    #         waypoints[idx].x += -head.x
    #         waypoints[idx].y += -head.y

    def update(self):
        # taking last point of path and add him to the beginning of path in the direction of heading
        self.pop_tail()
        actual_head = self.peek_head()
        new_head = self.calc_head(actual_head, self.direction)
        self.append_head(new_head)

    def get_waypoints(self):
        return self.waypoints
