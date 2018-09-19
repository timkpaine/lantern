from plotly.offline import iplot
import plotly.figure_factory as ff


def plotly_grid(data, indexed=True):
    return iplot(ff.create_table(data), filename='index_table_pd')
