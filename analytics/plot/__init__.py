import random
from .cufflinks import CufflinksPlotMap as _cpm
# from .plotly import PlotMap as _ppm
# from .bokeh import PlotMap as _bpm
from .matplotlib import MatplotlibPlotMap as _mpm
from .plottypes import lookup, BasePlotType
from enum import Enum


class Backend(Enum):
    CUFFLINKS = 'cufflinks'
    PLOTLY = 'plotly'
    BOKEH = 'bokeh'
    HIGHCHARTS = 'highcharts'
    MATPLOTLIB = 'matplotlib'


BACKEND = Backend.CUFFLINKS


def setBackend(backend):
    global BACKEND
    if isinstance(backend, str):
        if backend.upper() not in Backend.__members__:
            raise Exception('Backend not recognized - %s' % backend)
        else:
            BACKEND = Backend.__members__[backend.upper()]
    else:
        BACKEND = backend


def getBackend():
    return BACKEND

_cpm()  # ensure all methods are implemented
_mpm()  # ensure all methods are implemented

_pm = {
    Backend.CUFFLINKS: _cpm,
    # Backend.PLOTLY: _ppm,
    # Backend.BOKEH: _bpm,
    Backend.MATPLOTLIB: _mpm,
}


def _r():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def _conf(type, colors, i, col):
    if isinstance(type, str):
        typ = lookup(type)

        if isinstance(colors, list):
            color = (colors[i:i+1] or [_r()])[0]

        elif isinstance(colors, dict):
            color = colors.get(col, _r())
        else:
            color = _r()

    if isinstance(type, list):
        typ = (type[i:i+1] or ['line'])[0]
        if isinstance(typ, str):
            typ = lookup(typ)

        if isinstance(colors, list):
            color = (colors[i:i+1] or [_r()])[0]

        elif isinstance(colors, dict):
            color = colors.get(col, _r())
        else:
            color = _r()

    elif isinstance(type, dict):
        typ = type.get(col, 'line')
        if isinstance(type.get(col, 'line'), str):
            typ = lookup(typ)

        if isinstance(colors, list):
            color = (colors[i:i+1] or [_r()])[0]
        elif isinstance(colors, dict):
            color = colors.get(col, _r())
        else:
            color = _r()
    return typ, color


def plot(data, type=None, raw=False, colors=None, **kwargs):
    getattr(_pm[BACKEND], 'setup')()

    fig = []
    if type is None:
        type = 'line'

    for i, col in enumerate(data.columns):
        typ, color = _conf(type, colors, i, col)

        # require all to be present:
        if typ in [lookup('pie'), lookup('bubble')]:
            fig.append(getattr(_pm[BACKEND], typ.value)(data, type=typ, raw=raw, colors=colors, **kwargs))
        else:
            fig.append(getattr(_pm[BACKEND], typ.value)(data[col], type=typ, raw=True, colors=color, **kwargs))
    return _pm[BACKEND].plot(fig)
