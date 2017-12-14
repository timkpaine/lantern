from mock import patch


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

    def test_grid(self):
        with patch('lantern.grids.grid_plotly.in_ipynb', create=True) as mock1:
            import lantern as l
            mock1.return_value = True
            df = l.bar.sample()
            l.grid(df, 'plotly')
            l.grid(df, 'plotly', indexed=False)

