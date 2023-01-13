import threading
import time
import asyncio


class Client:
    def __init__(self, host, port):
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.make_connection(host, port))
        
        self.bg_loop_thread = threading.Thread(target=lambda loop: loop.run_forever(), args=(self.loop,), daemon=True)
        self.bg_loop_thread.start()

        self.clients = {}

    async def make_connection(self, host, port):
        client_reader, client_writer = await asyncio.open_connection(host, port)
        peername = client_reader._transport.get_extra_info('peername')
        print(peername)

        task = asyncio.Task(self.handle_client(client_reader, client_writer))
        self.clients[task] = (host, port)

        def client_done(task):
            del self.clients[task]

            if len(self.clients) == 0:
                self.loop.stop()

        task.add_done_callback(client_done)

    async def handle_client(self, client_reader, client_writer):
        while True:
            data = await client_reader.readline()
            if not data:
                break

def main():
    client = Client( 'localhost', 2991)
    time.sleep(1)

if __name__ == '__main__':
    main()