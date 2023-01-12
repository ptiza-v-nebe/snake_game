from path import Path
from grid import Grid

from snake import Snake
from point import Point
from direction import Direction

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

    fields = snake.render()

    grid = Grid()
    grid.add(fields)
    grid.draw()
    pass
