.. currentmodule:: usb

:mod:`usb` --- USB Peripheral Management
========================================

.. module:: usb
   :synopsis: USB Peripheral Management


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




