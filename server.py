from comm.gateway import OutgoingGateway, IncomingGateway
from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.user import User
from game.control import Control


class TestTransport(OutgoingGateway):
    def __init__(self):
        self.incoming_gateway = 0

    def set_incoming_gateway(self, incoming_gateway):
        self.incoming_gateway: IncomingGateway = incoming_gateway

    def to_transport(self, data):
        print("in transport: ", data)
        if self.incoming_gateway != 0:
            self.incoming_gateway.from_transport(data)


if __name__ == '__main__':
    # transport = TestTransport()
    # dispatcher = Dispatcher(transport)
    # transport.set_incoming_gateway(dispatcher)
    #
    # dispatcher.subscribe(msg_type=FoodPositionMsg,
    #                      cb=lambda msg: print("in user callback: ", msg.x, msg.y),
    #                      topic="/food")
    #
    # fp = FoodPositionMsg(3, 5)
    # dispatcher.publish(msg=fp, topic="/food")

    renderer = Renderer(width=20, height=20)

    game = Game(renderer.get_canvas_dimensions())
    user = User()

    up = lambda: game.control(Control.UP)
    down = lambda: game.control(Control.DOWN)
    right = lambda: game.control(Control.RIGHT)
    left = lambda: game.control(Control.LEFT)

    user.set_callbacks(up, down, right, left)
    user.start()

    while game.is_running():
        game.update()
        renderer.clear()
        for fields in game.render():
            renderer.add(fields)
        renderer.draw()
        sleep(0.5)

    print("end of game!")
