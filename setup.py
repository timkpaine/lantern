from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylantern',
    version='0.0.17',
    description='Analytics library',
    long_description=long_description,
    url='https://github.com/timkpaine/lantern',
    download_url='https://github.com/timkpaine/lantern/archive/v0.0.17.tar.gz',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='LGPL',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='analytics tools plotting',

    packages=find_packages(exclude=['tests', ]),
    package_data={'lantern': ['lantern/extensions/hideinput/templates/*',
                              'lantern/extensions/publish/templates/*']},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'nbconvert.exporters': [
            'pdf_hidecode = lantern.extensions.hideinput.exporters:PDFHideCodeExporter',
            'html_hidecode = lantern.extensions.hideinput.exporters:HTMLHideCodeExporter',
        ],
    }
)
