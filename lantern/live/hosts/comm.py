import logging
import time
from IPython import get_ipython
from ..utils import queue_get_all


class CommHandler(object):
    def __init__(self, q, channel):
        self.closed = False
        self.q = q
        self.channel = channel
        self.target_name = 'lantern.live'
        self.opened = False

        def on_close(msg):
            self.opensed = False

        def handle_open(comm, msg):
            self.opened = True
            comm.on_close = on_close
            self.comm = comm

        get_ipython().kernel.comm_manager.register_target('lantern.live.' + str(channel), handle_open)

    def run(self):
        # TODO wait until JS ready
        while not self.opened:
            time.sleep(5)

        while self.opened:
            # message = '[' + queue_get_all(self.q) + ']'
            message = queue_get_all(self.q)

            if message != '[]' and message != '':
                self.comm.send(data=message)
            time.sleep(1)


def runComm(q, channel):
    logging.info('adding handler %s%s' % ('lantern.live.', channel))
    comm = CommHandler(q, channel)
    comm.run()
