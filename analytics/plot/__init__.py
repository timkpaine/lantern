import random
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
    if isinstance(backend, str):
        if backend.upper() not in Backend.__members__:
            raise Exception('Backend not recognized - %s' % backend)
        else:
            BACKEND = Backend.__members__[backend.upper()]
    else:
        BACKEND = backend


def getBackend():
    return BACKEND

_pm = {
    Backend.CUFFLINKS: _cpm,
    Backend.PLOTLY: _ppm,
    Backend.BOKEH: _bpm,
    Backend.MATPLOTLIB: _mpm,
}


def _r():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def plot(data, type=None, raw=False, colors=None, **kwargs):
    _pm[BACKEND][lookup('pre')]()

    fig = []
    if type is None:
        type = 'line'
    elif isinstance(type, str):
        type = lookup(type)
    elif isinstance(type, list):
        for i, col in enumerate(data.columns):
            typ = (type[i:i+1] or ['line'])[0]
            if isinstance(typ, str):
                typ = lookup(typ)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))

            if isinstance(colors, list):
                color = (colors[i:i+1] or [_r()])[0]
            elif isinstance(colors, dict):
                color = colors.get(col, _r())
            else:
                color = _r()
            fig.append(_pm[BACKEND][typ](data[col], typ, raw=True, colors=color, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)

    elif isinstance(type, dict):
        for i, col in enumerate(data.columns):
            typ = type.get(col, 'line')
            if isinstance(type.get(col, 'line'), str):
                typ = lookup(typ)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))

            if isinstance(colors, list):
                color = (colors[i:i+1] or [_r()])[0]
            elif isinstance(colors, dict):
                color = colors.get(col, _r())
            else:
                color = _r()
            fig.append(_pm[BACKEND][typ](data[col], typ, raw=True, colors=color, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)

    if type not in _pm[BACKEND]:
        raise Exception('Cannot plot type %s with backend %s' % (type, BACKEND))
    else:
        for i, col in enumerate(data.columns):
            if isinstance(colors, list):
                    color = (colors[i:i+1] or [_r()])[0]
            elif isinstance(colors, dict):
                color = colors.get(col, _r())
            else:
                color = _r()
            fig.append(_pm[BACKEND][type](data[col], type, raw=True, colors=color, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)
