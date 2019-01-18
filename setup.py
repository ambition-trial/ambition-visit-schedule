# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()


tests_require = []
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ambition-visit-schedule',
    version=VERSION,
    author='Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ambition-trial/ambition-visit-schedule',
    license='GPL license, see LICENSE',
    description='Visit schedule for ambition/edc project',
    long_description=README,
    zip_safe=False,
    keywords='ambition visit schedule',
    install_requires=[
        'ambition-labs',
        'ambition-sites',
        'edc-base',
        'edc_visit_schedule',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.6",
    tests_require=tests_require,
    test_suite='runtests.main',
)
