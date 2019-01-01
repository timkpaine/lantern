# import altair as alt
from .plotobj import BasePlot
# from .plotutils import get_color


class AltairPlot(BasePlot):
    def __init__(self, size=None, theme=None):
        self.size = size or (700, 400)
        self._charts = []

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # require all data to be present before plotting
        return

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
        raise NotImplementedError()

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        raise NotImplementedError()

    def step(self, data, color=None, y_axis='left', **kwargs):
        raise NotImplementedError()

    def vline(self, x, color=None, **kwargs):
        raise NotImplementedError()

    def vspan(self, xhigh, xlow, color=None, **kwargs):
        raise NotImplementedError()
