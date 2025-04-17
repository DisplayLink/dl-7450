
.. currentmodule:: datetime
.. _datetime.tzinfo:

class tzinfo -- Timezone information
====================================

An abstract base class for time zone information objects. These are used by the
datetime and time classes to provide a customizable notion of time adjustment
(for example, to account for time zone and/or daylight saving time).

.. class:: tzinfo()
  
  .. method:: dst()

    Return the daylight saving time (DST) adjustment, as a `timedelta` object or
    None if DST information isn’t known.

  .. method:: fromutc()

  .. method:: isoformat()

  .. method:: tzname()

  .. method:: utcoffset()
