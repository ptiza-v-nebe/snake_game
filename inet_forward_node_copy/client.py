import asyncio
import logging
#from signal import SIGINT, SIGTERM
import threading
from collections import deque
import time
from .inet_ll_network import InetLLNetwork


import asyncio
import logging

#log= logging.getLogger(__name__)
#clients = {}  # task -> (reader, writer)

class Client:
    def __init__(self, host, port, on_connect_callback, on_disconnect_callback, is_logging=False):
        self.on_connect_callback = on_connect_callback
        self.on_disconnect_callback = on_disconnect_callback

        self.log = logging.getLogger("")
        self.log.disabled = not is_logging
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.main())
        self.loop.create_task(self.make_connection(host, port))
        
        self.bg_loop_thread = threading.Thread(target=lambda loop: loop.run_forever(), args=(self.loop,), daemon=True)
        self.bg_loop_thread.start()

        self.peernames = {}
        self.clients = {}

    # def on_connect(self, on_connect_callback):
    #     self.on_connect_callback = on_connect_callback

    # def on_disconnect(self, on_disconnect_callback):
    #     self.on_disconnect_callback = on_disconnect_callback

    async def make_connection(self, host, port):
        client_reader, client_writer = await asyncio.open_connection(host, port)

        time.sleep(1)
        print(client_reader)

        peername = client_reader._transport.get_extra_info('peername')
        print(peername)
        ll_network = InetLLNetwork(self.loop, peername, client_writer)

        task = asyncio.Task(self.handle_client(ll_network, client_reader, client_writer))

        if self.on_connect_callback != 0:
            self.on_connect_callback(peername,  ll_network)

        self.log.info("Connected to %s %d", host, port)

        self.clients[task] = (host, port)

        def client_done(task):
            print("done")
            if self.on_disconnect_callback != 0:
                self.on_disconnect_callback(peername)

            del self.clients[task]
            self.log.info("Disconnecting from %s %d", host, port)

            if not client_writer.transport.is_closing():
                client_writer.close()

            if len(self.clients) == 0:
                self.log.info("clients is empty, stopping loop.")
                self.loop.stop()

        
        task.add_done_callback(client_done)


    async def handle_client(self, network, client_reader, client_writer):
        self.log.info("handle_client")
        while True:
            try:
                #print("start loop")
                data = await client_reader.readline()
                #print(data)
                network.update_buffer(data)
                if not data:
                    #self.log.warning("Client disconnected")
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
        
    async def main(self):
        await asyncio.sleep(0)


networks = {}

def on_client_connect_callback(peername, ll_network: InetLLNetwork):
    global networks
    print("connect")
    s= "welcome!\n".encode()
    ll_network.write(s, len(s))
    networks[peername] = ll_network

def on_client_disconnect_callback(peername):
    print("disconnect")
    #remove controller from relay
    pass

def main():
    global networks

    client = InetLLClient(
        'localhost', 
        2991, 
        on_client_connect_callback, 
        on_client_disconnect_callback,
        True
    )

    time.sleep(1)

    print("size of networks ", len(networks))
    time.sleep(1)
    cnt = 0
    while True:
        #print("len networks", len(networks))
        for key, item in networks.items():
            s = b"hi from client! " + str(cnt).encode()
            item.write(s, len(s))
            if item.available():
                print(item.read())
        cnt += 1
        time.sleep(0.5)

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

    main()