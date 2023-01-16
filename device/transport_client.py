import socket
from dispatcher.transport import Transport
from .connection_state import ConnectionState
from threading import Thread
from time import sleep


# TransportClient represent the general UDP client part of the application
# should be started after TransportServer has started
class TransportClient(Transport):
    def __init__(self, ip="127.0.0.1"):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = ip
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect(self.ADDR)
        self.conn_state = ConnectionState.DISCONNECTED
        thread = Thread(target=self.recv_thread_callback)
        thread.start()
        sleep(0.05)
        self.connect()

    # send a !CONNECT to server before sending anything else
    def connect(self):
        if self.conn_state == ConnectionState.DISCONNECTED:
            self.conn_state = ConnectionState.CONNECTED
            data = "!CONNECT"
            self.send_message(data)

    # at the end of comm send a !DISCONNECT
    def disconnect(self):
        if self.conn_state == ConnectionState.CONNECTED:
            self.conn_state = ConnectionState.DISCONNECTED
            data = "!DISCONNECT"
            self.send_message(data)

    # if a client application wants to send some data call this method
    def to_transport(self, data):
        if self.conn_state == ConnectionState.CONNECTED:
            self.send_message(data)

    # sending one message with following protocol
    # [MSG_LEN][PAYLOAD]
    def send_message(self, data):
        message = data.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.sock.send(send_length)
        self.sock.send(message)

    # receiving one message with following protocol
    # [MSG_LEN][PAYLOAD]
    def recv_message(self):
        msg_length, address = self.sock.recvfrom(self.HEADER)
        msg_length = msg_length.decode(self.FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            frame, address = self.sock.recvfrom(msg_length)
            frame = frame.decode(self.FORMAT)
            return frame, address
        return None

    # receiver thread
    def recv_thread_callback(self):
        is_running = True

        while is_running:
            frame, address = self.recv_message()
            self.from_transport(frame)
