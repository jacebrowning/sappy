#!/usr/bin/env python

"""Setup script for sappy."""

import setuptools

from sappy import __project__, __version__

try:
    README = open("README.rst").read()
    CHANGELOG = open("CHANGELOG.rst").read()
except IOError:
    LONG_DESCRIPTION = "<placeholder>"
else:
    LONG_DESCRIPTION = README + '\n' + CHANGELOG

setuptools.setup(
    name=__project__,
    version=__version__,

    description="Single-page application server for end-to-end testing.",
    url='https://github.com/jacebrowning/sappy',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': ['sappy = sappy.cli:main']},

    long_description=LONG_DESCRIPTION,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
    ],

    install_requires=open("requirements.txt").readlines(),
)
