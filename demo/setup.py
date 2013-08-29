from setuptools import setup, find_packages

points = {
    "paste.app_factory": [
        "main=demo:main",
    ],
}

setup(
    name='demo',
    version='0.0',
    packages=find_packages(),
    url='',
    author='',
    author_email='',
    description='',
    install_requires=[
        'gargant',
    ],
    entry_points=points
)
