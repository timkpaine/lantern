from bokeh.plotting import figure, show, output_notebook
# from bokeh.models import HoverTool
from ..utils import in_ipynb
from .plotobj import BasePlot


if in_ipynb():
    output_notebook()
_BF = None


class BokehPlot(BasePlot):
    def __init__(self, theme):
        self.figure = figure(toolbar_location="below",
                             toolbar_sticky=False,
                             x_axis_type='datetime')  # TODO remove

    def show(self, **kwargs):
        # self.figure.add_tools(*[HoverTool(
        #     tooltips=[('x', '@x{%F}'), ('y', '@y')],
        #     formatters={'x': 'datetime'},
        #     mode='vline'
        # ) for _ in data])
        show(self.figure)
        return self.figure

    def line(self, data, **kwargs):
        for col in data:
            self.figure.line(x=data.index, y=data[col].values, **kwargs)
