
from .utils import in_ipynb

if in_ipynb():
    from .plotting import plot, setBackend, getBackend, Backend, setTheme, themes, getTheme
    from .data import *
    from .grids import grid

__all__ = ['plot', 'grids', 'data', 'extensions']


def _jupyter_server_extension_paths():
    return [{
        "module": "lantern.extensions.hideinput.extension"
    }]
