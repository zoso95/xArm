# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xArm',
    version='0.1.0',
    description='OsX xArm package',
    long_description=readme,
    author='Geoffrey Bradway',
    author_email='geoff.bradway@gmail.com',
    url='https://github.com/zoso95/xArm',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
