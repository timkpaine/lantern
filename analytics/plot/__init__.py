from .cufflinks import _plotmap as _cpm
from .plotly import _plotmap as _ppm
from .bokeh import _plotmap as _bpm
from .matplotlib import _plotmap as _mpm
from .plottypes import lookup
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
    if backend.upper() not in Backend.__members__:
        raise Exception('Backend not recognized - %s' % backend)
    else:
        BACKEND = Backend.__members__[backend.upper()]


def getBackend():
    return BACKEND

_pm = {
    Backend.CUFFLINKS: _cpm,
    Backend.PLOTLY: _ppm,
    Backend.BOKEH: _bpm,
    Backend.MATPLOTLIB: _mpm,
}


def _random_gen_color():
    pass


def plot(data, type=None, raw=False, colors=None, **kwargs):
    if type is None:
        type = 'line'
    elif isinstance(type, str):
        type = lookup(type)
    elif isinstance(type, list):
        fig = []
        for i, col in enumerate(data.columns):
            typ = (type[i:i+1] or ['line'])[0]
            if isinstance(typ, str):
                typ = lookup(typ)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))

            if isinstance(colors, list):
                color = (colors[i:i+1] or ['red'])[0]
            elif isinstance(colors, dict):
                pass
            else:
                color = ['green']
            fig.append(_pm[BACKEND][typ](data[col], typ, raw=True, colors=color, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)

    elif isinstance(type, dict):
        fig = []
        for i, col in enumerate(data.columns):
            typ = type.get(col, 'line')
            if isinstance(type.get(col, 'line'), str):
                typ = lookup(typ)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))

            if isinstance(colors, list):
                color = (colors[i:i+1] or ['red'])[0]
            elif isinstance(colors, dict):
                pass
            else:
                color = ['green']

            fig.append(_pm[BACKEND][typ](data[col], typ, raw=True, colors=color, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)

    if type not in _pm[BACKEND]:
        raise Exception('Cannot plot type %s with backend %s' % (type, BACKEND))
    else:
        return _pm[BACKEND][type](data, type, raw=raw**kwargs)
