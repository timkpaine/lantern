import os
import os.path
from nbconvert.nbconvertapp import NbConvertApp
from nbconvert.exporters.html import HTMLExporter
from nbconvert.exporters.pdf import PDFExporter


_html_no_code_template = os.path.join(os.path.dirname(__file__), 'templates', 'hide_code_cells_html.tpl')
_pdf_no_code_template = os.path.join(os.path.dirname(__file__), 'templates', 'hide_code_cells_pdf.tplx')


def export_pdf(nbpath):
    NbConvertApp.launch_instance([nbpath, '--template', _pdf_no_code_template, '--to', 'pdf'])


def export_html(nbpath):
    NbConvertApp.launch_instance([nbpath, '--template', _html_no_code_template, '--to', 'html'])


class HTMLHideCodeExporter(HTMLExporter):
    # exclude_input = True
    def _file_extension_default(self):
        return '.html'

    @property
    def template_path(self):
        return super(HTMLHideCodeExporter, self).template_path + [os.path.join(os.path.dirname(__file__), 'templates')]

    def _template_file_default(self):
        return 'hide_code_cells_html.tpl'


class PDFHideCodeExporter(PDFExporter):
    def _file_extension_default(self):
        return '.pdf'

    @property
    def template_path(self):
        return super(PDFHideCodeExporter, self).template_path + [os.path.join(os.path.dirname(__file__), 'templates')]

    def _template_file_default(self):
        return 'hide_code_cells_pdf.tplx'
