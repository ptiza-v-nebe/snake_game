from game_loop import GameLoop
from time import sleep

if __name__ == '__main__':
    loop = GameLoop()

    while True:
        loop.update()
        sleep(0.5)
