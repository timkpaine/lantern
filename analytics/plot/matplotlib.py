import matplotlib.pyplot as plt
from .plottypes import BasePlotType as p
from .plottypes import BasePlotMap as BPM
from .plottypes import lookup


_F = None


class MatplotlibPlotMap(BPM):
    def setup():
        global _F
        _F = plt.figure()

    def _wrapper(**kwargs):
        if 'type' in kwargs:
            kwargs.pop('type', None)
        if 'raw' in kwargs:
            kwargs.pop('raw')
        if 'colors' in kwargs:
            kwargs['color'] = kwargs.pop('colors')
        return kwargs

    @staticmethod
    def plot(data, **kwargs):
        _F.canvas.draw()
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        return plt.show()

    def line(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(**kwargs)
        #                   subplots=kwargs.get('subplots', False),
        #                   hline=kwargs.get('hline', []),
        #                   vline=kwargs.get('vline', []),
        #                   # hspan=kwargs.get('hspan', _HSPAN_NONE),
        #                   # vspan=kwargs.get('vspan', _VSPAN_NONE),
        #                   colors=kwargs.get('colors', []),
        #                   bestfit=kwargs.get('bestfit', False),
        #                   bestfit_colors=kwargs.get('bestfit_colors', []),
        #                   asFigure=kwargs.get('asFigure', False),

    def bar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=False,
                         **kwargs)

    def stackedbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='bar',
                         stacked=True,
                         **kwargs)

    def horizontalbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='barh',
                         stacked=False,
                         **kwargs)

    def horizontalstackedbar(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='barh',
                         stacked=True,
                         **kwargs)

    def histogram(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hist',
                         **kwargs)

    def box(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='box',
                         **kwargs)

    def density(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='density',
                         **kwargs)

    def area(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', False),
                         **kwargs)

    def stackedarea(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='area',
                         stacked=kwargs.get('stacked', True),
                         **kwargs)

    def scatter(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='scatter',
                         **kwargs)

    def hexbin(data, **kwargs):
        kwargs = MatplotlibPlotMap._wrapper(**kwargs)
        return data.plot(kind='hexbin',
                         **kwargs)
