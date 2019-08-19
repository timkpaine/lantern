============
Installation
============

From Pip
============

.. code:: bash

    pip install pylantern

From Source
============

.. code:: bash

    python setup.py install

or 

.. code:: bash

    make install


Other Requirements
==================
Lantern relies on a handful of JupyterLab extensions to operate:

.. code:: bash

    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install plotlywidget
    jupyter labextension install @jupyterlab/plotly-extension
    jupyter labextension install jupyterlab_bokeh
    jupyter labextension install qgrid
    jupyter labextension install @jpmorganchase/perspective-jupyterlab
    jupyter labextension install ipysheet
    jupyter labextension install lineup_widget

The following are for work in-progress on master:

.. code:: bash

    jupyter labextension install bqplot
