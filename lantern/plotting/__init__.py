from six import iteritems
from .plot_matplotlib import MatplotlibPlot
from .plot_plotly import PlotlyPlot
from .plot_bokeh import BokehPlot
# from .plot_altair import NVD3Plot
# from .plot_bqplot import BQPlotPlot
# from .plot_nvd3 import NVD3Plot
from ..utils import LanternException


_BACKENDS = ['cufflinks', 'plotly', 'bokeh', 'highcharts', 'matplotlib', 'seaborn', 'bqplot', 'd3']


def _backend_to_plot_obj(backend, size=None, theme=None):
    if backend == 'matplotlib' or backend == 'seaborn':
        return MatplotlibPlot(size, theme)
    if backend == 'cufflinks' or backend == 'plotly':
        return PlotlyPlot(size, theme)
    if backend == 'bokeh':
        return BokehPlot(size, theme)
    # if backend == 'altair':
    #     return AltairPlot(size, theme)
    # if backend == 'bqplot':
    #     return BQPlotPlot(size, theme)
    # if backend == 'd3':
    #     return NVD3Plot(size, theme)
    raise NotImplementedError()


def figure(backend='matplotlib', size=None, theme=None):
    if backend not in _BACKENDS:
        raise Exception('Must pick backend in %s' % _BACKENDS)
    return _backend_to_plot_obj(backend, size, theme)


def plot(data, kind='line', backend='matplotlib', size=None, theme=None, **kwargs):
    f = figure(backend, size, theme)

    show_args = {}
    show_args['title'] = kwargs.pop('title', '')
    show_args['xlabel'] = kwargs.pop('xlabel', '')
    show_args['ylabel'] = kwargs.pop('ylabel', '')
    show_args['xaxis'] = kwargs.pop('xaxis', True)
    show_args['yaxis'] = kwargs.pop('yaxis', True)
    show_args['xticks'] = kwargs.pop('xticks', True)
    show_args['yticks'] = kwargs.pop('yticks', True)
    show_args['legend'] = kwargs.pop('legend', True)
    show_args['grid'] = kwargs.pop('grid', True)

    # TODO
    if isinstance(kind, str):
        getattr(f, kind)(data, **kwargs)
        return f.show(**show_args)
    elif isinstance(kind, list):
        # TODO handle color, scatter, etc
        if len(kind) != len(data.columns):
            raise LanternException('Must specify type for each column')
        for i, k in enumerate(kind):
            getattr(f, k)(data[[data.columns[i]]], **kwargs)
        return f.show(**show_args)

    elif isinstance(kind, dict):
        # TODO handle color, scatter, etc
        if len(kind) != len(data.columns):
            raise LanternException('Must specify type for each column')
        for k, v in iteritems(kind):
            if k not in data.columns:
                raise LanternException('Unrecognized column: %s' % str(k))
            getattr(f, v)(data[[k]], **kwargs)
        return f.show(**show_args)
