from ..utils import in_ipynb

if in_ipynb():
    print('Qgrid loaded')


def qgrid_grid(df):
    from qgrid import show_grid
    return show_grid(df)
