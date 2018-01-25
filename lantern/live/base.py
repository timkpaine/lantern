import threading
from abc import abstractmethod, ABCMeta
from .hosts.comm import runComm
from queue import Queue

_LANTERN_LIVE_RANK = 0


class LanternLive(object):
    def __init__(self, queue, live_thread, path):
        self._thread = live_thread
        self._path = path
        self._queue = queue

    def load(self, data):
        self._queue.put(data)

    def path(self):
        return self._path

    def __repr__(self):
        return self._path

    def __del__(self):
        pass
        # self._thread.stop()
        # self._thread.join()


class Streaming(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    def on_data(self, data):
        getattr(self, 'callback')(data)


def run(streamer):
    global _LANTERN_LIVE_RANK
    q = Queue()

    def qput(message):
        q.put(message)

    # start comm sender thread
    t1 = threading.Thread(target=runComm, args=(q, 'lanternlive', str(_LANTERN_LIVE_RANK)))
    _LANTERN_LIVE_RANK += 1
    t1.start()

    # start streamer thread
    streamer.callback = qput
    t2 = threading.Thread(target=streamer.run)
    t2.start()

    ll = LanternLive(q, t2, 'comm://' + str(_LANTERN_LIVE_RANK-1))
    return ll
