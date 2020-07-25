CodernityDB pure python, NoSQL, fast database
=============================================

CodernityDB is opensource, pure python (no 3rd party dependency), fast (really fast check Speed in documentation if you don't believe in words), multiplatform, schema-less, `NoSQL <http://en.wikipedia.org/wiki/NoSQL>`_ database. It has optional support for HTTP server version (CodernityDB-HTTP), and also Python client library (CodernityDB-PyClient) that aims to be 100% compatible with embeded version.

.. image:: docs/CodernityDB.png
  :align: center

You can call it a more advanced key-value database. With multiple key-values indexes in the same engine. Also CodernityDB supports functions that are executed inside database.

Visit `Codernity Labs`_ to see documentation (included in repo).

Note: *documentation might be outdated due to migration*

Migration to Python 3.x
-----------------------

**MIGRATION IS IN PROGRESS - SOME FEATURES MAY BE NOT PROPERLY SUPPORTED YET**

Unfortunately, when I found this database, Python 2.7 reached the end of its life and was no longer supported.

So I decided to port CodernityDB to Python 3.x. 

I didn't want to use tools allows simultaneous support for both versions, as it make no sense due to Python 2 EOL. Instead I tried to modify the code to work correctly on Python 3.

Currently 98% of the test are successfully passed, but there's still a lot of work to do.

Version for Python 2.x
----------------------

Original version of CodernityDB is one of projects developed and released by `Codernity Labs`_.

Latest CodernityDB vesion with Python 2.x support was 0.5.0. You can find it's source code in the `official repository <https://bitbucket.org/codernity/codernitydb>`_.

Key features
------------

* Native python database
* Multiple indexes
* Fast (more than 50 000 insert operations per second see Speed in documentation for details)
* Embeded mode (default) and Server (CodernityDB-HTTP), with client library (CodernityDB-PyClient) that aims to be 100% compatible with embeded one.
* Easy way to implement custom Storage
* Sharding support

Install
-------

Because CodernityDB is pure Python you need to perform standard installation for Python applications::

   pip install codernitydb3

or using easy_install::

   easy_install codernitydb3

or from sources::

   git clone ssh://git@github.com:nickmasster/codernitydb3.git
   cd codernitydb3
   python setup.py install

License
-------

Copyright 2020 Nick M. (https://github.com/nickmasster)

Copyright 2011-2013 Codernity (http://codernity.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

.. _Codernity Labs: http://labs.codernity.com/codernitydb