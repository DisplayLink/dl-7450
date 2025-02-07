.. currentmodule:: datastore
.. _datastore.KvStore:

class KvStore -- store and retrieve simple data
===============================================


Constructors
------------

.. class:: KvStore()

   Construct a KvStore object.

Methods
-------

.. method:: KvStore.list()

   List the keys in the `KvStore` that have assigned values.

.. method:: KvStore.get(key)

   Retrieve a value using its key. Will return an empty string ``''`` in case the given key does not exist.

