from .websocket import WebSocket
from .base import run


if __name__ == '__main__':
    s = WebSocket("wss://ws-feed.gdax.com")
    run(s)
