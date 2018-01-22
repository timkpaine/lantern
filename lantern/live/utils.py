import logging
import queue
import socket
import tornado
import tornado.web
import ujson
from contextlib import closing


def find_free_port():
    '''https://stackoverflow.com/questions/1365265/on-localhost-how-do-i-pick-a-free-port-number'''
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def fqdn(port, rank):
    return 'http://' + socket.getfqdn() + ':' + str(port) + '/lantern/live/' + str(rank)


def queue_get_all(q):
    items = []
    while True:
        try:
            items.append(q.get_nowait())
        except queue.Empty:
            break
    return items


def add_to_tornado(app, queue, id):
    path = r"/lantern/live/" + str(id)
    logging.info('\nadding handler %s on %s\n' % (id, path))
    app.add_handlers(r".*", [(path,
                              Handler,
                              {'queue': queue})])


class Handler(tornado.web.RequestHandler):
    def initialize(self, queue=None):
        self._queue = queue

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        x = queue_get_all(self._queue)
        self.write(ujson.dumps(x))
