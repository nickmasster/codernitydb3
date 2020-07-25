#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Nick M. (https://github.com/nickmasster)
# Copyright 2011-2013 Codernity (http://codernity.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

from codernitydb3 import __version__, __license__

with open('README.rst') as fhd:
    L_DESCR = fhd.read()

keywords = ' '.join(('database', 'python', 'nosql', 'key-value', 'key/value',
                     'db', 'embedded'))

setup(name='codernitydb3',
      version=__version__,
      description='Pure python, embedded, fast, schema-less, NoSQL database',
      long_description=L_DESCR,
      long_description_content_type='text/x-rst',
      keywords=keywords,
      author='Nick M.',
      author_email='nickmasster@users.noreply.github.com',
      url='https://github.com/nickmasster/codernitydb3',
      packages=['codernitydb3'],
      license=__license__,
      classifiers=[
          'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8', 'Topic :: Database',
          'Topic :: Database :: Database Engines/Servers', 'Topic :: Internet',
          'Topic :: Software Development'
      ],
      python_requires='>=3.5')
