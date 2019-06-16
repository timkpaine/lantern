# <a href="https://pylantern.readthedocs.io"><img src="docs/img/logo.png" width="300"></a>
An orchestration layer for plots and tables, dummy datasets, widgets, research, reports, and anything else a data scientist might need.

[![Build Status](https://travis-ci.org/timkpaine/lantern.svg?branch=master)](https://travis-ci.org/timkpaine/lantern)
[![GitHub issues](https://img.shields.io/github/issues/timkpaine/lantern.svg)]()
[![codecov](https://codecov.io/gh/timkpaine/lantern/branch/master/graph/badge.svg)](https://codecov.io/gh/timkpaine/lantern)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/pylantern/Lobby)
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/lantern?branch=master)](https://bettercodehub.com/)
[![PyPI](https://img.shields.io/pypi/l/pylantern.svg)](https://pypi.python.org/pypi/pylantern)
[![PyPI](https://img.shields.io/pypi/v/pylantern.svg)](https://pypi.python.org/pypi/pylantern)
[![npm](https://img.shields.io/npm/v/pylantern.svg)](https://www.npmjs.com/package/pylantern)
[![Docs](https://img.shields.io/readthedocs/pylantern.svg)](https://pylantern.readthedocs.io)

<!-- [![Beerpay](https://beerpay.io/timkpaine/lantern/badge.svg?style=flat)](https://beerpay.io/timkpaine/lantern) -->


<!-- ![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/img/demo.gif) -->


## Note: Lantern Live has moved to [tributary](https://github.com/timkpaine/tributary)
## Note: Email reports have moved to [jupyterlab_email](https://github.com/timkpaine/https://github.com/timkpaine/jupyterlab_email)
## Note: `Publish` is removed in favor of [Voila](https://github.com/QuantStack/voila)

## Install
To install the base package from pip:

`pip install pylantern`

To Install from source:

`make install`


To install the JupyterLab extension:

`jupyter labextension install pylantern`

or from source:

`make labextension`

To enable the Jupyter server extension:

`jupyter serverextension enable --py lantern`



Or run the corresponding commands directly

Lantern relies on JupyterLab extensions:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install plotlywidget
jupyter labextension install @jupyterlab/plotly-extension
jupyter labextension install jupyterlab_bokeh
jupyter labextension install qgrid
jupyter labextension install @jpmorganchase/perspective-jupyterlab
jupyter labextension install ipysheet
jupyter labextension install lineup_widget
```

The following are for work in-progress on master:

```
jupyter labextension install bqplot
```


## Getting Started
[Read the docs!](http://pylantern.readthedocs.io/en/latest/index.html)


## Data
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/img/data.gif)

## Plots
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/img/plot/plots.gif)

## Grids
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/img/grids.gif)


## Export Without Code:
[Read the docs!](http://pylantern.readthedocs.io/en/latest/index.html)

## Widget Tools
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/img/widgets/widgets.gif)

