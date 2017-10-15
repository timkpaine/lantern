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
            from lantern import setBackend
            from lantern import area, bar, box, bubble, groupedbar, groupedhist, groupedscatter, heatmap, histogram, horizontalbar, horizontalstackedbar, line, ohlc, ohlcv, pie, scatter, sinwave, stackedarea, stackedbar, stackedhist, timeseries

            mock1.return_value = True
            setBackend('cufflinks')

            area.show()
            bar.show()
            box.show()
            bubble.show()
            groupedbar.show()
            groupedhist.show()
            # groupedscatter.show()
            heatmap.show()
            histogram.show()
            horizontalbar.show()
            horizontalstackedbar.show()
            line.show()
            ohlc.show()
            ohlcv.show()
            pie.show()
            scatter.show()
            # sinwave.show()
            stackedarea.show()
            stackedbar.show()
            stackedhist.show()
            timeseries.show()
