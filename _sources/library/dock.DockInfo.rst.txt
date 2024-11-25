.. currentmodule:: dock
.. _dock.DockInfo:

class DockInfo - current information about the dock
===================================================

The DockInfo class gives current information about the DL-7450.

Constructors
------------

.. class:: DockInfo()

   Construct a DockInfo object.

Methods
-------

.. method:: DockInfo.dock_id()

   Obtain the unique identifier of this dock. This identifier could be used for
   registering the dock as an IoT device with a service provider. For example::

      from dock import DockInfo
        info = DockInfo()
        dock_id = info.dock_id()

.. method:: DockInfo.monitors()

   Obtain the current monitors connected to the DL-7450. The return value is a
   list of :py:class:`monitor.Monitor <monitor.Monitor>`. There is an entry per output, the entry containing
   an invalid monitor if there is no monitor connected to that output. For example::

      from dock import DockInfo
      from splashscreen import Splashscreen

      screen = Splashscreen()
      info = DockInfo()
      monitors = info.monitors()

      for output, monitor in enumerate(monitors):
        if monitor.valid():
          screen.add_text_box(f"Output {output}: {monitor.name()}")
        else:
          screen.add_text_box(f"Output {output}: no monitor")


.. method:: DockInfo.host_status()

   Determine whether a host laptop or PC is connected to the DL-7450.

   Returns one of the constants described below.

.. admonition:: Coming soon
   :class: tip

   The return value will always be `DockInfo.HOST_NOT_CONNECTED` in this preview.

Constants
---------


.. data:: DockInfo.HOST_NOT_CONNECTED
          DockInfo.HOST_CONNECTED
          DockInfo.HOST_REQUIRES_DRIVER

   Describes whether a host laptop is connected to the DL-7450.

.. admonition:: Coming soon
   :class: tip

   The constant `DockInfo.HOST_REQUIRES_DRIVER` is not available in this
   preview. It is a service to applications to help users get DisplayLink drivers
   installed::

      from dock import DockInfo

      info = DockInfo()
      if info.host_status() == DockInfo.HOST_REQUIRES_DRIVER:
         # inform user how to get DisplayLink drivers, e.g with
         # a QR code

