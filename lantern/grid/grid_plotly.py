from ..utils import in_ipynb
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff


if in_ipynb():
    init_notebook_mode(connected=True)


def grid(data, indexed=True):

    if indexed:
        return iplot(ff.create_table(data), filename='index_table_pd')
    else:
        return iplot(data, filename='index_table_pd')
