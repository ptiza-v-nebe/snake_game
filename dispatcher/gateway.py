from abc import ABC, abstractmethod


class OutgoingGateway(ABC):
    @abstractmethod
    def to_transport(self, data):
        pass


class IncomingGateway(ABC):
    @abstractmethod
    def from_transport(self, data):
        pass
