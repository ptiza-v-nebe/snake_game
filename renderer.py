import sys


class Renderer:
    def __init__(self):
        self.grid = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                     [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

    def draw(self):
        for line in self.grid:
            for field in line:
                sys.stdout.write(field + "  ")
            print()

    def add(self, fields):
        for field in fields:
            self.grid[field.y][field.x] = field.t.value

    def clear(self):
        for row_idx, row_value in enumerate(self.grid):
            for column_idx, column_value in enumerate(row_value):
                self.grid[row_idx][column_idx] = " "

