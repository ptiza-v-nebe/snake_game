from game.loop import Loop
from time import sleep
from comm.msgs.food_position import FoodPosition
from comm import Comm
from comm.transport import TransportServer

if __name__ == '__main__':
    transport = TransportServer(port=5050)

    comm = Comm(transport)
    fp = FoodPosition(3, 5)

    comm.publish(msg=fp, topic="/food")
    comm.subscribe(cb=lambda msg: print(msg.x, msg.y), topic="/food")

    comm.update()


    # loop = Loop()
    #
    # while loop.is_running():
    #     loop.update()
    #     sleep(0.5)

    print("end of game!")
