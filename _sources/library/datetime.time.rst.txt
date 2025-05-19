.. currentmodule:: datetime
.. _datetime.time:

class time -- Represent a time
==============================

A representation of a time, assuming that every day is composed of 24 hours, each
hour composed of 60 minutes, and each minute composed of 60 seconds.

N.B. time objects have no notion of "leap seconds".

:py:class:`~datetime.time` objects support equality and comparison operators.

.. class:: time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

  Construct a time object representing a given ``hour``, ``minute``, ``second``
  and ``microsecond``. The arguments are as follows:

  - ``hour``, ``minute``, ``second`` and ``microsecond`` are integers in the
    given ranges:

    - ``0`` <= ``hour`` < ``24``
    - ``0`` <= ``minute`` < ``60``
    - ``0`` <= ``second`` < ``60``
    - ``0`` <= ``microsecond`` < ``1000000``

    Each of these arguments will default to ``0`` if omitted.
  - ``tzinfo`` is a :py:class:`datetime.tzinfo` object, allowing a time to be
    associated with a particular timezone. If this is not desired, the ``tzinfo``
    can be `None`.
  - ``fold`` is a value of either ``0`` or ``1`` used to disambiguate wall times
    during a repeated interval. A repeated interval occurs when clocks are rolled
    back at the end of daylight saving time, or when the UTC offset for the
    current zone is decreased for political reasons. The values ``0`` and ``1``
    represent, respectively, the earlier and later of the two moments with the
    same wall time representation.

  .. classmethod:: fromisoformat(time_string)

    Construct a :py:class:`~datetime.time` object from a string in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_::

        from datetime import time
        t = time.fromisoformat('07:55:27.999999')

  .. attribute:: min

    The earliest representable time, ``time(0, 0, 0, 0)``.

  .. attribute:: max

    The latest representable time, ``time(23, 59, 59, 999999)``.

  .. attribute:: resolution

    The smallest possible difference between non-equal time objects,
    ``timedelta(microseconds=1)``.

  .. attribute:: hour

    The hour of the time, an integer in the range ``0`` to ``23``.

  .. attribute:: minute

    The minute of the time, an integer in the range ``0`` to ``59``.

  .. attribute:: second

    The second of the time, an integer in the range ``0`` to ``59``.

  .. attribute:: microsecond

    The microsecond of the time, an integer in the range ``0`` to ``999999``.

  .. attribute:: tzinfo

    The :py:class:`datetime.tzinfo` object associated with the time, or `None`
    if no timezone information is associated with the time.

  .. attribute:: fold

    Used to disambiguate wall times during a repeated interval. The values ``0``
    and ``1`` represent, respectively, the earlier and later of the two moments
    with the same wall time representation.

  .. method:: replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

    Return a new :py:class:`~datetime.time` object with the same values as the
    existing time object, but with the specified parameters updated.

  .. method:: isoformat(timespec="auto")

    Return a string representing the time in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_.
    
    By default, this will output time in the format ``HH-MM-SS`` (or
    ``HH-MM-SS.ssssss`` if `microsecond` is not ``0``). The optional ``timespec``
    argument can be used to specify the number of digits to include in the output
    string:

    * ``'hours'``: ``HH``
    * ``'minutes'``: ``HH:MM``
    * ``'seconds'``: ``HH:MM:SS``
    * ``'milliseconds'``: ``HH:MM:SS.sss``
    * ``'microseconds'``: ``HH:MM:SS.ssssss``

  .. method:: tuple()

    Return the time as a 6-tuple
    ``(hour, minute, second, microsecond, tzinfo, fold)``.

  .. method:: dst()

    Return the daylight savings time offset as a :py:class:`datetime.timedelta`
    object, or `None` if the time has no associated timezone.

  .. method:: tzname()

    Return the name of the timezone as a string, or `None` if the time has no
    associated timezone.

  .. method:: utcoffset()

    Return the UTC offset as a :py:class:`datetime.timedelta` object, or `None`
    if the time has no associated timezone.
