
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
        import lantern as l
        l.area.sample()

    def test_bar(self):
        import lantern as l
        l.bar.sample()

    def test_box(self):
        import lantern as l
        l.box.sample()

    def test_bubble(self):
        import lantern as l
        l.bubble.sample()

    def test_groupedbar(self):
        import lantern as l
        l.groupedbar.sample()

    def test_groupedhist(self):
        import lantern as l
        l.groupedhist.sample()

    def test_groupedscatter(self):
        import lantern as l
        l.groupedscatter.sample()

    def test_heatmap(self):
        import lantern as l
        l.heatmap.sample()

    def test_histogram(self):
        import lantern as l
        l.histogram.sample()

    def test_horizontalbar(self):
        import lantern as l
        l.horizontalbar.sample()

    def test_horizontalstackedbar(self):
        import lantern as l
        l.horizontalstackedbar.sample()

    def test_line(self):
        import lantern as l
        l.line.sample()

    def test_ohlc(self):
        import lantern as l
        l.ohlc.sample()

    def test_ohlcv(self):
        import lantern as l
        l.ohlcv.sample()

    def test_pie(self):
        import lantern as l
        l.pie.sample()

    def test_scatter(self):
        import lantern as l
        l.scatter.sample()

    def test_stackedarea(self):
        import lantern as l
        l.stackedarea.sample()

    def test_stackedbar(self):
        import lantern as l
        l.stackedbar.sample()

    def test_stackedhist(self):
        import lantern as l
        l.stackedhist.sample()

    def test_timeseries(self):
        import lantern as l
        l.timeseries.sample()
