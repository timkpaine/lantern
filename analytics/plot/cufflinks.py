from .plottypes import PlotType as p
import cufflinks as cf

from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True)
cf.go_offline()


_HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
_VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}


def _wrapper(data, type=p.PLOT, raw=False, colors=None, **kwargs):
    if raw:
        kwargs['asFigure'] = True
    if colors:
        # so it looks the same as matplotlib
        kwargs['colors'] = colors
    return _plotmap_internal[type](data, **kwargs)


def plot(data, **kwargs):
    if isinstance(data, list):
        tdata = []

        for figure in data:
            for trace in figure.data:
                tdata.append(trace)
        data = tdata
        # data = [x.data[i] for x in data for i in x.data]
    return iplot(data)


def basic(data, **kwargs):
    if type == 'line0':
        return iplot([{
            'x': data.index,
            'y': data[col],
            'name': col
            } for col in data.columns])


def line(data, **kwargs):
    return data.iplot(kind='scatter',
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      bestfit=kwargs.get('bestfit', False),
                      bestfit_colors=kwargs.get('bestfit_colors', []),
                      filename='cufflinks/cf-simple-line',
                      **kwargs)


def area(data, **kwargs):
        return data.iplot(kind='area',
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          fill=True,
                          bestfit=kwargs.get('bestfit', False),
                          bestfit_colors=kwargs.get('bestfit_colors', []),
                          filename='cufflinks/filled-area',
                          **kwargs)


def spread(data, **kwargs):
    return data.iplot(kind='spread',
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      fill=True,
                      bestfit=kwargs.get('bestfit', False),
                      bestfit_colors=kwargs.get('bestfit_colors', []),
                      filename='cufflinks/cf-simple-line',
                      **kwargs)


def bar(data, **kwargs):
    return data.iplot(kind='bar',
                      subplots=kwargs.get('subplots', False),
                      bargap=kwargs.get('bargap', KWARGS[p.BAR]['bargap']),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/categorical-bar-chart',
                      **kwargs)


def groupedbar(data, **kwargs):
    return data.iplot(kind='bar',
                      bargap=kwargs.get('bargap', KWARGS[p.GROUPEDBAR]['bargap']),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/grouped-bar-chart',
                      **kwargs)


def stackedbar(data, **kwargs):
    return data.iplot(kind='bar',
                      barmode='stack',
                      bargap=kwargs.get('bargap', KWARGS[p.STACKEDBAR]['bargap']),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/grouped-bar-chart',
                      **kwargs)


def horizontalbar(data, **kwargs):
    return data.iplot(kind='barh',
                      bargap=kwargs.get('bargap', KWARGS[p.HORIZONTALBAR]['bargap']),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/barh',
                      **kwargs)


def horizontalstackedbar(data, **kwargs):
    return data.iplot(kind='barh',
                      barmode='stack',
                      bargap=kwargs.get('bargap', KWARGS[p.HORIZONTALSTACKEDBAR]['bargap']),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/barh',
                      **kwargs)


def histogram(data, **kwargs):
    return data.iplot(kind='histogram',
                      bins=kwargs.get('bins', KWARGS[p.HISTOGRAM]['bins']),
                      histnorm=kwargs.get('histnorm', KWARGS[p.HISTOGRAM]['histnorm'][0]),
                      histfunc=kwargs.get('histfunc', KWARGS[p.HISTOGRAM]['histfunc'][0]),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/basic-histogram',
                      **kwargs)


def groupedhist(data, **kwargs):
    return data.iplot(kind='histogram',
                      barmode='group',
                      bins=kwargs.get('bins', KWARGS[p.GROUPEDHIST]['bins']),
                      histnorm=kwargs.get('histnorm', KWARGS[p.GROUPEDHIST]['histnorm'][0]),
                      histfunc=kwargs.get('histfunc', KWARGS[p.GROUPEDHIST]['histfunc'][0]),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/basic-histogram',
                      **kwargs)


def stackedhist(data, **kwargs):
    return data.iplot(kind='histogram',
                      barmode='stack',
                      bins=kwargs.get('bins', KWARGS['stackedhist']['bins']),
                      histnorm=kwargs.get('histnorm', KWARGS[p.STACKEDHIST]['histnorm'][0]),
                      histfunc=kwargs.get('histfunc', KWARGS[p.STACKEDHIST]['histfunc'][0]),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _HSPAN_NONE),
                      filename='cufflinks/basic-histogram',
                      **kwargs)


def subplothist(data, **kwargs):
    return data.iplot(kind='histogram',
                      subplots=True,
                      shape=kwargs.get('shape', (len(data.columns), 1)),
                      bins=kwargs.get('bins', KWARGS['subplothist']['bins']),
                      histnorm=kwargs.get('histnorm', KWARGS['subplothist']['histnorm'][0]),
                      histfunc=kwargs.get('histfunc', KWARGS['subplothist']['histfunc'][0]),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/histogram-subplots',
                      **kwargs)


def box(data, **kwargs):
    return data.iplot(kind='box',
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/box-plots',
                      **kwargs)


def pie(data, **kwargs):
    return data.iplot(kind='pie',
                      labels=kwargs.get('labels', 'labels'),
                      values=kwargs.get('values', 'values'),
                      subplots=kwargs.get('subplots', False),
                      **kwargs)


def stackedarea(data, **kwargs):
    return data.iplot(kind='area',
                      fill=kwargs.get('fill', True),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cuflinks/stacked-area',
                      **kwargs)


def scatter(data, **kwargs):
    x = kwargs.get('x', data.columns[0])
    y = kwargs.get('y', data.columns[1]) if len(data.columns) > 1 else kwargs.get('y', data.columns[0])
    return data.iplot(kind='scatter',
                      mode='markers',
                      x=x,
                      y=y,
                      size=kwargs.get('size', None),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      bestfit=kwargs.get('bestfit', None),
                      bestfit_colors=kwargs.get('bestfit_colors', []),
                      filename='cufflinks/simple-scatter',
                      **kwargs)


def bubble(data, **kwargs):
    x = kwargs.get('x', data.columns[0])
    y = kwargs.get('y', data.columns[1]) if len(data.columns) > 1 else kwargs.get('y', data.columns[0])
    size = kwargs.get('size', data.columns[1]) if len(data.columns) > 1 else kwargs.get('size', data.columns[0])
    return data.iplot(kind='bubble',
                      x=x,
                      y=y,
                      size=size,
                      text=kwargs.get('text', None),
                      categories=kwargs.get('categories', None),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      bestfit=kwargs.get('bestfit', None),
                      bestfit_colors=kwargs.get('bestfit_colors', []),
                      filename='cufflinks/simple-bubble-chart',
                      **kwargs)


def scattermatrix(data, **kwargs):
    return data.scatter_matrix(filename='cufflinks/scatter-matrix-subplot',
                               **kwargs)


def heatmap(data, **kwargs):
    return data.iplot(kind='heatmap',
                      colorscale=kwargs.get('colorscale', 'spectral'),
                      subplots=kwargs.get('subplots', False),
                      hline=kwargs.get('hline', []),
                      vline=kwargs.get('vline', []),
                      hspan=kwargs.get('hspan', _HSPAN_NONE),
                      vspan=kwargs.get('vspan', _VSPAN_NONE),
                      filename='cufflinks/simple-heatmap',
                      **kwargs)


def multiscatter(data, **kwargs):
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


def groupedscatter(data, **kwargs):
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
    raise Exception('Not implemented')


def ohlcv(data, **kwargs):
    return cf.QuantFig(data,
                       legend=kwargs.get('legend', 'top')).iplot()


def candlestick(data, **kwargs):
    raise Exception('Not implemented')

# FIXME
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


KWARGS = {
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
    'subplothist': {'bins': None,
                    'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                    'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
}


def kwargs(which=None):
    return KWARGS.get(which, KWARGS)


def setTheme(theme='pearl'):
    if theme not in cf.getThemes():
        cf.set_config_file(theme='pearl')
    else:
        cf.set_config_file(theme)


def themes():
    return cf.getThemes()


_plotmap_internal = {
    p.PLOT: plot,
    p.BASIC: basic,
    p.LINE: line,
    p.SPREAD: spread,
    p.BAR: bar,
    p.GROUPEDBAR: groupedbar,
    p.STACKEDBAR: stackedbar,
    p.HORIZONTALBAR: horizontalbar,
    p.HORIZONTALSTACKEDBAR: horizontalstackedbar,
    p.HISTOGRAM: histogram,
    p.GROUPEDHIST: groupedhist,
    p.STACKEDHIST: stackedhist,
    p.BOX: box,
    p.PIE: pie,
    p.AREA: area,
    p.STACKEDAREA: stackedarea,
    p.SCATTER: scatter,
    p.BUBBLE: bubble,
    p.SCATTERMATRIX: scattermatrix,
    p.HEATMAP: heatmap,
    p.MULTISCATTER: multiscatter,
    p.GROUPEDSCATTER: groupedscatter,
    p.OHLC: ohlcv,
    p.OHLVC: ohlcv,
    p.CANDLESTICK: candlestick
}

_plotmap = {
    p.PLOT: _wrapper,
    p.BASIC: _wrapper,
    p.LINE: _wrapper,
    p.SPREAD: _wrapper,
    p.BAR: _wrapper,
    p.GROUPEDBAR: _wrapper,
    p.STACKEDBAR: _wrapper,
    p.HORIZONTALBAR: _wrapper,
    p.HORIZONTALSTACKEDBAR: _wrapper,
    p.HISTOGRAM: _wrapper,
    p.GROUPEDHIST: _wrapper,
    p.STACKEDHIST: _wrapper,
    p.BOX: _wrapper,
    p.PIE: _wrapper,
    p.AREA: _wrapper,
    p.STACKEDAREA: _wrapper,
    p.SCATTER: _wrapper,
    p.BUBBLE: _wrapper,
    p.SCATTERMATRIX: _wrapper,
    p.HEATMAP: _wrapper,
    p.MULTISCATTER: _wrapper,
    p.GROUPEDSCATTER: _wrapper,
    p.OHLC: _wrapper,
    p.OHLVC: _wrapper,
    p.CANDLESTICK: _wrapper
}
