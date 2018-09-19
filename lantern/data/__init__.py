from .data_cufflinks import getCFData
from .data_sklearn import getSKData
from .other import person, people, company, companies, ticker, currency, trades

# scikit learn
regression = lambda **kwargs: getSKData('regression', **kwargs)
blobs = lambda **kwargs: getSKData('blobs', **kwargs)
classification = lambda **kwargs: getSKData('classification', **kwargs)
multilabel = lambda **kwargs: getSKData('multilabel', **kwargs)
gaussian = lambda **kwargs: getSKData('gaussian', **kwargs)
hastie = lambda **kwargs: getSKData('hastie', **kwargs)
circles = lambda **kwargs: getSKData('circles', **kwargs)
moons = lambda **kwargs: getSKData('moons', **kwargs)
biclusters = lambda **kwargs: getSKData('biclusters', **kwargs)
scurve = lambda **kwargs: getSKData('scurve', **kwargs)
checker = lambda **kwargs: getSKData('checker', **kwargs)
friedman = lambda **kwargs: getSKData('friedman', **kwargs)
friedman2 = lambda **kwargs: getSKData('friedman2', **kwargs)
friedman3 = lambda **kwargs: getSKData('friedman3', **kwargs)

# cufflinks
area = lambda **kwargs: getCFData('area', **kwargs)
bar = lambda **kwargs: getCFData('bar', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)
box = lambda **kwargs: getCFData('box', **kwargs)
bubble = lambda **kwargs: getCFData('bubble', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)
bubble3d = lambda **kwargs: getCFData('bubble3d', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)
candlestick = lambda **kwargs: getCFData('ohlcv', **kwargs)
choropleth = None
density = None
heatmap = lambda **kwargs: getCFData('heatmap', n_x=kwargs.pop('n_x', 20), n_y=kwargs.pop('n_y', 10), **kwargs)
hexbin = None
histogram = lambda **kwargs: getCFData('histogram', n_traces=kwargs.pop('n_traces', 2), n=kwargs.pop('n', 100), **kwargs)
line = lambda **kwargs: getCFData('line', **kwargs)
ohlc = lambda **kwargs: getCFData('ohlc', **kwargs)
ohlcv = lambda **kwargs: getCFData('ohlcv', **kwargs)
pie = lambda **kwargs: getCFData('pie', **kwargs)
scatter = lambda **kwargs: getCFData('scatter', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)
scatter3d = lambda **kwargs: getCFData('scatter3d', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)
scattergeo = None
scattermat = None
spread = None
surface = None
timeseries = lambda **kwargs: getCFData('line', **kwargs)
