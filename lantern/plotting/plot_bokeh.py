import copy
import pandas as pd
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import Legend, Span
# from bokeh.models import HoverTool
from ..utils import in_ipynb
from .plotobj import BasePlot
from .plotutils import get_color


if in_ipynb():
    output_notebook()


class BokehPlot(BasePlot):
    def __init__(self, theme):
        self.figure = figure(toolbar_location="below",
                             toolbar_sticky=False,
                             x_axis_type='datetime')  # TODO remove
        self.legend = []

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # self.figure.add_tools(*[HoverTool(
        #     tooltips=[('x', '@x{%F}'), ('y', '@y')],
        #     formatters={'x': 'datetime'},
        #     mode='vline'
        # ) for _ in data])

        self.figure.outline_line_color = None
        # vline = Span(location=0, dimension='height', line_color='red', line_width=3)
        hline = Span(location=0, dimension='width', line_color='black', line_width=1)
        self.figure.renderers.append(hline)

        if xlabel:
            self.figure.xaxis.axis_label = kwargs.get('xlabel')
        if ylabel:
            self.figure.yaxis.axis_label = kwargs.get('ylabel')
        if title:
            self.figure.title.text = kwargs.get('title')

        self.figure.legend.location = None
        if legend:
            legend = Legend(items=self.legend, location=(10, 100))
            legend.click_policy = "mute"
            self.figure.add_layout(legend, 'right')

        if not grid:
            self.figure.xgrid.grid_line_color = None
            self.figure.ygrid.grid_line_color = None

        # FIXME
        if not yaxis:
            for ax in self.figure.yaxis:
                ax.axis_line_color = 'white'
        if not xaxis:
            for ax in self.figure.xaxis:
                ax.axis_line_color = 'white'

        # Turn off labels:
        # self.figure.xaxis.major_label_text_font_size = '0pt'

        show(self.figure)
        return self.figure

    def area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        data2 = data.append(data.iloc[-1]*0)
        data2 = data2.append(data2.iloc[0]*0)
        data2 = data2.sort_index()
        data2 = data2.sort_index()
        x, y = copy.deepcopy(data2.iloc[0]), copy.deepcopy(data2.iloc[1])
        data2.iloc[0], data2.iloc[1] = y, x

        for i, col in enumerate(data):
            c = get_color(i, col, color)
            l = self.figure.patch(x=data2.index, y=data2[col].values, legend=col, fill_alpha=.2, color=c, **kwargs)
            self.legend.append((col, [l]))

            # for stacked: https://bokeh.pydata.org/en/latest/docs/gallery/brewer.html
            # p.patches([x2] * areas.shape[1], [areas[c].values for c in areas], color=colors, alpha=0.8, line_color=None)

    def _stacked(df):
        df_top = df.cumsum(axis=1)
        df_bottom = df_top.shift(axis=1).fillna({'y0': 0})[::-1]
        df_stack = pd.concat([df_bottom, df_top], ignore_index=True)
        return df_stack

    def bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        # stacked bar: https://bokeh.pydata.org/en/latest/docs/gallery/bar_stacked.html
        # stacked bar: https://bokeh.pydata.org/en/latest/docs/gallery/bar_stacked_split.html
        c = []
        for i, col in enumerate(data):
            c.append(get_color(i, col, color))
            l = self.figure.vbar(x=data.index, top=data[col].values, width=.9, color=c, **kwargs)
            self.legend.append((col, [l]))

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        raise NotImplementedError()

    # def candlestick(self, data):
    #    # https://bokeh.pydata.org/en/latest/docs/gallery/candlestick.html

    def line(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            l = self.figure.line(x=data.index, y=data[col].values, legend=col, color=c, **kwargs)
            self.legend.append((col, [l]))

    def scatter(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            x = data.columns[0]
            y = data.columns[i]
            c = get_color(i, col, color)
            l = self.figure.scatter(x=data[x],
                                    y=data[y],
                                    legend='%s vs %s' % (x, y),
                                    fill_color=c,
                                    fill_alpha=0.6,
                                    line_color=None,
                                    **kwargs)
            self.legend.append(('%s vs %s' % (x, y), [l]))

    def step(self, data, color=None, y_axis='left', **kwargs):
        raise NotImplementedError()
