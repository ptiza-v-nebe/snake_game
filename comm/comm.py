import json
from .transport import Transport
from .gateway import OutgoingGateway, IncomingGateway


class Comm(IncomingGateway):
    def __init__(self, outgoing_gateway: OutgoingGateway):
        self.outgoing_gateway = outgoing_gateway

    def from_transport(self, data):
        pass

    def publish(self, msg, topic):
        msg_type = type(msg).__name__
        msg_payload = msg.serialize()
        tmp_dict = {"topic": topic, "msg_type": msg_type, "msg_payload": msg_payload}
        data = json.dumps(tmp_dict)
        self.outgoing_gateway.to_transport(data)

    def subscribe(self, cb, topic):
        pass

    # import importlib
    #
    # def class_for_name(module_name, class_name):
    #     # load the module, will raise ImportError if module cannot be loaded
    #     m = importlib.import_module(module_name)
    #     # get the class, will raise AttributeError if class cannot be found
    #     c = getattr(m, class_name)
    #     return c
