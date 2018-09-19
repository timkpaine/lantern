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

    def test_all(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            import lantern as l
            mock1.return_value = True
            df = l.bar()
            l.plot(df, 'line', 'matplotlib')

    def test_list(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            import lantern as l
            mock1.return_value = True
            df = l.bar()
            l.plot(df, ['line' for _ in df], 'matplotlib')

    def test_dict(self):
        with patch('lantern.plotting.plot_matplotlib.in_ipynb', create=True) as mock1:
            import lantern as l
            mock1.return_value = True
            df = l.bar()
            l.plot(df, {c: 'line' for c in df.columns}, 'matplotlib')
