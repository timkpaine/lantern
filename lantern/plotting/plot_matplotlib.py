import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .plottypes import BasePlotMap as BPM
from ..utils import in_ipynb

_MF = None
_MFA = []
sns.set()


if in_ipynb():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.magic("matplotlib inline")

print('Matplotlib loaded')


class MatplotlibPlotMap(BPM):
    @staticmethod
    def _newX():
        global _MFA
        _MFA.append(_MFA[0].twiny())
        _MFA[-1].get_xaxis().set_label_position("bottom")
        _MFA[-1].tick_params(axis='both', which='both', labelbottom=True, labeltop=False, labelleft=True, labelright=False)
        _MFA[-1].tick_params(axis='x', pad=30*len(_MFA))
        labels = _MFA[-1].get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=10)
        _MFA[-1].get_xaxis().set_visible(False)
        _MFA[-1].get_xaxis().get_major_formatter().set_useOffset(False)
        _MFA[-1].legend_ = None

        return _MFA[-1]

    @staticmethod
    def setup():
        global _MF, _MFA
        _MF, _MFA = plt.subplots(figsize=(12, 5))
        _MFA = [_MFA]
        _MFA[0].get_xaxis().set_label_position("bottom")
        _MFA[0].tick_params(axis='both', which='both', labelbottom=True, labeltop=False, labelleft=True, labelright=False)
        labels = _MFA[0].get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=10)
        _MFA[0].get_xaxis().get_major_formatter().set_useOffset(False)

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
        kwargs.pop('xlabel')
        kwargs.pop('ylabel')
        kwargs.pop('title')
        return kwargs

    @staticmethod
    def plot(data, **kwargs):
        _MF.canvas.draw()
        # ax = plt.gca()
        # ax.relim()
        _MFA[0].autoscale_view()
        h = []
        l = []
        for m in _MFA:
            h1, l1 = m.get_legend_handles_labels()
            h += h1
            l += l1
            print(h1)
            print(l1)
        # plt.legend([h,l])
        _MFA[0].legend(h, l, loc=2)
        plt.draw()
        if 'xlabel' in kwargs:
            _MFA[0].set_xlabel(kwargs.get('xlabel'))
        if 'ylabel' in kwargs:
            _MFA[0].set_ylabel(kwargs.get('ylabel'))
        if 'title' in kwargs:
            plt.title(kwargs.get('title'))
        return plt.show()

    @staticmethod
    def area(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        ax = _MFA[0]
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', False),
                         ax=ax,
                         **kwargs)

    @staticmethod
    def bar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        ax = MatplotlibPlotMap._newX()
        return data.plot(kind='bar',
                         stacked=False,
                         ax=ax,
                         **kwargs)

    @staticmethod
    def box(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        ax = MatplotlibPlotMap._newX()
        color = kwargs.pop('color', '')  # FIXME
        return data.plot(kind='box',
                         ax=ax,
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
        ax = _MFA[0]
        return data.plot(ax=ax, **kwargs)

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
        ax = MatplotlibPlotMap._newX()
        return data.plot(kind='bar',
                         stacked=True,
                         ax=ax,
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
