from .grid import Grid
from .snake import Snake
from .point import Point
from .direction import Direction

from .food import Food
from .generator import Generator
from .control import Control
from .game_state import GameState


class Game:
    def __init__(self, dimensions):
        self.snake = Snake(origin=Point(6, 6))
        self.food = Food()

        self.grid = Grid(*dimensions)
        #self.gen = Generator(self.food, self.grid.get_move_space())

        self._is_running = True
        self.state = GameState.IDLE

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
        self.state = GameState.STOPPED

    def start(self):
        self.state = GameState.RUNNING

    def get_state(self):
        return self.state

    def add_food(self, point):
        self.food.add(point)

    def update(self):
        # self.gen.random_add()

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

    def render(self):
        grid_fields = self.grid.render()
        food_fields = self.food.render()
        snake_fields = self.snake.render()

        return grid_fields, food_fields, snake_fields
