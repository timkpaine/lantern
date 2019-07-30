from .plotting import plot, figure
from .data import *  # noqa: F401, F403
from .grids import grid  # noqa: F401
from .utils import download  # noqa: F401
from .extensions import *  # noqa: F401, F403
from .widgets import *  # noqa: F401, F403


__all__ = ['plot', 'figure', 'grids', 'data', 'extensions', 'widgets']  # noqa: F405
__version__ = '0.1.3'


def _jupyter_server_extension_paths():
    return [{
        "name": "Lantern - HideInput",
        "module": "lantern.extensions.hideinput.extension",

    }]
