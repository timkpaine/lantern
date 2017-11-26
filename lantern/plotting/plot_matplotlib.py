from .plotobj import BasePlot
from .plotutils import align_yaxis_np
from ..utils import in_ipynb
import matplotlib.pyplot as plt

if in_ipynb():
    # auto-run the matplotlib inline magic
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython:
        ipython.magic("matplotlib inline")
        ipython.magic("config InlineBackend.figure_format = 'retina'")


class MatplotlibPlot(BasePlot):
    def __init__(self, theme=None):
        self.figure, self.ax = plt.subplots(figsize=(12, 5))
        self.axes = [self.ax]
        self.axes_by_side = {'left': [],
                             'right': [],
                             'top': [],
                             'bottom': []}
        self.axes_by_side['left'].append(self.ax)
        self.axes_by_side['bottom'].append(self.ax)
        self.ax.legend_ = None
        self.ax.get_xaxis().set_label_position("bottom")
        self.ax.tick_params(axis='both',
                            which='both',
                            bottom=True,
                            top=False,
                            left=True,
                            right=False,
                            labelbottom=False,
                            labeltop=False,
                            labelleft=True,
                            labelright=False)
        self.ax.autoscale(True)

    def _newAx(self, x=False, y=False, y_side='left', color='black'):
        # axis managemens
        if not x and not y:
            return self.ax
        if x and y:
            ax = self.ax.twiny()
            self.axes.append(ax)  # stash and delete superfluous axis later
            ax = ax.twinx()
            self.axes_by_side[y_side].append(ax)
            self.axes_by_side['bottom'].append(ax)
        elif x:
            ax = self.ax.twiny()
            self.axes_by_side['bottom'].append(ax)
        elif y:
            ax = self.ax.twinx()
            self.axes_by_side[y_side].append(ax)

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
        xpad = 30*(len(self.axes_by_side['bottom'])-1)
        ypad = 30*(len(self.axes_by_side[y_side])-1)
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
        self.axes.append(ax)

    def line(self, data, color=None, y_axis='left', **kwargs):
        ax = self._newAx(x=False, y=(y_axis == 'right'), y_side=y_axis, color=color)
        data.plot(ax=ax, **kwargs)

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        lines = []
        labels = []
        plt.legend([])
        for ax in self.axes:
            # no top spines if no right
            if len(self.axes_by_side['right']) == 0:
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

            if ax.has_data():
                ax.legend_ = None
                ax.relim()
                ax.autoscale_view()
            else:
                self.figure.delaxes(ax)

        align_yaxis_np(self.axes)

        for m in self.axes:
            line, label = m.get_legend_handles_labels()
            lines += line
            labels += label
        if legend:
            self.axes[-1].legend(lines, labels, loc='center left', bbox_to_anchor=(1 + .05*len(self.axes_by_side['right']), 0.5), fancybox=True)

        if xlabel:
            self.axes[-1].set_xlabel(xlabel)
        if ylabel:
            self.axes[-1].set_ylabel(ylabel)
        if title:
            plt.title(title)

        self.axes[-1].spines['left'].set_visible(yaxis)
        self.axes[-1].spines['bottom'].set_visible(xaxis)

        if not yticks:
            self.axes[-1].yaxis.set_ticks([])
        if not xticks:
            self.axes[-1].xaxis.set_ticks([])

        if grid:
            self.axes[-1].grid(which='both')
            self.axes[-1].grid(which='minor', alpha=0.2)
            self.axes[-1].grid(which='major', alpha=0.5)
        # self.figure.canvas.draw()
        # plt.draw()
