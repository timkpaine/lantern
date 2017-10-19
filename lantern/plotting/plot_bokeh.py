from bokeh.plotting import figure, show, output_notebook
from bokeh.models import HoverTool
from ..utils import in_ipynb
from .plottypes import BasePlotMap as BPM


if in_ipynb():
    output_notebook()
_BF = None


class BokehPlotMap(BPM):
    @staticmethod
    def setup():
        global _BF
        _BF = figure(toolbar_location="below",
                     toolbar_sticky=False,
                     x_axis_type='datetime')  ## TODO remove

    @staticmethod
    def _wrapper(**kwargs):
        if 'type' in kwargs:
            kwargs.pop('type', None)
        if 'raw' in kwargs:
            kwargs.pop('raw')
        if 'colors' in kwargs:
            kwargs['line_color'] = kwargs.pop('colors')

        kwargs.pop('x', None)  # FIXME
        kwargs.pop('y', None)  # FIXME
        return kwargs

    @staticmethod
    def args():
        raise NotImplementedError()

    @staticmethod
    def getTheme():
        raise NotImplementedError()

    @staticmethod
    def setTheme(theme):
        raise NotImplementedError()

    @staticmethod
    def themes():
        raise NotImplementedError()

    @staticmethod
    def plot(data, **kwargs):
        kwargs = BokehPlotMap._wrapper(**kwargs)
        if not isinstance(data, list):
            _BF.line(x=data.index, y=data.values, **kwargs)
        else:
            _BF.add_tools(*[HoverTool(
                tooltips=[('x', '@x{%F}'), ('y', '@y')],
                formatters={'x': 'datetime'},
                mode='vline'
            ) for _ in data])
        show(_BF)
        return _BF

    @staticmethod
    def line(data, **kwargs):
        kwargs = BokehPlotMap._wrapper(**kwargs)
        return _BF.line(x=data.index, y=data.values, **kwargs)

    @staticmethod
    def bar(data, **kwargs):
        kwargs = BokehPlotMap._wrapper(**kwargs)
        kwargs['width'] = kwargs.get('width', .9)
        return _BF.vbar(x=data.index, top=data.values, **kwargs)

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
        kwargs = BokehPlotMap._wrapper(**kwargs)
        # fill_color = kwargs.get('fill_color', kwargs.get('color'))
        return _BF.patch(x=data.index, y=data.values, fill_alpha=.2, **kwargs)

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
    def basic(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def bubble(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def candlestick(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedbar(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedhist(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def groupedscatter(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def heatmap(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def lmplot(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def multiscatter(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def ohlc(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def ohlcv(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def pie(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def scattermatrix(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def spread(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def stackedhist(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def pairplot(data, **kwargs):
        raise NotImplementedError()

    @staticmethod
    def probplot(data, **kwargs):
        raise NotImplementedError()
