from sidecar import Sidecar
from IPython.display import display  # noqa: F401
from .variable_inspector import VariableInspector  # noqa: F401


def sidebar(stuff, title='Sidebar'):
    sc = Sidecar(title=title)
    with sc:
        display(stuff)
