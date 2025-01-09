#!/usr/bin/env python
import os
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = [
    "anndata==0.8.0",
    "graphtools==1.5",
    "matplotlib==3.5",
    "networkx==2.8.4",
    "numpy==1.22.0",
    "pandas==1.4.3",
    "plotly==5.9.0",
    "scipy==1.10.0",
    "scprep==1.2.3",
    "seaborn==0.11",
    "scikit-learn==1.1.1",
    "torch==1.12"
]
# 3.5

test_requirements = [ ]

setup(
    author="Amrit Singh",
    author_email='amrit.singh@hli.ubc.ca',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'bruno=bruno.cli:main',
        ],
    },
    install_requires=install_requires,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bruno',
    name='bruno',
    packages=find_packages(include=['bruno', 'bruno.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='file://' + os.path.abspath(os.path.dirname(__file__)),
    version='0.1.0',
    zip_safe=False,
)

"""
To install, run the following commands
conda create --name=explain_two Python=3.10.16
conda activate explain_two
conda install pyg -c pyg
pip install .
pip install -q torch-scatter -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
pip install -q torch-sparse -f https://data.pyg.org/whl/torch-1.12.0+cu102.html
pip install -q git+https://github.com/pyg-team/pytorch_geometric.git
pip install notebook

"""
