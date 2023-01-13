from grid import Grid
from snake import Snake
from point import Point
from direction import Direction
from renderer import Renderer
from user import User
from time import sleep


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
        self._is_running = True

    def stop(self):
        self._is_running = False

    def is_running(self):
        return self._is_running

    def update(self):
        # move snake
        self.snake.update()

        # check if we have hit a wall or our self
        if self.grid.check_collision(self.snake.get_head()):
            self.stop()

        if self.snake.check_self_collision():
            self.stop()

        # draw
        snake_fields = self.snake.render()
        grid_fields = self.grid.render()
        self.renderer.clear()
        self.renderer.add(snake_fields)
        self.renderer.add(grid_fields)
        self.renderer.draw()

