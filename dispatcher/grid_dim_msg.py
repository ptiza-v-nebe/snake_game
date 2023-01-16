from .msg import Msg
import json


class GridDimensionsMsg(Msg):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_size(self):
        return self.width, self.height

    def serialize(self) -> str:
        tmp_dict = {"width": self.width, "height": self.height}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.width = tmp_dict["width"]
        self.height = tmp_dict["height"]
