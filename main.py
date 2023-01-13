from game_loop import GameLoop
from time import sleep

if __name__ == '__main__':
    loop = GameLoop()

    while loop.is_running():
        loop.update()
        sleep(0.5)

    print("end of game!")
