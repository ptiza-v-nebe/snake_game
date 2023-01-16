from .msg import Msg
from game.control import Control
import json


# message that represents user controlling of the snake
class ControlMsg(Msg):
    def __init__(self, control=Control.UP):
        self.control: Control = control

    def get_control(self):
        return self.control

    def serialize(self) -> str:
        tmp_dict = {"control": self.control}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.control = tmp_dict["control"]
