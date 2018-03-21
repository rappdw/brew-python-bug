#!/usr/bin/env python
from setuptools import setup


setup_options = dict(
    name='brew_python_bug',
    version='1.0.0',
    description='Small module to demonstrate brew bug',
    author='Dan Rapp',
    license="MIT License",
    python_requires='>=3.5',
    data_files=[('config', ['config/data.json'])]
)

setup(**setup_options)
