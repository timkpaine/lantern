from .plot_matplotlib import MatplotlibPlot
from .plot_cufflinks import CufflinksPlot
from .plot_bokeh import BokehPlot

_BACKENDS = ['cufflinks', 'plotly', 'bokeh', 'highcharts', 'matplotlib', 'seaborn']


def _backend_to_plot_obj(backend, theme=None):
    if backend == 'matplotlib' or backend == 'seaborn':
        return MatplotlibPlot(theme)
    if backend == 'cufflinks' or backend == 'plotly':
        return CufflinksPlot(theme)
    if backend == 'bokeh':
        return BokehPlot(theme)


def figure(backend='matplotlib', theme=None):
    if backend not in _BACKENDS:
        raise Exception('Must pick backend in %s' % _BACKENDS)
    return _backend_to_plot_obj(backend, theme)


def plot(data, kind='line', backend='matplotlib', theme=None, **kwargs):
    f = figure(backend, theme)

    # TODO
    if isinstance(kind, str):
        pass
    elif isinstance(kind, list):
        pass
    elif isinstance(kind, dict):
        pass
