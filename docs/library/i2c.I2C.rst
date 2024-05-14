.. currentmodule:: i2c
.. _i2c.I2C:


class I2C -- manage a DL-7450 I2C bus
=====================================

The *I2C* class provides an interface to one of DL7450's I\ :sup:`2`\ C buses. 

Constructor
-----------

.. class:: I2C(bus = i2c.Bus.I2C1)

   Obtain an interface to an I\ :sup:`2`\C interface. At present, the DL7450
   SDK only provides access to devices on the I2C1 bus. Calling this function
   with any other parameters will result in an :ref:`I2cError
   <i2c.I2cError>` being raised.

   The module factory function :func:`i2c.i2c <i2c.i2c>` is equivalent to
   creating an *I2C* object directly.

Methods
-------

There are two main methods, *read* and *write*. These functions take care of
initiating the underlying I\ :sup:`2`\C operation, and allow the application to
focus on transferring data to and from the devce. Please read the 



.. method:: I2C.read(address, register, nbytes) -> bytearray
   
   This method attempts to read data from a device node on the I\ :sup:`2`\C
   bus. The parameters are

      - *address*: the 7-bit base address of the device node.
      - *register*: the sub-address, or register address, to read data from.
        The register addresses of a particular I\ :sup:`2`\C device will be
        described in the vendor's datasheet.
      - *nbytes*: the number of bytes to read.
   
   If successful, this method returns a Python *bytearray* holding the data.
   
.. method:: I2C.write(address, register, payload)

   This method attempts to Write data to a device node on the I\ :sup:`2`\C
   bus. The parameters are

      - *address*: the 7-bit base address of the device node.
      - *register*: the sub-address, or register address, to read data from.
        The register addresses of a particular I\ :sup:`2`\C device will be
        described in the vendor's datasheet.
      - *payload* 

