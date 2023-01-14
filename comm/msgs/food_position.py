from .msg import Msg

from dataclasses import dataclass
import json


@dataclass
class FoodPosition(Msg):
    x: int
    y: int

    def serialize(self) -> str:
        tmp_dict = {"x": self.x, "y": self.y}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.x = tmp_dict["x"]
        self.y = tmp_dict["y"]
