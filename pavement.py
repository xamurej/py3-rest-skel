#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import paver.doctools  # NOQA
from paver.easy import Bunch, options, sh, task
from paver.setuputils import find_packages, setup


def requirements():
    with open('requirements.txt') as handle:
        return handle.read().splitlines()


setup(
    name='RESTapp',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    entry_points={'console_scripts': ['restapp=rest_app.server:main'], },
    install_requires=requirements(),
    zip_safe=True,

    # Metadata for PyPI upload
    description='REST example application',
    author='Your Name',
    author_email='you@example.com',
    url='https://github.com/xamurej/py3-rest-skel',
    # The complete list of classifiers can be checked at
    # <https://pypi.python.org/pypi?%3Aaction=list_classifiers>
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ], )

options(
    sphinx=Bunch(
        builddir="_build"
    )
)


@task
def check(options):
    """run flake8 linter from tox"""
    sh("tox -e py34-flake8")
