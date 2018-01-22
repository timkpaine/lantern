# import logging

from .websocket import WebSocket
from .base import run


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    s = WebSocket("wss://ws-feed.gdax.com")
    x = run(s)
    print(x)
