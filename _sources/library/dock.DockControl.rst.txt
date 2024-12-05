.. currentmodule:: dock
.. _dock.DockControl:

class DockControl -- Manage dock settings
=========================================

The DockControl class provides DL-7450 management services to applications.

Constructors
------------

.. class:: DockControl()

   Construct a DockControl object.

.. admonition:: Coming soon
   :class: tip

   In later releases, the DockControl interface will give the application developer
   more control of the dock including:

      - set the attached screens to different resolutions.
      - show different content on different attached monitors.
      - set WiFi credentials such as SSID and password.

Methods
-------

.. method:: DockControl.set_timezone(tz)

   Set the timezone of the DL-7450 device. The parameter is a string which can be any of
   the accepted abbreviations from the `Time Zone Database. <https://www.iana.org/time-zones>`_
   For example::

      from dock import DockControl
      control = DockControl()
      control.set_timezone("PST8PDT")

   If an attempt is made to set a timezone that does not exist a `ValueError` exception is raised.
   For an invalid type a `TypeError` is raised.

.. admonition:: Coming soon
   :class: tip

   In this preview a limited subset of the IANA timezones are supported.

   +----------------------+-----------------------------------------------------+
   | Zone Code            | Notes                                               |
   +======================+=====================================================+
   | CET                  | Central European Time                               |
   +----------------------+-----------------------------------------------------+
   | CST6CDT              | USA Central Standard Time with daylight saving      |
   +----------------------+-----------------------------------------------------+
   | EET                  | Eastern European Time with daylight saving          |
   +----------------------+-----------------------------------------------------+
   | EST                  | Eastern Standard Time                               |
   +----------------------+-----------------------------------------------------+
   | GB                   | UK/Eire with daylight saving                        |
   +----------------------+-----------------------------------------------------+
   | GMT                  | UK/Eire standard time                               |
   +----------------------+-----------------------------------------------------+
   | HST                  | Hawaii–Aleutian time                                |
   +----------------------+-----------------------------------------------------+
   | Hongkong             |                                                     |
   +----------------------+-----------------------------------------------------+
   | Israel               |                                                     |
   +----------------------+-----------------------------------------------------+
   | Japan                |                                                     |
   +----------------------+-----------------------------------------------------+
   | MET                  | Same as CET                                         |
   +----------------------+-----------------------------------------------------+
   | MST                  | A zone that observes MST without daylight saving    |
   |                      | such as Arizona                                     |
   +----------------------+-----------------------------------------------------+
   | MST7MDT              | Mountain Standard Time with daylight saving         |
   +----------------------+-----------------------------------------------------+
   | NZ                   |                                                     |
   +----------------------+-----------------------------------------------------+
   | PRC                  | China                                               |
   +----------------------+-----------------------------------------------------+
   | PST8PDT              | Pacific Standard Time with daylight saving          |
   +----------------------+-----------------------------------------------------+
   | ROC                  | Taipei                                              |
   +----------------------+-----------------------------------------------------+
   | ROK                  | Republic of Korea                                   |
   +----------------------+-----------------------------------------------------+
   | Singapore            |                                                     |
   +----------------------+-----------------------------------------------------+
   | UCT                  | Universal Coordinated Time                          |
   +----------------------+-----------------------------------------------------+
   | UTC                  | Universal Coordinated Time                          |
   +----------------------+-----------------------------------------------------+
   | W-SU                 | Moscow                                              |
   +----------------------+-----------------------------------------------------+
   | WET                  | West European Time                                  |
   +----------------------+-----------------------------------------------------+
