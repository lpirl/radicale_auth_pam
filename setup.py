#!/usr/bin/env python
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='radicale_auth_pam',
    version='0.0.1',
    description='Radicale Authentication through PAM',
    url='https://github.com/lpirl/radicale_auth_pam',
    author='Lukas Pirl',
    author_email='radicale@lukas-pirl.de',
    license="GNU GPL v3",
    keywords='Radicale authentication PAM',
    py_modules=["radicale_auth_pam"],
    provides=["radicale_auth_pam"],
    install_requires=['Radicale>=2.0', 'python-pam'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Office/Business :: Groupware",
    ],
)
