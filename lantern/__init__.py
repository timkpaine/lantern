from .plotting import plot, figure
from .data import *
from .grids import grid
from .live import run, pipeline, LanternLive, Streaming, WebSocketSource, RandomSource, RandomSource2
from .utils import download
from .extensions import *


__all__ = ['plot', 'figure', 'grids', 'data', 'extensions']
__version__ = '0.0.19'


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }, {
        "name": "Lantern - Publish",
        "module": "lantern.extensions.publish.extension"
    }
    ]
