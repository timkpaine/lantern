# import bqplot.pyplot as plt
from IPython.display import display
from ipywidgets import VBox
from bqplot.axes import Axis
from bqplot.scales import LinearScale
from bqplot.marks import Lines
from bqplot.figure import Figure
from bqplot.interacts import BrushIntervalSelector
from bqplot.toolbar import Toolbar
from .plotobj import BasePlot
from .plotutils import get_color


class BQPlotPlot(BasePlot):
    def __init__(self, size=None, theme=None):
        self.size = size or (12, 5)
        self._x_sc = LinearScale()
        self._y_sc = LinearScale()

        self._axes = []
        self._marks = []

    def _newAx(self, y_side='left', color='black'):
        # axis managemens
        raise NotImplementedError()

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # require all data to be present before plotting
        x = Axis(title=xlabel, scale=self._x_sc)
        y = Axis(title=ylabel, scale=self._y_sc, orientation='vertical')
        fig = Figure(axes=[x, y], marks=self._marks, title=title, legend_location='right', interactions=BrushIntervalSelector())

        display(VBox([fig, Toolbar(figure=fig)]))

    def area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        raise NotImplementedError()

    def bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        raise NotImplementedError()

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        raise NotImplementedError()

    def hline(self, y, color=None, **kwargs):
        raise NotImplementedError()

    def hspan(self, yhigh, ylow, color=None, **kwargs):
        raise NotImplementedError()

    def line(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            _color = get_color(i, col, color)
            self._marks.append(Lines(x=data.index,
                                     y=data[col],
                                     scales={'x': self._x_sc, 'y': self._y_sc},
                                     colors=[_color]))

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        raise NotImplementedError()

    def step(self, data, color=None, y_axis='left', **kwargs):
        raise NotImplementedError()

    def vline(self, x, color=None, **kwargs):
        raise NotImplementedError()

    def vspan(self, xhigh, xlow, color=None, **kwargs):
        raise NotImplementedError()
