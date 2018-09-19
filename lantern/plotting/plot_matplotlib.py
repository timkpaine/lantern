import matplotlib.pyplot as plt
from .plotobj import BasePlot
from .plotutils import align_yaxis_np, get_color
from ..utils import in_ipynb

_INITED = False


class MatplotlibPlot(BasePlot):
    def __init__(self, size=None, theme=None):
        global _INITED
        if not _INITED:
            if in_ipynb():
                from IPython import get_ipython
                ipython = get_ipython()
                if ipython:
                    ipython.magic("matplotlib inline")
                    ipython.magic("config InlineBackend.figure_format = 'retina'")
            _INITED = True

        size = size or (12, 5)
        self._figure, self._ax = plt.subplots(figsize=size)
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

        # store data for legend
        self._legend = []

        # require all data to be present before plotting
        self._bars = []
        self._hists = []

        # subplot support
        self._subplot = 111

    def _newAx(self, y_side='left', color='black'):
        # axis managemens
        if y_side == 'left':
            return self._ax
        elif y_side == 'right':
            ax = self._ax.twinx()
            self._axes_by_side[y_side].append(ax)

        # set positioning
        ax.get_xaxis().set_label_position("bottom")
        ax.tick_params(axis='both',
                       which='both',
                       bottom=True,
                       top=False,
                       left=(y_side == 'left'),
                       right=(y_side == 'right'),
                       labelbottom=False,
                       labeltop=False,
                       colors=color,
                       labelleft=(y_side == 'left'),
                       labelright=(y_side == 'right'))

        # pad axes
        xpad = 30*(len(self._axes_by_side['bottom'])-1)
        ypad = 30*(len(self._axes_by_side[y_side])-1)
        ax.tick_params(axis='x', pad=xpad+2)
        ax.tick_params(axis='y', pad=ypad+2)

        # colorize
        if isinstance(color, list):
            # Take just the first color
            color = color[0]
        elif color is None:
            # reset to black if no color
            color = 'black'

        ax.yaxis.label.set_color(color)
        ax.tick_params(axis='y', colors=color)

        # autoscale
        ax.autoscale(True)
        self._axes.append(ax)
        return ax

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # require all data to be present before plotting
        self._bar()
        self._hist()

        lines = []
        labels = []

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
            self._axes[-1].legend(lines, labels, loc='center left', bbox_to_anchor=(1 + .05*(min(len(self._axes_by_side['right']), 1)+1), 0.5), fancybox=True)

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
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            ax = self._newAx(y_side=y_axis, color=_color)
            x = ax.plot(data.index, data[col], color=_color, **kwargs)
            ax.fill_between(data.index, data[col], alpha=.7, color=_color)
            self._legend.append((col, x[0], y_axis))

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

        left_count = 1
        right_count = 1

        for d in self._bars:
            data.append(d[0])
            colors.append(d[1])
            y_axises.append(d[2])
            stackedes.append(d[3])
            kwargses.append(d[4])
            for col in d[0].columns:
                if (d[2] is None or d[2] == 'left') and not d[3]:
                    left_count += 1
                elif d[2] == 'right' and not d[3]:
                    right_count += 1

        width = 1/(left_count+right_count)
        count = 0

        ax = self._newAx(y_side='left', color=colors)
        ax2 = self._newAx(y_side='right', color=colors)

        for d in self._bars:
            for col in d[0].columns:
                if d[2] == 'right':
                    x = ax2.bar(d[0].index+count*((d[0].index[1]-d[0].index[0])/(left_count+right_count)), d[0][col], width=width, color=d[1], **d[4])
                    self._legend.append((col, x, d[2]))
                    x.set_label(col)
                    count += 1
                else:
                    x = ax.bar(d[0].index+count*((d[0].index[1]-d[0].index[0])/(left_count+right_count)), d[0][col], width=width, color=d[1], **d[4])
                    self._legend.append((col, x, d[2]))
                    x.set_label(col)
                    count += 1

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
        ax = self._newAx(y_side=y_axis, color=color)
        df.plot(kind='hist', alpha=.5, ax=ax, color=colors, stacked=stackedes[-1], **kwargses[-1])

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            self._hists.append((data[[col]], get_color(i, col, color), y_axis, stacked, kwargs))

    def hline(self, y, color=None, **kwargs):
        ax = self._newAx()
        color = color or get_color(None, None, None)
        ax.axhline(y, color=color, **kwargs)

    def hspan(self, yhigh, ylow, color=None, **kwargs):
        ax = self._newAx(x=False, y=False)
        color = color or get_color(None, None, None)
        ax.axhspan(ymin=ylow, ymax=yhigh, color=color, **kwargs)

    def line(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            ax = self._newAx(y_side=y_axis, color=_color)
            x = ax.plot(data.index, data[col], color=_color, **kwargs)
            self._legend.append((col, x[0], y_axis))

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            x = data.columns[0]
            y = data.columns[i]
            c = get_color(i, col, color)
            plt.plot(data[x], data[y], marker='.', linewidth=0, color=c, label='%s vs %s' % (x, y))

    def step(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            ax = self._newAx(y_side=y_axis, color=_color)
            x = ax.plot(data.index, data[col], drawstyle='steps', color=_color, **kwargs)
            self._legend.append((col, x[0], y_axis))

    def vline(self, x, color=None, **kwargs):
        ax = self._newAx()
        _color = color or get_color(None, None, None)
        ax.axvline(x, color=_color, **kwargs)

    def vspan(self, xhigh, xlow, color=None, **kwargs):
        ax = self._newAx()
        _color = color or get_color(None, None, None)
        ax.axvspan(xmin=xlow, xmax=xhigh, color=_color, **kwargs)
