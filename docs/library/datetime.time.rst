.. currentmodule:: datetime
.. _datetime.time:

class time -- Idealised time
============================

An idealized time, independent of any particular day, assuming that every day
has exactly 24*60*60 seconds. (There is no notion of “leap seconds” here).

:py:class:`~datetime.time` objects support equality and comparison operators.

.. class:: time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
  
  Create a time object. All paramteters are optional.

    - *hour*, *minute*, *second*, *microsecond*, integers.
    - *tzinfo* an object of the :py:class`datetime.tzinfo` class. May be `None`.
    - *fold*  In [0, 1]. Used to disambiguate wall times during a repeated
      interval. (A repeated interval occurs when clocks are rolled back at the end
      of daylight saving time or when the UTC offset for the current zone is
      decreased for political reasons.) The values 0 and 1 represent,
      respectively, the earlier and later of the two moments with the same wall
      time representation.

  Other constructors:

  .. classmethod:: fromisoformat(time_string)

    Construct a :py:class:`~datetime.time` object from an ISO 8601 string::

        from datetime import time
        t = time.fromisoformat('04:23:01.000384')

  Class attributes
  .. attribute:: min

  .. attribute:: max

  .. attribute:: resolution

  Instance attributes:

  .. attribute:: hour
  .. attribute:: minute
  .. attribute:: second
  .. attribute:: microsecond
  .. attribute:: tzinfo
  .. attribute:: fold

  Instance methods:

  .. method:: replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

    Return a new :py:class:`~datetime.time` objects with the specified parameters updated.

  .. method:: isoformat()

  .. method:: strftime()

    NOT IMPLEMENTED: use :py:meth:`time.strftime`

  .. method:: tuple()
  .. method:: dst()
  .. method:: tzname()
  .. method:: utcoffset()
