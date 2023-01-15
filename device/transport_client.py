import socket
from dispatcher.transport import Transport


class TransportClient(Transport):
    def __init__(self, ip="127.0.0.1"):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = ip
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect(self.ADDR)
        # self.from_transport()

    def to_transport(self, data):
        message = data.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.sock.send(send_length)
        self.sock.send(message)
