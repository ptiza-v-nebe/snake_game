import json
from .gateway import OutgoingGateway, IncomingGateway


class Dispatcher(IncomingGateway):
    def __init__(self, outgoing_gateway: OutgoingGateway):
        self.outgoing_gateway = outgoing_gateway
        self.callbacks = {}

    def from_transport(self, data):
        tmp_dict = json.loads(data)
        topic = tmp_dict["topic"]
        msg_type = tmp_dict["msg_type"]
        msg_json = json.loads(tmp_dict["msg_payload"])
        self.callbacks[topic](msg_type, msg_json)

    def publish(self, msg, topic):
        msg_type = type(msg).__name__
        msg_payload = msg.serialize()
        tmp_dict = {"topic": topic, "msg_type": msg_type, "msg_payload": msg_payload}
        data = json.dumps(tmp_dict)
        self.outgoing_gateway.to_transport(data)

    def subscribe(self, msg_type, cb, topic):
        def subscribe_callback(incoming_msg_type, msg_json):
            msg = msg_type()
            if incoming_msg_type == type(msg).__name__:
                msg.deserialize(msg_json)
                cb(msg)

        self.callbacks[topic] = subscribe_callback


