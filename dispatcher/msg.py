from abc import ABC, abstractmethod


# general message to be derived from
class Msg(ABC):
    # serialize the object structure
    @abstractmethod
    def serialize(self) -> str:
        pass

    # deserialize the object structure
    @abstractmethod
    def deserialize(self, buf) -> None:
        pass
