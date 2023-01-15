
from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.user import User
from game.control import Control

from comm.transport import Transport


class TestTransport(Transport):
    def to_transport(self, data):
        self.from_transport(data)


from comm.food_position_msg import FoodPositionMsg
from comm.dispatcher import Dispatcher


if __name__ == '__main__':
    transport = TestTransport()
    dispatcher = Dispatcher(transport)

    dispatcher.subscribe(msg_type=FoodPositionMsg,
                         cb=lambda msg: print("in user callback: ", msg.x, msg.y),
                         topic="/food")

    fp = FoodPositionMsg(3, 5)
    dispatcher.publish(msg=fp, topic="/food")

    # # the game
    # renderer = Renderer(width=20, height=20)
    #
    # game = Game(renderer.get_canvas_dimensions())
    # user = User()
    #
    # up = lambda: game.control(Control.UP)
    # down = lambda: game.control(Control.DOWN)
    # right = lambda: game.control(Control.RIGHT)
    # left = lambda: game.control(Control.LEFT)
    #
    # user.set_callbacks(up, down, right, left)
    # user.start()
    #
    # while game.is_running():
    #     game.update()
    #     renderer.clear()
    #     for fields in game.render():
    #         renderer.add(fields)
    #     renderer.draw()
    #     sleep(0.5)
    #
    # print("end of game!")
