import matplotlib.pyplot as plt
from .plottypes import BasePlotMap as BPM
from ..utils import in_ipynb


_MF = None


if in_ipynb():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.magic("matplotlib inline")

print('Matplotlib loaded')


class MatplotlibPlotMap(BPM):
    @staticmethod
    def setup():
        global _MF
        _MF = plt.figure()

    @staticmethod
    def args():
        raise NotImplementedError()

    @staticmethod
    def getTheme():
        raise NotImplementedError()

    @staticmethod
    def setTheme():
        raise NotImplementedError()

    @staticmethod
    def themes():
        raise NotImplementedError()

    @staticmethod
    def _wrapper(**kwargs):
        if 'type' in kwargs:
            kwargs.pop('type', None)
        if 'raw' in kwargs:
            kwargs.pop('raw')
        if 'colors' in kwargs:
            kwargs['color'] = kwargs.pop('colors')
        return kwargs

    @staticmethod
    def plot(data, **kwargs):
        _MF.canvas.draw()
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        return plt.show()

    @staticmethod
    def line(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
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

    @staticmethod
    def bar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=False,
                         **kwargs)

    @staticmethod
    def stackedbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=True,
                         **kwargs)

    @staticmethod
    def horizontalbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='barh',
                         stacked=False,
                         **kwargs)

    @staticmethod
    def horizontalstackedbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='barh',
                         stacked=True,
                         **kwargs)

    @staticmethod
    def histogram(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hist',
                         **kwargs)

    @staticmethod
    def box(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='box',
                         **kwargs)

    @staticmethod
    def density(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='density',
                         **kwargs)

    @staticmethod
    def area(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', False),
                         **kwargs)

    @staticmethod
    def stackedarea(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', True),
                         **kwargs)

    @staticmethod
    def scatter(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='scatter',
                         **kwargs)

    @staticmethod
    def hexbin(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hexbin',
                         **kwargs)

    @staticmethod
    def basic():
        raise NotImplementedError()

    @staticmethod
    def bubble():
        raise NotImplementedError()

    @staticmethod
    def candlestick():
        raise NotImplementedError()

    @staticmethod
    def groupedbar():
        raise NotImplementedError()

    @staticmethod
    def groupedhist():
        raise NotImplementedError()

    @staticmethod
    def groupedscatter():
        raise NotImplementedError()

    @staticmethod
    def heatmap():
        raise NotImplementedError()

    @staticmethod
    def multiscatter():
        raise NotImplementedError()

    @staticmethod
    def ohlc():
        raise NotImplementedError()

    @staticmethod
    def ohlcv():
        raise NotImplementedError()

    @staticmethod
    def pie():
        raise NotImplementedError()

    @staticmethod
    def scattermatrix():
        raise NotImplementedError()

    @staticmethod
    def spread():
        raise NotImplementedError()

    @staticmethod
    def stackedhist():
        raise NotImplementedError()
