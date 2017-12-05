from qgrid import show_grid
from ..utils import in_ipynb

if in_ipynb():
    print('Qgrid loaded')


def qgrid_grid(df):
    return show_grid(df)
