.. currentmodule:: gpio

:mod:`gpio` --- General-Purpose Input/Output Pin Management
===========================================================

.. module:: gpio
   :synopsis: General-Purpose Input/Output pin management

Most microcontrollers offer some General-Purpose Input/Output (GPIO) pins for
providing application functionality. GPIO pins can be used to detect digital
signal inputs or to emit digital output signals and are controlled by software.
A digital input pin is used for detecting signals from buttons and sensors,
while digital output pins can be used, for example, to light an LED. This
module provides DL-7450 application developers with an API for building docking
stations that have enhanced functionality using GPIO pins.


Docking station designers may wish to incorporate functionality that uses GPIO
pins. The DL-7450 has 16 built-in GPIOs, each of which can be configured via
the DisplayLink firmware web builder. The functionality for these native GPIO
pins is limited.  However, there are up to four I2C Input/Output expanders
available via the DL-7450 SDK. Each of them supports up to eight digital input
or output pins. To make these GPIOs constrollable using the SDK, the expander
must be wired to the the I2C1 bus.  Refer to `DL-12xx, DL-25xx and DL-7xx
Design Guidelines <https://cp.synaptics.com/cognidox/view/NR-152259-AN>`_ for a
description. For example, the Redwood reference design has an `NXP PCA9538A
<https://www.nxp.com/docs/en/data-sheet/PCA9538A.pdf>`_ I/O expander connected
to the i2c1 bus at address 0x72. The pins should be named in the configuration
that is programmed into the dock in the factory process. This abstracts the
hardware implementation, so that application code can be ported across
different board designs. It also provides the means for integrity checks in
application code. 

A example showing how a joystick can be incorporated into a Redwood
reference design is provided in the sample code.


Functions
---------

.. function:: create(pin_name, callback = None)

   Create a suitable control object based on the GPIO name defined for the
   board. This function will return either a :ref:`DigitalInput
   <gpio.DigitalInput>` or :ref:`DigitalOutput <gpio.DigitalOutput>` object.

   The parameters are:

      - *pin_name* the custom name of the GPIO pin, as defined in the
        manufacturing process for the board. If the pin name is not defined by
        the board configuration, a `TypeError` exception is raised.
      - *callback* (optional). For pins which are configured as digital inputs,
        a callback may be provided. The callback is any Python callable entity
        which takes no parameters. Any return value is ignored. Providing a
        callback for a pin that is configured as a digital output will result
        in a `TypeError` exception being raised.


Classes
-------

.. toctree::
    :maxdepth: 1

    gpio.DigitalInput.rst
    gpio.DigitalOutput.rst

