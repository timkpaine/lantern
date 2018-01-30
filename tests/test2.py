#!/usr/bin/env python
import asyncio
import websockets
import sys


async def hello():
    print(sys.argv[1])
    async with websockets.connect(sys.argv[1]) as websocket:
        while True:
            greeting = await websocket.recv()
            print("{}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
