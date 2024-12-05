# Driving GPIO input pins

The `gpio` module allows DL-7450 applications to write drivers for General
Purpose Input-Output (GPIO) pins. The DL-7450 allows application developers to
use an IO-expander attached to the I2C1 bus. The pins can be named in the
factory configuration for the board, and then referred to by this name in the
application code. Here we include two simple illustrations. Each of them relies
on the Redwood reference board configuration, which includes a joystick. The
joystick consists of five GPIO pins, configured to be digital inputs, with
names:

 * `JOYSTICK_CENTER`
 * `JOYSTICK_LEFT`
 * `JOYSTICK_RIGHT`
 * `JOYSTICK_UP`
 * `JOYSTICK_DOWN`

The sample scripts will fail with an error if the configuration does not name
these pins. Each application registers one or more callbacks that are invoked
when the named digital output is activated.


 * [A button application](button_gpio.py). This script uses the joystick center
   button as a digital input. It counts and displays on the splashcreen the
   number of times the button is pressed.
 * [A joystick application](joystick_gpio.py). This script uses all of the
   joystick positions as digital inputs. It keeps a count of how many times
   each direction has been chosen and displays the result on the screen.kkj:

There is a further sample, [ssd1360.py](../i2c/ssd1306.py) that uses the
joystick in combination with an OLED display connected to the I2C1 bus.
