from dispatcher.gateway import OutgoingGateway, IncomingGateway


# Transport is an abstract class to be used
# as interface for actual transport implementations
class Transport(OutgoingGateway):
    def __init__(self):
        self.incoming_gateway = 0

    # incoming gateway setup
    def set_incoming_gateway(self, incoming_gateway):
        self.incoming_gateway: IncomingGateway = incoming_gateway

    # calling user application class if some data arrived
    def from_transport(self, data):
        if self.incoming_gateway != 0:
            self.incoming_gateway.from_transport(data)
