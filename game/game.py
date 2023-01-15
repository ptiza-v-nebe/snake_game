from .grid import Grid
from .snake import Snake
from .point import Point
from .direction import Direction
from .renderer import Renderer
from .user import User
from .food import Food
from .generator import Generator
from .control import Control


class Game:
    def __init__(self):
        self.width = 12
        self.height = 12

        self.renderer = Renderer(self.width, self.height)

        self.snake = Snake(origin=Point(6, 6))
        self.food = Food()

        self.grid = Grid(*self.renderer.get_canvas_dimensions())
        self.gen = Generator(self.food, self.grid.get_move_space())

        self._is_running = True

    def control(self, control: Control):
        if control == Control.UP:
            self.snake.set_direction(Direction.SOUTH)
        elif control == Control.DOWN:
            self.snake.set_direction(Direction.NORTH)
        elif control == Control.RIGHT:
            self.snake.set_direction(Direction.EAST)
        elif control == Control.LEFT:
            self.snake.set_direction(Direction.WEST)

    def stop(self):
        self._is_running = False

    def is_running(self):
        return self._is_running

    def add_food(self, point):
        self.food.add(point)

    def update(self):
        self.gen.random_add()

        # check for upcoming collision
        phantom_head = self.snake.get_phantom_head()
        is_grid_collision = self.grid.check_collision(phantom_head)
        is_self_collision = self.snake.check_self_collision()

        if is_grid_collision or is_self_collision:
            self.stop()
            return
        else:
            self.snake.update()

        if self.snake.check_self_collision():
            self.stop()

        if self.food.check_collision(self.snake.get_head()):
            self.snake.grow()
            self.food.remove(self.snake.get_head())

        # draw
        grid_fields = self.grid.render()
        food_fields = self.food.render()
        snake_fields = self.snake.render()

        self.renderer.clear()
        self.renderer.add(grid_fields)
        self.renderer.add(food_fields)
        self.renderer.add(snake_fields)
        self.renderer.draw()
