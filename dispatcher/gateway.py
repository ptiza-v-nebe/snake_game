from abc import ABC, abstractmethod


# represents incoming and outgoing gateways to
# be derived from and implemented in user application

class OutgoingGateway(ABC):
    @abstractmethod
    def to_transport(self, data):
        pass


class IncomingGateway(ABC):
    @abstractmethod
    def from_transport(self, data):
        pass
