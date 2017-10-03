import random
from enum import Enum
from .plottypes import lookup


class Backend(Enum):
    CUFFLINKS = 'cufflinks'
    PLOTLY = 'plotly'
    BOKEH = 'bokeh'
    HIGHCHARTS = 'highcharts'
    MATPLOTLIB = 'matplotlib'

BACKEND = None
_pm = {}

try:
    from .plot_cufflinks import CufflinksPlotMap as _cpm
    _cpm()  # ensure all methods are implemented
    _pm[Backend.CUFFLINKS] = _cpm
    BACKEND = Backend.CUFFLINKS
except ImportError:
    pass

try:
    from .plot_plotly import PlotlyPlotMap as _ppm
    _ppm()  # ensure all methods are implemented
    _pm[Backend.PLOTLY] = _ppm
    BACKEND = Backend.PLOTLY
except ImportError:
    pass

try:
    from .plot_bokeh import BokehPlotMap as _bpm
    _bpm()  # ensure all methods are implemented
    _pm[Backend.BOKEH] = _bpm
    BACKEND = Backend.BOKEH
except ImportError:
    pass

try:
    from .plot_matplotlib import MatplotlibPlotMap as _mpm
    _mpm()  # ensure all methods are implemented
    _pm[Backend.MATPLOTLIB] = _mpm
    BACKEND = Backend.MATPLOTLIB
except ImportError:
    pass

if BACKEND is None:
    raise Exception('No backend available! Please install at least one \
        of {matplotlib, bokeh, plotly, cufflinks}')


def setBackend(backend):
    global BACKEND
    if isinstance(backend, str):
        if backend.upper() not in Backend.__members__:
            raise Exception('Backend not recognized - %s' % backend)
        elif Backend.__members__[backend.upper()] not in _pm.keys():
            raise Exception('Backend %s could not be loaded, did you install all dependencies?' % backend.upper())
        else:
            BACKEND = Backend.__members__[backend.upper()]
    else:
        if Backend.__members__[backend] not in _pm.keys():
            raise Exception('Backend %s could not be loaded, did you install all dependencies?' % backend.value)
        BACKEND = backend


def getBackend():
    return BACKEND


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
