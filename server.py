
from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.user import User
from game.control import Control

from device.transport_server import TransportServer

from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.control_msg import ControlMsg

from dispatcher.dispatcher import Dispatcher


# from comm.transport import Transport
# class TestTransport(Transport):
#     def to_transport(self, data):
#         self.from_transport(data)





if __name__ == '__main__':
    dispatcher = Dispatcher(TransportServer())
    renderer = Renderer(width=20, height=20)
    game = Game(renderer.get_canvas_dimensions())

    dispatcher.subscribe(msg_type=FoodPositionMsg,
                         cb=lambda msg: game.add_food(msg.get_position()),
                         topic="/food")

    dispatcher.subscribe(msg_type=ControlMsg,
                         cb=lambda msg: game.control(msg.get_control()),
                         topic="/control")

    while game.is_running():
        game.update()
        renderer.clear()
        for fields in game.render():
            renderer.add(fields)
        renderer.draw()
        sleep(0.5)

    print("end of game!")
