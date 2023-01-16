from game.game import Game
from time import sleep

from device.renderer import Renderer
from device.transport_server import TransportServer
from dispatcher.food_position_msg import FoodPositionMsg
from dispatcher.grid_dim_msg import GridDimensionsMsg
from dispatcher.control_msg import ControlMsg
from dispatcher.start_game_msg import StartGameMsg

from dispatcher.dispatcher import Dispatcher
from game.game_state import GameState


# this script is the main server implementation
# should be called first
if __name__ == '__main__':
    dispatcher = Dispatcher(TransportServer())
    renderer = Renderer(width=12, height=12)
    game = Game(renderer.get_canvas_dimensions())

    # add food on the message arrived at /food topic
    def food_position_callback(msg):
        if game.get_state() == GameState.RUNNING:
            game.add_food(msg.get_position())

    # listen for food messages on /food topic
    dispatcher.subscribe(msg_type=FoodPositionMsg,
                         cb=food_position_callback,
                         topic="/food")

    # listen for user control messages on /control topic
    dispatcher.subscribe(msg_type=ControlMsg,
                         cb=lambda msg: game.control(msg.get_control()),
                         topic="/control")

    # listen to game start message on /start
    # the client starts the game
    dispatcher.subscribe(msg_type=StartGameMsg, cb=lambda msg: game.start(), topic="/start")

    # main game loop
    print("[SERVER] Waiting for client to start up!")
    while True:
        # sending grid dimensions to the client until the client start the game
        if game.get_state() == GameState.IDLE:
            grid_dim_msg = GridDimensionsMsg(*renderer.get_canvas_dimensions())
            dispatcher.publish(msg=grid_dim_msg, topic="/grid_dim")
            sleep(1)
        # main game update and render loop
        elif game.get_state() == GameState.RUNNING:
            game.update()
            renderer.clear()
            for fields in game.render():
                renderer.add(fields)
            renderer.draw()
            sleep(0.5)
        # on game stop break the loop and exit
        elif game.get_state() == GameState.STOPPED:
            break

    print()
    print("[SERVER] End of game!")
    print("[SERVER] Exit with ctrl-c!")
