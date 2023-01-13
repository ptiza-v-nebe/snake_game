from symbol import Symbol
from field import Field
from point import Point


class Grid:
    def __init__(self):
        self.game_map = [["#", "#", "#", "#", "#", "0", "#", "#", "#", "#", "#", "#"],
                         ["#", " ", " ", " ", "#", "0", "#", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

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
