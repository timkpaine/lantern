from .plotting import plot, figure
from .data import *
from .grids import grid
from .live import run, pipeline, LanternLive, Streaming, WebSocketSource, RandomSource, RandomSource2


__all__ = ['plot', 'figure', 'grids', 'data', 'extensions']


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }, {
        "name": "Lantern - Publish",
        "module": "lantern.extensions.publish.extension"
    }
    ]
