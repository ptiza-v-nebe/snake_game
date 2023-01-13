import asyncio
import threading
import time


class Server:
    def __init__(self, host, port):
        self.loop = asyncio.new_event_loop()
        server = asyncio.start_server(self.accept_client, host=host, port=port) 
        self.loop.create_task(server)

        self.bg_loop_thread = threading.Thread(target=lambda loop: loop.run_forever(), args=(self.loop,), daemon=True)
        self.bg_loop_thread.start()

    async def handle_client(self, client_reader, client_writer):
        while True:
            data = await client_reader.readline()
            if not data:
                break
    
    async def accept_client(self, client_reader, client_writer):
        peername = client_reader._transport.get_extra_info('peername')
        print("connected: ", peername)
        task = asyncio.Task(self.handle_client(client_reader, client_writer))

        def client_done(_task):
            del task
        task.add_done_callback(client_done)


if __name__ == '__main__':
    server = Server(host=None, port=2991)

    print("started server")
    while True:
        time.sleep(1.0)
 