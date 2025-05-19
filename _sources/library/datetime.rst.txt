
:mod:`datetime` -- time manipulation functionality
==================================================

This module is a partial implementation of `datetime
<https://docs.python.org/3/library/datetime.html>`_ from standard CPython.

.. module:: datetime
  :synopsis: time manipulation functionality


Constants
---------

  .. data:: datetime.MINYEAR

    The smallest year that can be represented by a :py:class:`date` or :py:class:`datetime` object, which is ``1`` as per CPython.

  .. data:: datetime.MAXYEAR

    The largest year that can be represented by a :py:class:`date` or :py:class:`datetime` object, which is ``9999`` as per CPython.

Classes
-------
.. toctree::
  :maxdepth: 1

  datetime.date.rst
  datetime.datetime.rst
  datetime.time.rst
  datetime.timedelta.rst
  datetime.timezone.rst
  datetime.tzinfo.rst
