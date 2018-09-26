from sidecar import Sidecar
from IPython.display import display
from .variable_inspector import VariableInspector


def sidebar(stuff, title='Sidebar'):
    sc = Sidecar(title=title)
    with sc:
        display(stuff)
