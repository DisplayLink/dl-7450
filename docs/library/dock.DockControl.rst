.. currentmodule:: dock
.. _dock.DockControl:

class DockControl -- Manage dock settings
=========================================

The DockControl class provides DL-7450 management services to applications.

.. class:: DockControl()

   Construct a DockControl object.



   .. method:: DockControl.suspend_host_connection(suspend: bool) -> None

      Send a signal to suspend/resume the host connection when a host device, such as
      a laptop or a desktop, is connected.

      This allows the python application to take control of the splashscreen, display
      pixels, and revoke connection to the dock.

      .. caution::
         Suspending the connection locks out the dock from access to both pixels and usb
         devices, effectively preventing its use as a dock.

         The connection will be suspended until either a resume is sent, an
         unplug/plug cycle of the device happens, or power cycle of the dock.

      .. caution::
         The delay between requesting the suspend/resume signal and the actual
         suspension/resumption of the host connection is currently quite long
         - several seconds. This will be addressed in a future release.

      .. code-block:: python

         from dock import DockControl

         control = DockControl()
         control.suspend_host_connection(True)  # Suspend host connection
         control.suspend_host_connection(False)  # Resume host connection

   .. method:: DockControl.set_timezone(timezone: str) -> None

      Set the timezone of the DL-7450 device. The parameter is a string which can be any of
      the accepted abbreviations from the `Time Zone Database. <https://www.iana.org/time-zones>`_
      For example:

      .. code-block:: python

         from dock import DockControl

         control = DockControl()
         control.set_timezone("PST8PDT")

      If an attempt is made to set a timezone that does not exist a `ValueError` exception is raised.
      For an invalid type a `TypeError` is raised.

   .. admonition:: Note
      :class: tip

      The following subset of the IANA timezones are supported.

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
