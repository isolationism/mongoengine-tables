#!/usr/bin/env python
import os
import sys
from distutils.core import setup


import re
here = os.path.dirname(os.path.abspath(__file__))
version_re = re.compile(
    r'__version__ = (\(.*?\))')
fp = open(os.path.join(here, 'mongoengine_tables', '__init__.py'))
version = None
for line in fp:
    match = version_re.search(line)
    if match:
        version = eval(match.group(1))
        break
else:
    raise Exception("Cannot find version in __init__.py")
fp.close()


def find_packages(root):
    # so we don't depend on setuptools; from the Storm ORM setup.py
    packages = []
    for directory, subdirectories, files in os.walk(root):
        if '__init__.py' in files:
            packages.append(directory.replace(os.sep, '.'))
    return packages


requirements = []
if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requirements += ['ordereddict',]


setup(
    name = 'mogoengine-tables',
    version = '0.1',
    description = 'Render QuerySets as tabular data in MongoEngine.',
    license = 'BSD',
    url = 'https://github.com/isolationism/mongoengine-tables',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
    packages = find_packages('mongoengine_tables'),
    install_requires = requirements,
)
