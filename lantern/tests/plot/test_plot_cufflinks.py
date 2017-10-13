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

    def test_all(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern import lines, bar, area, bubble, pie, timeseries, scatter, heat, ohlc, ohlcv, box, histogram, setBackend
            mock1.return_value = True
            setBackend('cufflinks')

            lines.show()
            bar.show()
            area.show()
            bubble.show()
            pie.show()
            timeseries.show()
            scatter.show()
            heat.show()
            bar.show()
            ohlc.show()
            ohlcv.show()
            box.show()
            histogram.show()
