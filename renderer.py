import sys
import os


class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.canvas = []
        self.create_canvas(width, height)

    def get_canvas_dimensions(self):
        return self.width, self.height

    def create_canvas(self, width, height):
        for idx in range(0, height):
            self.canvas.append([" "] * width)

    def draw(self):
        for line in self.canvas:
            for field in line:
                sys.stdout.write(field + "  ")
            print()

    def add(self, fields):
        for field in fields:
            self.canvas[field.y][field.x] = field.t.value

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row_idx, row_value in enumerate(self.canvas):
            for column_idx, column_value in enumerate(row_value):
                self.canvas[row_idx][column_idx] = " "

