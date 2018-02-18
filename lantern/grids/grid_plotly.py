from ..utils import in_ipynb
from plotly.offline import init_notebook_mode, iplot


if in_ipynb():
    init_notebook_mode(connected=True)
    print('Plot.ly loaded')  # cufflinks plot message prints cufflinks


def plotly_grid(data, indexed=True):
    return iplot(data, filename='index_table_pd')
