from ..utils import in_ipynb
from .plottypes import BasePlotType as p
from .plottypes import BasePlotMap as BPM
from .plottypes import lookup
import cufflinks as cf
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go


if in_ipynb():
    init_notebook_mode(connected=True)
    cf.go_offline()
    print('Cufflinks loaded')

_HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
_VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}

# FIXME
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


class CufflinksPlotMap(BPM):
    @staticmethod
    def setup(**kwargs):
        if not in_ipynb():
            raise Exception('Cufflinks currently unsupported outside of notebooks')

    @staticmethod
    def args(plottype):
        return {
          p.BAR: {'bargap': .1},
          p.GROUPEDBAR: {'bargap': .1},
          p.STACKEDBAR: {'bargap': .1},
          p.HORIZONTALBAR: {'bargap': .1},
          p.HORIZONTALSTACKEDBAR: {'bargap': .1},
          p.HISTOGRAM: {'bins': None,
                        'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                        'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
          p.GROUPEDHIST: {'bins': None,
                          'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                          'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
          p.STACKEDHIST: {'bins': None,
                          'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                          'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
          # 'subplothist': {'bins': None,
          #                 'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
          #                 'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
        }.get(lookup(plottype), {})

    @staticmethod
    def _wrapper(**kwargs):
        if 'type' in kwargs:
            kwargs.pop('type', None)
        if 'raw' in kwargs:
            kwargs['asFigure'] = kwargs.pop('raw')
        else:
            kwargs['asFigure'] = False

        if 'colors' in kwargs:
            # no op
            # just do it so it looks the same as matplotlib
            kwargs['colors'] = kwargs['colors']
        else:
            kwargs['colors'] = None

        # purge from subplot calls, only use for main plot command
        kwargs.pop('xlabel', None)
        kwargs.pop('ylabel', None)
        kwargs.pop('title', None)
        kwargs.pop('x', None)
        kwargs.pop('y', None)
        return kwargs

    @staticmethod
    def plot(data, **kwargs):
        # get before wrapper strips
        title = kwargs.get('title', '')
        xlabel = kwargs.get('xlabel', '')
        ylabel = kwargs.get('ylabel', '')
        legend = kwargs.get('legend', True)
        x = kwargs.get('x', {})
        y = kwargs.get('y', {})

        kwargs = CufflinksPlotMap._wrapper(**kwargs)

        other_args = {}

        if isinstance(data, list):
            tdata = []

            for figure in data:
                for trace in figure.data:
                    if y.get(trace.name, 'left') == 'right':
                        trace.yaxis = 'y2'
                    tdata.append(trace)
                if 'barmode' in figure.layout:
                    other_args['barmode'] = figure.layout['barmode']
            data = tdata

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

        if 'right' in y.values():
            other_args['yaxis2'] = dict(
                                   anchor='x',
                                   overlaying='y',
                                   side='right'
                                   )

        fig = go.Figure(data=tdata, layout=other_args)
        return iplot(fig)

    @staticmethod
    def setTheme(theme='pearl'):
        if theme not in cf.getThemes():
            cf.set_config_file(theme='pearl')
        else:
            cf.set_config_file(theme)

    @staticmethod
    def getTheme():
        pass

    @staticmethod
    def themes():
        return cf.getThemes()

    @staticmethod
    def area(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        return data.iplot(fill=True,
                          filename='cufflinks/filled-area',
                          **kwargs)

    @staticmethod
    def basic(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        if type == 'line0':
            return iplot([{
                'x': data.index,
                'y': data[col],
                'name': col
                } for col in data.columns])

    @staticmethod
    def bar(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bargap = kwargs.pop('bargap', CufflinksPlotMap.args(p.BAR)['bargap'])

        return data.iplot(kind='bar',
                          bargap=bargap,
                          filename='cufflinks/categorical-bar-chart',
                          **kwargs)

    @staticmethod
    def bubble(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        size = scatter.pop('size', data.columns[0])
        text = scatter.pop('text', data.columns[0])
        categories = scatter.pop('categories', data.columns[0])
        return data.iplot(kind='bubble',
                          x=x,
                          y=y,
                          size=size,
                          text=text,
                          categories=categories,
                          filename='cufflinks/simple-bubble-chart',
                          **kwargs)

    @staticmethod
    def box(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        return data.iplot(kind='box',
                          filename='cufflinks/box-plots',
                          **kwargs)

    @staticmethod
    def groupedbar(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bargap = kwargs.pop('bargap', CufflinksPlotMap.args(p.GROUPEDBAR)['bargap'])

        return data.iplot(kind='bar',
                          bargap=bargap,
                          filename='cufflinks/grouped-bar-chart',
                          **kwargs)

    @staticmethod
    def groupedhist(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bins = kwargs.pop('bins', CufflinksPlotMap.args(p.GROUPEDHIST)['bins'])
        histnorm = kwargs.pop('histnorm', CufflinksPlotMap.args(p.GROUPEDHIST)['histnorm'][0])
        histfunc = kwargs.pop('histfunc', CufflinksPlotMap.args(p.GROUPEDHIST)['histfunc'][0])

        return data.iplot(kind='histogram',
                          barmode='group',
                          bins=bins,
                          histnorm=histnorm,
                          histfunc=histfunc,
                          filename='cufflinks/basic-histogram',
                          **kwargs)

    @staticmethod
    def horizontalbar(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bargap = kwargs.pop('bargap', CufflinksPlotMap.args(p.HORIZONTALBAR)['bargap'])

        return data.iplot(kind='barh',
                          bargap=bargap,
                          filename='cufflinks/barh',
                          **kwargs)

    @staticmethod
    def heatmap(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        colorscale = kwargs.pop('colorscale', 'spectral')
        return data.iplot(kind='heatmap',
                          colorscale=colorscale,
                          filename='cufflinks/simple-heatmap',
                          **kwargs)

    @staticmethod
    def horizontalstackedbar(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bargap = kwargs.pop('bargap', CufflinksPlotMap.args(p.HORIZONTALSTACKEDBAR)['bargap'])
        return data.iplot(kind='barh',
                          barmode='stack',
                          bargap=bargap,
                          filename='cufflinks/barh',
                          **kwargs)

    @staticmethod
    def histogram(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bins = kwargs.pop('bins', CufflinksPlotMap.args(p.HISTOGRAM)['bins'])
        histnorm = kwargs.pop('histnorm', CufflinksPlotMap.args(p.HISTOGRAM)['histnorm'][0])
        histfunc = kwargs.pop('histfunc', CufflinksPlotMap.args(p.HISTOGRAM)['histfunc'][0])

        return data.iplot(kind='histogram',
                          bins=bins,
                          histnorm=histnorm,
                          histfunc=histfunc,
                          filename='cufflinks/basic-histogram',
                          **kwargs)

    @staticmethod
    def line(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        return data.iplot(kind='scatter',
                          # subplots=kwargs.get('subplots', False),
                          # hline=kwargs.get('hline', []),
                          # vline=kwargs.get('vline', []),
                          # hspan=kwargs.get('hspan', _HSPAN_NONE),
                          # vspan=kwargs.get('vspan', _VSPAN_NONE),
                          # bestfit=kwargs.get('bestfit', False),
                          # bestfit_colors=kwargs.get('bestfit_colors', []),
                          filename='cufflinks/cf-simple-line',
                          **kwargs)

    @staticmethod
    def ohlc(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        legend = kwargs.pop('legend', 'top')
        qf = cf.QuantFig(data, legend=legend)
        # qf.add_sma([10, 20], width=2, color=['green', 'lightgreen'], legendgroup=True)
        qf.add_bollinger_bands()
        # qf.add_volume()
        # qf.add_macd()
        # qf.add_rsi(periods=20, color='java')
        return qf.iplot()

    @staticmethod
    def ohlcv(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        legend = kwargs.pop('legend', 'top')
        qf = cf.QuantFig(data, legend=legend)
        qf.add_sma([10, 20], width=2, color=['green', 'lightgreen'], legendgroup=True)
        qf.add_bollinger_bands(periods=20, boll_std=2, colors=['magenta', 'grey'], fill=True)
        qf.add_volume()
        qf.add_macd()
        qf.add_rsi(periods=20, color='java')
        return qf.iplot()

    @staticmethod
    def pie(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        labels = scatter.pop('labels', data.columns[0])
        values = scatter.pop('values', data.columns[0])
        return data.iplot(kind='pie',
                          labels=labels,
                          values=values,
                          **kwargs)

    @staticmethod
    def scatter(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        scatter = kwargs.pop('scatter', {})
        x = scatter.pop('x', data.columns[0])
        y = scatter.pop('y', data.columns[0])
        categories = scatter.pop('categories', data.columns[0])
        size = scatter.pop('size', 10)
        mode = kwargs.pop('mode', 'markers')
        return data.iplot(kind='scatter',
                          mode=mode,
                          x=x,
                          y=y,
                          size=size,
                          categories=categories,
                          filename='cufflinks/simple-scatter',
                          **kwargs)

    @staticmethod
    def scattermatrix(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        return data.scatter_matrix(filename='cufflinks/scatter-matrix-subplot',
                                   **kwargs)

    @staticmethod
    def spread(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)

        return data.iplot(kind='spread',
                          fill=True,
                          filename='cufflinks/cf-simple-line',
                          **kwargs)

    @staticmethod
    def stackedbar(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bargap = kwargs.pop('bargap', CufflinksPlotMap.args(p.STACKEDBAR)['bargap'])

        return data.iplot(kind='bar',
                          barmode='stack',
                          bargap=bargap,
                          filename='cufflinks/grouped-bar-chart',
                          **kwargs)

    @staticmethod
    def stackedhist(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        bins = kwargs.pop('bins', CufflinksPlotMap.args(p.STACKEDHIST)['bins'])
        histnorm = kwargs.pop('histnorm', CufflinksPlotMap.args(p.STACKEDHIST)['histnorm'][0])
        histfunc = kwargs.pop('histfunc', CufflinksPlotMap.args(p.STACKEDHIST)['histfunc'][0])

        return data.iplot(kind='histogram',
                          barmode='stack',
                          bins=bins,
                          histnorm=histnorm,
                          histfunc=histfunc,
                          filename='cufflinks/basic-histogram',
                          **kwargs)

    @staticmethod
    def subplothist(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        shape = kwargs.pop('shape', (len(data.columns), 1))
        bins = kwargs.pop('bins', CufflinksPlotMap.args('subplothist')['bins'])
        histnorm = kwargs.pop('histnorm', CufflinksPlotMap.args('subplothist')['histnorm'][0])
        histfunc = kwargs.pop('histfunc', CufflinksPlotMap.args('subplothist')['histfunc'][0])

        return data.iplot(kind='histogram',
                          subplots=True,
                          shape=shape,
                          bins=bins,
                          histnorm=histnorm,
                          histfunc=histfunc,
                          filename='cufflinks/histogram-subplots',
                          **kwargs)

    @staticmethod
    def stackedarea(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        fill = kwargs.pop('fill', True)

        return data.iplot(kind='area',
                          fill=fill,
                          filename='cuflinks/stacked-area',
                          **kwargs)

    @staticmethod
    def multiscatter(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        # TODO
        # fig = {
        #     'data': [
        #         {'x': df2007.gdpPercap, 'y': df2007.lifeExp, 'text': df2007.country, 'mode': 'markers', 'name': '2007'},
        #         {'x': df1952.gdpPercap, 'y': df1952.lifeExp, 'text': df1952.country, 'mode': 'markers', 'name': '1952'}
        #     ],
        #     'layout': {
        #         'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        #         'yaxis': {'title': "Life Expectancy"}
        #     }
        # }
        # return py.iplot(fig, filename='cufflinks/multiple-scatter')
        raise Exception('Not implemented')

    @staticmethod
    def groupedscatter(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        # TODO
        #         py.iplot(
        #     {
        #         'data': [
        #             {
        #                 'x': df[df['year']==year]['gdpPercap'],
        #                 'y': df[df['year']==year]['lifeExp'],
        #                 'name': year, 'mode': 'markers',
        #             } for year in [1952, 1982, 2007]
        #         ],
        #         'layout': {
        #             'xaxis': {'title': 'GDP per Capita', 'type': 'log'},
        #             'yaxis': {'title': "Life Expectancy"}
        #         }
        # }, filename='cufflinks/scatter-group-by')
        raise NotImplementedError()

    @staticmethod
    def candlestick(data, **kwargs):
        kwargs = CufflinksPlotMap._wrapper(**kwargs)
        raise NotImplementedError()

    @staticmethod
    def density(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def lmplot(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def hexbin(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def pairplot(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def probplot(data, **kwargs):
        raise NotImplementedError()
