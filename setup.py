"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open (path.join(here, 'README.md'), encoding = 'utf-8' as f:
    long_description = f.read()

setup(
    # install this project using:
    # $ pip install Voltcycle
    #
    # PyPI URL:
    name='Voltcycle',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/

    version='1.0' # Required

    # A one-line description of the project
    description='Automated batch cyclic voltammetry data analysis for electrochemical reversibility'
    url='https://github.com/sabiharustam/Voltcycle'
    author='The Voltcyclers'
    packages=find_packages()


    install_requires=[
