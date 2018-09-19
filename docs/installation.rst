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


Jupyter Extensions
==================
To install the server extensions:

.. code:: bash

    jupyter serverextension enable --py lantern

To install the JupyterLab extensions:

.. code:: bash

    jupyter labextension install pylantern


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


The following are for work in-progress on master:

.. code:: bash

    jupyter labextension install bqplot
