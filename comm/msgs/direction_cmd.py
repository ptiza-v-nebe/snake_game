from msg import Msg
from game.direction import Direction

from dataclasses import dataclass
import json


@dataclass
class DirectionCmd(Msg):
    dir: Direction

    def serialize(self) -> str:
        tmp_dict = {"dir": self.dir}
        return json.dumps(tmp_dict)

    def deserialize(self, buf) -> None:
        tmp_dict = json.loads(buf)
        self.dir = tmp_dict["dir"]
