from ..utils import in_ipynb
import cufflinks as cf
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from .plotobj import BasePlot


if in_ipynb():
    init_notebook_mode(connected=True)
    cf.go_offline()
    print('Cufflinks loaded')

# _HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# _VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


class CufflinksPlot(BasePlot):
    def __init__(self, theme=None):
        self.figures = []

    def show(self, **kwargs):
        # get before wrapper strips
        title = kwargs.get('title', '')
        xlabel = kwargs.get('xlabel', '')
        ylabel = kwargs.get('ylabel', '')
        legend = kwargs.get('legend', True)

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
                    color='#7f7f7f'
                )
            )
        if xlabel:
            other_args['xaxis'] = dict(
                title=xlabel,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
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

    def line(self, data, **kwargs):
        self.figures.append(data.iplot(kind='scatter',
                            asFigure=True,
                            filename='cufflinks/cf-simple-line',
                            **kwargs))
