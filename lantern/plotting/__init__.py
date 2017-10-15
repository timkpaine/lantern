import random
import pandas as pd
from enum import Enum
from .plottypes import lookup


class Backend(Enum):
    CUFFLINKS = 'cufflinks'
    PLOTLY = 'plotly'
    BOKEH = 'bokeh'
    HIGHCHARTS = 'highcharts'
    MATPLOTLIB = 'matplotlib'
    SEABORN = 'seaborn'

BACKEND = None
_pm = {}

try:
    from .plot_cufflinks import CufflinksPlotMap as _cpm
    _cpm()  # ensure all methods are implemented
    _pm[Backend.CUFFLINKS] = _cpm
    _pm[Backend.PLOTLY] = _cpm
    BACKEND = Backend.CUFFLINKS
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
    _pm[Backend.SEABORN] = _mpm
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


def themes():
    return _pm[BACKEND].themes()


def setTheme(theme):
    _pm[BACKEND].setTheme(theme)


def getTheme():
    return _pm[BACKEND].getTheme()


def _r():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def _conf(type, colors, i, col):
    # select type and color from their options, allow strings for some
    if isinstance(type, str):
        typ = lookup(type)
        if isinstance(colors, list):
            color = (colors[i:i+1] or [_r()])[0]
        elif isinstance(colors, dict):
            color = colors.get(col, _r())
        elif isinstance(colors, str) and colors:
            color = colors
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
        elif isinstance(colors, str) and colors:
            color = colors
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
        elif isinstance(colors, str):
            color = colors
        else:
            color = _r()
    return typ, color


def plot(data, type=None, raw=False, colors=None, **kwargs):
    getattr(_pm[BACKEND], 'setup')()

    # assemble figure as collection of subplots
    fig = []
    if type is None:
        type = 'line'

    # some plot types may utilize multiple types. skip these if so
    skip = set()

    for i, col in enumerate(data.columns):
        # if in skip, it has already been plotted or used
        if col in skip:
            continue
        typ, color = _conf(type, colors, i, col)

        if typ in [lookup('heatmap'), lookup('ohlc'), lookup('ohlcv'), lookup('histogram')]:
            return getattr(_pm[BACKEND], typ.value)(data, type=typ, colors=colors, **kwargs)

        # require all to be present:
        if typ in [lookup('pie'), lookup('bubble'), lookup('scatter'), lookup('bar'), lookup('stackedbar'), lookup('horizontalbar'), lookup('horizontalstackedbar'), lookup('box')]:
            select = [col]
            skip.add(col)

            # pie specific options
            if typ == lookup('pie'):
                labels = kwargs.get('labels', '')
                values = kwargs.get('values', '')
                select += [labels] if labels and labels in data.columns else []
                select += [values] if values and values in data.columns else []
                skip.add(labels)
                skip.add(values)

            # bubble specific options
            # scatter specific options
            if typ in [lookup('bubble'), lookup('scatter'), lookup('bubble3d'), lookup('scatter3d')]:
                x = kwargs.get('x', '')
                y = kwargs.get('y', '')
                size = kwargs.get('size', '')
                text = kwargs.get('text', '')
                categories = kwargs.get('categories', '')
                select += [x] if x and x in data.columns else []
                select += [y] if y and y in data.columns else []
                select += [size] if size and size in data.columns else []
                select += [text] if text and text in data.columns else []
                select += [categories] if categories and categories in data.columns else []
                skip.add(x)
                skip.add(y)
                skip.add(size)
                skip.add(text)
                skip.add(categories)

            # 3d plotters
            if typ in [lookup('bubble3d'), lookup('scatter3d')]:
                z = kwargs.get('z', '')
                select += [z] if z and z in data.columns else []
                skip.add(z)

            # plot all at the same time
            if typ in [lookup('bar'), lookup('horizontalbar'), lookup('stackedbar'), lookup('horizontalstackedbar'), lookup('box')]:
                cols_tmp = [col]
                colors_tmp = []
                # plot all bars at once
                for j, col_t in enumerate(data.columns):
                    typ2, color = _conf(type, colors, j, col_t)
                    if typ == typ2:
                        colors_tmp.append(color)
                        cols_tmp.append(col_t)
                        skip.add(col_t)
                fig.append(getattr(_pm[BACKEND], typ.value)(data[list(set(cols_tmp))], type=typ, raw=True, colors=colors_tmp, **kwargs))
            else:
                fig.append(getattr(_pm[BACKEND], typ.value)(data[list(set(select))], type=typ, raw=True, colors=colors, **kwargs))
        else:
            fig.append(getattr(_pm[BACKEND], typ.value)(data[col], type=typ, raw=True, colors=color, **kwargs))
    return _pm[BACKEND].plot(fig, **kwargs)
