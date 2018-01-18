import ujson
import queue
import tornado
import tornado.web
import logging


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
    logging.basicConfig(level=logging.INFO)
    logging.info('\nadding handlern %s on %s\n' % (id, path))
    app.add_handlers(r".*", [(path,
                              Handler,
                              {'queue': queue})])


class Handler(tornado.web.RequestHandler):
    def initialize(self, queue=None):
        self._queue = queue

    def get(self):
        x = queue_get_all(self._queue)
        self.write(ujson.dumps(len(x)))
