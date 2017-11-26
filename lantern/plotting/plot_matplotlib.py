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

    def show(self, **kwargs):
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
        self.axes[-1].legend(lines, labels, loc='center left', bbox_to_anchor=(1 + .05*len(self.axes_by_side['right']), 0.5), fancybox=True)
        self.figure.canvas.draw()
        plt.draw()

        if 'xlabel' in kwargs:
            self.axes[0].set_xlabel(kwargs.get('xlabel'))
        if 'ylabel' in kwargs:
            self.axes[0].set_ylabel(kwargs.get('ylabel'))
        if 'title' in kwargs:
            plt.title(kwargs.get('title'))
        # return self.figure
