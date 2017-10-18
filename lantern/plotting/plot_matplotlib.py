import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .plottypes import BasePlotMap as BPM
from ..utils import in_ipynb

_MF = None
_MFA = []


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
        ax = _MFA[0].twiny()
        ax.get_xaxis().set_label_position("bottom")
        ax.tick_params(axis='both', which='both', labelbottom=True, labeltop=False, labelleft=True, labelright=False)
        ax.tick_params(axis='x', pad=30*len(_MFA))
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=10)
        ax.get_xaxis().set_visible(False)
        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        ax.legend_ = None
        ax.autoscale(True)
        _MFA.append(ax)
        return ax

    @staticmethod
    def setup():
        global _MF, _MFA
        _MF, _MFA = plt.subplots(figsize=(12, 5))
        _MFA.legend_ = None
        _MFA.get_xaxis().set_label_position("bottom")
        _MFA.tick_params(axis='both', which='both', labelbottom=True, labeltop=False, labelleft=True, labelright=False)
        labels = _MFA.get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=10)
        _MFA.get_xaxis().get_major_formatter().set_useOffset(False)
        _MFA.autoscale(True)
        _MFA = [_MFA]

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

        # purge from subplot calls, only use for main plot command
        kwargs.pop('xlabel', None)
        kwargs.pop('ylabel', None)
        kwargs.pop('title', None)

        return kwargs

    @staticmethod
    def plot(data, **kwargs):
        lines = []
        labels = []
        plt.legend([])
        for ax in _MFA:
            if ax.has_data():
                ax.legend_ = None
                ax.relim()
                ax.autoscale_view()
            else:
                _MF.delaxes(ax)
        for m in _MFA:
            line, label = m.get_legend_handles_labels()
            lines += line
            labels += label
        if kwargs.get('legend', True):
            _MFA[0].legend(lines, labels, loc=2)
        _MF.canvas.draw()
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
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        markers = kwargs.pop('symbol', '.')
        size = scatter.pop('size', 10)

        if isinstance(size, str):
            size = data[size] * 10

        mode = scatter.pop('mode', '')  # FIXME
        categories = scatter.pop('categories', 'categories') # FIXME
        text = scatter.pop('text', '') # FIXME
        colorscale = scatter.pop('colorscale', '')  # FIXME
        color = kwargs.pop('color', '')


        groups = list(set(data[categories].values))

        fg = sns.FacetGrid(data=data, hue='categories', hue_order=groups, aspect=1.61)
        return fg.map(plt.scatter,
                      x,
                      y,
                      s=size,
                      marker=markers,
                      **kwargs)

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
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        markers = kwargs.pop('symbol', '.')
        size = kwargs.pop('size', 50)

        mode = kwargs.pop('mode', '')  # FIXME
        categories = scatter.pop('categories', 'categories') # FIXME
        text = scatter.pop('text', '') # FIXME
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
