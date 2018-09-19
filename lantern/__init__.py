from .plotting import plot, figure
from .data import *
from .grids import grid
from .utils import download
from .extensions import *


__all__ = ['plot', 'figure', 'grids', 'data', 'extensions']
__version__ = '0.1.0'


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }]
