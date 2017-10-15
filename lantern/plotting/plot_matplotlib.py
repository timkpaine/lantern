import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .plottypes import BasePlotMap as BPM
from ..utils import in_ipynb

_MF = None
sns.set()


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
    def setTheme(theme):
        plt.style.use(theme)

    @staticmethod
    def themes():
        return plt.style.available

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
        # ax.relim()
        ax.autoscale_view()
        plt.draw()
        return plt.show()

    @staticmethod
    def area(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', False),
                         **kwargs)

    @staticmethod
    def bar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=False,
                         **kwargs)

    @staticmethod
    def box(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        color = kwargs.pop('color', '')  # FIXME
        return data.plot(kind='box',
                         **kwargs)

    @staticmethod
    def bubble(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        x = kwargs.pop('x', data.columns[0])
        y = kwargs.pop('y', data.columns[0])
        markers = kwargs.pop('symbol', '.')
        size = kwargs.pop('size', 10)

        if isinstance(size, str):
            size = data[size] * 10

        mode = kwargs.pop('mode', '')  # FIXME
        categories = kwargs.pop('categories', 'categories') # FIXME
        text = kwargs.pop('text', '') # FIXME
        colorscale = kwargs.pop('colorscale', '')  # FIXME
        color = kwargs.pop('color', '')


        groups = list(set(data[categories].values))

        fg = sns.FacetGrid(data=data, hue='categories', hue_order=groups, aspect=1.61)
        return fg.map(plt.scatter, x, y, s=size, marker=markers, **kwargs)

    @staticmethod
    def density(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='density',
                         **kwargs)

    @staticmethod
    def hexbin(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hexbin',
                         **kwargs)

    @staticmethod
    def histogram(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return plt.hist(data.values, **kwargs)
        # return data.plot(kind='hist',
        #                  **kwargs)

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
    def line(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(**kwargs)

    @staticmethod
    def scatter(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)

        x = kwargs.pop('x', data.columns[0])
        y = kwargs.pop('y', data.columns[0])
        markers = kwargs.pop('symbol', '.')
        size = kwargs.pop('size', 10)

        mode = kwargs.pop('mode', '')  # FIXME
        categories = kwargs.pop('categories', 'categories') # FIXME
        text = kwargs.pop('text', '') # FIXME
        colorscale = kwargs.pop('colorscale', '')  # FIXME
        color = kwargs.pop('color', '')

        return data.plot(kind='scatter',
                         x=x,
                         y=y,
                         s=size,
                         marker=markers,
                         **kwargs)

    @staticmethod
    def stackedarea(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', True),
                         **kwargs)

    @staticmethod
    def stackedbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=True,
                         **kwargs)

    @staticmethod
    def stackedhist(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hist',
                         stacked=True,
                         **kwargs)

    @staticmethod
    def basic(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def candlestick(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedbar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedhist(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedscatter(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def heatmap(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def multiscatter(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def ohlc(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def ohlcv(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def pie(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def scattermatrix(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def spread(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def pairplot(data, **kwargs):
        raise NotImplementedError()
