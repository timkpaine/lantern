import cufflinks as cf
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
from .plotobj import BasePlot
from .plotutils import get_color
from ..utils import in_ipynb


if in_ipynb():
    # cf.go_offline()
    print('Cufflinks loaded')  # plotly grid message prints cufflinks

# _HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# _VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


class CufflinksPlot(BasePlot):
    def __init__(self, theme=None):
        self.figures = []
        self.bars = []

    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        # get before wrapper strips
        other_args = {}

        tdata = []

        for figure in self.figures:
            for trace in figure.data:
                # if y.get(trace.name, 'left') == 'right':
                #     trace.yaxis = 'y2'
                tdata.append(trace)
            if 'barmode' in figure.layout:
                other_args['barmode'] = figure.layout['barmode']

        if title:
            other_args['title'] = title
        if ylabel:
            other_args['yaxis'] = dict(
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
            other_args['xaxis'] = dict(
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

        other_args['showlegend'] = legend

        # if 'right' in y.values():
        #     other_args['yaxis2'] = dict(
        #                            anchor='x',
        #                            overlaying='y',
        #                            side='right'
        #                            )

        fig = go.Figure(data=tdata, layout=other_args)
        return iplot(fig)

    def area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            self.figures.append(data[[col]].iplot(fill=True,
                                asFigure=True,
                                filename='cufflinks/filled-area',
                                color=c,
                                **kwargs))

    def bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            self.figures.append(data[[col]].iplot(kind='bar',
                                asFigure=True,
                                bargap=.1,
                                color=c,
                                filename='cufflinks/categorical-bar-chart',
                                **kwargs))

    def hist(self, data, color=None, y_axis='left', stacked=False, **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            '''barmode (overlay | group | stack)
                bins (int)
                histnorm ('' | 'percent' | 'probability' | 'density' | 'probability density')
                histfunc ('count' | 'sum' | 'avg' | 'min' | 'max')
            '''

            self.figures.append(data[[col]].iplot(kind='histogram',
                                asFigure=True,
                                bargap=.1,
                                color=c,
                                barmode='stack' if stacked else 'overlay',
                                filename='cufflinks/multiple-histograms',
                                **kwargs))

    def line(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            self.figures.append(data[[col]].iplot(kind='scatter',
                                asFigure=True,
                                filename='cufflinks/cf-simple-line',
                                color=c,
                                **kwargs))

    def scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
        # Scatter all
        for i, col in enumerate(data):
            if i == 0:
                continue  # don't scatter against self
            x = data.columns[0]
            y = data.columns[i]
            c = get_color(i, col, color)
            self.figures.append(go.Figure(data=[go.Scatter(
                x=data[x],
                y=data[y],
                mode='markers',
                marker={'color': c},
                name='%s vs %s' % (x, y),
                **kwargs)]))

    def step(self, data, color=None, y_axis='left', **kwargs):
        for i, col in enumerate(data):
            c = get_color(i, col, color)
            self.figures.append(data[[col]].iplot(kind='scatter',
                                asFigure=True,
                                interpolation='hv',
                                filename='cufflinks/cf-simple-line',
                                color=c,
                                **kwargs))
