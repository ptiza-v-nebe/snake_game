from point import Point
from collections import deque
from direction import Direction
import itertools

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

    def peek_body(self):
        return list(itertools.islice(self.waypoints, 1, len(self.waypoints)))

    def peek_tail(self):
        return self.waypoints[-1]

    def is_opposite(self, direction):
        if self.direction == Direction.NORTH and direction == Direction.SOUTH:
            return True
        elif self.direction == Direction.SOUTH and direction == Direction.NORTH:
            return True
        elif self.direction == Direction.WEST and direction == Direction.EAST:
            return True
        elif self.direction == Direction.EAST and direction == Direction.WEST:
            return True
        return False

    def set_direction(self, direction):
        # check if we are not trying to reverse into our self
        if not self.is_opposite(direction):
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

    def update(self):
        # taking last point of path and add him to the beginning of path in the direction of heading
        self.pop_tail()
        actual_head = self.peek_head()
        new_head = self.calc_head(actual_head, self.direction)
        self.append_head(new_head)

    def peek_phantom_head(self):
        actual_head = self.peek_head()
        phantom_head = self.calc_head(actual_head, self.direction)
        return phantom_head

    def check_self_collision(self):
        # has head and body same point?
        for body in self.peek_body():
            if self.peek_head() == body:
                return True
        return False

    def get_waypoints(self):
        return self.waypoints
