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

    # reset for divide by zero issues
    for i in range(len(extrema)):
        if np.isclose(extrema[i, 0], 0.0):
            extrema[i, 0] = -1
        if np.isclose(extrema[i, 1], 0.0):
            extrema[i, 1] = 1

    # upper and lower limits
    lowers = extrema[:, 0]
    uppers = extrema[:, 1]

    # if all pos or all neg, don't scale
    all_positive = False
    all_negative = False
    if lowers.min() > 0.0:
        all_positive = True

    if uppers.max() < 0.0:
        all_negative = True

    if all_negative or all_positive:
        # don't scale
        return

    # pick "most centered" axis
    res = abs(uppers+lowers)
    min_index = np.argmin(res)

    # scale positive or negative part
    multiplier1 = abs(uppers[min_index]/lowers[min_index])
    multiplier2 = abs(lowers[min_index]/uppers[min_index])

    for i in range(len(extrema)):
        # scale positive or negative part based on which induces valid
        if i != min_index:
            lower_change = extrema[i, 1] * -1*multiplier2
            upper_change = extrema[i, 0] * -1*multiplier1
            if upper_change < extrema[i, 1]:
                extrema[i, 0] = lower_change
            else:
                extrema[i, 1] = upper_change

        # bump by 10% for a margin
        extrema[i, 0] *= 1.1
        extrema[i, 1] *= 1.1

    # set axes limits
    [axes[i].set_ylim(*extrema[i]) for i in range(len(extrema))]


class MatplotlibPlotMap(BPM):
    @staticmethod
    def _newAx(x=False, y=False, y_side='left', color='black'):
        global _MFA, _AXES

        # axis managemens
        if not x and not y:
            return _MFA[0]
        if x and y:
            ax = _MFA[0].twiny()
            _MFA.append(ax)  # stash and delete superfluous axis later
            ax = ax.twinx()
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
        ax.tick_params(axis='both',
                       which='both',
                       bottom=True,
                       top=False,
                       left=(y_side == 'left') and y,
                       right=(y_side == 'right') and y,
                       labelbottom=False,
                       labeltop=False,
                       labelleft=(y_side == 'left') and y,
                       labelright=(y_side == 'right') and y)

        # pad axes
        xpad = 30*(len(_AXES['bottom'])-1)
        ypad = 30*(len(_AXES[y_side])-1)
        ax.tick_params(axis='x', pad=xpad+2)
        ax.tick_params(axis='y', pad=ypad+2)

        # colorize
        if isinstance(color, list):
            # Take just the first color
            color = color[0]

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
        _MFA.tick_params(axis='both',
                         which='both',
                         bottom=True,
                         top=False,
                         left=True,
                         right=False,
                         labelbottom=False,
                         labeltop=False,
                         labelleft=True,
                         labelright=False)
        _MFA.autoscale(True)
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
            # no top spines if no right
            if len(_AXES['right']) == 0:
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

            if ax.has_data():
                ax.legend_ = None
                ax.relim()
                ax.autoscale_view()
            else:
                _MF.delaxes(ax)

        align_yaxis_np(_MFA)

        for m in _MFA:
            line, label = m.get_legend_handles_labels()
            lines += line
            labels += label
        if kwargs.get('legend', True):
            _MFA[-1].legend(lines, labels, loc='center left', bbox_to_anchor=(1 + .05*len(_AXES['right']), 0.5), fancybox=True)
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
        ax = MatplotlibPlotMap._newAx(x=False, y=kwargs.get('y', 'left') == 'right', y_side=kwargs.pop('y', 'left'), color=kwargs.get('colors'))
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(ax=ax, **kwargs)

    @staticmethod
    def lmplot(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])

        color = kwargs.pop('color')
        scatter_kws = {'color': kwargs.pop('scatter_color', color)}
        line_kws = {'color': kwargs.pop('line_color', color)}
        return sns.lmplot(x=x, y=y, data=data, scatter_kws=scatter_kws, line_kws=line_kws, **kwargs)

    @staticmethod
    def pairplot(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        color = kwargs.pop('color')
        plot_kws = {'color': kwargs.pop('plot_color', color)}
        diag_kws = {'color': kwargs.pop('diag_color', color)}
        return sns.pairplot(data, plot_kws=plot_kws, diag_kws=diag_kws, **kwargs)

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
