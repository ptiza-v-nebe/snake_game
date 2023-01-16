from device.user import User
from game.control import Control

from device.transport_client import TransportClient
from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.control_msg import ControlMsg
from dispatcher.grid_dim_msg import GridDimensionsMsg
from dispatcher.start_game_msg import StartGameMsg

from dispatcher.dispatcher import Dispatcher
from game.generator import Generator

import threading

if __name__ == '__main__':
    transport = TransportClient(ip="127.0.0.1")
    dispatcher = Dispatcher(transport)
    generator = Generator()

    def grid_dim_callback(msg):
        print("Got grid dimensions from server!")
        width, heigt = msg.get_size()
        generator.set_dim(width, heigt)
        dispatcher.publish(msg=StartGameMsg(), topic="/start")
    dispatcher.subscribe(msg_type=GridDimensionsMsg, cb=grid_dim_callback, topic="/grid_dim")

    def timer_callback():
        point = generator.get_random_position()
        fp_msg = FoodPositionMsg(point.x, point.y)
        dispatcher.publish(msg=fp_msg, topic="/food")
        threading.Timer(5, timer_callback).start()
    timer_callback()

    user = User()
    up = lambda: dispatcher.publish(msg=ControlMsg(Control.UP), topic="/control")
    down = lambda: dispatcher.publish(msg=ControlMsg(Control.DOWN), topic="/control")
    right = lambda: dispatcher.publish(msg=ControlMsg(Control.RIGHT), topic="/control")
    left = lambda: dispatcher.publish(msg=ControlMsg(Control.LEFT), topic="/control")

    user.set_callbacks(up, down, right, left)
    user.start()

    while True:
        pass
