import os.path
from nbconvert.nbconvertapp import NbConvertApp

_html_no_code_template = os.path.join('/'.join(__file__.split('/')[:-1]), 'hide_code_cells_html.tpl')
_pdf_no_code_template = os.path.join('/'.join(__file__.split('/')[:-1]), 'hide_code_cells_pdf.tplx')


def export_pdf(nbpath):
    NbConvertApp.launch_instance([nbpath, '--template', _pdf_no_code_template, '--to', 'pdf'])


def export_html(nbpath):
    NbConvertApp.launch_instance([nbpath, '--template', _html_no_code_template, '--to', 'html'])
