from ..utils import in_ipynb
from .plottypes import BasePlotType as p
from .plottypes import BasePlotMap as BPM
from .plottypes import lookup
from plotly.offline import init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter
from IPython.display import HTML


if in_ipynb():
    init_notebook_mode()
    print('Plot.ly loaded')

_HSPAN_NONE = {'x0': 0, 'x1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}
_VSPAN_NONE = {'y0': 0, 'y1': 0, 'color': 'rgba(30,30,30,0.0)', 'fill': False, 'opacity': 1.0}

# FIXME
# vspan={'x0':'2015-02-15','x1':'2015-03-15','color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4},


class PlotlyPlotMap(BPM):
    @staticmethod
    def setup(**kwargs):
        pass

    @staticmethod
    def _wrapper(**kwargs):
        if 'raw' in kwargs:
            kwargs['asFigure'] = kwargs.pop('raw')
        return kwargs

    @staticmethod
    def args():
        raise NotImplementedError()

    @staticmethod
    def getTheme():
        raise NotImplementedError()

    @staticmethod
    def setTheme():
        raise NotImplementedError()

    @staticmethod
    def themes():
        raise NotImplementedError()

    @staticmethod
    def plot(data, **kwargs):
        kwargs = PlotlyPlotMap._wrapper(**kwargs)
        if in_ipynb():
            return iplot(data, show_link=False)
        return plot(data, show_link=False)

    @staticmethod
    def line(data, **kwargs):
        return Scatter(x=[1, 2, 3], y=[3, 1, 6])

    @staticmethod
    def bar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def stackedbar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def horizontalbar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def horizontalstackedbar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def histogram(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def box(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def density(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def area(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def stackedarea(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def scatter(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def hexbin(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def basic():
        raise NotImplementedError()

    @staticmethod
    def bubble():
        raise NotImplementedError()

    @staticmethod
    def candlestick():
        raise NotImplementedError()

    @staticmethod
    def groupedbar():
        raise NotImplementedError()

    @staticmethod
    def groupedhist():
        raise NotImplementedError()

    @staticmethod
    def groupedscatter():
        raise NotImplementedError()

    @staticmethod
    def heatmap():
        raise NotImplementedError()

    @staticmethod
    def multiscatter():
        raise NotImplementedError()

    @staticmethod
    def ohlc():
        raise NotImplementedError()

    @staticmethod
    def ohlcv():
        raise NotImplementedError()

    @staticmethod
    def pie():
        raise NotImplementedError()

    @staticmethod
    def scattermatrix():
        raise NotImplementedError()

    @staticmethod
    def spread():
        raise NotImplementedError()

    @staticmethod
    def stackedhist():
        raise NotImplementedError()
