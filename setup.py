#! /usr/bin/env python

from setuptools import setup, find_packages
from testharness.rest_api import __version__


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='testharness_rest_api',
      version=__version__,
      license='PSF',
      description='REST API Test Harness for unittest',
      long_description=readme(),
      author='Andrew Droffner',
      author_email='ad718x@us.att.com',
      url='https://codecloud.web.att.com/projects/ST_TITAN/repos/test-harness-rest-api-lib/browse',
      packages=find_packages(exclude=['docs', 'tests']),
      install_requires=[
          'requests>=2.20.1',
      ],
      test_suite='nose.collector',
      # tests_require=['nose>=1.3.7', 'coverage>=4.4.1'],
      # NOTE: ./setup.py nosetests <= needs "setup_requires"
      setup_requires=['nose>=1.3.7', 'coverage>=4.4.1'],
      keywords=[
          'testharness', 'test', 'harness',
          'REST', 'API'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ])
