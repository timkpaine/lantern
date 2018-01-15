==============
Plotting
==============

Plot command
=============
.. method:: lantern.plot(data, kind='line', backend='matplotlib', theme=None, **kwargs)

TODO 

Object Oriented
================
.. method:: lantern.figure(backend='matplotlib', theme=None)

.. code:: python3

    import lantern as l
    f = l.figure('matplotlib')

TODO 


Plot Types
===========
- line
- area
- step
- bar
- scatter
.. NOTE:: Development of additional plot types is logged on the project's `Waffle.io pages <https://waffle.io/timkpaine/lantern>`_.

For the following code, we will assume the following commands were executed:

.. code:: python3

    import lantern as l
    df = l.bar.sample()
    f = l.figure('matplotlib')


Line
-----
.. method:: line(self, data, color=None, y_axis='left', **kwargs):
.. code:: python3

    f.line(df)
    f.show()

.. image:: ./img/plot/line.png
    :scale: 100%
    :alt: line.png

Area
-----
.. method:: area(self, data, color=None, y_axis='left', stacked=False, **kwargs):
.. code:: python3

    f.area(df)
    f.show()

.. image:: ./img/plot/area.png
    :scale: 100%
    :alt: area.png

Step
-----
.. method:: step(self, data, color=None, y_axis='left', **kwargs):
.. code:: python3

    f.step(df)
    f.show()

.. image:: ./img/plot/step.png
    :scale: 100%
    :alt: step.png

Bar
----
.. method:: bar(self, data, color=None, y_axis='left', stacked=False, **kwargs):
.. code:: python3

    f.bar(df)
    f.show()

.. image:: ./img/plot/bar.png
    :scale: 100%
    :alt: bar.png

Scatter
--------
.. method:: scatter(self, data, color=None, x=None, y=None,  y_axis='left', **kwargs):
.. code:: python3

    f.scatter(df)
    f.show()


Mixed-type Plots
=================

.. WARNING:: Mixing temporal and categorical charts can yield unexpected results!

Advanced Usage
===============
.. method:: show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):

For the following examples, we assume the following code:

.. code:: python3

    import lantern as l
    df = l.bar.sample()
    f = l.figure('matplotlib')
    f.line(df)


Axis labels
------------
.. code:: python3

    f.show(xlabel='Test X', ylabel='Test Y')

.. image:: ./img/plot/labels.png
    :scale: 100%
    :alt: labels.png

Axis ticks
------------
.. code:: python3

    f.show(yticks=False)

.. image:: ./img/plot/ticks.png
    :scale: 100%
    :alt: ticks.png

Axis lines
-----------
.. code:: python3

    f.show(xaxis=False, yaxis=False)

.. image:: ./img/plot/axis.png
    :scale: 100%
    :alt: axis.png

Grid
--------
.. code:: python3

    f.show(grid=False)

.. image:: ./img/plot/grid.png
    :scale: 100%
    :alt: grid.png

Legend
--------
.. code:: python3

    f.show(legend=False)

.. image:: ./img/plot/legend.png
    :scale: 100%
    :alt: legend.png

Right Y Axis
-------------
.. WARNING:: TODO

Horizontal Lines
-----------------
.. WARNING:: TODO

Vertical Lines
-----------------
.. WARNING:: TODO
