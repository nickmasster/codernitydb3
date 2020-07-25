.. _api_database:

API docs
========

Here you will find API docs. If you're python user you will probably
understand it. In other case you should visit:

- :ref:`database_operations_description`
- :ref:`design`
- :ref:`quick_tutorial`

And you probably want to use |CodernityDBHTTP-link| instead this embedded version.

Database
--------

.. note::
    Please refer to :ref:`database_operations_description` for general description


Standard
^^^^^^^^

.. automodule:: codernitydb3.database
    :members:
    :undoc-members:
    :show-inheritance:


Thread Safe Database
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: codernitydb3.database_thread_safe.ThreadSafeDatabase
    :members:
    :undoc-members:
    :show-inheritance:


Super Thread Safe Database
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: codernitydb3.database_super_thread_safe
    :members:
    :undoc-members:
    :show-inheritance:


Gevent Database
^^^^^^^^^^^^^^^

.. automodule:: codernitydb3.database_gevent
    :members:
    :undoc-members:
    :show-inheritance:


Indexes
-------

.. note::
   If you're **not interested in codernitydb3 development / extending** you don't need to read this section, 
   please then refer to :ref:`database_indexes`, **otherwise** please remember that index methods are called from
   ``Database`` object.

   

General Index
^^^^^^^^^^^^^

.. automodule:: codernitydb3.index
    :members:
    :undoc-members:
    :show-inheritance:


Hash Index specific
^^^^^^^^^^^^^^^^^^^

.. note::
    Please refer to :ref:`internal_hash_index` for description

.. automodule:: codernitydb3.hash_index
    :members:
    :undoc-members:
    :show-inheritance:


B+Tree Index specific
^^^^^^^^^^^^^^^^^^^^^

.. note::
    Please refer to :ref:`internal_tree_index` for description

.. automodule:: codernitydb3.tree_index
    :members:
    :undoc-members:
    :show-inheritance:



Storage
-------

.. automodule:: codernitydb3.storage
    :members:
    :undoc-members:
    :show-inheritance:


Patches
-------

.. automodule:: codernitydb3.patch
    :members:
    :show-inheritance:
    :undoc-members:
