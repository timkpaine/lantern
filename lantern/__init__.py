from .plotting import plot, figure
from .data import *
from .grids import grid
from .utils import download
from .extensions import *
from .widgets import *


__all__ = ['plot', 'figure', 'grids', 'data', 'extensions', 'widgets']
__version__ = '0.1.1'


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }]
