from grid import Grid
from snake import Snake
from point import Point
from direction import Direction
from renderer import Renderer


class GameLoop:
    def __init__(self):
        self.snake = Snake(origin=Point(6, 6))
        self.grid = Grid()
        self.renderer = Renderer()

    def update(self):
        self.snake.update()
        print(self.grid.check_collision(self.snake.get_head()))

        snake_fields = self.snake.render()
        grid_fields = self.grid.render()

        self.renderer.clear()
        self.renderer.add(snake_fields)
        self.renderer.add(grid_fields)
        self.renderer.draw()
