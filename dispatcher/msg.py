from abc import ABC, abstractmethod


class Msg(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

    @abstractmethod
    def deserialize(self, buf) -> None:
        pass
