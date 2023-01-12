from symbol import Symbol
from field import Field

game_map = [["#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
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


class Grid:
    def __init__(self):
        pass

    @staticmethod
    def check_collision(point):
        if game_map[point.y][point.x] == "#":
            return True
        else:
            return False

    @staticmethod
    def render():
        fields = []

        for row_idx, row_value in enumerate(game_map):
            for column_idx, column_value in enumerate(row_value):
                if column_value == "#":
                    fields.append(Field(x=column_idx, y=row_idx, t=Symbol.WALL))

        return fields
