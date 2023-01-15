from .msg import Msg
from game.direction import Direction
import json


class DirectionMsg(Msg):
    def __init__(self, direction=Direction.NORTH):
        self.direction: Direction = direction

    def serialize(self) -> str:
        tmp_dict = {"direction": self.direction}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.direction = tmp_dict["direction"]
