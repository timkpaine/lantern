
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
        l.area()

    def test_bar(self):
        import lantern as l
        l.bar()

    def test_box(self):
        import lantern as l
        l.box()

    def test_bubble(self):
        import lantern as l
        l.bubble()

    def test_heatmap(self):
        import lantern as l
        l.heatmap()

    def test_histogram(self):
        import lantern as l
        l.histogram()

    def test_line(self):
        import lantern as l
        l.line()

    def test_ohlc(self):
        import lantern as l
        l.ohlc()

    def test_ohlcv(self):
        import lantern as l
        l.ohlcv()

    def test_pie(self):
        import lantern as l
        l.pie()

    def test_scatter(self):
        import lantern as l
        l.scatter()

    def test_timeseries(self):
        import lantern as l
        l.timeseries()
