from ..plot import plot
from .data_cufflinks import getCFData
from .other import getTsData, getTicker
from .data_sklearn import getSKData


class Style(object):
    def __init__(self, typ, source, sampler, plotter):
        self.type = typ
        self.source = source
        self.sample = lambda: source(**sampler)
        self.sampler = sampler
        self.plotter = plotter

    def show(self):
        return plot(self.source(**self.sampler), **self.plotter)

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

# cufflinks
lines = Style('line',
              getCFData,
              {'type': 'line'},
              {'type': 'line'})

area = Style('line',
             getCFData,
             {'type': 'line'},
             {'type': 'area'})

timeseries = Style('line',
                   getCFData,
                   {'type': 'line'},
                   {'type': 'line'})

scatter = Style('scatter',
                getCFData,
                {'type': 'scatter', 'n_categories': 5, 'n': 10},
                {'type': 'scatter', 'mode': 'markers', 'size': 10, 'symbol': 'x', 'colorscale': 'paired'})

scatter3d = Style('scatter3d',
                  getCFData,
                  {'type': 'scatter3d'},
                  {'type': 'scatter3d'})

bubble = Style('bubble',
               getCFData,
               {'type': 'bubble', 'n_categories': 5, 'n': 10},
               {'type': 'bubble', 'x': 'x', 'y': 'y', 'size': 'size', 'categories': 'categories', 'text': 'text'})

bubble3d = Style('bubble3d',
                 getCFData,
                 {'type': 'bubble3d', 'n_categories': 5, 'n': 10},
                 {'type': 'bubble3d', 'x': 'x', 'y': 'y', 'z': 'z', 'size': 'size', 'categories': 'categories', 'text': 'text'})

pie = Style('pie',
            getCFData,
            {'type': 'pie'},
            {'type': 'pie', 'labels': 'labels', 'values': 'values'})

heat = Style('heatmap',
             getCFData,
             {'type': 'heatmap', 'n_x': 20, 'n_y': 20},
             {'type': 'heatmap'})

bar = Style('bar',
            getCFData,
            {'type': 'bar', 'n_categories': 5, 'n': 10},
            {'type': 'bar'})

ohlc = Style('ohlc',
             getCFData,
             {'type': 'ohlc'},
             {'type': 'ohlc'})
ohlcv = Style('ohlcv',
              getCFData,
              {'type': 'ohlcv'},
              {'type': 'ohlcv'})

box = Style('box',
            getCFData,
            {'type': 'box'},
            {'type': 'box'})

histogram = Style('histogram',
                  getCFData,
                  {'type': 'histogram', 'n_traces': 2, 'n': 100},
                  {'type': 'histogram'})

# FIXME
# scattergeo = Style('scattergeo',
#                    getCFData,
#                    {'type': 'scattergeo'},
#                    {'type': 'scattergeo'})

surface = 'surface'

sinwave = Style('line', getCFData, {'type': 'line'}, {'type': 'sin'})

choropleth = 'choropleth'
stock = 'stock'

# other
simple_ts = 'timeseries'
ticker = 'ticker'


def getData(typ, **kwargs):
    if type == lines:
        return
