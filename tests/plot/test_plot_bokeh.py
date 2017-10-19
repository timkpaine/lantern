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

    def test_area(self):
        with patch('lantern.plotting.plot_bokeh.in_ipynb', create=True) as mock1:
            from bokeh.plotting import output_notebook
            output_notebook()

            from lantern import setBackend
            from lantern import area
            mock1.return_value = True
            setBackend('bokeh')
            area.show()

    def test_line(self):
        with patch('lantern.plotting.plot_bokeh.in_ipynb', create=True) as mock1:
            from bokeh.plotting import output_notebook
            output_notebook()

            from lantern import setBackend
            from lantern import line
            mock1.return_value = True
            setBackend('bokeh')
            line.show()
