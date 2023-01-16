from .msg import Msg
import json
from game.point import Point


# message that represents position of the food object
class FoodPositionMsg(Msg):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_position(self):
        return Point(self.x, self.y)

    def serialize(self) -> str:
        tmp_dict = {"x": self.x, "y": self.y}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.x = tmp_dict["x"]
        self.y = tmp_dict["y"]
