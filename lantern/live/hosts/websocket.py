# import logging
# import tornado
# import tornado.gen
# from tornado.websocket import WebSocketHandler, WebSocketClosedError


# def add_to_tornado_ws(app, queue, id, secret):
#     '''duplicated from http in case i change libs'''
#     path = r"/lantern/live/api/v1/" + str(id)
#     logging.info('\nadding handler %s on %s\n' % (id, path))
#     app.add_handlers(r".*", [(path,
#                               WebSocketHandler,
#                               {'queue': queue,
#                                'secret': secret})])


# class WebSocketHandler(WebSocketHandler):
#     '''websocket reference: https://gist.github.com/mivade/0ac9e8ec58acd2366133'''
#     def initialize(self, queue=None, secret=None):
#         self._queue = queue
#         self._secret = secret
#         self._finished = False

#     def open(self):
#         logging.info('WEBSOCKET OPEN')
#         self.run()

#     def on_close(self):
#         logging.info('WEBSOCKET CLOSED')
#         self._close()

#     def _close(self):
#         self._finished = True

#     @tornado.gen.coroutine
#     def run(self):
#         self._finished = False
#         while not self._finished:
#             # TODO replay
#             message = yield self._queue.get()
#             self.send(message)

#     def send(self, message):
#         try:
#             self.write_message(dict(value=message))
#         except WebSocketClosedError:
#             self._close()
