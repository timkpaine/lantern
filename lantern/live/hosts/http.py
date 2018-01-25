# import logging
# import tornado
# import tornado.web
# import ujson
# from ..utils import queue_get_all


# def add_to_tornado(app, queue, id, secret):
#     '''duplicated from websocket in case i change libs'''
#     path = r"/api/kernels/0/channel/lantern/live/api/v1/" + str(id)
#     logging.info('\nadding handler %s on %s\n' % (id, path))
#     app.add_handlers(r".*", [(path,
#                               HttpHandler,
#                               {'queue': queue,
#                                'secret': secret})])


# class HttpHandler(tornado.web.RequestHandler):
#     def initialize(self, queue=None, secret=None):
#         self._queue = queue
#         self._secret = secret

#     def set_default_headers(self):
#         self.set_header("Access-Control-Allow-Origin", "*")
#         self.set_header("Access-Control-Allow-Headers", "x-requested-with")
#         self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

#     def get(self):
#         # TODO check secret
#         x = queue_get_all(self._queue)
#         self.write(ujson.dumps(x))
