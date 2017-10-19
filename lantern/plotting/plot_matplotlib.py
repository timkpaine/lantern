import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from .plottypes import BasePlotMap as BPM
from ..utils import in_ipynb

_MF = None
_MFA = []
_AXES = {'left': [],
         'right': [],
         'top': [],
         'bottom': []}

_MPLTHEME = 'classic'


if in_ipynb():
    # auto-run the matplotlib inline magic
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.magic("matplotlib inline")

print('Matplotlib loaded')


def align_yaxis_np(axes):
    """Align zeros of the two axes, zooming them out by same ratio"""
    axes = np.array(axes)
    extrema = np.array([ax.get_ylim() for ax in axes])
    tops = extrema[:,1] / (extrema[:,1] - extrema[:,0])

    # Ensure that plots (intervals) are ordered bottom to top:
    if tops[0] > tops[1]:
        axes, extrema, tops = [a[::-1] for a in (axes, extrema, tops)]

    # How much would the plot overflow if we kept current zoom levels?
    tot_span = tops[1] + 1 - tops[0]

    extrema[0,1] = extrema[0,0] + tot_span * (extrema[0,1] - extrema[0,0])
    extrema[1,0] = extrema[1,1] + tot_span * (extrema[1,0] - extrema[1,1])
    [axes[i].set_ylim(*extrema[i]) for i in range(2)]


class MatplotlibPlotMap(BPM):
    @staticmethod
    def _newAx(x=False, y=False, y_side='left', color='black'):
        global _MFA, _AXES

        # axis managemens
        if not x and not y:
            return _MFA[0]
        if x and y:
            ax = _MFA[0].twiny().twinx()
            _AXES[y_side].append(ax)
            _AXES['bottom'].append(ax)
        elif x:
            ax = _MFA[0].twiny()
            _AXES['bottom'].append(ax)
        elif y:
            ax = _MFA[0].twinx()
            _AXES[y_side].append(ax)

        # set positioning
        ax.get_xaxis().set_label_position("bottom")
        ax.tick_params(axis='both', which='both',
                       labelbottom=False,
                       labeltop=False,
                       labelleft=(y_side == 'left') and y,
                       labelright=(y_side == 'right') and y)

        # pad axes
        xpad = 30*(len(_AXES['bottom'])-1)
        ypad = 30*(len(_AXES[y_side])-1)
        ax.tick_params(axis='x', pad=xpad)
        ax.tick_params(axis='y', pad=ypad)

        # hide
        ax.get_xaxis().get_major_formatter().set_useOffset(False)
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=30, fontsize=0)
        ax.get_xaxis().set_visible(False)
        ax.get_xaxis().set_ticks([])

        # manage legend later
        ax.legend_ = None

        # colorize
        if isinstance(color, list):
            # Take just the first color
            color = color[0]
        if y:
            ax.spines[y_side].set_color(color)
            ax.yaxis.label.set_color(color)
            ax.tick_params(axis='y', colors=color)

        # autoscale
        ax.autoscale(True)
        _MFA.append(ax)
        return ax

    @staticmethod
    def setup():
        global _MF, _MFA, _AXES
        # reset
        _MF = None
        _MFA = []
        _AXES = {'left': [],
                 'right': [],
                 'top': [],
                 'bottom': []}

        # initialize
        _MF, _MFA = plt.subplots(figsize=(12, 5))

        # default axis
        # deal with legends later
        _MFA.legend_ = None
        _MFA.get_xaxis().set_label_position("bottom")
        _MFA.tick_params(axis='both', which='both', labelbottom=True, labeltop=False, labelleft=True, labelright=False)
        _AXES['bottom'].append(_MFA)
        _AXES['left'].append(_MFA)
        _MFA = [_MFA]

    @staticmethod
    def args():
        raise NotImplementedError()

    @staticmethod
    def getTheme():
        return _MPLTHEME

    @staticmethod
    def setTheme(theme):
        global _MPLTHEME
        plt.style.use(theme)
        _MPLTHEME = theme

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
        kwargs.pop('x', None)  # FIXME
        kwargs.pop('y', None)  # FIXME
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

        # align_yaxis_np(_MFA)

        for m in _MFA:
            line, label = m.get_legend_handles_labels()
            lines += line
            labels += label
        if kwargs.get('legend', True):
            _MFA[0].legend(lines, labels, loc=2)
        plt.axhline(0, color='black')
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
        ax = MatplotlibPlotMap._newAx(x=False, y=kwargs.get('y', 'left') == 'right', y_side=kwargs.pop('y', 'left'), color=kwargs.get('colors'))

        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', False),
                         ax=ax,
                         **kwargs)

    @staticmethod
    def bar(data, **kwargs):
        ax = MatplotlibPlotMap._newAx(x=True, y=kwargs.get('y', 'left') == 'right', y_side=kwargs.pop('y', 'left'), color=kwargs.get('colors'))
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=False,
                         ax=ax,
                         **kwargs)

    @staticmethod
    def box(data, **kwargs):
        ax = MatplotlibPlotMap._newAx(x=True, y=kwargs.pop('y', 'left') == 'right')
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        kwargs.pop('color', '')  # FIXME
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

        scatter.pop('mode', '')  # FIXME
        categories = scatter.pop('categories', 'categories')  # FIXME
        scatter.pop('text', '')  # FIXME
        scatter.pop('colorscale', '')  # FIXME
        kwargs.pop('color', '')  # FIXME

        groups = list(set(data[categories].values))

        fg = sns.FacetGrid(data=data, hue='categories', hue_order=groups, aspect=2.4)
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
        ax = MatplotlibPlotMap._newAx(x=False, y=kwargs.pop('y', 'left') == 'right')
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(ax=ax, **kwargs)

    @staticmethod
    def lmplot(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        kwargs.pop('color', None)  # FIXME
        return sns.lmplot(x=x, y=y, data=data, **kwargs)

    @staticmethod
    def pairplot(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        kwargs.pop('color', None)  # FIXME
        return sns.pairplot(data, **kwargs)

    @staticmethod
    def probplot(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        kwargs.pop('color', None)  # FIXME
        return stats.probplot(data, dist='norm', plot=plt, **kwargs)

    @staticmethod
    def scatter(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        markers = kwargs.pop('symbol', '.')
        size = kwargs.pop('size', 50)

        kwargs.pop('mode', '')  # FIXME
        scatter.pop('categories', 'categories')  # FIXME
        scatter.pop('text', '')  # FIXME
        kwargs.pop('colorscale', '')  # FIXME
        kwargs.pop('color', '')  # FIXME

        return data.plot(kind='scatter',
                         x=x,
                         y=y,
                         s=size,
                         marker=markers,
                         **kwargs)

    @staticmethod
    def stackedarea(data, **kwargs):
        ax = MatplotlibPlotMap._newAx(x=False, y=kwargs.pop('y', 'left') == 'right')
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', True),
                         ax=ax,
                         **kwargs)

    @staticmethod
    def stackedbar(data, **kwargs):
        ax = MatplotlibPlotMap._newAx(x=True, y=kwargs.pop('y', 'left') == 'right')
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
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
