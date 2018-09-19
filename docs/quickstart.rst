===============
Getting started
===============
.. WARNING:: Lantern is under active beta development, so interfaces and functionality may change

Overview
===============
Lantern provides a number of utility facilities for working in Jupyter notebooks. These include:

- quick and easy plotting, across several popular plotting libraries
- quick and easy tables, across several popular table libraries
- utilities for working with live data
- easy export (including code-less) for reports
- publishing read-only dashboards from notebooks
- sample datasets


Plotting libraries
===================
Lantern utilizes the following plotting libraries:

- `Matplotlib <https://matplotlib.org>`_ / `Seaborn <https://seaborn.pydata.org>`_
- `Plotly <https://plot.ly>`_ / `Cufflinks <https://github.com/santosjorge/cufflinks>`_
- `Bokeh <https://bokeh.pydata.org/en/latest/>`_


Table Libraries
================
Lantern utilizes the following table libraries:

- `Qgrid <https://github.com/quantopian/qgrid>`_
- `Plotly <https://plot.ly>`_


Live Data
==========
.. WARNING:: This functionality is deprecated in favor of TimKPaine/tributary


Export
=======
JupyterLab uses `NBconvert <https://nbconvert.readthedocs.io/en/latest/>`_ provides the ability to export to PDF, HTML, LaTeX, ReStructured Text, Markdown, Executable Script, and Reveal JS Slideshow. On top of this, lantern provides the ability to export to:

- PDF with no code
- HTML with no code

.. WARNING:: Some functionality is deprecated in favor of TimKPaine/jupyterlab_email

Publish
========
Lantern provides a read-only view on your notebook, for quick-and-dirty web based reports. 
.. WARNING:: This functionality is deprecated in favor of QuantStack/Voila


Sample Datasets
================
Lantern utilizes `Cufflinks <https://github.com/santosjorge/cufflinks>`_ and `scikit learn <http://scikit-learn.org/stable/>`_ to provide a variety of sample datasets:

- Lines
- Scatter
- Bubble
- Pie
- Bars
- Open, high, low, close, volume
- Box
- Histogram
- Surface
- Sinwave
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

and more.
