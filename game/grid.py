from .symbol import Symbol
from .field import Field
from .point import Point


class Grid:
    def __init__(self, width, height):
        self.game_map = []
        self.create_map(width, height)
        self.create_walls()

    def create_map(self, width, height):
        for idx in range(0, height):
            self.game_map.append([" "] * width)

    def create_walls(self):
        for idx, column in enumerate(self.game_map[0]):
            self.game_map[0][idx] = "#"
            self.game_map[len(self.game_map)-1][idx] = "#"

        for idx, row in enumerate(self.game_map):
            self.game_map[idx][0] = "#"
            self.game_map[idx][len(self.game_map[0])-1] = "#"

    def check_collision(self, point):
        if self.game_map[point.y][point.x] == "#":
            return True
        else:
            return False

    def get_move_space(self):
        points = []

        for row_idx, row_value in enumerate(self.game_map):
            for column_idx, column_value in enumerate(row_value):
                if column_value == " ":
                    points.append(Point(x=column_idx, y=row_idx))
        return points

    def render(self):
        fields = []

        for row_idx, row_value in enumerate(self.game_map):
            for column_idx, column_value in enumerate(row_value):
                if column_value == "#":
                    fields.append(Field(x=column_idx, y=row_idx, t=Symbol.WALL))

        return fields
