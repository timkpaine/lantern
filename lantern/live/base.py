import os
import os.path
import threading
from IPython import get_ipython
from abc import abstractmethod, ABCMeta
from .hosts.comm import runComm
from queue import Queue
from future.utils import with_metaclass

_LANTERN_LIVE_RANK = 0


class LanternLive(object):
    def __init__(self, queue, path, live_thread=None, qput=None):
        self._path = path
        self._queue = queue
        self._thread = live_thread

        # if not a Streaming
        if not self._thread:
            self.on_data = qput

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


class Streaming(with_metaclass(ABCMeta)):
    @abstractmethod
    def run(self):
        pass

    def on_data(self, data):
        getattr(self, '_qput')(data)


def run(streamer, sleep=1):
    global _LANTERN_LIVE_RANK
    q = Queue()

    def qput(message):
        q.put(message)

    # TODO add secret
    p = os.path.abspath(get_ipython().kernel.session.config['IPKernelApp']['connection_file'])
    sessionid = p.split(os.sep)[-1].replace('kernel-', '').replace('.json', '')

    # start comm sender thread
    t1 = threading.Thread(target=runComm, args=(q, str(_LANTERN_LIVE_RANK), sleep))
    _LANTERN_LIVE_RANK += 1
    t1.start()

    # start streamer thread
    streamer._qput = qput
    t2 = threading.Thread(target=streamer.run)
    t2.start()

    ll = LanternLive(q, 'comm://' + sessionid + '/' + 'lantern.live/' + str(_LANTERN_LIVE_RANK-1), t2, qput)
    return ll


def pipeline(foos, foo_callbacks, foo_args=None, foo_kwargs=None, sleep=1):
    foo_args = foo_args or []
    foo_kwargs = foo_kwargs or []

    global _LANTERN_LIVE_RANK
    q = Queue()

    def qput(message):
        q.put(message)

    # TODO add secret
    p = os.path.abspath(get_ipython().kernel.session.config['IPKernelApp']['connection_file'])
    sessionid = p.split(os.sep)[-1].replace('kernel-', '').replace('.json', '')

    # start comm sender thread
    t1 = threading.Thread(target=runComm, args=(q, str(_LANTERN_LIVE_RANK), sleep))
    _LANTERN_LIVE_RANK += 1
    t1.start()

    # start streamer thread

    ll = LanternLive(q, 'comm://' + sessionid + '/' + 'lantern.live/' + str(_LANTERN_LIVE_RANK-1), None, qput)
    return ll
