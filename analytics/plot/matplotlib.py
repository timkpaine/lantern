import matplotlib.pyplot as plt
from .plottypes import PlotType as p


def _wrapper(data, type=p.PLOT, raw=False, colors=None, **kwargs):
    if raw:
        pass
    if colors:
        kwargs['color'] = colors
    return _plotmap_internal[type](data, **kwargs)


def plot(data, **kwargs):
    return plt.show()


def line(data, **kwargs):
    return data.plot(**kwargs)
    #                   subplots=kwargs.get('subplots', False),
    #                   hline=kwargs.get('hline', []),
    #                   vline=kwargs.get('vline', []),
    #                   # hspan=kwargs.get('hspan', _HSPAN_NONE),
    #                   # vspan=kwargs.get('vspan', _VSPAN_NONE),
    #                   colors=kwargs.get('colors', []),
    #                   bestfit=kwargs.get('bestfit', False),
    #                   bestfit_colors=kwargs.get('bestfit_colors', []),
    #                   asFigure=kwargs.get('asFigure', False),


def bar(data, **kwargs):
    return data.plot(kind='bar',
                     **kwargs)


def histogram(data, **kwargs):
    return data.plot(kind='hist',
                     **kwargs)


def box(data, **kwargs):
    return data.plot(kind='box',
                     **kwargs)


def density(data, **kwargs):
    return data.plot(kind='density',
                     **kwargs)


def area(data, **kwargs):
    return data.plot(kind='area',
                     stacked=kwargs.get('stacked', False),
                     **kwargs)


def stackedarea(data, **kwargs):
    return data.plot(kind='area',
                     stacked=kwargs.get('stacked', True),
                     **kwargs)


def scatter(data, **kwargs):
    return data.plot(kind='scatter',
                     **kwargs)


def hexbin(data, **kwargs):
    return data.plot(kind='hexbin',
                     **kwargs)

_plotmap_internal = {
    p.PLOT: plot,
    p.LINE: line,
    p.BAR: bar,
    p.HISTOGRAM: histogram,
    p.BOX: box,
    p.AREA: area,
    p.SCATTER: scatter,
    p.DENSITY: density,
    p.HEXBIN: hexbin,
}

_plotmap = {
    p.PLOT: _wrapper,
    # p.BASIC: basic,
    p.LINE: _wrapper,
    # p.SPREAD: spread,
    p.BAR: _wrapper,
    # p.GROUPEDBAR: groupedbar,
    # p.STACKEDBAR: stackedbar,
    # p.HORIZONTALBAR: horizontalbar,
    # p.HORIZONTALSTACKEDBAR: horizontalstackedbar,
    p.HISTOGRAM: _wrapper,
    # p.GROUPEDHIST: groupedhist,
    # p.STACKEDHIST: stackedhist,
    p.BOX: _wrapper,
    # p.PIE: pie,
    p.AREA: _wrapper,
    p.STACKEDAREA: stackedarea,
    # p.FILLEDAREA: filledarea,
    p.SCATTER: _wrapper,
    # p.BUBBLE: bubble,
    # p.SCATTERMATRIX: scattermatrix,
    # p.HEATMAP: heatmap,
    # p.MULTISCATTER: multiscatter,
    # p.GROUPEDSCATTER: groupedscatter,
    # p.OHLC: ohlcv,
    # p.OHLVC: ohlcv,
    # p.CANDLESTICK: candlestick
    p.DENSITY: _wrapper,
    p.HEXBIN: _wrapper
}
