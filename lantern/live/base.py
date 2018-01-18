import queue
import threading
import tornado
from abc import abstractmethod, ABCMeta
from .utils import add_to_tornado


_LANTERN_LIVE = None


class Streaming(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    def on_data(self, data):
        getattr(self, 'callback')(data)


def run(streamer, port=8889):
    global _LANTERN_LIVE
    if not _LANTERN_LIVE:
        _LANTERN_LIVE = tornado.web.Application()

    q = queue.Queue()
    _LANTERN_LIVE.listen(port)
    add_to_tornado(_LANTERN_LIVE, q, 1)

    def qput(message):
        q.put(message)

    streamer.callback = qput
    t = threading.Thread(target=streamer.run)
    t.start()

    tornado.ioloop.IOLoop.current().start()
