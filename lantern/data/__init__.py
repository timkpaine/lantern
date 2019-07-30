try:
    from .data_cufflinks import getCFData
except ImportError:
    getCFData = lambda **kwargs: None  # noqa: E731

try:
    from .data_sklearn import getSKData
except ImportError:
    getSKData = lambda **kwargs: None  # noqa: E731

from .other import person, people, company, companies, ticker, currency, trades, superstore  # noqa: F401

# scikit learn
regression = lambda **kwargs: getSKData('regression', **kwargs)  # noqa: E731
blobs = lambda **kwargs: getSKData('blobs', **kwargs)  # noqa: E731
classification = lambda **kwargs: getSKData('classification', **kwargs)  # noqa: E731
multilabel = lambda **kwargs: getSKData('multilabel', **kwargs)  # noqa: E731
gaussian = lambda **kwargs: getSKData('gaussian', **kwargs)  # noqa: E731
hastie = lambda **kwargs: getSKData('hastie', **kwargs)  # noqa: E731
circles = lambda **kwargs: getSKData('circles', **kwargs)  # noqa: E731
moons = lambda **kwargs: getSKData('moons', **kwargs)  # noqa: E731
biclusters = lambda **kwargs: getSKData('biclusters', **kwargs)  # noqa: E731
scurve = lambda **kwargs: getSKData('scurve', **kwargs)  # noqa: E731
checker = lambda **kwargs: getSKData('checker', **kwargs)  # noqa: E731
friedman = lambda **kwargs: getSKData('friedman', **kwargs)  # noqa: E731
friedman2 = lambda **kwargs: getSKData('friedman2', **kwargs)  # noqa: E731
friedman3 = lambda **kwargs: getSKData('friedman3', **kwargs)  # noqa: E731

# cufflinks
area = lambda **kwargs: getCFData('area', **kwargs)  # noqa: E731
bar = lambda **kwargs: getCFData('bar', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)  # noqa: E731
box = lambda **kwargs: getCFData('box', **kwargs)  # noqa: E731
bubble = lambda **kwargs: getCFData('bubble', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)  # noqa: E731
bubble3d = lambda **kwargs: getCFData('bubble3d', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)  # noqa: E731
candlestick = lambda **kwargs: getCFData('ohlcv', **kwargs)  # noqa: E731
choropleth = None
density = None
heatmap = lambda **kwargs: getCFData('heatmap', n_x=kwargs.pop('n_x', 20), n_y=kwargs.pop('n_y', 10), **kwargs)  # noqa: E731
hexbin = None
histogram = lambda **kwargs: getCFData('histogram', n_traces=kwargs.pop('n_traces', 2), n=kwargs.pop('n', 100), **kwargs)  # noqa: E731
line = lambda **kwargs: getCFData('line', **kwargs)  # noqa: E731
ohlc = lambda **kwargs: getCFData('ohlc', **kwargs)  # noqa: E731
ohlcv = lambda **kwargs: getCFData('ohlcv', **kwargs)  # noqa: E731
pie = lambda **kwargs: getCFData('pie', **kwargs)  # noqa: E731
scatter = lambda **kwargs: getCFData('scatter', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)  # noqa: E731
scatter3d = lambda **kwargs: getCFData('scatter3d', n_categories=kwargs.pop('n_categories', 5), n=kwargs.pop('n', 10), **kwargs)  # noqa: E731
scattergeo = None
scattermat = None
spread = None
surface = None
timeseries = lambda **kwargs: getCFData('line', **kwargs)  # noqa: E731
