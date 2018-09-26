import ipywidgets as widgets
from sidecar import Sidecar
from IPython import get_ipython
from IPython.core.magics.namespace import NamespaceMagics
from sys import getsizeof


def _getsizeof(x):
    if type(x).__name__ in ['ndarray', 'Series']:
        return x.nbytes
    elif type(x).__name__ == 'DataFrame':
        return x.memory_usage().sum()
    else:
        return getsizeof(x)


def _getshapeof(x):
    try:
        return x.shape
    except AttributeError:
        return None


class VariableInspector(object):
    def __init__(self):
        self._sc = Sidecar(title='Variables')
        get_ipython().user_ns_hidden['widgets'] = widgets
        get_ipython().user_ns_hidden['NamespaceMagics'] = NamespaceMagics

        self.closed = False
        self.namespace = NamespaceMagics()
        self.namespace.shell = get_ipython().kernel.shell

        self._box = widgets.Box()
        self._box.layout.overflow_y = 'scroll'
        self._table = widgets.HTML(value='Not hooked')
        self._box.children = [self._table]

        self._ipython = get_ipython()
        self._ipython.events.register('post_run_cell', self._fill)

    def close(self):
        """Close and remove hooks."""
        if not self.closed:
            self._ipython.events.unregister('post_run_cell', self._fill)
            self._box.close()
            self.closed = True

    def _fill(self):
        """Fill self with variable information."""
        types_to_exclude = ['module', 'function', 'builtin_function_or_method',
                            'instance', '_Feature', 'type', 'ufunc']
        values = self.namespace.who_ls()

        def eval(expr):
            return self.namespace.shell.ev(expr)

        var = [(v,
                type(eval(v)).__name__,
                str(_getsizeof(eval(v))),
                str(_getshapeof(eval(v))) if _getshapeof(eval(v)) else '',
                str(eval(v))[:200])
               for v in values if (v not in ['_html', '_nms', 'NamespaceMagics', '_Jupyter']) & (type(eval(v)).__name__ not in types_to_exclude)]

        self._table.value = '<div class="rendered_html jp-RenderedHTMLCommon"><table><thead><tr><th>Name</th><th>Type</th><th>Size</th><th>Shape</th><th>Value</th></tr></thead><tr><td>' + \
            '</td></tr><tr><td>'.join(['{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}'.format(v1, v2, v3, v4, v5) for v1, v2, v3, v4, v5 in var]) + \
            '</td></tr></table></div>'

    def _ipython_display_(self):
        """Called when display() or pyout is used to display the Variable
        Inspector."""
        with self._sc:
            self._box._ipython_display_()
