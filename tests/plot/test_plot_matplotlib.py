from mock import patch

import matplotlib
matplotlib.use('Agg')


class TestConfig:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_area(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import area
            mock1.return_value = True
            setBackend('matplotlib')
            area.show()

    def test_bar(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import bar
            mock1.return_value = True
            setBackend('matplotlib')
            bar.show()

    def test_box(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import box
            mock1.return_value = True
            setBackend('matplotlib')
            box.show()

    def test_bubble(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import bubble
            mock1.return_value = True
            setBackend('matplotlib')
            bubble.show()

    def test_histogram(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import histogram
            mock1.return_value = True
            setBackend('matplotlib')
            histogram.show()

    def test_horizontalbar(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import horizontalbar
            mock1.return_value = True
            setBackend('matplotlib')
            horizontalbar.show()

    def test_horizontalstackedbar(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import horizontalstackedbar
            mock1.return_value = True
            setBackend('matplotlib')
            horizontalstackedbar.show()

    def test_line(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import line
            mock1.return_value = True
            setBackend('matplotlib')
            line.show()

    def test_scatter(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import scatter
            mock1.return_value = True
            setBackend('matplotlib')
            scatter.show()

    def test_stackedbar(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import stackedbar
            mock1.return_value = True
            setBackend('matplotlib')
            stackedbar.show()

    def test_stackedhist(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import stackedhist
            mock1.return_value = True
            setBackend('matplotlib')
            stackedhist.show()

    def test_timeseries(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import timeseries
            mock1.return_value = True
            setBackend('matplotlib')
            timeseries.show()

    def test_lmplot(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import line, plot
            mock1.return_value = True
            setBackend('matplotlib')
            df = line.sample()
            plot(df[[df.columns[0], df.columns[1]]], type='lmplot', scatter={df.columns[0]: {'x': df.columns[0], 'y': df.columns[1]}})

    def test_probplot(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import line, plot
            mock1.return_value = True
            setBackend('matplotlib')
            df = line.sample()
            plot(df[[df.columns[0]]], type='probplot')

    def test_pairplot(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            from lantern import setBackend
            from lantern import line, plot
            mock1.return_value = True
            setBackend('matplotlib')
            df = line.sample()
            plot(df, type='pairplot')
