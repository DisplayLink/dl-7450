.. currentmodule:: dock
.. _dock.DockInfo:

class DockInfo - current information about the dock
===================================================

The DockInfo class gives current information about the DL-7450.

.. class:: DockInfo()

   Construct a DockInfo object.

   .. method:: DockInfo.dock_id() -> str

      Obtain the unique identifier of this dock. This identifier could be used for
      registering the dock as an IoT device with a service provider. For example:

      .. code-block:: python

         from dock import DockInfo
         info = DockInfo()
         dock_id = info.dock_id()

   .. method:: DockInfo.monitors() -> list[Monitor]

      Obtain the current monitors connected to the DL-7450. The return value is a
      list of :py:class:`monitor.Monitor <monitor.Monitor>`. There is an entry per output, the entry containing
      an invalid monitor if there is no monitor connected to that output. For example:

      .. code-block:: python

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

   .. method:: DockInfo.host_status() -> int

      Determine whether a host laptop or PC is connected to the DL-7450. Returns an
      integer which can be any of the values below.

   .. data:: DockInfo.HOST_NOT_CONNECTED

      No host is connected to the dock.

   .. data:: DockInfo.HOST_CONNECTED

      A host is connected to the dock.

   .. data:: DockInfo.HOST_CONNECTION_SUSPENDED

      A host is connected to the dock, but the connection has been
      suspended by the dock.

      These values are read-only attributes, and can be accessed via either
      the class directly, or an object of the class.

   .. code-block:: python

      from dock import DockInfo

      assert DockInfo.HOST_NOT_CONNECTED == DockInfo().HOST_NOT_CONNECTED
      assert DockInfo.HOST_CONNECTED == DockInfo().HOST_CONNECTED
      assert DockInfo.HOST_CONNECTION_SUSPENDED == DockInfo().HOST_CONNECTION_SUSPENDED
