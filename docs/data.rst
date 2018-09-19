==============
Data
==============

Fake Data
=============
Lantern relies on Faker and Mimesis to generate fake data

People
-------
Generate an individual (dict) or a dataframe of people
.. code::python
    lantern.person()
.. code::bash
    {'first_name': 'Francoise',
     'last_name': 'Houston',
     'name': 'Francoise Houston',
     'age': 29,
     'gender': 'Female',
     'id': '44-72/01',
     'occupation': 'Technical Analyst',
     'telephone': '519.196.0471',
     'title': 'PhD',
     'username': 'simoniac.2029',
     'university': 'Eastern Connecticut State University (ECSU)'}
.. code::python
    lantern.people()


Companies
----------
Generate an individual (dict) or a dataframe of companies
.. code::python
    lantern.company()

.. code::bash
    {'name': 'Gordon, Rodriguez and Salazar',
     'address': '351 Ralph Stream Apt. 203\nMargaretview, NE 00811-8677',
     'ticker': 'AYG',
     'last_price': 53.96174484497788,
     'market_cap': 76809360484,
     'exchange': 'F',
     'ceo': 'Patricia Woodard',
     'sector': 'Real Estate',
     'industry': 'Real Estate Management & Development'}

.. code::python
    lantern.companies()

Financial
----------
Generate tickers and exchange codes, currencies, and trades (dataframe)
.. code::python
    lantern.ticker(country='us')
    lantern.currency()
    lantern.trades()


Cufflinks Data
===========
We wrap `cufflinks.datagen` and expose a variety of data types as dataframes
.. code::python
    lantern.area()
    lantern.bar()
    lantern.box()
    lantern.bubble()
    lantern.bubble3d()
    lantern.candlestick()
    lantern.heatmap()
    lantern.histogram()
    lantern.line()
    lantern.ohlc()
    lantern.ohlcv()
    lantern.pie()
    lantern.scatter()
    lantern.scatter3d()
    lantern.timeseries()

Scikit-learn Data
===========
We wrap `sklearn.datasets` and expose a variety of data types as either numpy arrays or dataframes
.. code::python
    lantern.regression()
    lantern.blobs()
    lantern.classification()
    lantern.multilabel()
    lantern.gaussian()
    lantern.hastie()
    lantern.circles()
    lantern.moons()
    lantern.biclusters()
    lantern.scurve()
    lantern.checker()
    lantern.friedman()
    lantern.friedman2()
    lantern.friedman3()

