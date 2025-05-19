
.. currentmodule:: datetime
.. _datetime.tzinfo:

class tzinfo -- Timezone information
====================================

An abstract base class for time zone information objects. These are used by the
:py:class:`~datetime.datetime` and :py:class:`~datetime.time` classes to provide
a customizable notion of time adjustment (for example, to account for time zone
and/or daylight saving time).

For many use cases, it is recommended to use the :py:class:`~datetime.timezone`
class, which models fixed offsets from UTC. If these are not suitable, a
subclass of :py:class:`tzinfo` can be created, with all abstract methods
implemented.

.. class:: tzinfo()

  .. method:: dst(dt)
    :abstractmethod:

    Return the daylight saving time (DST) adjustment as a `timedelta` object, or
    `None` if DST information isn’t known, given a particular ``dt``.

  .. method:: tzname(dt)
    :abstractmethod:

    Return the time zone name as a string, or `None` if the time zone name isn’t
    known, given a particular ``dt``.

  .. method:: utcoffset(dt)
    :abstractmethod:

    Return the UTC offset as a `timedelta` object, or `None` if the UTC offset
    isn’t known, given a particular ``dt``.

  .. method:: fromutc(dt)

    Convert a UTC time given by ``dt`` to the local time in the time zone
    represented by this object. This method is called by
    :py:meth:`datetime.datetime.astimezone()`.

    Note that the datetime object passed to this method is in UTC, but the
    :py:attr:`datetime.tzinfo` attribute is already set to the desired tzinfo.
    This function should merely subtract the desired UTC offset from the
    passed-in datetime object.

    The default implementation works well for coverting between timezones, but
    can handle the hours around some DST transitions incorrectly. This method
    can be overridden to handle this, as well as other exceptional situations.
    Please read `PEP 495 <https://peps.python.org/pep-0495/>`_ for more
    information.

  .. method:: isoformat(dt)

    Return a string representing the time zone in
    `ISO 8601 format <https://www.iso.org/iso-8601-date-and-time-format.html>`_,
    given a particular ``dt``.
