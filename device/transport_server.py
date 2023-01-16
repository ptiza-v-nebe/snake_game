from threading import Thread
import socket
from dispatcher.transport import Transport
from .connection_state import ConnectionState


class TransportServer(Transport):
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.SERVER = "127.0.0.1"
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.sock.settimeout(2)
        self.sock.bind(self.ADDR)
        self.conn_state = ConnectionState.DISCONNECTED
        self.client_addr = 0

        thread = Thread(target=self.recv_thread_callback)
        thread.start()

    def to_transport(self, data):
        if self.conn_state == ConnectionState.CONNECTED and self.client_addr != 0:
            self.send_message(data, self.client_addr)

    def send_message(self, data, client_addr):
        message = data.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.sock.sendto(send_length, client_addr)
        self.sock.sendto(message, client_addr)

    def recv_message(self):
        msg_length, address = self.sock.recvfrom(self.HEADER)
        msg_length = msg_length.decode(self.FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            frame, address = self.sock.recvfrom(msg_length)
            frame = frame.decode(self.FORMAT)
            return frame, address
        return None, None

    def recv_thread_callback(self):
        is_running = True

        while is_running:
            if self.conn_state == ConnectionState.DISCONNECTED:
                frame, address = self.recv_message()
                if frame == "!CONNECT":
                    print("[SERVER] Client connected!", frame, address)
                    self.conn_state = ConnectionState.CONNECTED
                    self.client_addr = address

            elif self.conn_state == ConnectionState.CONNECTED:
                frame, address = self.recv_message()
                if frame == "!DISCONNECT":
                    print("[SERVER] Client disconnected!", frame, address)
                    self.conn_state = ConnectionState.DISCONNECTED
                    continue
                self.from_transport(frame)
