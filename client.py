from device.user import User
from game.control import Control

from device.transport_client import TransportClient
from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.control_msg import ControlMsg
from dispatcher.dispatcher import Dispatcher

import time, threading




if __name__ == '__main__':
    transport = TransportClient(ip="127.0.0.1")
    dispatcher = Dispatcher(transport)




    def timer_callback():
        fp_msg = FoodPositionMsg(3, 5)
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