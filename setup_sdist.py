'''
Setup.py only for creating a source distributions.

This file holds all the common setup.py keyword arguments between the source
distribution and the ordinary setup.py for binary distribution. Running this
instead of the default setup.py will create a GitHub-like archive with setup.py
meant for installing via pip.
'''

# pylint: disable=import-error,no-name-in-module
from distutils.core import setup
from os.path import join


with open(join('pyobjus', '__init__.py')) as fd:
    VERSION = [
        x for x in fd.readlines()
        if x.startswith('__version__')
    ][0].split("'")[-2]


SETUP_KWARGS = {
    'name': 'pyobjus',
    'version': VERSION,
    'packages': ['pyobjus', pyobjus.consts],
    'py_modules': ['setup'],
    'ext_package': 'pyobjus',
    'package_data': {
        'objc_classes': ['aux/*', 'test/*'],
    },
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
}

if __name__ == '__main__':
    setup(**SETUP_KWARGS)
