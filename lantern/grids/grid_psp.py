from ..utils import in_ipynb
from IPython.display import display
from perspective import PerspectiveWidget

if in_ipynb():
    print('Perspective loaded')


def psp_grid(data, **kwargs):
    return PerspectiveWidget(data=data, **kwargs)
