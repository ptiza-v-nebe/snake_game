from threading import Thread
import socket
from .transport import Transport


class TransportServer(Transport):
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def to_transport(self, data):
        pass

    def start(self):
        self.sock.bind(self.ADDR)
        self.sock.listen()
        while True:
            conn, addr = self.sock.accept()
            thread = Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn):
        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                self.incoming_gateway.from_transport(msg)
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False

        conn.close()


class TransportClient:
    def __init__(self):
        pass

    def send(self, buf):
        print(buf)

