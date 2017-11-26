from .plot_matplotlib import MatplotlibPlot
from .plot_cufflinks import CufflinksPlot
from .plot_bokeh import BokehPlot

_BACKENDS = ['cufflinks', 'plotly', 'bokeh', 'highcharts', 'matplotlib', 'seaborn']


def backend_to_plot_obj(backend, theme=None):
    if backend == 'matplotlib' or backend == 'seaborn':
        return MatplotlibPlot(theme)
    if backend == 'cufflinks' or backend == 'plotly':
        return CufflinksPlot(theme)
    if backend == 'bokeh':
        return BokehPlot(theme)


def plot(backend, theme=None):
    if backend not in _BACKENDS:
        raise Exception('Must pick backend in %s' % _BACKENDS)
    return backend_to_plot_obj(backend, theme)
