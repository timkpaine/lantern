# from ..plotting import plot
from .data_cufflinks import getCFData
# from .data_sklearn import getSKData


class Style(object):
    def __init__(self, typ, source, sampler, plotter):
        self.type = typ
        self.source = source
        self.sample = lambda: source(**sampler)
        self.sampler = sampler
        self.plotter = plotter

    # def show(self):
    #     return plot(self.source(**self.sampler), **self.plotter)

    def __eq__(self, other):
        return self.type.lower() == other.lower()

    def getData(self, **kwargs):
        return self.source(self.type, **kwargs)

    def __str__(self):
        return self.type

    def __repr__(self):
        return self.sample().__repr__()

    def _repr_html_(self):
        return self.sample()._repr_html_()

# scikit learn
REGRESSION = 'regression'
BLOBS = 'blobs'
CLASSIFICATION = 'classification'
MULTILABEL = 'multilabel'
GAUSSIAN = 'gaussian'
HASTIE = 'hastie'
CIRCLES = 'circles'
MOONS = 'moons'
BICLUSTERS = 'biclusters'
SCURVE = 'scurve'
CHECKER = 'checker'
FRIEDMAN = 'friedman'
FRIEDMAN2 = 'friedman2'
FRIEDMAN3 = 'friedman3'

# plotting
AREA = 'area'
BASIC = 'basic'
BAR = 'bar'
BOX = 'box'
BUBBLE = 'bubble'
BUBBLE3D = 'bubble3d'
CANDLESTICK = 'candlestick'
DENSITY = 'density'
GROUPEDBAR = 'groupedbar'
GROUPEDHIST = 'groupedhist'
GROUPEDSCATTER = 'groupedscatter'
HEATMAP = 'heatmap'
HEXBIN = 'hexbin'
HISTOGRAM = 'histogram'
HORIZONTALBAR = 'horizontalbar'
HORIZONTALSTACKEDBAR = 'horizontalstackedbar'
LINE = 'line'
MULTISCATTER = 'multiscatter'
OHLC = 'ohlc'
OHLVC = 'ohlcv'
PAIRPLOT = 'pairplot'
PIE = 'pie'
SCATTER = 'scatter'
SCATTER3D = 'scatter3d'
SCATTERMATRIX = 'scattermatrix'
SPREAD = 'spread'
STACKEDBAR = 'stackedbar'
STACKEDHIST = 'stackedhist'
STACKEDAREA = 'stackedarea'

# cufflinks
area = Style('area',
             getCFData,
             {'type': 'line'},
             {'type': 'area'})

bar = Style('bar',
            getCFData,
            {'type': 'bar', 'n_categories': 5, 'n': 10},
            {'type': 'bar'})

box = Style('box',
            getCFData,
            {'type': 'box'},
            {'type': 'box'})

bubble = Style('bubble',
               getCFData,
               {'type': 'bubble', 'n_categories': 5, 'n': 10},
               {'type': 'bubble', 'scatter': {'x': {'x': 'x', 'y': 'y', 'size': 'size', 'categories': 'categories', 'text': 'text'}}})

# bubble3d = Style('bubble3d',
#                  getCFData,
#                  {'type': 'bubble3d', 'n_categories': 5, 'n': 10},
#                  {'type': 'bubble3d', 'x': 'x', 'y': 'y', 'z': 'z', 'size': 'size', 'categories': 'categories', 'text': 'text'})

candlestick = None
choropleth = None
density = None

groupedbar = Style('groupedbar',
                   getCFData,
                   {'type': 'bar', 'n_categories': 5, 'n': 10},
                   {'type': 'groupedbar'})

groupedhist = Style('histogram',
                    getCFData,
                    {'type': 'histogram', 'n_traces': 2, 'n': 100},
                    {'type': 'groupedhist'})

groupedscatter = Style('scatter',
                       getCFData,
                       {'type': 'scatter', 'n_categories': 5, 'n': 10},
                       {'type': 'groupedscatter', 'mode': 'markers', 'size': 10, 'x': 'x', 'y': 'y', 'categories': 'categories', 'text': 'text', 'symbol': 'x', 'colorscale': 'paired'})


heatmap = Style('heatmap',
                getCFData,
                {'type': 'heatmap', 'n_x': 20, 'n_y': 20},
                {'type': 'heatmap'})


hexbin = None

histogram = Style('histogram',
                  getCFData,
                  {'type': 'histogram', 'n_traces': 2, 'n': 100},
                  {'type': 'histogram'})

horizontalbar = Style('horizontalbar',
                      getCFData,
                      {'type': 'bar', 'n_categories': 5, 'n': 10},
                      {'type': 'horizontalbar'})

horizontalstackedbar = Style('horizontalstackedbar',
                             getCFData,
                             {'type': 'bar', 'n_categories': 5, 'n': 10},
                             {'type': 'horizontalstackedbar'})

line = Style('line',
             getCFData,
             {'type': 'line'},
             {'type': 'line'})

multiscatter = None

ohlc = Style('ohlc',
             getCFData,
             {'type': 'ohlc'},
             {'type': 'ohlc'})
ohlcv = Style('ohlcv',
              getCFData,
              {'type': 'ohlcv'},
              {'type': 'ohlcv'})

pairplot = None

pie = Style('pie',
            getCFData,
            {'type': 'pie'},
            {'type': 'pie', 'scatter': {'values': {'labels': 'labels', 'values': 'values'}}})

scatter = Style('scatter',
                getCFData,
                {'type': 'scatter', 'n_categories': 5, 'n': 10},
                {'type': 'scatter', 'mode': 'markers', 'scatter': {'x': {'x': 'x', 'y': 'y', 'size': 'size', 'categories': 'categories', 'text': 'text'}}, 'symbol': 'x', 'colorscale': 'paired'})

# scatter3d = Style('scatter3d',
#                   getCFData,
#                   {'type': 'scatter3d'},
#                   {'type': 'scatter3d', 'mode': 'markers', 'size': 10, 'x': 'x', 'y': 'y', 'z': 'z', 'categories': 'categories', 'text': 'text', 'symbol': 'x', 'colorscale': 'paired'})

# FIXME
# scattergeo = Style('scattergeo',
#                    getCFData,
#                    {'type': 'scattergeo'},
#                    {'type': 'scattergeo'})

scattermat = None
spread = None

stackedarea = Style('line',
                    getCFData,
                    {'type': 'line'},
                    {'type': 'stackedarea'})

stackedbar = Style('stackedbar',
                   getCFData,
                   {'type': 'bar', 'n_categories': 5, 'n': 10},
                   {'type': 'stackedbar'})

stackedhist = Style('histogram',
                    getCFData,
                    {'type': 'histogram', 'n_traces': 2, 'n': 100},
                    {'type': 'stackedhist'})
surface = None

timeseries = Style('line',
                   getCFData,
                   {'type': 'line'},
                   {'type': 'line'})
