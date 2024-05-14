.. currentmodule:: i2c

:mod:`i2c` --- I\ :sup:`2`\ C Device Management
===============================================

.. module:: i2c
   :synopsis: i2c Peripheral Management

Inter-Integrated Circuit (I\ :sup:`2`\ C) is a simple two-wire serial
communication protocol. The two lines are the *serial data line* (SDA) and the
*serial clock line* (SCL). A controller, or master, node on the bus can send
commands to and read data from target, or slave, nodes on the bus. Texas Instruments provides
`A Basic Guide to I2C
<https://www.ti.com/lit/an/sbaa565/sbaa565.pdf?ts=1726027662062>`_.

As outlined in the `DL-12xx, DL-25xx and DL-7xx Design Guidelines
<https://cp.synaptics.com/cognidox/view/NR-152259-AN>`_ there are several I\
:sup:`2`\ C interfaces available to the DL7450. At present the *i2c* module
gives application developers an interface to the I2C1 bus via the SDK. The SDK
samples include simple examples of drivers for I\ :sup:`2`\ C devices. 


Tips For Writing an I\ :sup:`2`\C Driver
----------------------------------------

The application developer is responsible for the placement of the I\ :sup:`2`\C
device on the bus, and understanding how its address is assigned. The base
address of the device is a 7-bit number determined by the vendor. Often vendors
allow the application developer to specify the lowest 2 or 3 bits by providing
2 or 3 pins which can be brought high or low using resistors. For example the
`MCP9808 Temperature Sensor
<https://ww1.microchip.com/downloads/en/DeviceDoc/25095A.pdf>`_  uses a base
address of 0x18, or 0b0011000. Any of the 3 least significant bits can be set
using the address pins, giving a possible range of addresses from 0x18 to 0x1F.
Please read the vendor data sheet carefully.

Sometimes a vendor datasheet will provide two *8*-bit device addresses, one for
read operations and one for write operations. To use the DL7450 i2c module
correctly, you must obtain the correct 7-bit address in such cases. The 8-bit
number arises from including the read-write bit of the register in the device
address. To extract the correct 7-bit address, use the most-significant 7 bits
and apply a right shift (half).  For example if the datasheet might give a
write address of 0x92 (0b10010010) and a read address of 0x93 (0b10010011).  To
use the DL7450 SDK use a device address of 0x49 (0b1001001).

Finally, there are some addresses that are reserved.

  - 000 0xxx (0x00 to 0x07) reserved.
  - 0x08 to 0x77 valid address range.
  - 111 1xxx (0x78 to 0x7f) reserved

The read and write methods in the DL7450 i2c module will raise an error if the
device address is outside the valid range of 7-bit addresses, or if there is
not device present at the given address. In all cases, it is the responsibility
of the application developer to provide the correct device address. An
incorrect address will result in an :ref:`I2cError <i2c.I2cError>` being
raised.


.. code-block:: python

   from i2c import I2C, I2cError

   BASE_ADDRESS = 0x18

   class MCP9808
     def __init__(self):
       self.i2c = I2C()
       try:
         self.i2c.read(BASE_ADDRESS, 0, 1)
       except I2cError:
         # invalid base address.
         pass



Functions
---------

.. function:: i2c(bus = i2c.Bus.I2C1)

   Obtain an interface to an I\ :sup:`2`\C interface. At present, the DL7450
   SDK only provides access to devices on the I2C1 bus. Calling this function
   with any other parameters will result in an :ref:`I2cError
   <i2c.I2cError>` being raised. Returns an :ref:`I2C <i2c.I2C>` object.

Constants
---------

.. data:: Bus.I2C1
          Bus.I2C0

   An identifier for one of the DL7450 I\ :sup:`2`\ C buses. At present the SDK
   only provides an interface to the I2C1 bus.


Classes
-------

.. toctree::
    :maxdepth: 1

    i2c.I2C
    i2c.I2cError

        
