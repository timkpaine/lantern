from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler


class HostHandler(IPythonHandler):
    '''Just a default handler'''
    def get(self, which):
        self.write(which)


def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/host/([^/]+)')
    web_app.add_handlers(host_pattern, [(route_pattern, HostHandler)])
