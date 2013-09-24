#!/usr/bin/env python

from setuptools import setup, Extension, Command, find_packages
import sys,os,platform
osname=platform.uname()[0].lower()


VERSION = '0.1.0'
DESCRIPTION = "zBzOCR is specifically designed for usage with zBzQuiz web API which can be used to extract text from images."
LONG_DESCRIPTION = """
zBzOCR is specifically designed for usage with zBzQuiz web API which can be used to extract text from images.

It also comes with a setup.py front-end that
will allow you to easily install it on your system.
"""


CLASSIFIERS = filter(None, map(str.strip,
"""
Intended Audience :: Educational Institute
License :: Apache License version 2.0
Programming Language :: Python
Operating System :: Linux :: MacOS X
Topic :: Education Software
Topic :: Office/Business
""".splitlines()))

setup(
    name="zBzOCR",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Bhavyanshu Parasher",
    author_email="bhavyanshu@codershangout.org",
    url="https://github.com/bhavyanshu/zBzQuiz",
    license="Apache License, Version 2.0",
    packages = find_packages(),
    platforms=['any'],
    zip_safe=True,
    install_requires = [
        'setuptools',
        'docutils',
	'pil',
        ],
)
