from path import Path
from grid import Grid
from field import Field
from symbol import Symbol
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

    waypoints = snake.get_waypoints()

    fields = []
    for waypoint in waypoints:
        print(waypoint.x, waypoint.y)
        fields.append(Field(waypoint.x, waypoint.y, Symbol.PATH))

    print()

    grid = Grid()
    grid.add(fields)
    grid.draw()
    pass
