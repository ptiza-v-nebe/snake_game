import asyncio
import logging
#from signal import SIGINT, SIGTERM
import threading
from collections import deque
import time


class Server:
    def __init__(self, host, port):
        self.on_connect_callback = 0
        self.on_disconnect_callback = 0
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.main())

        server = asyncio.start_server(self.accept_client, host=host, port=port) 
        self.loop.create_task(server)

        self.bg_loop_thread = threading.Thread(target=lambda loop: loop.run_forever(), args=(self.loop,), daemon=True)
        self.bg_loop_thread.start()

    def on_connect(self, on_connect_callback):
        self.on_connect_callback = on_connect_callback

    def on_disconnect(self, on_disconnect_callback):
        self.on_disconnect_callback = on_disconnect_callback

    async def handle_client(self, network, client_reader, client_writer):
        while True:
            try:
                data = await client_reader.readline()
                network.update_buffer(data)
                if not data:
                    break
            except ConnectionError:
                self.log.warning("peer disconnected, cannot read!")
                break
            except ConnectionResetError:
                self.log.warning("peer disconnected, cannot read!")
                break
            except BrokenPipeError: 
                self.log.warning("peer disconnected, cannot read!")
                break
    
    async def accept_client(self, client_reader, client_writer):
        peername = client_reader._transport.get_extra_info('peername')
        ll_network = InetLLNetwork(self.loop, peername, client_writer)
        task = asyncio.Task(self.handle_client(ll_network, client_reader, client_writer))
        self.log.info("New Connection")

        if self.on_connect_callback != 0:
            self.on_connect_callback(peername,  ll_network)

        def client_done(task):
            del task
            if self.on_disconnect_callback != 0:
                self.on_disconnect_callback(peername)
            if not client_writer.transport.is_closing():
                client_writer.close()
            self.log.info("End Connection")
        
        task.add_done_callback(client_done)

    async def main(self):
        await asyncio.sleep(0)


networks = {}

def on_client_connect_callback(peername, ll_network: InetLLNetwork):
    global networks
    s = "welcome to server!\n".encode()
    ll_network.write(s, len(s))
    networks[peername] = ll_network

def on_client_disconnect_callback(peername):
    del networks[peername]

#sync code
if __name__ == '__main__':
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                 "[%(module)s:%(lineno)d] %(message)s")
    #setup console logging
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    ch.setFormatter(formatter)
    log.addHandler(ch)

    server = InetLLServer(host=None, port=2991)
    server.on_connect(on_client_connect_callback)
    server.on_disconnect(on_client_disconnect_callback)

    print("started server")
    while True:
        for key, item in networks.items():
            s = "hahaho\n".encode()
            item.write(s, len(s))
            if item.available():
                print(item.read())
        time.sleep(1.0)
 