import os.path
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler, path_regex


class PublishHandler(IPythonHandler):
    '''Just a default handler'''
    def get(self, path):
        t = os.path.join(os.path.dirname(__file__), 'templates', 'publish.html')
        name = path.rsplit('/', 1)[-1]
        self.write(self.render_template(t,
                   notebook_path=path,
                   notebook_name=name,
                   kill_kernel=False,
                   mathjax_url=self.mathjax_url,
                   mathjax_config=self.mathjax_config))


def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], r'/publish%s' % path_regex)
    web_app.add_handlers(host_pattern, [(route_pattern, PublishHandler)])

    t = os.path.join(os.path.dirname(__file__), 'templates')
    nb_server_app.config['NotebookApp']['extra_template_paths'] = [t]
    nb_server_app.extra_template_paths = [t]
    import ipdb; ipdb.set_trace()