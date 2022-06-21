"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# prefer setuptools over distutils
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    # install this project using:
    # $ pip install voltcycle
    #
    # PyPI URL: https://pypi.org/project/voltcycle/
    name='voltcycle',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.0', # Required

    # A one-line description of the project
    description=('Automated batch cyclic voltammetry data'
                 'analysis for electrochemical reversibility'),
    url='https://github.com/sabiharustam/voltcycle',
    author='voltcycle',
    packages=find_packages(),


    install_requires=[
        'pandas==0.23.4',
        'numpy==1.22.0',
        'PeakUtils==1.3.2',
        'plotly==3.6.1',
        'dash==0.39.0',
        'dash-core-components==0.44.0',
        'dash-html-components==0.14.0',
        'dash-renderer==0.20.0',
        'dash-resumable-upload==0.0.3',
        'dash-table==3.6.0',
        'dash-table-experiments==0.6.0',
        'dashtable==1.4.5',
    ]
)
