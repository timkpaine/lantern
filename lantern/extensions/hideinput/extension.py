from nbconvert.exporters.export import exporter_map
from .exporters import PDFHideCodeExporter, HTMLHideCodeExporter


def load_jupyter_server_extension(nb_server_app):
    exporter_map['pdf_hidecode'] = PDFHideCodeExporter
    exporter_map['html_hidecode'] = HTMLHideCodeExporter
    print('Installing lantern nbconvert endpoints')
