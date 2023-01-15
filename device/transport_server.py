from threading import Thread
import socket
from dispatcher.transport import Transport


class TransportServer(Transport):
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = "127.0.0.1"
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.ADDR)

        thread = Thread(target=self.recv_thread_callback)
        thread.start()

    def to_transport(self, data):
        pass

    def recv_thread_callback(self):
        connected = True
        while connected:
            msg_length, address = self.sock.recvfrom(self.HEADER)
            if msg_length:
                msg_length = int(msg_length)
                msg_frame, address = self.sock.recvfrom(msg_length)
                self.from_transport(msg_frame)
                if msg_frame == self.DISCONNECT_MESSAGE:
                    connected = False
