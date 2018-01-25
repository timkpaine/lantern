import logging
import ujson
from .sources.websocket import WebSocketSource
from .base import runWS


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    def foo(ws):
        req = ujson.dumps({
            "type": "subscribe",
            "product_id": "ETH-USD"
        })
        ws.send(req)

        req = ujson.dumps({
            "type": "heartbeat",
            "on": True
        })

        ws.send(req)

    s = WebSocketSource("wss://ws-feed.gdax.com", on_open=foo)
    x = runWS(s)
    print(x)
