.. currentmodule:: monitor
.. _monitor.Monitor:

class Monitor -- information about connected monitors
=====================================================

The :ref:`monitor.Monitor <monitor.Monitor>` class provided information about monitors connected to the
DL-7450. Applications should not need to create Monitor objects, but they may be
returned from various :py:mod:`dock <dock>` module interfaces, such as :ref:`dock.DockInfo <dock.DockInfo>`.

For example::

    from dock import DockInfo
    from splashscreen import Splashscreen

    screen = Splashscreen()
    info = DockInfo()
    monitors = info.monitors()
    text = []
    for monitor in monitors:
        if monitor.valid():
            text.append(f"{monitor.name()} {monitor.preferred_mode()}")
        else:
            text.append("No monitor")
    screen.add_text_box(text)

Constructors
------------

.. class:: Monitor(edid)

   Construct a Monitor object. The input parameter is a `bytearray` representing the EDID
   from the monitor. Note, monitors do not always present a valid EDID, so always check the
   `Monitor.valid` method before any other details.

Methods
-------

.. method:: Monitor.name()

   The manufacturer's recognisable name for this monitor.

.. method:: Monitor.preferred_mode()

   The preferred screen resolution for this monitor. The return value is a pair ``(width, height)``.

.. method:: Monitor.serial_number()

   The serial number for this monitor. The return value is an `int`, based on the four byte representation
   in the underlying EDID.

.. method:: Monitor.valid()

   Check whether the EDID of this monitor is valid. If ``False``, all other methods of this class
   will return empty data.




