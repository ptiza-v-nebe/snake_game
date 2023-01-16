from .msg import Msg
import json


# message that represents start of the game
class StartGameMsg(Msg):
    def __init__(self):
        pass

    def serialize(self) -> str:
        tmp_dict = {}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
