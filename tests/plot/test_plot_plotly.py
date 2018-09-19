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
        with patch('lantern.plotting.plot_plotly.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            import lantern as l
            mock1.return_value = True
            p = l.figure('cufflinks')
            df = l.bar()
            p.area(df)
            p.show()

    def test_bar(self):
        with patch('lantern.plotting.plot_plotly.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            import lantern as l
            mock1.return_value = True
            p = l.figure('cufflinks')
            df = l.bar()
            p.bar(df)
            p.show()

    def test_line(self):
        with patch('lantern.plotting.plot_plotly.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            import lantern as l
            mock1.return_value = True
            p = l.figure('cufflinks')
            df = l.bar()
            p.line(df)
            p.show()

    def test_scatter(self):
        with patch('lantern.plotting.plot_plotly.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            import lantern as l
            mock1.return_value = True
            p = l.figure('cufflinks')
            df = l.bar()
            p.scatter(df)
            p.show()

    def test_step(self):
        with patch('lantern.plotting.plot_plotly.in_ipynb', create=True) as mock1:
            import cufflinks
            cufflinks.go_offline()
            import lantern as l
            mock1.return_value = True
            p = l.figure('cufflinks')
            df = l.bar()
            p.step(df)
            p.show()
