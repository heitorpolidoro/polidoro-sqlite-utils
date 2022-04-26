"""
Setup to create the package
"""
from setuptools import setup, find_packages

import polidoro_sqlite_utils

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='polidoro-sqlite-utils',
    version=polidoro_sqlite_utils.VERSION,
    description='Polidoro SQLite Utils.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/heitorpolidoro/polidoro-sqlite-utils',
    author='Heitor Polidoro',
    license='unlicense',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    include_package_data=True
)
