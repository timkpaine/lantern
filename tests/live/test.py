# import logging
import ujson
from .sources.websocket import WebSocket
from .base import run


if __name__ == '__main__':
    # loggingt st.basicConfig(level=logging.INFO)
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

    s = WebSocket("wss://ws-feed.gdax.com", on_open=foo)
    x = run(s)
    print(x)
