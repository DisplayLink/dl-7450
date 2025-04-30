.. currentmodule:: gpio
.. _gpio.DigitalOutput:

class DigitalOutput -- manage a GPIO configured as a digital output
===================================================================

The *DigitalOutput* class provides an interface for applications to write to a
GPIO pin. Applications should not try to create *DigitalOutput* objects
directly, but should use the :func:`gpio.create <gpio.create>` function
instead. This function reads the underlying configuration and raises an
exception if the named pin does not exist, whereas the *DigitalOutput*
constructor will create a non-functional object.

Constructor
-----------

.. class:: DigitalOutput(pin_name, active_high)

   The parameters are:

      - *pin_name* the name of the GPIO pin.
      - *active_high* is a boolean value that indicates whether the pin is
        considered active when it is at the high voltage level. The I/O
        expanders on the DL-7450 are configured to be active low, that is, the
        pin is held at the high value by default and pulled down to the low
        voltage level on activation.  

Methods
-------

.. method:: DigitalOutput.write(val)


   Write to the pin. The value must be 1 or 0 to activate or deactivate the
   pin. Attempting to write any other value will result in a *ValueError* being
   raised. 


   For example::
   
      import gpio
      pin = gpio.create("MyLed")
      pin.write(1)
   
.. method:: DigitalOutput.active_high()


   Returns a boolean that is `True` if the pin is configured to be active in
   the high state, or `False` if the pin is configured to be active in the low
   state.

   For example::

      import gpio
      from wakeup import wakeup

      pin = gpio.create("led")

      val = 0

      def blink(): 
         global val
         pin.write(val)
         if val == 0:
            val = 1
         else: 
            val = 0
          

      wakeup(blink, 0, blink) 
