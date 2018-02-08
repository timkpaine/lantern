import matplotlib.pyplot as plt
from .plotobj import BasePlot
from .plotutils import align_yaxis_np, get_color
from ..utils import in_ipynb

if in_ipynb():
    print('Matplotlib loaded')
    # auto-run the matplotlib inline magic
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.magic("matplotlib inline")
        ipython.magic("config InlineBackend.figure_format = 'retina'")


class MatplotlibPlot(BasePlot):
    def __init__(self, theme=None):
        self._figure, self._ax = plt.subplots(figsize=(12, 5))
        self._axes = [self._ax]
        self._axes_by_side = {'left': [],
                              'right': [],
                              'top': [],
                              'bottom': []}
        self._axes_by_side['left'].append(self._ax)
        self._axes_by_side['bottom'].append(self._ax)
        self._ax.legend_ = None
        self._ax.get_xaxis().set_label_position("bottom")
        self._ax.autoscale(True)

        # require all data to be present before plotting
        self._bars = []
        self._hists = []

    def _newAx(self, x=False, y=False, y_side='left', color='black'):
        # axis managemens
        if not x and not y:
            return self._ax
        if x and y:
            ax = self._ax.twiny()
            self._axes.append(ax)  # stash and delete superfluous axis later
            ax = ax.twinx()
            self._axes_by_side[y_side].append(ax)
            self._axes_by_side['bottom'].append(ax)
        elif x:
            ax = self._ax.twiny()
            self._axes_by_side['bottom'].append(ax)
        elif y:
            ax = self._ax.twinx()
            self._axes_by_side[y_side].append(ax)

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
        xpad = 30*(len(self._axes_by_side['bottom'])-1)
        ypad = 30*(len(self._axes_by_side[y_side])-1)
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
        self._axes.append(ax)

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # require all data to be present before plotting
        self._bar()
        self._hist()

        lines = []
        labels = []
        # plt.legend([])
        # leg = set(ax.legend for ax in self._axes)

        # FIXME these rescale the axis
        # plt.axhline(0, color='black')
        # plt.axvline(0, color='black')

        to_delete = []
        for ax in self._axes:
            # no top spines if no right
            if len(self._axes_by_side['right']) == 0:
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

            if ax.has_data():
                ax.legend_ = None
                ax.relim()
                ax.autoscale_view()

            else:
                print(ax)
                self._figure.delaxes(ax)
                to_delete.append(ax)
        for ax in to_delete:
            self._axes.remove(ax)

        align_yaxis_np(self._axes)

        for m in self._axes:
            line, label = m.get_legend_handles_labels()
            lines += line
            labels += label

        if legend:
            self._axes[-1].legend(lines, labels, loc='center left', bbox_to_anchor=(1 + .05*min(len(self._axes_by_side['right']), 1), 0.5), fancybox=True)

        if xlabel:
            self._axes[-1].set_xlabel(xlabel)
        if ylabel:
            self._axes[-1].set_ylabel(ylabel)
        if title:
            plt.title(title)

        self._axes[-1].spines['left'].set_visible(yaxis)
        self._axes[-1].spines['bottom'].set_visible(xaxis)

        if not yticks:
            for ax in self._axes:
                ax.yaxis.set_ticks([])
        if not xticks:
            # FIXME this doesnt work
            for ax in self._axes:
                ax.xaxis.set_ticks([])

        if grid:
            self._axes[-1].grid(which='both')
            self._axes[-1].grid(which='minor', alpha=0.2)
            self._axes[-1].grid(which='major', alpha=0.5)

        self._figure.canvas.draw()
        plt.draw()

    def area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        data.plot(kind='area', ax=ax, stacked=stacked, **kwargs)

    def bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            self._bars.append((data[[col]], get_color(i, col, color), y_axis, stacked, kwargs))

    def _bar(self):
        if not self._bars:
            return
        data = []
        colors = []
        y_axises = []
        stackedes = []
        kwargses = []
        for d in self._bars:
            data.append(d[0])
            colors.append(d[1])
            y_axises.append(d[2])
            stackedes.append(d[3])
            kwargses.append(d[4])
        df = data[0]
        df = df.join(data[1:])
        y_axis = 'left'
        color = colors
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        df.plot(kind='bar', ax=ax, stacked=stackedes[-1], **kwargses[-1])

    def _hist(self):
        if not self._hists:
            return
        data = []
        colors = []
        y_axises = []
        stackedes = []
        kwargses = []
        for d in self._hists:
            data.append(d[0])
            colors.append(d[1])
            y_axises.append(d[2])
            stackedes.append(d[3])
            kwargses.append(d[4])
        df = data[0]
        df = df.join(data[1:])
        y_axis = 'left'
        color = colors
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        df.plot(kind='hist', alpha=.5, ax=ax, stacked=stackedes[-1], **kwargses[-1])

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            self._hists.append((data[[col]], get_color(i, col, color), y_axis, stacked, kwargs))

    def line(self, data, color=None, y_axis='left', **kwargs):
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        data.plot(ax=ax, **kwargs)

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            x = data.columns[0]
            y = data.columns[i]
            c = get_color(i, col, color)
            plt.plot(data[x], data[y], marker='.', linewidth=0, color=c, label='%s vs %s' % (x, y))

    def step(self, data, color=None, y_axis='left', **kwargs):
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        data.plot(ax=ax, drawstyle='steps', **kwargs)
