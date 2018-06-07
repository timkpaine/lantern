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

    def test_obj(self):
        from lantern.extensions.hideinput.extension import HTMLHideCodeExporter, PDFHideCodeExporter
        x = HTMLHideCodeExporter()
        y = PDFHideCodeExporter()

        x.template_path
        x._template_file_default()
        x._file_extension_default()
        y.template_path
        y._template_file_default()
        y._file_extension_default()

    def test_launch(self):
        from lantern.extensions.hideinput.extension import load_jupyter_server_extension
        load_jupyter_server_extension(MagicMock())

    def test_export(self):
        with patch('lantern.extensions.hideinput.exporters.NbConvertApp'):
            from lantern.extensions.hideinput.exporters import export_pdf, export_html
            export_html(MagicMock())
            export_pdf(MagicMock())
