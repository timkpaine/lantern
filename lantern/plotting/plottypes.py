from enum import Enum
from abc import abstractmethod, ABCMeta


class abstractstatic(staticmethod):
    __slots__ = ()

    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True


class BasePlotType(Enum):
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
    LMPLOT = 'lmplot'
    MULTISCATTER = 'multiscatter'
    NONE = 'none'
    OHLC = 'ohlc'
    OHLVC = 'ohlcv'
    PAIRPLOT = 'pairplot'
    PIE = 'pie'
    PROBPLOT = 'probplot'
    SCATTER = 'scatter'
    SCATTER3D = 'scatter3d'
    SCATTERMATRIX = 'scattermatrix'
    SPREAD = 'spread'
    STACKEDBAR = 'stackedbar'
    STACKEDHIST = 'stackedhist'
    STACKEDAREA = 'stackedarea'


class BasePlotMap(metaclass=ABCMeta):
    @abstractstatic
    def setup():
        '''called prior to plotting in case of initialization'''

    @abstractstatic
    def args():
        '''return lib-specific args for the plot type'''

    @abstractstatic
    def plot():
        '''base plot command'''

    @abstractmethod
    def setTheme():
        '''set the plotting theme'''

    @abstractmethod
    def getTheme():
        '''get the current theme'''

    @abstractstatic
    def themes():
        '''get available themes'''

    @abstractstatic
    def area():
        '''plot type'''

    @abstractstatic
    def basic():
        '''basic plotting'''

    @abstractstatic
    def bar():
        '''plot type'''

    @abstractstatic
    def box():
        '''plot type'''

    @abstractstatic
    def bubble():
        '''plot type'''

    @abstractstatic
    def candlestick():
        '''plot type'''

    @abstractstatic
    def density():
        '''plot type'''

    @abstractstatic
    def groupedbar():
        '''plot type'''

    @abstractstatic
    def heatmap():
        '''plot type'''

    @abstractstatic
    def hexbin():
        '''plot type'''
    @abstractstatic
    def histogram():
        '''plot type'''

    @abstractstatic
    def groupedscatter():
        '''plot type'''

    @abstractstatic
    def groupedhist():
        '''plot type'''

    @abstractstatic
    def horizontalbar():
        '''plot type'''

    @abstractstatic
    def horizontalstackedbar():
        '''plot type'''

    @abstractstatic
    def line():
        '''plot type'''

    @abstractstatic
    def lmplot():
        '''plot type'''

    @abstractstatic
    def multiscatter():
        '''plot type'''

    @abstractstatic
    def ohlc():
        '''plot type'''

    @abstractstatic
    def ohlcv():
        '''plot type'''

    @abstractstatic
    def pairplot():
        '''plot type'''

    @abstractstatic
    def pie():
        '''plot type'''

    @abstractstatic
    def probplot():
        '''plot type'''

    @abstractstatic
    def scatter():
        '''plot type'''
    @abstractstatic
    def spread():
        '''plot type'''

    @abstractstatic
    def stackedbar():
        '''plot type'''

    @abstractstatic
    def stackedhist():
        '''plot type'''

    @abstractstatic
    def stackedarea():
        '''plot type'''

    @abstractstatic
    def scattermatrix():
        '''plot type'''


_lookup = {v: k for k, v in BasePlotType.__members__.items()}


def lookup(s):
    if isinstance(s, str):
        return BasePlotType(s)
    elif isinstance(s, BasePlotType) or type(s) == BasePlotType:
        return s
    else:
        raise Exception('Cannot convert from %s to PlotType' % type(s))
