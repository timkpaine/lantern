import plotly.graph_objs as go
from matplotlib.colors import to_rgb
from plotly.graph_objs import FigureWidget
from .plotobj import BasePlot
from .plotutils import get_color
from ..utils import in_ipynb


if in_ipynb():
    print('Plot.ly loaded')

# _HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# _VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


class PlotlyPlot(BasePlot):
    def __init__(self, theme=None):
        self.figures = []
        self.bars = []
        self.hlines = []
        self.vlines = []
        self.hspans = []
        self.vspans = []

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # get before wrapper strips
        tdata = []
        ldata = {}

        for col, figure, axis in self.figures:
            for trace in figure['data']:
                if axis == 'right':
                    trace['yaxis'] = 'y2'
                    trace['xaxis'] = 'x1'
                else:
                    trace['yaxis'] = 'y1'
                    trace['xaxis'] = 'x1'
                tdata.append(trace)

            if axis == 'right':
                ldata['yaxis2'] = dict(
                        side='right',
                        anchor='x1',
                        overlaying='y1'
                    )
            else:
                ldata['yaxis1'] = dict(
                        side='left',
                        anchor='x1',
                        overlaying='y1'
                    )

            # if 'barmode' in figure.layout:
            #     other_args['barmode'] = figure.layout['barmode']

        ldata['shapes'] = []
        for line in self.hlines:
            ldata['shapes'].append({'x0': 0,
                                    'x1': 1,
                                    'y0': line[0],
                                    'y1': line[0],
                                    'line': {'color': line[1], 'width': 1, 'dash': 'solid'},
                                    'xref': 'paper',
                                    'yref': 'y',
                                    'type': 'line'})
        for line in self.vlines:
            ldata['shapes'].append({'y0': 0,
                                    'y1': 1,
                                    'x0': line[0],
                                    'x1': line[0],
                                    'line': {'color': line[1], 'width': 1, 'dash': 'solid'},
                                    'xref': 'x',
                                    'yref': 'paper',
                                    'type': 'line'})

        for line in self.hspans:
            col = to_rgb(line[2])
            r = str(round(col[0]*255))
            g = str(round(col[1]*255))
            b = str(round(col[2]*255))

            ldata['shapes'].append({'x0': 0,
                                    'x1': 1,
                                    'y0': line[1],
                                    'y1': line[0],
                                    'line': {'color': line[2], 'width': 1, 'dash': 'solid'},
                                    'xref': 'paper',
                                    'yref': 'y',
                                    'type': 'rect',
                                    'fillcolor': 'rgba(' + r + ',' + g + ',' + b + ',.5)'})

        for line in self.vspans:
            col = to_rgb(line[2])
            r = str(round(col[0]*255))
            g = str(round(col[1]*255))
            b = str(round(col[2]*255))

            ldata['shapes'].append({'y0': 0,
                                    'y1': 1,
                                    'x0': line[1],
                                    'x1': line[0],
                                    'line': {'color': line[2], 'width': 1, 'dash': 'solid'},
                                    'xref': 'x',
                                    'yref': 'paper',
                                    'type': 'rect',
                                    'fillcolor': 'rgba(' + r + ',' + g + ',' + b + ',.5)'})

        if title:
            ldata['title'] = title

        if ylabel:
            for k in ldata:
                if 'yaxis' in k:
                    ldata[k] = dict(
                        title=ylabel,
                        titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f',
                        ),
                        showgrid=grid,
                        showline=yaxis,
                        showticklabels=yticks,
                    )

        if xlabel:
            for k in ldata:
                if 'xaxis' in k:
                    ldata['xaxis'] = dict(
                        title=xlabel,
                        titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f',
                        ),
                        showgrid=grid,
                        showline=xaxis,
                        showticklabels=xticks,
                    )

        ldata['showlegend'] = legend
        return FigureWidget(data=tdata, layout=ldata)

    def area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            fig = data[[col]].iplot(fill=True,
                                    asFigure=True,
                                    filename='cufflinks/filled-area',
                                    color=c,
                                    **kwargs)
            self.figures.append((col, fig, y_axis))

    def bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            fig = data[[col]].iplot(kind='bar',
                                    asFigure=True,
                                    bargap=.1,
                                    color=c,
                                    filename='cufflinks/categorical-bar-chart',
                                    **kwargs)
            self.figures.append((col, fig, y_axis))

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            '''barmode (overlay | group | stack)
                bins (int)
                histnorm ('' | 'percent' | 'probability' | 'density' | 'probability density')
                histfunc ('count' | 'sum' | 'avg' | 'min' | 'max')
            '''

            fig = data[[col]].iplot(kind='histogram',
                                    asFigure=True,
                                    bargap=.1,
                                    color=c,
                                    barmode='stack' if stacked else 'overlay',
                                    filename='cufflinks/multiple-histograms',
                                    **kwargs)
            self.figures.append((col, fig, y_axis))

    def hline(self, y, color=None, **kwargs):
        self.hlines.append((y, color))

    def hspan(self, yhigh, ylow, color=None, **kwargs):
        self.hspans.append((yhigh, ylow, color))

    def line(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            fig = data[[col]].iplot(kind='scatter',
                                    asFigure=True,
                                    filename='cufflinks/cf-simple-line',
                                    color=c,
                                    **kwargs)
            self.figures.append((col, fig, y_axis))

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        # Scatter all
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            x = data.columns[0]
            y = data.columns[i]
            c = get_color(i, col, color)
            fig = go.Figure(data=[go.Scatter(
                            x=data[x],
                            y=data[y],
                            mode='markers',
                            marker={'color': c},
                            name='%s vs %s' % (x, y),
                            **kwargs)])
            self.figures.append((col, fig, y_axis))

    def step(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            fig = data[[col]].iplot(kind='scatter',
                                    asFigure=True,
                                    interpolation='hv',
                                    filename='cufflinks/cf-simple-line',
                                    color=c,
                                    **kwargs)
            self.figures.append((col, fig, y_axis))

    def vline(self, x, color=None, **kwargs):
        self.vlines.append((x, color))

    def vspan(self, xhigh, xlow, color=None, **kwargs):
        self.vspans.append((xhigh, xlow, color))
