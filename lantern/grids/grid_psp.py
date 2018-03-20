from ..utils import in_ipynb
from perspective import psp

if in_ipynb():
    print('Perspective loaded')


def psp_grid(data, **kwargs):
    return psp(data, **kwargs)
