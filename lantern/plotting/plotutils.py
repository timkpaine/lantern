import random
import numpy as np


def _r():
    '''generate random color'''
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_color(i, col, color):
    if isinstance(color, list):
        c = (color[i:i+1] or [_r()])[0]
    elif isinstance(color, dict):
        c = color.get(col, _r())
    elif isinstance(color, str) and color:
        c = color
    else:
        c = _r()
    return c


# def _conf(type, colors, x, y, i, col):
#     from .plottypes import lookup
#     '''select type and color from their options, allow strings for some'''
#     if isinstance(type, str):
#         typ = lookup(type)
#         if isinstance(colors, list):
#             color = (colors[i:i+1] or [_r()])[0]
#         elif isinstance(colors, dict):
#             color = colors.get(col, _r())
#         elif isinstance(colors, str) and colors:
#             color = colors
#         else:
#             color = _r()

#     if isinstance(type, list):
#         typ = (type[i:i+1] or ['line'])[0]
#         if isinstance(typ, str):
#             typ = lookup(typ)
#         if isinstance(colors, list):
#             color = (colors[i:i+1] or [_r()])[0]
#         elif isinstance(colors, dict):
#             color = colors.get(col, _r())
#         elif isinstance(colors, str) and colors:
#             color = colors
#         else:
#             color = _r()

#     elif isinstance(type, dict):
#         typ = type.get(col, 'line')
#         if isinstance(type.get(col, 'line'), str):
#             typ = lookup(typ)

#         if isinstance(colors, list):
#             color = (colors[i:i+1] or [_r()])[0]
#         elif isinstance(colors, dict):
#             color = colors.get(col, _r())
#         elif isinstance(colors, str):
#             color = colors
#         else:
#             color = _r()

#     if y and isinstance(y, dict):
#         y = y.get(col, 'left')
#     else:
#         y = 'left'

#     if x and isinstance(x, dict):
#         x = x.get(col, 'left')
#     else:
#         x = 'bottom'

#     return typ, color, x, y


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


def align_yaxis_np(axes):
    """Align zeros of the two axes, zooming them out by same ratio"""
    axes = np.array(axes)
    extrema = np.array([ax.get_ylim() for ax in axes])

    # reset for divide by zero issues
    for i in range(len(extrema)):
        if np.isclose(extrema[i, 0], 0.0):
            extrema[i, 0] = -1
        if np.isclose(extrema[i, 1], 0.0):
            extrema[i, 1] = 1

    # upper and lower limits
    lowers = extrema[:, 0]
    uppers = extrema[:, 1]

    # if all pos or all neg, don't scale
    all_positive = False
    all_negative = False
    if lowers.min() > 0.0:
        all_positive = True

    if uppers.max() < 0.0:
        all_negative = True

    if all_negative or all_positive:
        # don't scale
        return

    # pick "most centered" axis
    res = abs(uppers+lowers)
    min_index = np.argmin(res)

    # scale positive or negative part
    multiplier1 = abs(uppers[min_index]/lowers[min_index])
    multiplier2 = abs(lowers[min_index]/uppers[min_index])

    for i in range(len(extrema)):
        # scale positive or negative part based on which induces valid
        if i != min_index:
            lower_change = extrema[i, 1] * -1*multiplier2
            upper_change = extrema[i, 0] * -1*multiplier1
            if upper_change < extrema[i, 1]:
                extrema[i, 0] = lower_change
            else:
                extrema[i, 1] = upper_change

        # bump by 10% for a margin
        extrema[i, 0] *= 1.1
        extrema[i, 1] *= 1.1

    # set axes limits
    [axes[i].set_ylim(*extrema[i]) for i in range(len(extrema))]
