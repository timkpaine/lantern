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
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import area
            mock1.return_value = True
            setBackend('cufflinks')
            area.show()

    def test_bar(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import bar
            mock1.return_value = True
            setBackend('cufflinks')
            bar.show()

    def test_box(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import box
            mock1.return_value = True
            setBackend('cufflinks')
            box.show()

    def test_bubble(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import bubble
            mock1.return_value = True
            setBackend('cufflinks')
            bubble.show()

    def test_groupedbar(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import groupedbar
            mock1.return_value = True
            setBackend('cufflinks')
            groupedbar.show()

    def test_groupedhist(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import groupedhist
            mock1.return_value = True
            setBackend('cufflinks')
            groupedhist.show()

    def test_heatmap(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import heatmap
            mock1.return_value = True
            setBackend('cufflinks')
            heatmap.show()

    def test_histogram(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import histogram
            mock1.return_value = True
            setBackend('cufflinks')
            histogram.show()

    def test_horizontalbar(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import horizontalbar
            mock1.return_value = True
            setBackend('cufflinks')
            horizontalbar.show()

    def test_horizontalstackedbar(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import horizontalstackedbar
            mock1.return_value = True
            setBackend('cufflinks')
            horizontalstackedbar.show()

    def test_line(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import line
            mock1.return_value = True
            setBackend('cufflinks')
            line.show()

    def test_ohlc(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import ohlc
            mock1.return_value = True
            setBackend('cufflinks')
            ohlc.show()

    def test_ohlcv(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import ohlcv
            mock1.return_value = True
            setBackend('cufflinks')
            ohlcv.show()

    def test_pie(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import pie
            mock1.return_value = True
            setBackend('cufflinks')
            pie.show()

    def test_scatter(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import scatter
            mock1.return_value = True
            setBackend('cufflinks')
            scatter.show()

    def test_stackedarea(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import stackedarea
            mock1.return_value = True
            setBackend('cufflinks')
            stackedarea.show()

    def test_stackedbar(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import stackedbar
            mock1.return_value = True
            setBackend('cufflinks')
            stackedbar.show()

    def test_stackedhist(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import stackedhist
            mock1.return_value = True
            setBackend('cufflinks')
            stackedhist.show()

    def test_timeseries(self):
        with patch('lantern.plotting.plot_cufflinks.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            from lantern.plotting import setBackend
            from lantern import timeseries
            mock1.return_value = True
            setBackend('cufflinks')
            timeseries.show()
