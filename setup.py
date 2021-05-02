"""
Building with:
python setup.py bdist_wheel sdist
twine upload dist/*
"""

from setuptools import setup
from os import path

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="QuickCite",
    version="0.0.4",
    description="Pure Python wrapper for the Formatically Citation Website.",
    py_modules=["QuickCite"],
    package_dir={'':'src'},
    install_requires = [
        "requests==2.25.1"
    ],
    url="https://github.com/http-samc/citer",
    author="Samarth Chitgopekar",
    author_email="sam@chitgopekar.tech",
    long_description=long_description,
    long_description_content_type='text/markdown'
)