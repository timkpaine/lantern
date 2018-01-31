# Lantern
An orchestration layer for plots and tables, dummy datasets, research, reports, and anything else a data scientist might need.

[![Version](https://img.shields.io/badge/version-0.0.12-lightgrey.svg)](https://img.shields.io/badge/version-0.0.12-lightgrey.svg)
[![Build Status](https://travis-ci.org/timkpaine/lantern.svg?branch=master)](https://travis-ci.org/timkpaine/lantern)
[![GitHub issues](https://img.shields.io/github/issues/timkpaine/lantern.svg)]()
[![Waffle.io](https://badge.waffle.io/timkpaine/lantern.svg?label=ready&title=Ready)](http://waffle.io/timkpaine/lantern)
[![codecov](https://codecov.io/gh/timkpaine/lantern/branch/master/graph/badge.svg)](https://codecov.io/gh/timkpaine/lantern)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/pylantern/Lobby)
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/lantern?branch=master)](https://bettercodehub.com/)
[![PyPI](https://img.shields.io/pypi/v/pylantern.svg)]()
[![PyPI](https://img.shields.io/pypi/l/pylantern.svg)]()
[![Docs](https://img.shields.io/readthedocs/pylantern.svg)]()
[![Site](https://img.shields.io/badge/Site--grey.svg?colorB=FFFFFF)](http://paine.nyc/lantern)

<!-- [![Beerpay](https://beerpay.io/timkpaine/lantern/badge.svg?style=flat)](https://beerpay.io/timkpaine/lantern) -->

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
jupyter labextension install @jupyterlab/plotly-extension
jupyter labextension install jupyterlab_bokeh
jupyter labextension install qgrid
```

The following are for work in-progress on master:

```
jupyter labextension install @jpmorganchase/perspective-jupyterlab
jupyter labextension install bqplot
```


## Getting Started
[Read the docs!](http://pylantern.readthedocs.io/en/latest/index.html)
