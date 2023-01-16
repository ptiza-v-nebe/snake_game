import json
from .gateway import OutgoingGateway, IncomingGateway


# Dispatcher class implements a basic publisher subscriber pattern.
# It can publish on topics and subscribe from it.
# On subscribe it calls the user specified callback with specific
# message
class Dispatcher(IncomingGateway):
    def __init__(self, transport):
        transport.set_incoming_gateway(self)
        self.outgoing_gateway = transport
        self.callbacks = {}

    # if new message arrives on transport it should call
    # a specified callback for a topic
    def from_transport(self, data):
        tmp_dict = json.loads(data)
        topic = tmp_dict["topic"]
        msg_type = tmp_dict["msg_type"]
        msg_json = tmp_dict["msg_payload"]
        if topic in self.callbacks.keys():
            self.callbacks[topic](msg_type, msg_json)

    # on a publish prepare the frame and send it to transport
    def publish(self, msg, topic):
        msg_type = type(msg).__name__
        msg_payload = msg.serialize()
        tmp_dict = {"topic": topic, "msg_type": msg_type, "msg_payload": msg_payload}
        data = json.dumps(tmp_dict)
        self.outgoing_gateway.to_transport(data)

    # on subscribe wrap the callback in another function
    # for handling the deserialization prior the actual
    # callback calling
    # checks if the specified msg_type is same as the one
    # that has arrived
    def subscribe(self, msg_type, cb, topic):
        def subscribe_callback(incoming_msg_type, msg_json):
            msg = msg_type()
            if incoming_msg_type == type(msg).__name__:
                msg.deserialize(msg_json)
                cb(msg)

        self.callbacks[topic] = subscribe_callback


