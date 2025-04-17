.. currentmodule:: timezone
.. _datetime.timezone:

class timezone -- Represents a time zone
========================================

  The timezone class is a subclass of :py:class:`~datetime.tzinfo`, each instance
  of which represents a time zone defined by a fixed offset from UTC.

.. class:: timezone(offset, name=None)

   .. method:: dst
   .. method:: fromutc
   .. method:: isoformat
   .. method:: tzname
   .. method:: utc
   .. method:: utcoffset
