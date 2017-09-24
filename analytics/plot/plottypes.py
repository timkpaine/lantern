from enum import Enum
from abc import abstractmethod, ABCMeta


class BasePlotType(Enum):
    BASIC = 'basic'
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


class BasePlotMap(object):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def setup():
        '''called prior to plotting in case of initialization'''

    @staticmethod
    @abstractmethod
    def args():
        '''return lib-specific args for the plot type'''

    @staticmethod
    @abstractmethod
    def plot():
        '''base plot command'''

    @staticmethod
    @abstractmethod
    def setTheme():
        '''set the plotting theme'''

    @staticmethod
    @abstractmethod
    def getTheme():
        '''get the current theme'''

    @staticmethod
    @abstractmethod
    def themes():
        '''get available themes'''

    @staticmethod
    @abstractmethod
    def basic():
        '''basic plotting'''

    @staticmethod
    @abstractmethod
    def line():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def spread():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def bar():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def groupedbar():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def stackedbar():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def horizontalbar():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def horizontalstackedbar():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def histogram():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def groupedhist():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def stackedhist():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def box():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def pie():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def area():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def stackedarea():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def scatter():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def bubble():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def scattermatrix():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def heatmap():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def multiscatter():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def groupedscatter():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def ohlc():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def ohlcv():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def candlestick():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def density():
        '''plot type'''

    @staticmethod
    @abstractmethod
    def hexbin():
        '''plot type'''

_lookup = {v: k for k, v in BasePlotType.__members__.items()}


def lookup(s):
    if isinstance(s, str):
        return BasePlotType(s)
    elif isinstance(s, BasePlotType) or type(s) == BasePlotType:
        return s
    else:
        raise Exception('Cannot convert from %s to PlotType' % type(s))
