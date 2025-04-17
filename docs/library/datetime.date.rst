.. currentmodule:: datetime
.. _datetime.date:

class date -- Represent a date
===============================

:py:class:`~datetime.date` objects support equality and comparison operators.

.. class:: date(year, month, day)

  All arguments are required. Arguments must be integers, in the following ranges:

    - :py:class:`~datetime.MINYEAR` <= year <= :py:class:`~datetime.MAXYEAR`
    - 1 <= month <= 12
    - 1 <= day <= number of days in the given month and year

  Other constructors:

  .. classmethod:: today()

  .. classmethod:: fromtimestamp(timestamp)

  .. classmethod:: fromordinal(ordinal)

  .. classmethod:: fromisoformate(date_string)

  Class attributes:
  
  .. attribute:: min

    The earliest representable date, date(:py:attr:`~datetime.MINYEAR`, 1, 1).

  .. attribute:: max

    The latest representable date, date(:py:attr:`~datetime.MAXYEAR`, 12, 31).

  .. attribute:: resolution

    The smallest possible difference between non-equal date objects, ``timedelta(days=1)`` .

  Instance attributes:

  .. attribute:: year

  .. attribute:: month

  .. attribute:: day

  Instance methods

  .. method:: replace(year = self.year, month = self.month, day = self.day)

    Return a new :py:class:`~datetime.date` object with the same values but the specified parameters updated.

  .. method:: tuple()

    Return the date as a tuple (year, month, day)

  .. method:: timetuple()

    Return the date as a 9-tuple

  .. method:: toordinal()
    
    Return an integer representing the ordinal of the date, where January 1st of year 1 has ordinal 1.

  .. method:: isoformat()

    Return a string representing the date in ISO 8601 format, YYYY-MM-DD::

        from datetime import date
        date(2002, 12, 4).isoformat()
        # outputs '2002-12-04'

  .. method:: isoweekday()

    Return the day of the week as an integer, where Monday is 1 and Sunday is 7.

  .. method:: weekday()

    Return the day of the week as an integer, where Monday is 0 and Sunday is 6. 
