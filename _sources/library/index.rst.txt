.. _dl7450_sdk:

Python API reference guide
==========================

This chapter describes modules (function and class libraries) which are built
into the DisplayLink DL-7450 SDK.

.. note::
   * The DL-7450 SDK provides built-in modules that mirror the functionality of the
     :ref:`Python standard library <dl7450_lib_python>` (e.g. :mod:`time`), as
     well as :ref:`DL-7450-specific modules <dl7450_lib>`
     (e.g. :mod:`splashscreen`, :mod:`wakeup`).
   * Most built-in standard library modules implement a subset of the
     functionality of the equivalent Python module.

.. _dl7450_lib_python:

Python standard libraries
-------------------------

The following standard Python libraries are available in the DisplayLink DL-7450 SDK. In some cases 
they may be cut-down versions. 

.. toctree::
   :maxdepth: 1

   binascii.rst
   builtins.rst
   io.rst
   json.rst
   time.rst

.. _dl7450_extmod:

Micropython modules
-------------------

The following Micropython extension modules are available

.. toctree::
   :maxdepth: 1

   framebuf.rst

.. _dl7450_lib:

DL-7450 foundation libraries
----------------------------

Functionality specific to the DisplayLink DL-7450 SDK

.. toctree::
   :maxdepth: 1

   image.rst
   wakeup.rst


.. _dl7450_management:

DL-7450 Dock Management libraries
---------------------------------

The following libraries provide management of the DisplayLink DL-7450 platform

.. toctree::
   :maxdepth: 1

   datastore.rst
   dock.rst
   monitor.rst
   network.rst
   image.rst
   gpio.rst
   i2c.rst
   splashscreen.rst
   usb.rst


.. _dl7450_web:

DL-7450 web libraries
---------------------

The following libraries enable the DisplayLink DL-7450 to access external web
services. The allows applications to fetch content from webservices or to interact
with REST APIs. 

.. toctree::
  :maxdepth: 1

  http.rst


.. _dl7450_iot:

DL-7450 Internet-of-Things libraries 
------------------------------------

The following libraries enable the DL-7450 to be purposed as an
Internet-of-Things device. 

.. toctree::
  :maxdepth: 1

  mqtt.rst
  vision_client.rst
