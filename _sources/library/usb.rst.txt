.. currentmodule:: usb

:mod:`usb` --- USB Peripheral Management
========================================

.. module:: usb
   :synopsis: USB Peripheral Management

.. admonition:: Coming soon
   :class: tip

   In this preview, we provide a very minimal usb module, which is only capable of
   a simple enumeration of USB devices which are connected to the DL-7450. In a
   subsequent release, this module will contain much fuller functionality for enumerating
   by Vendor ID and Product ID, or USB class. It will enable application developers to
   read USB device descriptors and write drivers for connected USB peripherals.

Functions
---------

.. function:: find()

   Obtain a list of currently connected USB devices. The return value is a list of 3-tuples, where each
   tuple is the Vendor ID, Product ID and a readable name. For example::

      import usb
      from splashscreen import Splashscreen

      info = DockInfo()
      screen = Splashscreen()

      text = [
          f"{vid:04x}:{pid:04x} {name}" for vid, pid, name in usb.find()
      ]

      screen.add_text_box(text)




