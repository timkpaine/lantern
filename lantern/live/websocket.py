import ujson
import websocket
import time
import threading
from .base import Streaming


class WebSocket(Streaming):
    def __init__(self, addr):
        websocket.enableTrace(True)

        def on_message(ws, message):
            self.on_data(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            def run(*args):
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
                time.sleep(10)
                ws.close()
                print("thread terminating...")

            t = threading.Thread(target=run)
            t.start()

        self.ws = websocket.WebSocketApp(addr,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.on_open = on_open

    def run(self):
        self.ws.run_forever()
