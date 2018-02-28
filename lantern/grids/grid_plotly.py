from ..utils import in_ipynb
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff


if in_ipynb():
    print('Plot.ly loaded')  # cufflinks plot message prints cufflinks


def plotly_grid(data, indexed=True):
    return iplot(ff.create_table(data), filename='index_table_pd')
