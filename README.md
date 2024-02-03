# <a href="https://pylantern.readthedocs.io"><img src="docs/img/logo.png" width="300"></a>
An orchestration layer for plots and tables, dummy datasets, widgets, research, reports, and anything else a data scientist might need.

[![Build Status](https://github.com/timkpaine/lantern/workflows/Build%20Status/badge.svg)](https://github.com/timkpaine/lantern/actions/)
[![GitHub issues](https://img.shields.io/github/issues/timkpaine/lantern.svg)]()
[![codecov](https://codecov.io/gh/timkpaine/lantern/branch/main/graph/badge.svg)](https://codecov.io/gh/timkpaine/lantern)
[![PyPI](https://img.shields.io/pypi/l/pylantern.svg)](https://pypi.python.org/pypi/pylantern)
[![PyPI](https://img.shields.io/pypi/v/pylantern.svg)](https://pypi.python.org/pypi/pylantern)

<!-- [![Beerpay](https://beerpay.io/timkpaine/lantern/badge.svg?style=flat)](https://beerpay.io/timkpaine/lantern) -->


<!-- ![](https://raw.githubusercontent.com/timkpaine/lantern/main/docs/img/demo.gif) -->


## Note: Lantern Live has moved to [tributary](https://github.com/timkpaine/tributary)
## Note: Email reports have moved to [jupyterlab_email](https://github.com/timkpaine/jupyterlab_email)
## Note: `Publish` is removed in favor of [Voila](https://github.com/voila-dashboards/voila)
## Note: `Export` code has has moved to [jupyterlab_commands](https://github.com/timkpaine/jupyterlab_commands/) and [jupyterlab_nbconvert_nocode](https://github.com/timkpaine/jupyterlab_nbconvert_nocode)

## About
This library is designed to fill gaps between other libraries with the JupyterLab ecosystem. The motivation was initially to allow for plots generated with a javascript library (like `plotly` or `bokeh`) to trivially swap out for `matplotlib` in non-browser contexts such as NBConvert generation of PDFs.

It has expanded to include a variety of functions, including grids, emailing notebooks, publishing notebooks, custom nbconvert exporters for JupyterLab, variable inpection, custom streaming operations, and other helpful functions and widgets. As these functionalities mature, or as competeting libraries emerge, they are cut out into their own standalone libraries or removed from `Lantern`, respectively.

This library has produced or ceded functionality to:
- [jupyterlab_email](https://github.com/timkpaine/jupyterlab_email)
- [tributary](https://github.com/timkpaine/tributary)
- [jupyterlab_commands](https://github.com/timkpaine/jupyterlab_commands/)
- [jupyterlab_nbconvert_nocode](https://github.com/timkpaine/jupyterlab_nbconvert_nocode)
- [Voila](https://github.com/voila-dashboards/voila)

## Install
To install the base package from pip:

`pip install pylantern`

To Install from source:

`make install`


Lantern relies on JupyterLab extensions:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install plotlywidget
jupyter labextension install @jupyterlab/plotly-extension
jupyter labextension install jupyterlab_bokeh
jupyter labextension install qgrid
jupyter labextension install @finos/perspective-jupyterlab
jupyter labextension install ipysheet
jupyter labextension install lineup_widget
```

The following are for work in-progress on main:

```
jupyter labextension install bqplot
```


## Data
![](https://raw.githubusercontent.com/timkpaine/lantern/main/docs/img/data.gif)

## Plots
![](https://raw.githubusercontent.com/timkpaine/lantern/main/docs/img/plot/plots.gif)

## Grids
![](https://raw.githubusercontent.com/timkpaine/lantern/main/docs/img/grids.gif)


## Export Without Code:
Note: this has moved to [jupyterlab_commands](https://github.com/timkpaine/jupyterlab_commands/)

## Widget Tools
![](https://raw.githubusercontent.com/timkpaine/lantern/main/docs/img/widgets/widgets.gif)

