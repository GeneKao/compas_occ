#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# flake8: noqa
import io
from os import path

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


here = path.abspath(path.dirname(__file__))


def read(*names, **kwargs):
    return io.open(
        path.join(here, *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


long_description = read("README.md")
requirements = read("requirements.txt").split("\n")
optional_requirements = {}

setup(
    name="compas_occ",
    version="0.4.2",
    description="COMPAS wrapper for the Python bindings of OCC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/compas-dev/compas_occ",
    author="tom van mele",
    author_email="van.mele@arch.ethz.ch",
    license="MIT license",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords=[],
    project_urls={},
    packages=["compas_occ"],
    package_dir={"": "src"},
    package_data={},
    data_files=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    python_requires=">=3.6",
    extras_require=optional_requirements,
    entry_points={
        "console_scripts": [],
    },
    ext_modules=[],
)
