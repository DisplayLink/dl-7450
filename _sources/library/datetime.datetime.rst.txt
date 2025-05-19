.. currentmodule:: datetime
.. _datetime.datetime:

class datetime -- Represent a date and time
===========================================

.. class:: datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

  A datetime object is a single object containing all the information from a
  :py:class:`~datetime.date` object and a :py:class:`~datetime.time` object.

  The arguments are as follows:

  - ``year``, ``month``, ``day``, ``hour``, ``minute``, ``second`` and
    ``microsecond`` are integers in the given ranges:

    - :py:class:`~datetime.MINYEAR` <= ``year`` <= :py:class:`~datetime.MAXYEAR`
    - ``1`` <= ``month`` <= ``12``
    - ``1`` <= ``day`` <= number of days in the given month and year
    - ``0`` <= ``hour`` < ``24``
    - ``0`` <= ``minute`` < ``60``
    - ``0`` <= ``second`` < ``60``
    - ``0`` <= ``microsecond`` < ``1000000``

    Each of these arguments will default to ``0`` if omitted.

  - ``tzinfo`` is a :py:class:`datetime.tzinfo` object, allowing a datetime to be
    associated with a particular timezone. If this is not desired, the ``tzinfo``
    can be `None`.
  - ``fold`` is a value of either ``0`` or ``1`` used to disambiguate wall times
    during a repeated interval. A repeated interval occurs when clocks are rolled
    back at the end of daylight saving time, or when the UTC offset for the
    current zone is decreased for political reasons. The values ``0`` and ``1``
    represent, respectively, the earlier and later of the two moments with the
    same wall time representation.

  .. classmethod:: fromisoformat

    Construct a datetime object from a string in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_::

        from datetime import datetime
        dt = datetime.fromisoformat('2012-12-21 07:55:27.999999')

  .. classmethod:: fromordinal(ordinal)

    Construct a datetime object representing the year, month and day specified by
    the provided ``ordinal``.

    An ``ordinal`` is an integer representing the number of days since January
    1st of year 1.

    The ``hour``, ``minute``, ``second``, and ``microsecond`` arguments will all
    be set to ``0``, and ``tzinfo`` will be set to `None`.

  .. classmethod:: fromtimestamp(timestamp, tz=None)

    Construct a datetime object representing the year, month and day specified by
    the provided ``timestamp``.

    A ``timestamp`` in this case is a floating point number representing the
    number of seconds since the epoch (January 1, 1970, 00:00:00 UTC).

    An optional ``tz`` argument may be provided to specify the timezone of the
    resulting datetime.

  .. classmethod:: now(tz=None)

    Construct a datetime object representing the current date and time.

    An optional ``tz`` argument may be provided to specify the timezone of the
    resulting datetime.

  .. classmethod:: combine(date, time, tzinfo=None)

    Construct a datetime object from a date and time object.

    The ``date`` and ``time`` arguments must be instances of
    :py:class:`~datetime.date` and :py:class:`~datetime.time`, respectively.

    The ``tzinfo`` argument is optional and will be used to set the timezone of
    the resulting datetime. If not provided, the timezone (or lack thereof) will
    be inferred from the ``time`` argument.

  .. attribute:: EPOCH

    A :py:class:`~datetime.datetime` object representing the Unix epoch (January
    1, 1970, 00:00:00 UTC).

  .. attribute:: year

    The year of the datetime, an integer in the range
    :py:class:`~datetime.MINYEAR` to :py:class:`~datetime.MAXYEAR`.

  .. attribute:: month

    The month of the datetime, an integer in the range ``1`` to ``12``.

  .. attribute:: day

    The day of the datetime, an integer in the range ``1`` to the number of days
    in the month represented by `month`.

  .. attribute:: hour

    The hour of the datetime, an integer in the range ``0`` to ``23``.

  .. attribute:: minute

    The minute of the datetime, an integer in the range ``0`` to ``59``.

  .. attribute:: second

    The second of the datetime, an integer in the range ``0`` to ``59``.

  .. attribute:: microsecond

    The microsecond of the datetime, an integer in the range ``0`` to
    ``999999``.

  .. attribute:: tzinfo

    The :py:class:`datetime.tzinfo` object associated with the datetime, or
    `None` if no timezone information is associated with the datetime.

  .. attribute:: fold

    Used to disambiguate wall times during a repeated interval. The values
    ``0`` and ``1`` represent, respectively, the earlier and later of the two
    moments with the same wall time representation.

  .. method:: replace(year=self.year, month=self.year, day=self.year, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

    Return a new :py:class:`~datetime.datetime` object with the same values as
    the existing datetime object, but with the specified parameters updated.

  .. method:: tuple()

    Return the datetime as a 9-tuple
    ``(year, month, day, hour, minute, second, microsecond, tzinfo, fold)``.

  .. method:: astimezone(tz=None)

    Return a datetime that represents the same point in time, relative to the
    specified timezone ``tz``. The current datetime must already have an
    associated ``tzinfo``, otherwise this method will raise a
    `NotImplementedError`.

  .. method:: date()

    Return the date portion of the datetime as a :py:class:`~datetime.date`
    object. The resulting object will have no timezone information.

  .. method:: time()

    Return the time portion of the datetime as a :py:class:`~datetime.time`
    object. The resulting object will have no timezone information.

  .. method:: timetz()

    Return the time portion of the datetime as a :py:class:`~datetime.time`
    object. The resulting object will have the same timezone information as the
    original datetime.

  .. method:: dst()

    Return the daylight savings time offset as a :py:class:`datetime.timedelta`
    object, or `None` if the time has no associated timezone.

  .. method:: isoformat(sep="T", timespec="auto")

    Return a string representing the datetime in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_.

    By default, this will output the date and time in the format
    ``YYYY-MM-DDTHH:MM:SS`` (or ``YYYY-MM-DDTHH:MM:SS.ssssss`` if
    `microsecond` is not ``0``). The optional ``sep`` argument can be
    used to specify the separator between the date and time portions of the
    output string. The optional ``timespec`` argument can be used to specify
    the number of digits to include in the output string:

    * ``'hours'``: ``YYYY-MM-DDTHH``
    * ``'minutes'``: ``YYYY-MM-DDTHH:MM``
    * ``'seconds'``: ``YYYY-MM-DDTHH:MM:SS``
    * ``'milliseconds'``: ``YYYY-MM-DDTHH:MM:SS.sss``
    * ``'microseconds'``: ``YYYY-MM-DDTHH:MM:SS.ssssss``

  .. method:: isoweekday()

    Return the day of the week as an integer, where Monday is ``1`` and Sunday is
    ``7``.

  .. method:: weekday()

    Return the day of the week as an integer, where Monday is ``0`` and Sunday is
    ``6``. 

  .. method:: timetuple()

    Return the datetime as a 9-tuple
    ``(year, month, day, hour, minute, second, weekday, yearday, dst)``.

    In this case:

    * ``weekday`` is the day of the week as an integer, where Monday is ``0``
      and Sunday is ``6``.
    * ``yearday`` is the day of the year as an integer, where January 1st is
      ``1``.
    * ``dst`` is ``-1`` if there is no associated timezone, ``0`` if the
      associated timezone does not observe daylight savings time, or ``1`` if it
      does.

  .. method:: toordinal()

    Return an integer representing the ordinal of the date, where January 1st
    of year 1 has ordinal ``1``.

  .. method:: tzname()

    Return the name of the timezone as a string, or `None` if the datetime has no
    associated timezone.

  .. method:: utcoffset()

    Return the UTC offset as a :py:class:`datetime.timedelta` object, or `None`
    if the datetime has no associated timezone.
