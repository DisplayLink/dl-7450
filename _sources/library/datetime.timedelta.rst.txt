.. currentmodule:: datetime
.. _datetime.timedelta:

class timedelta -- Represents a duration
========================================

A timedelta object represents a duration, or the difference between two
:py:class:`~datetime.datetime` or :py:class:`~datetime.date` instances.

Note that :py:class:`~datetime.time` objects do not support arithmetic, due to
their cyclical, non-unique nature.

.. class:: timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

  Construct a timedelta object representing a duration or a difference between
  two points in time.

  The arguments must all be integers or floats, but may be positive or negative.
  They are subsequently combined together to form the final timedelta. That is to
  say, the following are all equivalent::

    timedelta(days=1, seconds=3600)
    timedelta(days=1, hours=1)
    timedelta(minutes=1500)

  .. attribute:: days

    The number of days in the duration. This is an integer value.

  .. attribute:: seconds

    The number of seconds in the duration. This is an integer value.

  .. attribute:: microseconds

    The number of microseconds in the duration. This is an integer value.

  .. attribute:: min

    The largest negative representable timedelta, ``timedelta(days=-999999999,
    seconds=0, microseconds=0)``.

  .. attribute:: max

    The largest positive representable timedelta, ``timedelta(days=999999999,
    seconds=86399, microseconds=999999)``.

  .. attribute:: resolution

    The smallest possible difference between non-equal timedelta objects,
    ``timedelta(microseconds=1)``.

  .. method:: total_seconds

    Return the total number of seconds contained in the duration, as a float.

  .. method:: isoformat

    Return a string representing the duration in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_.
