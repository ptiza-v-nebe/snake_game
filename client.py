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

# this script is the main client implementation
# requires on mac accesibility configuration in
# settings and also privacy tab
# client.py should be run after the server.py

if __name__ == '__main__':
    print("[CLIENT] Starting client")
    transport = TransportClient(ip="127.0.0.1")
    dispatcher = Dispatcher(transport)
    generator = Generator()

    # will be called on a publish to /grid_dim
    def grid_dim_callback(msg):
        print("[CLIENT] Got grid dimensions from server!")
        width, heigt = msg.get_size()
        generator.set_dim(width, heigt)
        dispatcher.publish(msg=StartGameMsg(), topic="/start")
    dispatcher.subscribe(msg_type=GridDimensionsMsg, cb=grid_dim_callback, topic="/grid_dim")

    # timer for generating and sending food position
    # to the server
    def timer_callback():
        point = generator.get_random_position()
        fp_msg = FoodPositionMsg(point.x, point.y)
        dispatcher.publish(msg=fp_msg, topic="/food")
        threading.Timer(5, timer_callback).start()
    timer_callback()

    # configuration of user controls
    user = User()
    up = lambda: dispatcher.publish(msg=ControlMsg(Control.UP), topic="/control")
    down = lambda: dispatcher.publish(msg=ControlMsg(Control.DOWN), topic="/control")
    right = lambda: dispatcher.publish(msg=ControlMsg(Control.RIGHT), topic="/control")
    left = lambda: dispatcher.publish(msg=ControlMsg(Control.LEFT), topic="/control")

    user.set_callbacks(up, down, right, left)
    user.start()
    print("[CLIENT] Use following key for controlling the snake:")
    print("[CLIENT] W for UP, S for DOWN, A for LEFT, D for RIGHT movements")
    print("[CLIENT] Exit with ctrl-c!")

    # infinite loop to let the program run its threads
    while True:
        pass
