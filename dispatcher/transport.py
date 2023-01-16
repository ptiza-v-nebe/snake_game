from dispatcher.gateway import OutgoingGateway, IncomingGateway


class Transport(OutgoingGateway):
    def __init__(self):
        self.incoming_gateway = 0

    def set_incoming_gateway(self, incoming_gateway):
        self.incoming_gateway: IncomingGateway = incoming_gateway

    def from_transport(self, data):
        if self.incoming_gateway != 0:
            self.incoming_gateway.from_transport(data)

    # def to_transport(self, data):
    #     raise NotImplementedError("overload to_transport in derived!")