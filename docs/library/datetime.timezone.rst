.. currentmodule:: datetime
.. _datetime.timezone:

class timezone -- Represents a fixed offset time zone
=====================================================

  The timezone class is a subclass of :py:class:`~datetime.tzinfo`, each instance
  of which represents a time zone defined by a fixed offset from UTC.

  Note that these timezones do not have any offset capability beyond the fixed
  offset provided during construction. To represent such a timezone, such as a
  timezone with daylight saving time, a subclass of :py:class:`~datetime.tzinfo`
  must be created.

.. class:: timezone(offset, name=None)

  Construct a timezone object with a fixed :py:class:`~datetime.timedelta`
  ``offset`` from UTC. An optional ``name`` may be provided, which is a string
  representing the time zone name.

  .. method:: dst(dt)

    As these classes are not aware of daylight saving time, this method always
    returns `None`.

  .. method:: fromutc(dt)

    Convert a UTC time given by ``dt`` to the local time in this timezone by
    adding its ``offset``.

  .. method:: isoformat(dt)

    Return a string representing the time zone in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_.

  .. method:: tzname(dt)

    Return the time zone name as a string, or `None` if the time zone name isn’t
    known.

  .. attribute:: utcoffset(dt)

    The `timedelta` representing the timezone's UTC offset.
