from mock import patch, MagicMock


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

    def test_ip1(self):
        with patch('lantern.utils.get_ipython') as m:
            m.return_value = None
            from lantern.utils import in_ipynb
            assert in_ipynb() == False

    def test_ip2(self):

        with patch('lantern.utils.get_ipython') as m:
            m.return_value = MagicMock()
            from lantern.utils import in_ipynb
            m.return_value.config = {'IPKernelApp': {'parent_appname': False}}
            assert in_ipynb() == False

    def test_ip3(self):

        with patch('lantern.utils.get_ipython') as m:
            m.return_value = MagicMock()
            m.return_value.config = {'IPKernelApp': {'parent_appname': True}}

            from lantern.utils import in_ipynb
            assert in_ipynb() == True
