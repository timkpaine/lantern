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


def plot(data, type=None, raw=False, **kwargs):
    if type is None:
        type = 'line'
    elif isinstance(type, str):
        type = lookup(type)
    elif isinstance(type, list):
        fig = []
        for i, typ in enumerate(type):
            if isinstance(typ, str):
                typ = lookup(typ)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))
            fig.append(_pm[BACKEND][typ](data[data.columns[i]], typ, raw=True, **kwargs))
            print(i)
        return _pm[BACKEND][lookup('plot')](fig)

    elif isinstance(type, dict):
        fig = []
        print(type)
        for k, v in type.items():
            if isinstance(v, str):
                typ = lookup(v)
            if typ not in _pm[BACKEND]:
                raise Exception('Cannot plot type %s with backend %s' % (typ, BACKEND))
            fig.append(_pm[BACKEND][typ](data[k], typ, raw=True, **kwargs))
        return _pm[BACKEND][lookup('plot')](fig)

    if type not in _pm[BACKEND]:
        raise Exception('Cannot plot type %s with backend %s' % (type, BACKEND))
    else:
        return _pm[BACKEND][type](data, type, raw=raw**kwargs)
