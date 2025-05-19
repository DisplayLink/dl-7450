.. currentmodule:: datetime
.. _datetime.date:

class date -- Represent a date
===============================

A representation of a date, according to the Gregorian calendar.

:py:class:`~datetime.date` objects support equality and comparison operators.

.. class:: date(year, month, day)

  Construct a date object representing the given ``year``, ``month`` and ``day``.

  Arguments must be integers in the following ranges:

    - :py:class:`~datetime.MINYEAR` <= ``year`` <= :py:class:`~datetime.MAXYEAR`
    - ``1`` <= ``month`` <= ``12``
    - ``1`` <= ``day`` <= number of days in the given month and year

  .. classmethod:: today()

    Construct a date object representing today's year, month and day.

  .. classmethod:: fromtimestamp(timestamp)

    Construct a date object representing the year, month and day specified by the
    provided ``timestamp``.

    A ``timestamp`` in this case is a floating point number representing the
    number of seconds since the epoch (January 1, 1970, 00:00:00 UTC).

  .. classmethod:: fromordinal(ordinal)

    Construct a date object representing the year, month and day specified by the
    provided ``ordinal``.

    An ``ordinal`` is an integer representing the number of days since January
    1st of year 1.

  .. classmethod:: fromisoformat(date_string)

    Construct a date object from a string in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_::

        from datetime import date
        d = date.fromisoformat('2012-12-21')

  .. attribute:: min

    The earliest representable date, ``date(datetime.MINYEAR, 1, 1)``.

  .. attribute:: max

    The latest representable date, ``date(datetime.MAXYEAR, 12, 31)``.

  .. attribute:: resolution

    The smallest possible difference between non-equal date objects,
    ``timedelta(days=1)``.

  .. attribute:: year

    The year of the date, an integer in the range :py:class:`~datetime.MINYEAR`
    to :py:class:`~datetime.MAXYEAR`.

  .. attribute:: month

    The month of the date, an integer in the range ``1`` to ``12``.

  .. attribute:: day

    The day of the date, an integer in the range ``1`` to the number of days
    in the month represented by :py:attr:`month`.

  .. method:: replace(year = self.year, month = self.month, day = self.day)

    Return a new :py:class:`~datetime.date` object with the same values as the
    existing date object, but with the specified parameters updated.

  .. method:: tuple()

    Return the date as a 3-tuple ``(year, month, day)``.

  .. method:: timetuple()

    Return the date as a 9-tuple
    ``(year, month, day, hour, minute, second, weekday, yearday, dst)``, as
    described in :py:meth:`datetime.datetime.timetuple`.

    In this case:

    * ``hour``, ``minute`` and ``second`` are all ``0``, as the date object does
      not contain time information.
    * ``weekday`` is the day of the week as an integer, where Monday is ``0`` and
      Sunday is ``6``.
    * ``yearday`` is the day of the year as an integer, where January 1st is
      ``1``.
    * ``dst`` is ``-1``, as the date object does not contain daylight savings
      information.

  .. method:: toordinal()

    Return an integer representing the ordinal of the date, where January 1st
    of year 1 has ordinal ``1``.

  .. method:: isoformat()

    Return a string representing the date in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_,
    ``YYYY-MM-DD``::

        from datetime import date
        date(2002, 12, 4).isoformat()
        # outputs '2002-12-04'

  .. method:: isoweekday()

    Return the day of the week as an integer, where Monday is ``1`` and Sunday is
    ``7``.

  .. method:: weekday()

    Return the day of the week as an integer, where Monday is ``0`` and Sunday is
    ``6``.
