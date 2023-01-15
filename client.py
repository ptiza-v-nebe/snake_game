
from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.user import User
from game.control import Control

from device.transport_client import TransportClient


from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.dispatcher import Dispatcher


if __name__ == '__main__':
    transport = TransportClient(ip="127.0.0.1")
    dispatcher = Dispatcher(transport)

    fp = FoodPositionMsg(3, 5)
    dispatcher.publish(msg=fp, topic="/food")
