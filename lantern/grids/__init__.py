from .grid_plotly import plotly_grid
from .grid_qgrid import qgrid_grid
from .grid_psp import psp_grid


_BACKENDS = ['plotly', 'qgrid', 'psp']


def _backend_to_grid_foo(backend, theme=None):
    if backend == 'plotly' or backend == 'cufflinks':
        return plotly_grid
    if backend == 'qgrid':
        return qgrid_grid
    if backend == 'psp':
        return psp_grid


def grid(data, backend='psp', **kwargs):
    if backend not in _BACKENDS:
        raise Exception('Must pick backend in %s' % _BACKENDS)
    return _backend_to_grid_foo(backend)(data, **kwargs)
