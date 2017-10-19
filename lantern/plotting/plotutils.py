from .plottypes import lookup
import random


def _r():
    '''generate random color'''
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def _conf(type, colors, x, y, i, col):
    '''select type and color from their options, allow strings for some'''
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

    if y and isinstance(y, dict):
        y = y.get(col, 'left')
    else:
        y = 'left'

    if x and isinstance(x, dict):
        x = x.get(col, 'left')
    else:
        x = 'bottom'

    return typ, color, x, y


def _parseScatter(kwargs, col):
    ret = {}
    ret['x'] = kwargs.get(col, {}).get('x', col)
    ret['y'] = kwargs.get(col, {}).get('y', col)
    ret['categories'] = kwargs.get(col, {}).get('categories', col)
    ret['text'] = kwargs.get(col, {}).get('text', col)
    ret['size'] = kwargs.get(col, {}).get('size', 10)
    return ret


def _parseScatterPie(kwargs, col):
    ret = {}
    ret['values'] = kwargs.get(col, {}).get('values', col)
    ret['labels'] = kwargs.get(col, {}).get('labels', col)
    return ret
