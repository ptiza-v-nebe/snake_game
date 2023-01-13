import asyncio
import logging
from collections import deque

import logging

class InetLLNetwork:
    def __init__(self, loop, peername, writer):
        self.peername = peername
        self.incoming_buffer = deque()
        self.writer = writer
        self.loop = loop
        self.log = logging.getLogger("")

    def update_buffer(self, data: bytes):
        self.incoming_buffer.append(data)

    def write(self, data, size):
        asyncio.run_coroutine_threadsafe(self._write(data, size), self.loop)

    async def _write(self, data: bytes, size):
        tmp_data = data[0:size] + b'\n'
        self.writer.write(tmp_data)
        await self.writer.drain()

    def read(self) -> bytes:
        if self.available() > 0:
            return self.incoming_buffer.popleft()[:-1] #removes last byte (\n)
        return None

    def available(self) -> int:
        return len(self.incoming_buffer)
