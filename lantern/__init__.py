
from .utils import in_ipynb
from .plotting import plot
from .data import *
from .grids import grid

__all__ = ['plot', 'grids', 'data', 'extensions']


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }, {
        "name": "Lantern - Publish",
        "module": "lantern.extensions.publish.extension"
    }
    ]
