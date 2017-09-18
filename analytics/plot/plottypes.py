from enum import Enum


class PlotType(Enum):
    PLOT = 'plot'
    PREPLOT = 'pre'
    POSTPLOT = 'post'
    BASIC = 'line0'
    LINE = 'line'
    SPREAD = 'spread'
    BAR = 'bar'
    GROUPEDBAR = 'groupedbar'
    STACKEDBAR = 'stackedbar'
    HORIZONTALBAR = 'horizontalbar'
    HORIZONTALSTACKEDBAR = 'horizontalstackedbar'
    HISTOGRAM = 'histogram'
    GROUPEDHIST = 'groupedhist'
    STACKEDHIST = 'stackedhist'
    BOX = 'box'
    PIE = 'pie'
    AREA = 'area'
    STACKEDAREA = 'stackedarea'
    SCATTER = 'scatter'
    BUBBLE = 'bubble'
    SCATTERMATRIX = 'scattermatrix'
    HEATMAP = 'heatmap'
    MULTISCATTER = 'multiscatter'
    GROUPEDSCATTER = 'groupedscatter'
    OHLC = 'ohlc'
    OHLVC = 'ohlcv'
    CANDLESTICK = 'candlestick'
    DENSITY = 'density'
    HEXBIN = 'hexbin'

_lookup = {v: k for k, v in PlotType.__members__.items()}


def lookup(str):
    return PlotType(str)
