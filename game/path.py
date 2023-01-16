from .point import Point
from collections import deque
from .direction import Direction
import itertools


# Path class represents the core of the snake move engine
class Path:
    def __init__(self):
        self.waypoints = deque()
        self.direction = Direction.NORTH
        self.last_tail = 0

    # append a point before head of the snake
    def append_head(self, point):
        return self.waypoints.appendleft(point)

    # append a point after the tail of the snake
    def append_tail(self, point):
        self.last_tail = point  # TODO: overlapping tails could happen, CHECK!
        return self.waypoints.append(point)

    # remove head of the snake and return it
    def pop_head(self):
        return self.waypoints.popleft()

    # remove the tail of the snake and return it
    def pop_tail(self):
        return self.waypoints.pop()

    # return head of snake without removing
    def peek_head(self):
        return self.waypoints[0]

    # return all tail points without removing them
    def peek_body(self):
        return list(itertools.islice(self.waypoints, 1, len(self.waypoints)))

    # return tail of snake without removing
    def peek_tail(self):
        return self.waypoints[-1]

    # check if last saved direction is opposite to the given direction
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

    # set moving direction
    # useful for defining with external systems the moving vector
    def set_direction(self, direction):
        # check if we are not trying to reverse into our self
        if not self.is_opposite(direction):
            self.direction = direction

    # calculte next head position given direction
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

    # taking last point of path and add him to the beginning of path in the direction of heading
    def update(self):

        self.last_tail = self.pop_tail()
        actual_head = self.peek_head()
        new_head = self.calc_head(actual_head, self.direction)
        self.append_head(new_head)

    # generate another head infront of the actual head and return it
    # useful for collision checker for walls and body
    def peek_phantom_head(self):
        actual_head = self.peek_head()
        phantom_head = self.calc_head(actual_head, self.direction)
        return phantom_head

    # check if the snake has collision with its own body
    def check_self_collision(self):
        # has head and body same point?
        for body in self.peek_body():
            if self.peek_phantom_head() == body:
                return True
        return False

    # get all working waypoints
    # in local coordinates
    def get_waypoints(self):
        return self.waypoints

    # get last saved tail
    def get_last_tail(self):
        return self.last_tail
