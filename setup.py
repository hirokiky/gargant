import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)

readme = open(os.path.join(here, "README.rst")).read()

setup(
    name='gargant',
    version='0.0',
    packages=find_packages(),
    url='https://github.com/hirokiky/gargant/',
    license='MIT License',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='experimental web framework',
    install_requires=[
        'webob',
        'mako',
        'gearbox',
        'paste',
    ],
)
