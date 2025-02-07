:mod:`framebuf` --- frame buffer manipulation
=============================================

.. module:: framebuf
   :synopsis: Frame buffer manipulation

This module is imported from the Micropython extended modules library. It
provides helper functions for manipulating images. It includes support for
monochrome images, and so is useful for supporting applications that run on
OLED or E Ink displays. There are several monochrome image types supported by
this module: :data:`framebuf.MONO_VLSB`, :data:`framebuf.MONO_HLSB`,
:data:`framebuf.HMSB` according to how each byte in the underlying buffer
represents the pixels.

There is also a font available for drawing text, and includes the ASCII set
from the space character (ASCII 32) to the tilde character (ASCII 126). The
font is the Commodore Pet Me 128 font, with fixed width characters of 8x8
pixels. 


Classes
-------

.. toctree::
    :maxdepth: 1

    framebuf.FrameBuffer

Constants
---------

The following constants are used to define the pixel format.

.. data:: framebuf.MONO_VLSB

    Monochrome (1-bit) color format
    This defines a mapping where the bits in a byte are vertically mapped with
    bit 0 being nearest the top of the screen. Consequently each byte occupies
    8 vertical pixels. Subsequent bytes appear at successive horizontal
    locations until the rightmost edge is reached. Further bytes are rendered
    at locations starting at the leftmost edge, 8 pixels lower.

.. data:: framebuf.MONO_HLSB

    Monochrome (1-bit) color format
    This defines a mapping where the bits in a byte are horizontally mapped.
    Each byte occupies 8 horizontal pixels with bit 7 being the leftmost.
    Subsequent bytes appear at successive horizontal locations until the
    rightmost edge is reached. Further bytes are rendered on the next row, one
    pixel lower.

.. data:: framebuf.MONO_HMSB

    Monochrome (1-bit) color format
    This defines a mapping where the bits in a byte are horizontally mapped.
    Each byte occupies 8 horizontal pixels with bit 0 being the leftmost.
    Subsequent bytes appear at successive horizontal locations until the
    rightmost edge is reached. Further bytes are rendered on the next row, one
    pixel lower.

.. data:: framebuf.RGB565

    Red Green Blue (16-bit, 5+6+5) color format

.. data:: framebuf.GS2_HMSB

    Grayscale (2-bit) color format

.. data:: framebuf.GS4_HMSB

    Grayscale (4-bit) color format

.. data:: framebuf.GS8

    Grayscale (8-bit) color format
