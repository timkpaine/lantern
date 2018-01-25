import logging
from ipykernel.comm import Comm


class CommHandler(object):
    def __init__(self, q, target_name, channel):
        self.closed = False
        self.q = q
        self.target_name = target_name
        self.channel = channel

        self.comm = Comm(target_name="lanternlive")

        def close():
            self.closed = True

        self.comm.on_close(close)

    def run(self):
        while not self.closed:
            message = self.q.get()
            self.comm.send(data=message)


def runComm(q, target_name, channel):
    logging.info('adding handler %s on %s' % (target_name, channel))
    comm = CommHandler(q, target_name, channel)
    comm.run()
