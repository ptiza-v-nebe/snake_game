from path import Path
from grid import Grid

from snake import Snake
from point import Point
from direction import Direction
from renderer import Renderer

if __name__ == '__main__':
    snake = Snake(origin=Point(6, 6))

    snake.update()
    snake.update()
    snake.set_direction(Direction.WEST)
    snake.update()
    snake.update()
    snake.set_direction(Direction.SOUTH)
    snake.update()
    snake.update()
    snake.update()
    snake.update()

    snake_fields = snake.render()


    renderer = Renderer()
    renderer.add(snake_fields)
    renderer.add(grid_fields)
    renderer.draw()
