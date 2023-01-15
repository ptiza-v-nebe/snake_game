from .msg import Msg
import json


class FoodPositionMsg(Msg):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def serialize(self) -> str:
        tmp_dict = {"x": self.x, "y": self.y}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.x = tmp_dict["x"]
        self.y = tmp_dict["y"]
