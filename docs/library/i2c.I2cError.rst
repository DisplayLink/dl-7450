.. currentmodule:: i2c
.. _i2c.I2cError:


class I2cError
==============

Represents an error during an I\ :sup:`2`\ C operation.

.. class:: I2cError(err_num, message)

   A python *Exception* class representing an I2C error


   .. attribute:: errno: int

      Value representing the error code
      
      +---------------+------------------------------------+
      | errno         | Meaning                            |
      +===============+====================================+
      | 0             | No error                           |
      +---------------+------------------------------------+
      | 1             | Invalid bus ID                     |
      +---------------+------------------------------------+
      | 2             | Device address out of range        |
      +---------------+------------------------------------+
      | 3             | Transmit select error\ :sup:`1`    |
      +---------------+------------------------------------+
      | 4             | Read error\ :sup:`2`               |
      +---------------+------------------------------------+
      | 5             | Write error\ :sup:`2`              |
      +---------------+------------------------------------+

      Notes:
         
      \ :sup:`1` a transmit select error can arise when the DL-7450 sends the
      7-bit device address before it starts a read or write operation. If you
      encounter this error, check the address of your device. 

      \ :sup:`2` the most likely reason for a read or write error is a failure
      to use the device as described by the vendor. For example, using an
      unknown register, attempting to write to a read-only register or
      vice-versa.
   
   .. attribute:: args: List
   
      Further arguments for the error. At present only *args[1]* is used, and is
      human-readable string describing the error. Please note, *I2cError.args[0]*
      is equivalent to *I2cError.errno*.
