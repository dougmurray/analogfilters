
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='analogfilters',
    version='0.0.1',
    description='Electronic analog filter realizations.',
    long_description=readme,
    author='Douglass Murray',
    author_email='douglass.murray@gmail.com',
    url='https://github.com/dougmurray/analogfilters.git',
    license='MIT license',
    packages=find_packages(exclude=('notebooks', 'examples'))
)
