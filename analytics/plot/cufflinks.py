from plotly.offline import init_notebook_mode, iplot
import cufflinks as cf

init_notebook_mode(connected=True)
cf.go_offline()


def themes():
    return cf.getThemes()


_HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
_VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}


def plot(data, type='line', theme='pearl', **kwargs):
    if theme not in cf.getThemes():
        cf.set_config_file(theme='pearl')
    else:
        cf.set_config_file(theme)

    type = str(type)
    print(type)
    if type == 'line0':
        return iplot([{
            'x': data.index,
            'y': data[col],
            'name': col
            } for col in data.columns])
    elif type == 'line':
        return data.iplot(kind='scatter',
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          color=kwargs.get('colors', []),
                          bestfit=kwargs.get('bestfit', False),
                          bestfit_colors=kwargs.get('bestfit_colors', []),
                          filename='cufflinks/cf-simple-line')
    elif type == 'area':
        return data.iplot(kind='scatter',
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          fill=True,
                          color=kwargs.get('colors', []),
                          bestfit=kwargs.get('bestfit', False),
                          bestfit_colors=kwargs.get('bestfit_colors', []),
                          filename='cufflinks/cf-simple-line')
    elif type == 'bar':
        return data.iplot(kind='bar',
                          subplots=kwargs.get('subplots', False),
                          bargap=kwargs.get('bargap', KWARGS['bar']['bargap']),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/categorical-bar-chart')
    elif type == 'groupedbar':
        return data.iplot(kind='bar',
                          bargap=kwargs.get('bargap', KWARGS['groupedbar']['bargap']),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/grouped-bar-chart')
    elif type == 'stackedbar':
        return data.iplot(kind='bar',
                          barmode='stack',
                          bargap=kwargs.get('bargap', KWARGS['stackedbar']['bargap']),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/grouped-bar-chart')
    elif type == 'horizontalbar':
        return data.iplot(kind='barh',
                          bargap=kwargs.get('bargap', KWARGS['horizontalbar']['bargap']),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/barh')
    elif type == 'horizontalstackedbar':
        return data.iplot(kind='barh',
                          barmode='stack',
                          bargap=kwargs.get('bargap', KWARGS['horizontalstackedbar']['bargap']),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/barh')
    elif type == 'hist':
        return data.iplot(kind='histogram',
                          bins=kwargs.get('bins', KWARGS['hist']['bins']),
                          histnorm=kwargs.get('histnorm', KWARGS['hist']['histnorm'][0]),
                          histfunc=kwargs.get('histfunc', KWARGS['hist']['histfunc'][0]),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/basic-histogram')
    elif type == 'groupedhist':
        return data.iplot(kind='histogram',
                          barmode='group',
                          bins=kwargs.get('bins', KWARGS['groupedhist']['bins']),
                          histnorm=kwargs.get('histnorm', KWARGS['groupedhist']['histnorm'][0]),
                          histfunc=kwargs.get('histfunc', KWARGS['groupedhist']['histfunc'][0]),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/basic-histogram')
    elif type == 'stackedhist':
        return data.iplot(kind='histogram',
                          barmode='stack',
                          bins=kwargs.get('bins', KWARGS['stackedhist']['bins']),
                          histnorm=kwargs.get('histnorm', KWARGS['stackedhist']['histnorm'][0]),
                          histfunc=kwargs.get('histfunc', KWARGS['stackedhist']['histfunc'][0]),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _HSPAN_NONE),
                          filename='cufflinks/basic-histogram')
    elif type == 'subplothist':
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
                          filename='cufflinks/histogram-subplots')
    elif type == 'box':
        return data.iplot(kind='box',
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/box-plots')
    elif type == 'stackedarea':
        return data.iplot(kind='area',
                          fill=kwargs.get('fill', True),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cuflinks/stacked-area')
    elif type == 'filledarea':
        return data.iplot(fill=True,
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cuflinks/filled-area')
    elif type == 'scatter':
        x = kwargs.get('x', data.columns[0])
        y = kwargs.get('y', data.columns[1]) if len(data.columns) > 1 else kwargs.get('y', data.columns[0])
        return data.iplot(kind='scatter',
                          mode='markers',
                          x=x,
                          y=y,
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/simple-scatter')
    elif type == 'bubble':
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
                          filename='cufflinks/simple-bubble-chart')
    elif type == 'scattermatrix' or type == 'scattermat':
        return data.scatter_matrix(filename='cufflinks/scatter-matrix-subplot')
    elif type == 'heatmat':
        return data.iplot(kind='heatmap',
                          colorscale=kwargs.get('colorscale', 'spectral'),
                          subplots=kwargs.get('subplots', False),
                          hline=kwargs.get('hline', []),
                          vline=kwargs.get('vline', []),
                          hspan=kwargs.get('hspan', _HSPAN_NONE),
                          vspan=kwargs.get('vspan', _VSPAN_NONE),
                          filename='cufflinks/simple-heatmap')
    elif type == 'multiscatter':
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
        pass
    elif type == 'groupedscatter':
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
        pass


# FIXME
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


KWARGS = {
    'bar': {'bargap': .1},
    'groupedbar': {'bargap': .1},
    'stackedbar': {'bargap': .1},
    'horizontalbar': {'bargap': .1},
    'horizontalstackedbar': {'bargap': .1},
    'hist': {'bins': None,
             'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
             'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
    'groupedhist': {'bins': None,
                    'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                    'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
    'stackedhist': {'bins': None,
                    'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                    'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
    'subplothist': {'bins': None,
                    'histnorm': ['', 'percent', 'probability', 'density', 'probability density'],
                    'histfunc': ['count', 'sum', 'avg', 'min', 'max']},
}


def kwargs(which=None):
    return KWARGS.get(which, KWARGS)
