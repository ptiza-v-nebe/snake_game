from grid import Grid
from snake import Snake
from point import Point
from direction import Direction
from renderer import Renderer
from user import User


class GameLoop:
    def __init__(self):
        self.snake = Snake(origin=Point(6, 6))
        self.grid = Grid()
        self.renderer = Renderer()

        self.up = lambda: self.snake.set_direction(Direction.SOUTH)
        self.down = lambda: self.snake.set_direction(Direction.NORTH)
        self.right = lambda: self.snake.set_direction(Direction.EAST)
        self.left = lambda: self.snake.set_direction(Direction.WEST)

        self.user = User(self.up, self.down, self.right, self.left)
        self.user.start()

    def update(self):
        self.snake.update()
        print(self.grid.check_collision(self.snake.get_head()))

        snake_fields = self.snake.render()
        grid_fields = self.grid.render()

        self.renderer.clear()
        self.renderer.add(snake_fields)
        self.renderer.add(grid_fields)
        self.renderer.draw()

