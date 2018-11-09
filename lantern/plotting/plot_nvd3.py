from nvd3 import lineChart
from nvd3.ipynb import initialize_javascript
from IPython.display import display
from .plotobj import BasePlot
from .plotutils import get_color

_INITED = False


class NVD3Plot(BasePlot):
    def __init__(self, size=None, theme=None):
        global _INITED
        if not _INITED:
            initialize_javascript()
            _INITED = True

        self.size = size or (700, 400)
        self._lines = lineChart(name='lineChart', x_is_date=True, x_axis_format='%Y-%m-%d', height=self.size[1], width=self.size[0])

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # require all data to be present before plotting
        display(self._lines)

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
            y = data[col].astype(float).tolist()
            x = data.index.astype(str).tolist()
            self._lines.add_serie(y=y,
                                  x=x,
                                  color=_color,
                                  name=col,
                                  extra={"tooltip": {"y_start": "Test ", "y_end": " test"}})

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        raise NotImplementedError()

    def step(self, data, color=None, y_axis='left', **kwargs):
        raise NotImplementedError()

    def vline(self, x, color=None, **kwargs):
        raise NotImplementedError()

    def vspan(self, xhigh, xlow, color=None, **kwargs):
        raise NotImplementedError()
