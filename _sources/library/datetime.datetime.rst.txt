.. currentmodule:: datetime
.. _datetime.datetime:

class datetime -- Information about a date and time
===================================================

.. class:: datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

    A datetime object is a single object containing all the information from a
    :py:class:`~datetime.date` object and a :py:class:`~datetime.time` object.

    Other constructors:

    .. classmethod:: fromisoformat
    .. classmethod:: fromordinal
    .. classmethod:: fromtimestamp
    .. classmethod:: now

      NOT IMPLEMENTED

    .. classmethod:: combine

    .. classmethod:: strptime

        *NOT IMPLEMENTED*

    Class attributes:

    .. attribute:: EPOCH
      
      A :py:class:`~datetime.datetime` object representing the epoch.

    Instance attributes:

    .. attribute:: year
    .. attribute:: month
    .. attribute:: day
    .. attribute:: hour
    .. attribute:: minute
    .. attribute:: second
    .. attribute:: microsecond
    .. attribute:: tzinfo
    .. attribute:: fold

    Instance methods:

    .. method:: replace
    .. method:: tuple
    .. method:: time
    .. method:: astimezone
    .. method:: date
    .. method:: dst
    .. method:: isoformat

    .. method:: isoweekday()

      Return the day of the week as an integer, where Monday is 1 and Sunday is 7.

    .. method:: weekday()

      Return the day of the week as an integer, where Monday is 0 and Sunday is 6. 

    .. method:: timetuple()
    .. method:: timetz()
    .. method:: toordinal()
    .. method:: tzname()
    .. method:: utcoffset()
