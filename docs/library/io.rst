:mod:`io` -- input/output streams
=================================

.. module:: io
   :synopsis: input/output streams

This module contains additional types of stream (file-like) objects
and helper functions.

Conceptual hierarchy
--------------------

.. admonition:: Difference to CPython
   :class: attention

   The hierarchy of stream base classes is simplified compared to CPython.

Functions
---------

.. function:: open(name, mode='r', **kwargs)

    Open a file. The builtin :py:func:`open` function is aliased to this function.

Classes
-------

.. class:: StringIO([string])
.. class:: BytesIO([string])

    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with the *string* parameter (should be `str`
    for `StringIO` or `bytes` for `BytesIO`). All the usual file
    methods from CPython like ``read()``, ``write()``, ``seek()``,
    ``flush()`` and ``close()`` are available on these objects, and
    additionally, a following method:

    .. method:: getvalue()

        Get the current contents of the underlying buffer which holds data.

.. class:: StringIO(alloc_size)
    :noindex:
.. class:: BytesIO(alloc_size)
    :noindex:

    Create an empty `StringIO`/`BytesIO` object, preallocated to hold up
    to *alloc_size* number of bytes. That means that writing that amount
    of bytes won't lead to reallocation of the buffer, and thus won't hit
    out-of-memory situation or lead to memory fragmentation. These constructors
    are recommended for usage only in special cases.
