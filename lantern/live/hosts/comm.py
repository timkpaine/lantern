import logging
import time
from ipykernel.comm import Comm
from ..utils import queue_get_all


class CommHandler(object):
    def __init__(self, q, target_name, channel):
        self.closed = False
        self.q = q
        self.channel = channel
        self.target_name = target_name + '-' + channel

        self.comm = Comm(target_name=self.target_name)

        def foo(comm, msg):
            print(comm)
            print(msg)

        def close():
            self.closed = True

        self.comm.on_close(close)

    def run(self):
        # TODO wait until JS ready
        self.comm.open('')
        while not self.closed:
            message = '[' + queue_get_all(self.q) + ']'

            if message != '[]':
                self.comm.send(data=message)
            time.sleep(5)


def runComm(q, target_name, channel):
    logging.info('adding handler %s on %s' % (target_name, channel))
    comm = CommHandler(q, target_name, channel)
    comm.run()
