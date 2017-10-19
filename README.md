# Lantern
(analytics was too general a name..)

An orchestration layer for plots and tables, dummy datasets, research, reports, and anything else a data scientist might need.

[![Version](https://img.shields.io/badge/version-0.0.9-lightgrey.svg)](https://img.shields.io/badge/version-0.0.9-lightgrey.svg)
[![Build Status](https://travis-ci.org/timkpaine/lantern.svg?branch=master)](https://travis-ci.org/timkpaine/lantern)
[![GitHub issues](https://img.shields.io/github/issues/timkpaine/lantern.svg)]()
[![Waffle.io](https://badge.waffle.io/timkpaine/lantern.svg?label=ready&title=Ready)](http://waffle.io/timkpaine/lantern)
[![codecov](https://codecov.io/gh/timkpaine/lantern/branch/master/graph/badge.svg)](https://codecov.io/gh/timkpaine/lantern)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/pylantern/Lobby)
[![BCH compliance](https://bettercodehub.com/edge/badge/timkpaine/lantern?branch=master)](https://bettercodehub.com/)
[![PyPI](https://img.shields.io/pypi/v/pylantern.svg)]()
[![PyPI](https://img.shields.io/pypi/l/pylantern.svg)]()
[![Beerpay](https://beerpay.io/timkpaine/lantern/badge.svg?style=flat)](https://beerpay.io/timkpaine/lantern)
[![Site](https://img.shields.io/badge/Site--grey.svg?colorB=FFFFFF)](http://paine.nyc/lantern)

## Plotting
Abstracts away the nuances of individual charting libraries by providing a single `plot` command with library specific kwarg introspection.

### Dummy data
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/preview.gif)

### Plot command
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/preview2.gif)

## Advanced Plotting
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/plot2.png)
![](https://raw.githubusercontent.com/timkpaine/lantern/master/docs/plot1.png)

## Grids
The same.

## Jupyter Integration
Single-command code-less exporting for report generation.
```python
    import lantern.extensions
    lantern.extensions.export_pdf('my_notebook.ipynb')  # my_notebook.pdf
    lantern.extensions.export_html('my_notebook.ipynb') # my_notebook.html
```

## Dummy datasets
- Lines
- Scatter
- Scatter3d
- Bubble
- Bubble3d
- Pie
- Bars
- Open, high, low, close
- Open, high, low, close, volume
- Box
- Histogram
- Surface
- Sinwave
- Scattergeo
- Choropleth
- Stock
- Regression
- Blobs
- Classification
- Multilabel classification
- Gaussian
- Hasti
- Circles
- Moons
- Biclusters
- S Curve
- Checker
- Friedman
- Friedman 2
- Friedman 3
