.. currentmodule:: gpio
.. _gpio.DigitalInput:


class DigitalInput -- manage a GPIO configured as a digital input
=================================================================

The *DigitalInput* class provides an interface for applications to read and
react to inputs from a GPIO pin. Applications should not try to create
*DigitalInput* objects directly, but should use the :func:`gpio.create
<gpio.create>` function instead. This function reads the underlying
configuration and raises an exception if the named pin does not exist,
whereas the *DigitalInput* constructor will create a non-functional object.

Constructor
-----------

.. class:: DigitalInput(pin_name, active_high, callback=None)

   The parameters are:

      - *pin_name*: the name of the GPIO pin, as set in the board configuration.
      - *active_high*: is a boolean value that indicates whether the pin is
        considered active when it is at the high voltage level. The I/O
        expanders on the DL-7450 are configured to be active low, that is, the
        pin is held at the high value by default and pulled down to the low
        voltage level on activation.  
      - *callback*: (optional). Any Python callable entity which takes no
        parameters. Any return value is ignored. The callback is invoked on a
        transition from the pin being inactive to it being active, for example
        when a button is pressed. Future enhancements of this module may
        additionally provide for callbacks to be registered on transitions
        between active and inactive states, such as a button release. Note, the
        callback is not a genuine interrupt - i.e. it will not pre-empt any
        application code that is currently running. The callback will be queued
        and invoked when the application is next idle.  This includes
        subsequent pin active events.

   Applications should prefer to use the :func:`gpio.create <gpio.create>`
   function, which reads the board configuration, to create *DigitalInput*
   objects. Example using callback::

      # Example relies on a configuration where there is a digital input
      # pin named 'button'

      from splashscreen import Splashscreen
      import gpio

      PIN_NAME = "button"

      class Button:
          def __init__(self):
              self.press_count = 0
              self.pin = gpio.create(PIN_NAME, callback=self.cb)
              self.screen = Splashscreen()
              self.screen.add_text_box("Waiting for button press...")

          def screen_msg(self):
              return f"PinName : {PIN_NAME}\nPressed {self.press_count} times"

          def cb(self):
              self.press_count = self.press_count+1
              self.screen.add_text_box(self.screen_msg())

      pin = Button()




Methods
-------

.. method:: DigitalInput.read()


   Read the value of the pin. The return value is either 0 or 1, and indicates
   if the pin state is high or low. If the pin is not configured for this board
   then this function will return -1.

   For example::
   
      import gpio
      pin = gpio.create("MyPin")
      value = pin.read()
   
.. method:: DigitalInput.active_high()


   Returns a boolean that is *True* if the pin is configured to be active in
   the high state, or *False* if the pin is configured to be active in the low
   state.

   For example::

      import gpio
      from wakeup import wakeup
      from splashscreen import Splashscreen

      class Button:
        def __init__(self):
          self.pin = gpio.create("button")
          self.screen = Splashscreen()
          self.current = -1
          self.timer = wakeup(self.read_pin, 0, 100)
          if self.pin.active_high():
            self.active_value = 1
          else:
            self.active_value = 0
        
        def active(self):
          if self.current == self.active_value:
            return "active"
          return "inactive"
      
        def display(self):
          self.screen.add_text_box(f"{self.active()}")
      
        def read_pin(self):
          value = self.pin.read()
          if value == self.current:
            return
          self.current = value
          self.display()
          
      button = Button()

