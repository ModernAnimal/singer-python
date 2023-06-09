#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='5.13.0',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'pytz',
          'jsonschema',
          'simplejson',
          'python-dateutil',
          'backoff',
	  'ciso8601',
      ],
      extras_require={
          'dev': [
              'pylint',
              'ipython',
              'ipdb',
              'nose',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
