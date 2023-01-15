
from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.user import User
from game.control import Control

from device.transport_server import TransportServer


# from comm.transport import Transport
# class TestTransport(Transport):
#     def to_transport(self, data):
#         self.from_transport(data)


from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.dispatcher import Dispatcher


if __name__ == '__main__':
    dispatcher = Dispatcher(TransportServer())

    dispatcher.subscribe(msg_type=FoodPositionMsg,
                         cb=lambda msg: print("in user callback: ", msg.x, msg.y),
                         topic="/food")



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
    print("end of game!")
