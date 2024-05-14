# Interacting with I<sup>2</sup>C devices

The DL-7450 has the capability to communicate with I<sup>2</sup>C devices. The
DL-7450 chip acts as a controller which can connect to multiple targets through
the I<sup>2</sup>C bus and both read and write arbitrary amounts of data.
Two sample applications have been provided that showcase each of these
operations individually:

## I<sup>2</sup>C reading

A [sample app](mcp9808.py) for the MCP9808 temperature sensor has been provided
to demonstrate how to perform I<sup>2</sup>C reads.

The provided app reads and displays the ambient temperature of the sensor on
the screen, with updates to the value every few seconds. The temperature output
from the sensor is provided in fractions of degrees Celsius by default, but the
different levels of precision can be configured.

There are a number of changes that can be made to the sample app, including:

* The configuration register at address `0x01` can be read from, parsed and
  displayed on the screen.
* As previously mentioned, the precision of the sensor's output can be changed
  via address `0x08`.
* Upper, lower and critical temperature limits can be set via the configuration
  register `0x01` and detected as part of the temeprature register output.

The datasheet for the MCP9808 sensor can be found at
https://ww1.microchip.com/downloads/en/DeviceDoc/25095A.pdf.

## I<sup>2</sup>C writing

A [sample app](ssd1306.py) for the SSD1306 OLED screen has been provided to
demonstrate how to perform I<sup>2</sup>C writes.

The provided app displays the Synaptics logo, scrolling horizontally across the
screen. It also performs the required set-up commands for the SSD1306 screen to
display the image correctly.

There are a number of changes that can be made to the sample app, including:

* The screen initialisation step configures a lot of aspects of the screen, one
  of these being the contrast. This can be tweaked to show the image at
  different intensities.
* The scroll direction can be changed so that the image scrolls from right to
  left. In fact, the scroll can be modified so that it occurs vertically, or
  even horizontally and vertically simultaneously.
* The logo to display can be changed. The expected format of the image is as a
  `list` of `bytes`, where each entry of the list corresponds to a row in the
  image, and each byte in that entry is either `b'\0'` or `b'\1'`,
  corresponding to pixel off and pixel on respectively.

The datasheet for the SSD1306 OLED screen can be found at
https://www.digikey.com/htmldatasheets/production/2047793/0/0/1/SSD1306.pdf.
