#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = [
    "anndata",
    "graphtools",
    "matplotlib",
    "networkx",
    "numpy",
    "scipy",
    "scprep",
    "sklearn",
    "torch",
    "torch_sparse",
    "torch_scatter",
    "torch_geometric"
]

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
    url='https://github.com/singha53/bruno',
    version='0.1.0',
    zip_safe=False,
)
