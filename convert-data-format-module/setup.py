'''
Created on 2019. 1. 2.

@author: Taehyoung Yim
'''
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='ConvertDataFormatModule',
    version='0.1.0',
    description='Convert csv file to other formats.',
    long_description=readme,
    author='Taehyoung Yim',
    author_email='yim0823@naver.com',
    packages=find_packages(exclude=('tests', 'docs'))
)